#ProbabilityTheory
- requires knowledge : [[Expectation]], [[Joint Distribution]]
---

For the [Joint Distribution](Joint%20Distribution.md) on random variable $X$ and $Y$, the [expectation](Expectation.md) is calculated through:

$$E[g(X,Y)]=\sum_{x \in Val(X)} \sum_{y \in Val(y)} g(x,y)f_{X,Y}(x,y) $$
and in the continuous case:

$$E[g(X,Y)] = \int_{-\infty}^\infty\int_{-\infty}^\infty g(x,y)F_{X,Y}(x,y)dxdy$$

With the expecation defined, the covariance is given as:

$$Cov[X,Y] = E[(X-E[X])(Y-E[Y])]$$

and with a similar rearranging process as the original [[Variance]] we have

$$Cov[X,Y] = E[XY] - E[X]E[Y]$$

![[Visualize Covariance.png]]

- Visualized covariance : red stands for positive covariance and blue stands for negative covariance

Covariance can be viewed as the correlation between the random variables. For discrete random variables, it is the sum of total distance for each data point to the mean ([[Expectation]]) of all random variables multiplied. The value of covariance would increase given the strength of the correlation between random variables. if the variables are not correlated, then covariance will be 0.

[[Expectation]] and Covariance have the following properties:

- 1: Linearity -> $E[f(X,Y) + g(X,Y)] = E[f(X,Y)] + E[g(X,Y)]$
- 2: $Var[X + Y] = Var[X] + Var[Y] + 2*Cov[X,Y]$
- if X and Y are independent random variables, then $Cov[X,Y] = 0$
- if X and Y are independent, then $E[f(x)g(y)] = E[f(x)] * E[g(y)]*$



