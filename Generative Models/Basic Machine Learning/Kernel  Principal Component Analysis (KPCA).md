-----
#BasicMachineLearning 
> ***Problem Type***: [[Embedding]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$  
> SOLVE: The transformation $f : \mathbb{R}^n \rightarrow \mathbb{R}^k$ maximizing the variance between data points.
> ***Closed-form Solution***: 
> 1: Calculate the kernel matrix $K$ = $K(x^{(i)},x^{(j)})$
> 2: Normalize the kernel matrix: $\tilde K = K - \mathbb{1}_NK - K \mathbb{1}_N + \mathbb{1}_NK \mathbb{1}_N$
> 3: Do the eigen decomposition: $KP = \Lambda P$ where  $\Lambda = diag\{\lambda_1,\lambda_2,...,\lambda_n\}$, $P = \{\alpha_1,\alpha_2,...,\alpha_n\}$
> 4: Run the transformation: $X' = P_k^TK$

Kernel [[Principal Component Analysis (PCA)]] is designed after the idea of high dimensional mappings using [[Kernel]]s. After data is remapped into a higher dimension, we search for the orthnormal [[Basis]] that maximized data variance in the kernel space, and use that as our projection matrix for dimension reduction for $\phi(x)$.

## Eigenvalues in the feature space

Because we incorporated high dimensional projection $\phi : \mathbb{R}^n \rightarrow \mathbb{R}^d, d > n$, we name this space the feature space or $\mathcal{F}$.

We start by get the kernel projected matrix $\phi(X)$ by :
$$\phi(X) = [\phi(x_1), \phi(x_2),...,\phi(x_N)]$$
Assume $\phi(X)$ is already decentralized with mean of zero. In the traditional PCA, we can calculate the [[Covariance]] matrix by:
$$\frac{1}{N}XX^T$$
  
With the mapping implemented, we have:
$$C_\mathcal{F} = \frac{1}{N} \phi(X)[\phi(X)]^T = \frac{1}{N}\sum _{i=1} ^N \phi(x^{(i)}) \phi(x^{(i)})^T$$
And in theory, we can solve for the eigenvectors with $C_{\mathcal{F}}u = \lambda u$ , where $u$ is the orthnormal basis we are looking for. However, since $\phi(x)$ is not explicitly defined, we can not directly solve for $\phi(x)\phi(x)^T$. 

## Kernel Trick Conversion

Since in the original [[Principal Component Analysis (PCA)]], we are only solving for the eigenvectors corresponding to the largest eigenvalues. If we consider only $\lambda \neq 0$, we have the following formula:
$$u = \frac{1}{\lambda} \sum _{i=1}^N(\phi(x^{(i)})[\phi(x^{(i)})^Tu])$$
And since $[\phi(x^{(i)})^Tu]$ yields a constant, meaning when $\lambda \neq 0$, the corresponding eigen vector can be represented as the linear combination of all projected data samples $\phi(x^{(i)})$, as:
$$u =  \frac{1}{\lambda}\sum_{i=1} ^N\alpha_i\phi(x^{(i)}) =  \frac{1}{\lambda}\phi(X)\alpha$$
- $\alpha = [\alpha_1, \alpha_2,...,\alpha_N]^T$ 

We can rewrite the original equation without $u$ as:
$$ \frac{1}{\lambda}\phi(X)[\phi(X)]^T\phi(X)\alpha =   \phi(X)\alpha$$

abd multiply $\phi(X)^T$ on both side to get:
$$ \frac{1}{\lambda}[\phi(X)]^T\phi(X)[\phi(X)]^T\phi(X)\alpha =  [\phi(X)]^T\phi(X)\alpha$$
Here, we can replace the projection operation to a Kernel Matrix $K = [\phi(X)]^T\phi(X)$, as:
$$ \frac{1}{\lambda}K\cdot K \alpha =  K\alpha$$
And we can solve for the non-zero eigenvalues through:
$$K \alpha = \lambda \alpha$$
> Note: Because $K$ is a symmetric matrix, its eigenvectors can cover the entire input vector space, thus the formula $K \alpha = \lambda \alpha$ can give all solutions to the formula $K\cdot K \alpha = \lambda K\alpha$

Note $\alpha$ is the eigenvector for the Kernel matrix $K$ where we can directly solve for. However, since we still have
$$u =  \frac{1}{\lambda}\sum_{i=1}^N \alpha_i \phi(x^{(i)}) = \phi(X)\alpha$$
we will not be ables to solve for orthnormal basis directly (and also does not need to).

And since we are looking for orthnormal basis, we have the constraint:
$$u^Tu = 1$$
and from the formula above, we have:

$(\dfrac{1}{\lambda}\phi(X)\alpha)^T(\dfrac{1}{\lambda}\phi(X)\alpha) = 1$

$\dfrac{1}{\lambda^2} \alpha^T \phi(X)^T \phi(X) \alpha=1$

$\dfrac{1}{\lambda^2} \alpha^T K \alpha=1$

$\dfrac{1}{\lambda^2} \alpha^T \lambda \alpha=1$

$\alpha^T\alpha = \lambda$

And we can get the corresponding $\alpha$ values by multiplying $\sqrt \lambda$ 

And for the mapping process, we conduct the [[Eigen Decomposition]] to Kernel Matrix $K$, as
$$KP = \Lambda P$$
where $\Lambda = diag\{\lambda_1,\lambda_2,...,\lambda_n\}$, $P = \{\alpha_1,\alpha_2,...,\alpha_n\}$
(with eigen vectors sorted from max to min)

Here we can write the projected form as:
$$x'^{(i)} = \phi(X)^Tu_i = \phi(X)^T\phi(X)\alpha_i = K\alpha_i = \lambda_i\alpha_i$$

The final projection can be calculated by solving the following equations:
$$X' = P_k^TK$$

## Normalize Mapped Data

> To easily represent the following operation, we have definition:
> $\mathbb{1}_N$ is the matrix of $1/N$ with the dimension $N \times N$ 
> $e_N$ is the colum vector of dimension $N$ with all elements being $1$

We can calculate the averaged mapped vectors by:
$$\bar\phi(x^{(i)}) = \frac{\sum _{i=1} ^N \phi(x^{(i)})}{N} = \frac{1}{N} \phi(X)e_N$$
And here we can get the normalized data:
$$\tilde \phi(X) = \phi(X) - \bar\phi(X)e_N = (I - \frac{1}{N}e_Ne_N^T)\phi(X) = (I - \mathbb{1}_N)\phi(X)$$
And here we have the normalized Kernel matrix as:
$$\tilde K = \tilde\phi(x)^T\tilde\phi(x) = [(I - \mathbb{1}_N)\phi(X)]^T[(I - \mathbb{1}_N)\phi(X)]$$
And with some simplification we have:
$$(I - \mathbb{1}_N)^T \phi(X)^T\phi(X)(I - \mathbb{1}_N) = (I - \mathbb{1}_N)^TK(I - \mathbb{1}_N)$$
With the final equation being:
$$\tilde K = K - \mathbb{1}_NK - K \mathbb{1}_N + \mathbb{1}_NK \mathbb{1}_N$$
