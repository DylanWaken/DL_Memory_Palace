## Marginal Distribution
----

Marginal distribution is the idea derived from [[Joint Distribution]]

Marginal distribution is the "conditional" distribution of a specefic random variable or a set of specific random variables witout the reference to other random variables in the system.

in this case, the marginal distribution CDF is defined as:

1: $F_X(x) = F_{X,Y}(x, \infty)$ for any $x$              ->   The marginal CDF of $x$
2: $F_Y(y) = F_{X,Y}(\infty,y)$ for any $y$               ->   The marginal CDF of $y$

In this 2 dimensional distribution graph, the function at positive $\infty$ on both axis stands for the point where one random variable is not influencing the overal distribution, since the value of its part will always be 1, and this gives the "marginal" distribution of the other variable.

To solve for marginal PDF:

for all x:
$$f_X(x)=\int _{-\infty} ^\infty f_{X,Y}(x,y)dy$$ 
for all y:
$$f_Y(y)=\int _{-\infty} ^\infty f_{X,Y}(x,y)dx$$
