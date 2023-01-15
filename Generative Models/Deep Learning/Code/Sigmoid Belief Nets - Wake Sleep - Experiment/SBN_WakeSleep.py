import torch
import torchvision
import cv2

import PIL.Image as Image
import seaborn as sns
import glob
import os

from matplotlib import pyplot as plt

import SBN_Render as renderer

# calculate the forward pass of a SBN
def SBN_calc(s0: torch.Tensor, w: torch.Tensor, b: torch.Tensor) \
        -> (torch.Tensor, torch.Tensor):
    # calculate the forward posterior probability P(s_t|s_{t-1})
    s1 = torch.nn.functional.linear(s0, w, b)
    s1 = torch.torch.nn.functional.sigmoid(s1)

    # do a bernoulli sampling
    s2 = torch.bernoulli(s1)
    return s1, s2


# SBN calculation for the top layers with no previous layer
def SBN_calc_tb(b: torch.Tensor) -> (torch.Tensor, torch.Tensor):
    # do a bernoulli sampling
    s1 = torch.nn.functional.sigmoid(b)
    s2 = torch.bernoulli(s1)
    return s1, s2


# SBN gradients "backward pass"
# This is not a back propagation, because we are using the values produced
# by the reverse directional SBN as our gradient estimator
def SBN_update_w(s0: torch.Tensor, w: torch.Tensor, b: torch.Tensor, s1: torch.Tensor,
                 epsilon: float) -> torch.Tensor:
    # -(s_l - \sigmoid(w^G_{l}s_{l+1}+b^G_{l})) (s_{l+1})^T
    delta = -torch.outer(s0 - torch.torch.nn.functional.sigmoid
        (torch.nn.functional.linear(s1, w, b)), s1)

    # update the weights (gradient descent)
    w = w - epsilon * delta
    return w


# SBN gradients "backward pass" for bias:
def SBN_update_b(s0: torch.Tensor, w: torch.Tensor, b: torch.Tensor, s1: torch.Tensor,
                 epsilon: float) -> torch.Tensor:
    # -(s_l - \sigmoid(w^G_{l}s_{l+1}+b^G_{l}))
    delta = -(s0 - torch.torch.nn.functional.sigmoid
        (torch.nn.functional.linear(s1, w, b)))
    # update the bias (gradient descent)
    b = b - epsilon * delta
    return b


# bias updates for the top layer:
def SBN_update_bb(s0: torch.Tensor, b: torch.Tensor, epsilon: float) -> torch.Tensor:
    # update the bias (gradient descent)
    delta = -(s0 - torch.torch.nn.functional.sigmoid(b))
    b = b - epsilon * delta
    return b

# main program
class SBN_Helmholtz_Model:

    WG = []  # weights for the generative model
    WR = []  # weights for the recognition model
    BG = []  # bias for the generative model
    BR = []  # bias for the recognition model
    S = [] # states of the SBN by layer
    S_G = []  # probabilities of the generative model
    S_R = []  # probabilities of the recognition model

    def __init__(self, layerSizes):
        for layerSize in layerSizes:
            self.S.append(torch.zeros(layerSize))
            self.S_G.append(torch.zeros(layerSize))
            self.S_R.append(torch.zeros(layerSize))

        for i in range(1,len(self.S)):
            # the dimensions are different since
            self.WG.append(torch.zeros(self.S[i-1].size(0), self.S[i].size(0)))
            self.WR.append(torch.zeros(self.S[i].size(0), self.S[i-1].size(0)))
            self.BG.append(torch.zeros(self.S[i-1].size(0)))
            self.BR.append(torch.zeros(self.S[i].size(0)))

        # add the top layer bias
        self.BG.append(torch.zeros(self.S[-1].size(0)))

    def toCuda(self):
        for i in range(0, len(self.WG)):
            self.WG[i] = self.WG[i].cuda()
            self.WR[i] = self.WR[i].cuda()
            self.BG[i] = self.BG[i].cuda()
            self.BR[i] = self.BR[i].cuda()
            self.S[i] = self.S[i].cuda()
            self.S_G[i] = self.S_G[i].cuda()
            self.S_R[i] = self.S_R[i].cuda()

        self.S[-1] = self.S[-1].cuda()
        self.S_G[-1] = self.S_G[-1].cuda()
        self.S_R[-1] = self.S_R[-1].cuda()
        self.BG[-1] = self.BG[-1].cuda()

    def wake(self, data : torch.Tensor):
        # set the data
        self.S[0] = data

        # wake phase : run the recognition model
        for i in range(1,len(self.S)):
            self.S_R[i], self.S[i] = SBN_calc(self.S[i-1], self.WR[i-1], self.BR[i-1])

        # update the weights of the generative network
        for i in range(1, len(self.S)):
            # we compute outwards so the update direction is inverse form calc direction
            self.WG[i-1] = SBN_update_w(self.S[i-1], self.WG[i-1], self.BG[i-1], self.S[i], 0.2)
            self.BG[i-1] = SBN_update_b(self.S[i-1], self.WG[i-1], self.BG[i-1], self.S[i], 0.2)

        # update the bias of the top layer
        self.BG[-1] = SBN_update_bb(self.S[-1], self.BG[-1], 0.1)

    def dream(self):
        # dream phase : run the sampling of the top layer
        self.S_G[-1], self.S[-1] = SBN_calc_tb(self.BG[-1])

        # dream phase : run the generative model
        for i in range(len(self.S)-1, 0, -1):
            self.S_G[i-1], self.S[i-1] = SBN_calc(self.S[i], self.WG[i-1], self.BG[i-1])

        # update the weights of the recognition network
        for i in range(1, len(self.S)):
            self.WR[i-1] = SBN_update_w(self.S[i], self.WR[i-1], self.BR[i-1], self.S[i-1], 0.2)
            self.BR[i-1] = SBN_update_b(self.S[i], self.WR[i-1], self.BR[i-1], self.S[i-1], 0.2)


