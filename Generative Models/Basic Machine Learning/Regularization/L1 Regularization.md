-----
#BasicMachineLearning 

L1 Regularization is the generalized form of [[LASSO]] regularization. It is designed to set a hard limit for the maximum value of the absolute values of the parameters. 

For the loss function, we have in linear regression:
$$J(\theta)= || X\theta - y||_2^2 + \lambda||\theta||$$
Or generally for all models:
$$J(\theta)' = J(\theta) + \lambda||\theta||$$
The formal proof of this regularization term is in [[LASSO]] , and its generalized solution for linear regression is in [[LASSO Regression]]

## Probabilistic Understanding:

Another form of understanding is not exactly the same.
From the [[Regularization]] note, we have the current [[Maximum Likelihood Estimation]] being:
$$\mathcal{l}(\theta) = \sum _{i=1} ^N log(p(y^{(i)}|x^{(i)};\theta)) + log(f(\theta))$$
If we assume that our parameters are distributed in [[Laplace Distribution]]:
$$f(\theta; \mu, b) = \frac{1}{2b} \exp(-\frac{\theta-\mu}{b})$$
And by throw this into the [[Likelihood]] function:
$$\mathcal{l}(\theta) = \sum _{i=1} ^N log(p(y^{(i)}|x^{(i)};\theta)) + \log(\frac{1}{2b}) + log(\exp(-\frac{\theta-\mu}{b}))$$
removing constants and we will have:
$$\mathcal{l}(\theta) = \sum _{i=1} ^N log(p(y^{(i)}|x^{(i)};\theta)) -\frac{1}{b}||\theta||$$

