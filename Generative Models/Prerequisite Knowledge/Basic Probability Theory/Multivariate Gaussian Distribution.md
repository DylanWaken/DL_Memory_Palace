----
#ProbabilityTheory 
Required knowledge :
[[Covariance Matrix]]
[[Gaussian Distribution]]

![[MultiVariate Gaussian.png]]

Maltivariate [[Gaussian Distribution]] is the higher dimensional version of the [[Gaussian Distribution]], it features the random variable vector instead of the single random variable. The general formula looks like this:

$$\mathcal{N}(\vec{x}; \vec{\mu}, \Sigma) = \frac{1}{(2\pi)^{n/2}} |\Sigma|^{-\frac{1}{2}} exp(-\frac{1}{2}(x - \mu)^T\Sigma^{-1}(x-\mu))$$

Where:

- $n$ is the number of variables in $\vec{x}$
- $\Sigma \rightarrow \mathbb{R}^{n \times n}$ is the [[Covariance]] matrix
- $\mu \rightarrow \mathbb{R}^n$  is the mean vector

In the multivariate [[Gaussian Distribution]], changing the mean vector would change the center location of the distribution in the n dimension space, and the elements on $diag(\Sigma)$ would determin the spread of each corresponding [[Gaussian Distribution]] (graph 0,1). 

The rest of elements in the [[Covariance]] matrix would determin how tilted the graph is, or how the distributions correlated to each others. (as shown in graph 5,6,8,9)

## Derive the Multivariate [[Gaussian Distribution]]
----

Suppose we have the 2 following 1d gaussian distributions:

$$p(x_1) = \frac{1}{Z_1} \exp(-\frac{(x_1-\mu_1)^2}{2\sigma_1^2})$$
$$p(x_2) = \frac{1}{Z_2} \exp(-\frac{(x_2-\mu_2)^2}{2\sigma_2^2})$$
- $Z_1, Z_2$ are just constants (repalcement of the 2$\pi$ stuff)

To get the multivariate distribution, we define the random vectors and the covariate matrix (assuming there are no correlations between the distributions):

$$x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \quad \mu = \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix} \quad \Sigma = \begin{bmatrix} \sigma_1^2 \quad 0 \\ 0 \quad \sigma_2^2 \end{bmatrix}$$

Since the distributions are not correlated (independent), we can write the multivariate distribution in terms of products:

$$p(\vec{x}) = p(x_1)p(x_2) = \frac{1}{Z_1Z_2} exp(-\frac{1}{2}(x - \mu)^T\Sigma^{-1}(x-\mu))$$
