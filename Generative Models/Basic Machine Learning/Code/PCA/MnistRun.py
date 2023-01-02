import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
from matplotlib import pyplot as plt

import PCA_algo

# Training settings
batch_size = 64

def cvtMnistData(mnist_dataset,k):
    data = mnist_dataset.train_data.numpy().reshape(60000, 28*28)
    labels = mnist_dataset.train_labels.numpy()

    data = PCA_algo.PCA(data, k)

    # pick the first 50000 samples as training set
    train_data = data[:50000,:]
    train_labels = labels[:50000]

    test_data = data[-10000:, :]
    test_labels = labels[-10000:]

    return CustomDataset(train_data, train_labels), CustomDataset(test_data, test_labels)

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __getitem__(self, index):
        return self.data[index], self.labels[index]

    def __len__(self):
        return len(self.data)


class Net(nn.Module):

    def __init__(self, k):
        super(Net, self).__init__()
        self.l3 = nn.Linear(k, 16)
        self.l4 = nn.Linear(16, 16)
        self.l5 = nn.Linear(16, 10)
        self.k = k

    def forward(self, x):
        x = x.view(-1, self.k)  # Flatten the data (n, 1, 28, 28)-> (n, 784)
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)

def runTest(k):
    test_accuracy = []

    # MNIST Dataset
    train_dataset = datasets.MNIST(root='./mnist_data/',
                                   train=True,
                                   transform=transforms.ToTensor(),
                                   download=True)

    test_dataset = datasets.MNIST(root='./mnist_data/',
                                  train=False,
                                  transform=transforms.ToTensor())

    train_set, test_set = cvtMnistData(train_dataset, k)

    # Data Loader (Input Pipeline)
    train_loader = torch.utils.data.DataLoader(dataset=train_set,
                                               batch_size=batch_size,
                                               shuffle=True)

    test_loader = torch.utils.data.DataLoader(dataset=test_set,
                                              batch_size=batch_size,
                                              shuffle=False)

    model = Net(k)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


    def train(epoch):
        model.train()
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = Variable(data), Variable(target)
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            if batch_idx % 100 == 0:
                test()
                # print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                #     epoch, batch_idx * len(data), len(train_loader.dataset),
                #     100. * batch_idx / len(train_loader), loss.data))


    def test():
        model.eval()
        test_loss = 0
        correct = 0
        for data, target in test_loader:
            data, target = Variable(data, volatile=True), Variable(target)
            output = model(data)
            # sum up batch loss
            test_loss += criterion(output, target).data
            # get the index of the max
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).cpu().sum()

        test_loss /= len(test_loader.dataset)
        # print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        #     test_loss, correct, len(test_loader.dataset),
        #     100. * correct / len(test_loader.dataset)))
        test_accuracy.append(float(100. * correct / len(test_loader.dataset)))


    for epoch in range(1, 30):
        train(epoch)
        print("Epoch: ", epoch)

    return test_accuracy

if __name__ == '__main__':
    k = 4
    accuracys = []
    while k < 784:
        print("k = ", k)
        accus = runTest(k)
        print(accus)
        accuracys.append(accus)
        k *= 2

    color = 0.2
    for i in range(len(accuracys)):
        plt.plot(accuracys[i], label="k = %d" % (4 * 2 ** i), color=(color, 0, color))
        if color >= 1:
            color = 1
        else:
            color += 0.08

    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Accuracy of MNIST with different PCA downscale")
    plt.show()
