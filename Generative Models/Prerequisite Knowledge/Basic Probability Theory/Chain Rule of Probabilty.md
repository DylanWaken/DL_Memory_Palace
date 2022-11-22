----
#ProbabilityTheory 
required knowledge:
[[Bayes Rule]]

When we have multiple random variables to consider (more than 2), the [[Joint Distribution]] of the random variables $X_1,X_2,$ ... $,X_n$ is defined as:

CDF:

$$F_{X_1,...,Xn}(x_1,x_2,...,x_n) = P(X_1 \leq x_1, X_2 \leq x_2, ...,X_n \leq x_n)$$

PDF:
 $$f_{X_1,X_2...X_n} (x_1,x_2...x_n) = \dfrac{\partial^nF_{X_1...X_n}(x_1,...,x_n)}{\partial x_1...\partial x_n}$$

To get the conditional distribution of one variable given the others, with the [[Bayes Rule]]:

$$f_{X_1|X_2...X_n}(x_1|x_2...x_n) = \frac{f_{X_1,...X_n}(x_1,x_2...x_n)}{f_{X_2...X_n}(x_2...x_n)}$$

To calculate the [[Marginal Distribution]] of one variable, we have

$$f_{X_1}(x_1) = \int_{-\infty}^\infty ... \int_{-\infty}^\infty f_{X_1,...X_n}(x_1,x_2...x_n) dx_2...dx_n$$

The [[Joint Distribution]] chained all the different random variables together, and the ***chain rule*** is an iterative process that we can decompose the [[Joint Distribution]] following the [[Bayes Rule]], to covert it into the product of conditional distributions.

$f(x_1,x_2,...,x_n)$
$= f(x_n | x_1 ... x_{n-1}) \cdot f(x_1,...,x_{n-1})$                                                //decomposition with [[Bayes Rule]]
$= f(x_{n} | x_1...x_{n-1}) \cdot f(x_{n-1} | x1...x_{n-2}) \cdot f(x_1,...,x_{n-2})$
$= ...$

With this process going on, we get the final formation of chain rule as:

$$f(x_1,...,x_n) = f(x_1) \cdot \prod _{i=2}^{n} f(x_i | x_1 ...x_{i-1})$$

