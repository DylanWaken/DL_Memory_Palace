import torch
import torch.nn as nn
import torch.nn.functional as F
from matplotlib import pyplot as plt
import seaborn as sns

def generateWeightsGraph(weight : torch.Tensor, C, H, W, C_h, C_w, plot,transpose=False, cmap="YlGnBu"):
    weightBF = weight.cpu()
    if transpose:
        weightBF = weightBF.t()
    buf = torch.reshape(weightBF, (C, H, W))

    subplots = plot.subplots(nrows=C_h, ncols=C_w)

    # get every layer of the channels
    for i in range(0,C):
        W_i = buf[i,:,:]

        # seaborn heatmap of the weights
        if plot:
            sns.heatmap(W_i.numpy(), ax=subplots[i//C_h,i%C_h],  cmap=cmap, cbar=False)

    plot.subplots_adjust(wspace=0.3, hspace=0.3)

    return plot

