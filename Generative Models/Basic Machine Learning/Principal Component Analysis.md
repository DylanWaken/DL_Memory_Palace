------
#BasicMachineLearning 
> ***Problem Type***: [[Dimension Reduction]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$  
> SOLVE: orthnormal basis $u_1,u_2,...,u_k$ such that the variance of the projected data is maximized : for each $u_i$ : $\max_{u_i}J_j = \frac{1}{N} \sum_{i=1} ^N (x_i^T u_j -\mu_x^Tu_j)^2$
> ***Closed-form Solution***: $u_i \in U$ from $svd(X)$  with maximum eigenvalues from $\Sigma^2$ of the $\Sigma$ in $svd(X)$ 

The objective of PCA algorithm is to descover a new set of $k$ dimensional orthnormal [[Basis]] $\{u_1, u_2,....,u_k\}$($k<n$), such that the projection of the $n$ dimensional data onto it would have the maximum distance between individual data points.

In the other word, we are looking for the maximum variance between individual data points.

For the orthnormal basis $u_j$ and data point $x_i$ , the projection distance is $x_i^T u_j$, and the variance for all data points projecting on this orthnormal basis is given as:
$$J_j = \frac{1}{N} \sum_{i=1} ^N (x_i^T u_j -\mu_x^Tu_j)^2$$
And if we normalize data with zero mean, we would have the simplified form:
$$J_j =\frac{1}{N}\sum _{i=1} ^N (x_i^Tu_j)^2 = \frac{1}{N} \sum _{i=1}^N u_j^Tx_ix_i^Tu_j = u_j^T\frac{1}{N} \sum_{i=1} ^N (x_ix_i^T) u_j $$
By this form, we have:
$$J_j = u_j^T \frac{1}{N}[x_1, x_2,...,x_N] \begin{bmatrix}
x_1 \\x_2 \\ .\\.\\x_N
\end{bmatrix} u_j = \frac{1}{N}u_j^T XX^T u_j$$
And $XX^T$ is the [[Covariance Matrix]] of the input data samples (since data have zero mean).
Since $\frac{1}{N} XX^T$ is a constant, we set it as $S = \frac{1}{N} XX^T$, and we have:

With the objective of PCA, we are solving for the maximum variance, as:
$$\max_{u_j} u_j^TSu_j \quad s.t. \quad u_j^Tu_j = 1$$
(we need non-zero unit vectors so $u_j^Tu_j =1$ )

And by using [[Lagrange Multiplier]], we convert the problem into:
$$L(u_j, \lambda_j) = u_j^TSu_j + \lambda_j(1-u_j^Tu_j)$$
And by solving for zero derivative:
$$\dfrac{\partial L}{\partial u_j} = 2Su_j - 2\lambda_j u_j = 0 \Rightarrow Su_j = \lambda_ju_j$$
This conclusion indicates when $u_j$ is the eigenvector and $\lambda_j$ is the eigenvalue, the maximum difference in variance is achieved. 

And under the optimal case, we bring back this conclusion into the original formula, we have the optimal $J_j$ as:
$$J_{j_{\max}} = u_j^T \lambda_ju_j = \lambda_j$$
In the vector notation. If $\lambda$ is the set of all eigenvalues for matrix $S$, then:
$$J_{\max}  = \sum_{i=1} ^k\lambda_i$$ 
- Note, $\lambda_i$ is the $i$ **th largest eigenvalue** for matrix $S$

To get the orthnormal basis, we run a [[Singular Value Decomposition]] on matrix $X$. because of the correlation between SVD and [[Eigen Decomposition]], the fist decomposed matrix $U$ of $XX^T$ will be the set of eigenvectors, as 
$$svd(X) = U\Sigma V^T \quad ed(XX^T) = U \Sigma^2U^{-1}$$
With the new set of orthnormal basis being:
$${u_1,u_2,...,u_k} \in col(U)$$
- The eigenvectors corresponding to the series of largest eigenvalues

And the eigenvalues are the diagnol of $\Sigma^2$ 

The final PCA transformation is:
$$X_{new} ^{k \times N} = \begin{bmatrix} u_1^T \\ u_2^T \\ ..\\ u_k^T\end{bmatrix} ^{k \times n} X ^{n \times N}$$
## Selection of minimum dimension k

Normally when we use PCA to downscale $n$ dimensional data to $k$ dimensions, and the minimum $k$ we can choose from is dependent on the ratio of projected variance to source variance, as:
$$\frac{Var_{X_{new}}}{Var_{X}} \geq q$$
- by practice, we choose $q = 0.99$
