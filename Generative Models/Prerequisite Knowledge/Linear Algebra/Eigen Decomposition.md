------
#LinearAlgebra 

In the original definition, for a matrix $A \in \mathbb{R}^{N \times N}$ , the eigenvector $v \in \mathbb {R}^N$ and eigenvalue $\lambda \in \mathbb{R}$ is defined as tje vector and scalar that follows this relationship:
$$Av = \lambda v \longrightarrow (\lambda I - A)v = 0$$
- intuitively, the eigen vector is a vector in which linear transformation $A$ did not knock it out of its span
- $(\lambda I - A)$ is a singular matrix, making determinant $\det(\lambda I - A) = 0$ 

By having such relationship, we can view eigenvectors as the root of the function  $\det(xI - A) = 0$ 
In this manner, we can write the characteristic polynomial $p(\lambda)$:
$$p(\lambda) = \det(\lambda I-A) = \prod _{i=1} ^{N_\lambda} (\lambda -\lambda_i)^{n_i}$$
- Where $N_\lambda$ is the number of eigen values, $N_\lambda \leq N$  
- $n_i$ is the [[algebraic multiplicity]], The algebraic multiplicities sum to $\sum _{i=1} ^{N_\lambda} n_i = N$

## Eigen Decomposition

If matrix $A \in \mathbb{R}^{N \times N}$ have $N$ linearly independent eigenvectors, then the matrix can be factorized as:
$$Q \Lambda Q^{-1}$$
-  $Q \in \mathbb{R}^{N \times N}$ is the matrix with the ith column being the ith eigenvector.
- $\Lambda \in \mathbb{R}^{N \times N}$ is the diagnol matrix of eigenvalues $\Lambda = diag\{\lambda_1, \lambda_2,...,\lambda_N\}$ 

The process of getting the decomposition:

$Av = \lambda v$

$QA= Q\Lambda$

$A = Q\Lambda Q^{-1}$


