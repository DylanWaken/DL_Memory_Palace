#ProbabilityTheory
## Expectations
----
Suppose $X$ is a discrete random variable with [PMF](Probability%20Mass.md) $P_X(x)$ and $g(x)$ is an arbitrary scalar function. In the following case, $g(x)$ can be considered as a random variable, and the calculation for expectation is defined as:

$$E[g(x)] = \sum _{x \in Var(X)} g(x) P_X(x)$$

In the case which $g(x) = x$ , the expectation $E[X]$ is exactly the mean of the distribution, in which:

$$E[X] =  \sum _{x \in Var(X)} x P_X(x)$$
In the case of continuous random variable $X$ and its [PDF](Probability%20Density.md) $f_X(x)$:

$$E[g(x)] = \int _{- \infty} ^{\infty} g(x) f_X(x) dx$$

Expectation can be viewed as a "weighted average" of the function $g(x)$ by the probabilistic distribution of $X$. Note that the result of expectation is a **number** (or a scalar value)

Some important properties of expectations:

$E[a] = a$ for any constant value $a \in \mathbb{R}$ 

linearity properties:

$E[a f(x)] = a * E[f(x)]$ 
$E[f(x) + g(x)] = E[f(x)] + E[g(x)]$ 

