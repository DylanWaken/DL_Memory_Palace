----
#BasicMachineLearning 

The specifal form of [[Tikhonov Regularization]] that prefered the smaller norms for the weights or parameters vector. The name L2 Regularization from the L2 Norm used in the regularization term.

The original TR function:
$$||X\theta-y||_2^2 + ||\Gamma \theta||_2^2$$
With the L2 regularization changing the definition as:
$$||X\theta-y||_2^2 + ||\alpha I \theta||_2^2$$
The optimal solution is now as:
$$\hat{\theta} = (X^TX + \alpha^2I)^{-1} X^Ty$$
In the general form:
$$J(\theta)-||\alpha I\theta||_2 ^2$$

## Probabilistic Understanding

From the [[Regularization]] note, we have the current [[Maximum Likelihood Estimation]] being:
$$\mathcal{l}(\theta) = \sum _{i=1} ^N log(p(y^{(i)}|x^{(i)};\theta)) + log(f(\theta))$$
And in this form we assume $f(\theta)$ is a [[Gaussian Distribution]], this will turn our optimization target to be (proof is the same as the original LMS algorithm):
$$\mathcal{l}(\theta) = \sum _{i=1} ^N log(p(y^{(i)}|x^{(i)};\theta) ) - \frac{1}{2\sigma^2}||\theta||^2$$
If we replace the first term with the linear regression [[Likelihood]]:
$$- \frac{1}{2\sigma_0^2} \sum _{i=1} ^N (y^{(i)} - \theta^Tx^{(i)})^2- \frac{1}{2 \sigma^2}||\theta||^2$$
And by switching to argmin with vector notations, we will have: 
$$argmin_\theta \,||X\theta-y||_2^2 + ||\theta||_2^2$$
The term $\frac{1}{2 \sigma^2}$ as the prefix of our regularization term corresponds to the desired variance of our parametersm at the same position of $\alpha$. If we set the $\alpha$ from the original function greater, we are having our parameter distribution narrower, with parameters approaching 0.

