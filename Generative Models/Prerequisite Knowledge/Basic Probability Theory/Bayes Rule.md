#ProbabilityTheory 
required knowledge:
[[Conditional Probability]],
[[Conditional Independence]], 
[[Joint Distribution]]

----
### Conditional Distribution:

Conditional distribution represents the probability distribution of one variable given the other variable(s). The discrete version of such distribution looks like:

$$P_{Y|X}(y|x) = \frac{P_{X,Y}(x,y)}{P_X(x)}$$

For continuous random variables, we define the conditional PDF of the random variable Y given X=x to be:

$$f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}$$

provided $f_X(x)$ is not 0

### Bayes Rule:

The bayes rule provided the ways to calculate conditional distributions from other conditional distributions:

For discrete random variables:

$$P_{Y|X}(y|x) = \frac{ P_{X|Y}(x|y) P_Y(y)}{\sum_{y \in Val(Y)} P_{X|Y}(x|y')P_Y(y')}$$

The thing can be also written as:
$$P(y|x)=\frac{ \exp(\alpha_y)}{\sum_{y \in Val(Y)} \exp(\alpha_{y'})}, \quad\alpha_y = \log(P_{X|Y}(x|y) P_Y(y))$$
The terms on the bottom is the [[Marginal Distribution]] of X

For continuous random variables:

$$f_{Y|X}(y|x) = \frac{ f_{X|Y}(x|y) f_Y(y)}{\int_{-\infty}^\infty f_{X|Y}(x|y')f_Y(y')dy'}$$

With the independence of two random variables defined as $F_{X,Y}(x,y) = F_X(x)F_Y(y)$ :

$$f_{X,Y}(x,y) = f_X(x)f_Y(y)$$
$$f_{Y|X}(y|x) = f_Y(y)$$

without independence, we can get the conditional CDFs of the distributions by:

$$F_{Y|X}(y|x) = \int_{-\infty}^y \frac{f_{X,Y}(x, \alpha)}{f_X(\alpha)}d\alpha$$
