----
#BasicMachineLearning 

## Feature Mapping:

Feature mapping is the mapping of the input features such that the mapped features have a linear relationship with the non-linear target estimating function.  

For example $y = \theta_0 + \theta_1x + \theta_2x^2 + \theta_3x^3$: $\mathbb{R} \rightarrow \mathbb{R}$:

We can use a mappin function $\phi$ such that:

$$\phi(x) = \begin{bmatrix}
1 \\
x \\
x^2\\
x^3
\end{bmatrix}$$
And we can have the $\theta$ vector by doing the remap and apply our normal linear approaches to the problem.

In the linear regression interative solution, well will swap $x$ for $\phi(x)$ and solve the optimal parameters for $\theta^T \phi(x)$ 

## Kernel Method

Here the [[Least Mean Squares (LMS)]] is used:

In an iterative linear regression problem, if we initialize $\theta$ to be zero, and with $N$ training samples, we can represent $\theta$ as the linear combination of all the feature maps $\phi(x)$ , as:
$$\theta = \sum _{i=1}^N\beta_i \phi(x^{(i)})$$
 And by swap out the original update function, we have:
$$\theta := \theta + \alpha\sum_{i=1}^N (y^{(i)}-\theta^T \phi(x^{(i)}))\phi(x^{(i)})$$
$$\theta := \sum _{i=1} ^N (\beta_i + \alpha(y^{(i)}-\theta^T \phi(x^{(i)})))\phi(x^{(i)})$$
And where we can easily derive the update rule for every coefficient:
$$\beta_i := \beta_i + \alpha(y^{(i)}-\theta^T\phi(x^{(i)}))$$
When we swap the final $\theta$ in the expression, we have:
$$\forall i\in [1,n], \beta_i:=\beta_i + \alpha(y^{(i)} -\sum_{j=1}^N\beta_j\phi(x^{(j)})^T\phi(x^{(i)}))$$
- $\phi(x^{(j)})^T\phi(x^{(i)})$ is a inner product, also written as $<\phi(x^{(j)}), \phi(x^{(i)})>$ 

A **Kernel function** is defined upon the concept of inner product, it is a function mapping $\mathcal{X} \times \mathcal{X} \rightarrow \mathbb{R}$ satisfying:
$$K(x,z) \triangleq <\phi(x), \phi(z)>$$

And our prediction will be :
$$\forall i\in [1,n], \beta_i:=\beta_i + \alpha(y^{(i)} -\sum_{j=1}^N\beta_jK(x^{(i)},x^{(j)}))$$
SInce K will iterate all $i$ and $j$, $K \in \mathbb{R}^{N \times N}$, And in vector notation:
$$\beta := \beta + \alpha(\vec{y} - K\beta)$$
Note: The kernel matrix is a [[Gram Matrix]]

## Kernel Properties

In our definition, kernels themselves would include the mapping of features in its definition.  

For example, $K(x,z) = (x^Tz)^2$ woule have the following feature remap:
$$\phi(x) = \begin{bmatrix}
x_1x_1\\
x_1x_2\\
...\\
x_1x_N\\
x_2x_1\\
...\\
x_Nx_{N-1}\\
x_Nx_N
\end{bmatrix}$$
Since:
$$(x^Tz)^2 =(\sum_{i=1}^Nx_iz_i)(\sum_{i=1}^Nx_iz_i) = \sum ^N _{i,j=1} (x_ix_j)(z_iz_j)$$
Since inner products measures the similarities between vectors, the output of a kernel function $K(x,z)$ will be corresponding to the similarity between $x,z$. 

In some case, if we comprehend kernel from this perspective, and we can define a reasonable measure of that similarity:
$$K(x,z) = \exp(-\frac{||x-z||^2}{2\sigma^2})$$
- This kernel is the **Gaussian Kernel** , derived from [[Gaussian Distribution]] 
- The kernel produce 1 when $x$ and $z$ are close, and zero when $x \perp z$

## Kernel Conditions

If we have a set of finite vectors $\{x^{(1)} ... x^{(n)}\}$ , A **kernel matrix** of specific kernel $K(x,z)$ is:
$$K_{ij} = K(x^{(i)},x^{(j)})$$
**The Mercer Theorem**:

Let $K : \mathbb{R} ^d \times \mathbb{R} ^d \rightarrow \mathbb{R}$  be  given. For $K$ to be a valid kernel, it is necessary and sufficient that for any $\{x^{(1)} ... x^{(n)}\}$ , the corresponding kernel matrix is symmetric positive semi-definite ([[Definite Matrix]]).