def generateData():
    # get the first 200 patterns in the mnist dataset transform to torch tensor
    trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=torchvision.transforms.ToTensor())
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=1, shuffle=True, num_workers=16)

    # load 200 samples
    data = []
    i0 = 0
    for i ,(inputs, labels) in enumerate(trainloader):
        if i0 >= 2000:
            break
        if labels != 4:
            continue
        data.append(torch.reshape(inputs,(1,28,28)))
        i0 += 1

    # scale to 8*8
    for i in range(0, len(data)):
        data[i] = torchvision.transforms.functional.resize(data[i], (16,16))

    # convert to binary
    for i in range(0, len(data)):
        data[i] = torch.where(data[i] > 0.3, torch.ones_like(data[i]), torch.zeros_like(data[i]))
        data[i] = torch.flatten(data[i])

    return data

def train(model : SBN_Helmholtz_Model, data, epochs : int):
    steps = 0
    for i in range(0, epochs):
        for d in data:
            dt = d.cuda()
            model.wake(dt)
            model.dream()
            steps += 1

            if steps % 20 == 0:
                renderR(model, steps)
                renderG(model, steps)

                # save data image
                cv2.imwrite("./frames/Mem/" + str(steps) + ".png", torch.reshape(d, (16,16)).cpu().numpy() * 255)

                # save dream image
                cv2.imwrite("./frames/Dream/" + str(steps) + ".png", torch.reshape(model.S[0], (16,16)).cpu().numpy() * 255)

        if (i % 10 == 0):
            print("epoch: ", i)

        if (i % 1 == 0):
            devT = model.S[0].cpu()
            devT = torch.permute(torch.reshape(devT, (1,16,16)), (1,2,0))
            cv2.imshow("mat",devT.numpy())
            cv2.waitKey(1)

def renderR(model : SBN_Helmholtz_Model, ID):
    fig = plt.figure()
    fig = renderer.generateWeightsGraph(model.WR[0], 16, 16, 16, 4, 4, fig)
    # save figure as png
    fig.savefig("./frames/R/weightsR" + str(ID) + ".png")
    plt.close(fig)

def renderG(model : SBN_Helmholtz_Model, ID):
    fig = plt.figure()
    fig = renderer.generateWeightsGraph(model.WG[0], 16, 16, 16, 4, 4, fig, transpose=True, cmap="rocket")
    # save figure as png
    fig.savefig("./frames/G/weightsG" + str(ID) + ".png")
    plt.close(fig)

def resetCache():
    #delete all files in ./frames/Dream/
    files = glob.glob('./frames/Dream/*')
    for f in files:
        os.remove(f)

    #delete all files in ./frames/Mem/
    files = glob.glob('./frames/Mem/*')
    for f in files:
        os.remove(f)

    #delete all files in ./frames/R/
    files = glob.glob('./frames/R/*')
    for f in files:
        os.remove(f)

    #delete all files in ./frames/G/
    files = glob.glob('./frames/G/*')
    for f in files:
        os.remove(f)

resetCache()

model = SBN_Helmholtz_Model({16*16,16,8})
model.toCuda()

print("Register Complete:")

data = generateData()
train(model, data, 2)
