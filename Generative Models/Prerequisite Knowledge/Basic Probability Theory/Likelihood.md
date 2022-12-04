----
#ProbabilityTheory 
Required Knowledge: 
[[Probability Mass]]
[[Expectation]]
[[Conditional Independence]]
[[Joint Distribution]]

Likelihood function is the ***joint probability*** of  observed data viewed as a function to the parameters of a statistical model or distribution

Likelihood measure how closely a given set of data fits a distribution. By intuition, the better a distribution or model fits the dataset, the higher this value would be.

![[Likelihood.gif]]

For a distribution $P$ parameterized (;) by parameter(s) $\theta$ , we write this as:

$$P(X; \theta)$$
- Note: $\theta$ is **NOT** random variables  

To measure how well the current configurations of the parameter(s) fits the real dataset, we define the likelyhood funtion as:

$$\mathcal{L}(\theta) = \mathcal{L}(\theta;\vec{y}\,) = p(y_1, y_2,...,y_n; \theta)$$
- y is the set of observed data points
- $\theta$ is the parameter(s)

If we assume that all data $y$ is independent from each others, we can use the rule of independence in joint probability to decomposite this as:

$$\mathcal{L}(\theta; y) = p(\vec{y}; \theta) = \prod_{i=1}^n p(y^{(i)};\theta)$$ 
For an easier understanding, we are just throwing all the data into the distribution or model and check the result. If the desity of the data matches the distribution, then we will achieve the maximum likelihood distribution on the observed data. 

Likelihood is the joint density of data.

In a more precise explanation, we have:
$$L(\theta) = L(\theta|y) = p(y;\theta)$$

### log likelihood

In practice, since the product over all the model outputs on the data is both hard to operate and computationally inefficient, we normally replace the likelihood function with the log likelihood function, which is:

$$\mathcal{l}(\theta;\vec{y}) = \log(\mathcal{L}(\theta; y))$$

Because logrithm function is monotonically increasing, the remapping of the function will not change the maximum of the function. log can decompose product into summation:

$$\mathcal{l}(\theta;\vec{y}) = \log( \prod_{i=1}^n p(y^{(i)};\theta)) = \sum _{i=1} ^n \log( p(y^{(i)};\theta))$$

