#ProbabilityTheory 
## Variances
----
The variance of the random variable $X$ is the measure of how concentrated the distribution of a random variable $X$ around its mean (or [[Expectation]])

$$Var[X] = E[(X - E[X])^2]$$

The variabce can be also derived into an alternative form:

$$Var[X] = E[X^2] - (E[X])^2$$
Proof:

$E[(X-E[X])^2]$
$= E[X^2 - 2E[X]*X + E[X]^2]$
$=E[X^2]-2E[X]E[X] + E[X]^2$
$= E[X^2] - (E[X])^2$

Variance have the following properties:

$Var[a] = 0$ for any const $a \in \mathbb{R}$

$Var[a * f(x)] = a^2 * Var[f(x)]$

For continuous random variables:

$$Var[X] = \int _{- \infty} ^{\infty} x^2 f_X(x) dx - (\int _{- \infty} ^{\infty} x f_X(x) dx)^2$$

