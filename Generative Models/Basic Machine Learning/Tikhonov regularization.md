----
#BasicMachineLearning 

Tikhonov [[regularization]] is the methodology for stablize numerical solutions for inverse and ill-posed problems (problems with more than one unique solution).

In the original linear regression problem, we seeks to solve $\theta$ such that:
$$X\theta = y$$
However, since $X$ and $y$ can be with any dimension with train data size $N$, we may have the system to be [[Overdetermined]] or underdetermined (less equations than needed). This is called a ill-posed linear problem, and $X$ may have a ill-determined [[Rank]].

In the original [[Least Mean Squares]] Estimation, we have to minimize:
$$||X\theta-y||_2^2$$
- where $||\cdot||_2$ is the Euclidean Norm

In order to have the solutions better converging toward to desired outcome, we add a regularization term to the minimizing target:

$$||X\theta-y||_2^2 + ||\Gamma \theta||_2^2$$
- $\Gamma$ is the Tikhonov matrix 

By using this definition and run the optimization process, we have the optimal soluiton being:
$$\hat{\theta} = (X^TX + \Gamma^T \Gamma)^{-1} X^Ty$$
A specific case of Tikhonov [[regularization]] is the [[L2 regularization]], but with the regularizing term set as $\Gamma = \alpha I$ . This regularization term have the tendency of reducing the norm for vector $\theta$. 

Another explanation why TIkhonov regularization works:

> The function acts as a [[Low Pass Filter]] in the forward direction where $X$ maps $\theta$  to $y$. Therefore, in solving the inverse-problem, the inverse mapping operates as a [[High Pass Filter]] that has the undesirable tendency of amplifying noise (eigenvalues / singular values are largest in the reverse mapping where they were smallest in the forward mapping)




