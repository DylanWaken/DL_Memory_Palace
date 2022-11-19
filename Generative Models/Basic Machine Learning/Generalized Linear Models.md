------
#BasicMachineLearning 

Gemeralized linear models are the collection of all forms of linear models that are used in regressions and classifications.  [[Linear Regression]] and [[Logistic Regression]] are all specific cases in the generalized linear models. 

## Exponential Family Distributions

The exponential family distribution function looks like this:

$$p(y;\eta) = b(y) \exp(\eta^T T(y) - \alpha(\eta))$$

- $\eta$ is the **natural (canonical) parameter** of the distribution
- $T(y)$ is the **sufficient statistic** (normally $T(y) = y$)
- $\alpha (\eta)$ is the **partition function** (make sure the thing integrate to 1) 

A set of common distributions can be derived to this standard form ([[Gaussian Distribution]] and Bernouili Distribution as an example, process can be found in CS229 notes)


## Construction of GLM

For any given distributions in the exponential family, we can construct a generalized linear model to approach and estimate it. 

The 3 pre-conditions for construct GLM for $P(y|X)$

- 1: $y | X ; \theta \sim ExponentialFamily(\eta)$  
- 2: With $T(y) = y$ , the prediction $h(X)$ should satisfy $h(X)$ = $E[y|X]$
- 3: The natural parameter is linearly related to $X$ : $\eta = X\theta$

In this case, we call $\eta$ the linear predictor of the GLM

Since our hypothesis function is producing the mean or the expectation of the exponential family distribution, to apply the linear predictor, we need to assure that $E[y|X]$ have the linear relationship with $\eta$ .

To assure the relationship, we apply the ***Link Function*** $g^{-1}(\eta)$ to the predictor for the linear relationship, such that: 

$$g(E[y|X]]) = X\theta = \eta$$

The inverse of the Link Function is also called the ***Mean Function***, as we can calculate the mean value from the linear predictor $\eta$ 
