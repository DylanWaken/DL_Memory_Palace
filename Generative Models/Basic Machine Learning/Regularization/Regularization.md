----
#BasicMachineLearning 

Regularization is a technique used for tuning the function by adding an additional penalty term in the error function. The additional term controls the excessively fluctuating function such that the coefficients don’t take extreme values.

![[Overfit.png]]

By intuition, regularization is looking for the minimal complexity for models to complete given tasks. By limiting the "complexity" of the model parameters, overfitting of the model can be limited. 

regularization is usually conducted in the following manner:

$$J(\theta) + r(\theta)$$

- wihe $r(\theta)$ being a part of model loss that measures complexity, and is also being considered as a optimization target.

For the most common regularization, we consider complexity through norms pf parameter vectors.

- L0 norm or $||\cdot||_0$ , which is the amount of non-zero params in param vectors
- L1 norm or $||\cdot||_1$ , which is the sum of absolute values
- L2 norm or Euclidean Norm $||\cdot||_2$ , squareroot of  the sum of squared elements

Since L0 is directly a part of model design, so we consider L1 and L2 norms, which corresponds to [[L1 Regularization]] and [[L2 Regularization]].

## Probabilistic Explanation

If we assume parameters $\theta$ is subjected to a optimal distribution:
$$\theta \sim f(\theta)$$
if we add this distribution to the optimization target:
$$\mathcal{L}(\theta) = \mathcal{L}(\theta;X,\vec{y}) = p(\vec{y}|X;\theta) \cdot f(\theta)$$
And run the maximum [[Likelihood]] estimation:
$$\mathcal{L}(\theta) = (\prod _{i=1} ^N p(y^{(i)}|x^{(i)};\theta) ) \cdot f(\theta)$$
Take the log [[Likelihood]]:
$$\mathcal{l}(\theta) = \sum _{i=1} ^N log(p(y^{(i)}|x^{(i)};\theta) + log(f(\theta)))$$
From here, we are able to derive the term $log(f(\theta))$ with the assumed distribution. Interestingly, if we have $\theta$ subject to [[Laplace Distribution]], we get [[L1 Regularization]] term, and with $\theta$ subject to [[Gaussian Distribution]], we have L2 regularizatoin term. 

(detailed process in L1 and L2 notes)