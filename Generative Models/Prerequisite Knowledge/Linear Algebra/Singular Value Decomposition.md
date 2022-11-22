----
#LinearAlgebra 

Singular Value Decomposition (SVD) is a type of matrix factorization of a real or complex matrix. It is the generalized form of  [[Eigen Decomposition]]. A singular matrix is square matrices with no inverse, its determinent is zero.

For any given matrix $A \in \mathbb{R} ^ {M \times N}$,  it can be factored in the following form:
$$A = U\Sigma V$$
Matrix $A$ have the [[Rank]] of $rank(A) = p \leq \min(M,N)$

A matrix can be decomposed into the summation of rank 1 matrices, or atoms:
$$A = \sigma_1u_1v_1^T + ...+ \sigma_pu_pv_p^T$$
- $u_i \in \mathbb{R}^m, v_i \in \mathbb{R}^n, \sigma_i \in \mathbb{R}$ 
- $u_1 ... u_p$ are [[Linearly independent]] to each others, and $v_1 ... v_p$ also does

In the matrix form, this property is represented as:
$$A = \begin{bmatrix}
| \\ 
u_1,u_2...u_p
\\
|\\
\end{bmatrix}
\begin{bmatrix}
\sigma_1 ...... \\
\sigma_2 \
\\....
\\.......\sigma_p
\end{bmatrix}
\begin{bmatrix}
- v_1^T- \\
- v_2^T-
\\...
\\ -v_p^T-
\end{bmatrix}$$
- $U \in \mathbb{R}^{M \times P}, \Sigma \in \mathbb{R}^{P \times P}, V \in \mathbb{R}^{P \times N}$
- $U,V$ are [[Orthnormal Matrix]], with $U^TU = I$ and $V^TV = I$ 

The original formula also produce the following conclusions:
$$AV = U\Sigma,\quad U^TA = \Sigma V$$
And here we have the definition:

- $v_1 ... v_p \in Row(V)$ are the **Right Singular Vectors** of $A$
- $u_1 ... u_p \in Col(U)$ are the **Left Singular Vectors** of $A$ 
- $\sigma_1 ... \sigma_p$ are called the singular values.

## The relation between SVD and Eigen Decomposition

For any matrix $A$ and its SVD $U\Sigma V^T$, we have the following property:
$$AA^T = U\Sigma V^T \cdot V\Sigma U^T = U\Sigma^2 U^T = U\Sigma^2U^{-1} $$
If we have $\Sigma' = \Sigma^2$, we have the following form:
$$AA^T = U\Sigma'U^{-1}$$
- Which using the definition of [[Eigen Decomposition]], $U$ is the matrix of eigen vectors for $AA^T$ , and $\Sigma'$ is the eigenvalues for $AA^T$ 

For $A^TA$ , the process is exactly same, with eigenvectors being $V$ instead of $U$ 
