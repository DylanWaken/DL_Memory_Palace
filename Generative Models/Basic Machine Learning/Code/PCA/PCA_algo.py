import numpy as np
import torch
import matplotlib.pyplot as plt

def PCA(x, k):
    if k == 0:
        return x.astype(np.float32) / 255.0

    x = x.astype(np.float32)
    x -= x.mean(axis=0)  # mean normalize

    C = x.T.dot(x)  # covariance matrix
    lam, v = np.linalg.eig(C)  # eigenvalues and eigenvectors
    new_index = np.argsort(lam)[::-1]  # sort eigenvalues in descending order
    A = -v[:, new_index]  # transform matrix
    x_n = x.dot(A)  # transformed data

    r0 = lam[new_index] / lam.sum()
    # get cumulative sum of eigenvalues
    r = np.cumsum(r0)

    plt.plot(r, color='red', label='cumulative representation')
    plt.xlabel('Target Dimension (k)')
    plt.ylabel('representation (eigenvalues)')
    plt.title('PCA')
    plt.legend()
    plt.show()
    exit(0)

    for i in range(len(r)):
        if r[i] > 0.99:
            print("perfect representation limit: ",i)
            break

    return x_n[:, :k]  # return first k components





