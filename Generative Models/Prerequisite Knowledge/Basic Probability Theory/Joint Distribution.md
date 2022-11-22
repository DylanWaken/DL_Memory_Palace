#ProbabilityTheory
## Joint Distribution
----
The joint CDF of 2 random variables $X$ and $Y$ is referred as the following:

$$F_{X,Y}(x,y) = P(X \leq x, Y \leq y)$$

And the  joint CDF would have the following property:

1: $F_X(x) = F_{X,Y}(x, \infty)$ for any $x$  -> The marginal CDF of $x$
2: $F_Y(y) = F_{X,Y}(\infty,y)$ for any $y$ -> The marginal CDF of $y$

Property as being cumulative density function:

3: $F_{X,Y}(\infty,\infty) = 1$ 
4: $F_{X,Y}(x, - \infty)=F_{X,Y}(-\infty, y)=0$

Getting probability value from CDF:

5: $P(x_1 < X \leq x_2, y_1 < Y \leq y_2 ) = F_{X,Y}(x_2,y_2) - F _{X,Y} (x_1,y_2) - F_{X,Y}(x_2, y_1) + F_{X,Y}(x_1,y_1)$

Calculating the joint CDF:

if X and Y are independent, then
$$F_{X,Y}(x,y) = F_X(x) F_Y(y)$$

### Joint  PDF:

The [[Probability Density]] function is still the derivative of the joint CDF, as follows:

$$f_{X,Y}(x,y) = \dfrac{\partial^2 F_{X,Y}(x,y)}{\partial x \partial y}$$
for independent random variables the joint PDF can be written as:

$$f_{X,Y}(x,y) = f_X(x) f_Y(y)$$
- Note: this will produce a 2 dimensional function

Like in the original PDF definition, the probability of a specific point  is not ensured to be the value on the joint PDF, but the probability of an  $A$ can sill be represented using the function by:

$$\iint_{x \in A} f_{X,Y}(x,y)dxdy = P(x \in A, y \in A)$$


