----
#LinearAlgebra 

Countour integration is a special branch of integrals used in evaluating certain integrals along paths in the complex plane. 

A **smooth curve** is a curve $z : [a,b] \rightarrow C$ with non-vanishing continuous derivative with each point only traversed once (z is one-to-one) with the only exception being the endpoitns ($z(a) = z(b)$). If the endpoints are repeated, then the curve is closed, and the derivative is required to be existed on the closed end such that ($z'(a) = z'(b)$).

A **directed smooth curve** is the natural ordering of the points on the curve by some parameterization: $z(x)$ comes before $z(y)$ if $x < y$. There can only exist two orders on the same smooth curve.  

A **contour** is a directed curve made up of a finite sequence of directed smooth curves whose endpoints are matched to give a single direction. 

For a sequence of curves $\gamma_1, \gamma_2,...,\gamma_n$, the following condition must be satisfied: the terminal point of $\gamma_i$ must coincide with the initial point of $\gamma_{i+1} \forall i, 1 \leq i < n$.

And we can define a contour $\Gamma$ as:
$$\Gamma = \gamma_1 + \gamma_2 +...+\gamma_n$$
## Contour Integral

The contour integral for a complex function $f:C\rightarrow C$ is the generalized form of real integrals, as given:
$$f(t) = u(t) + iv(t)$$
And the integral of $f$ over the interval $[a,b]$ is defined as:
$$\int _a^b f(t)dt = \int_a^b u(t)dt + i\int_a^b v(t)dt$$
Let $f:C \rightarrow C$ be a continuous funciton on the directed smooth curve $\gamma$ and $z:R\rightarrow C$ be any parameterization (direction) of the curve. The integral along $\gamma$ can be written as:
$$\int _\gamma f(z)dz = \int_a^b f(z(t))z'(t)dt$$
- where $z$ is the function of $t$ where the domain is $a \leq t \leq b$, and the direction of t increasing on the curve would be the direction of the curve.
$$\int _\gamma f(z)dz = F(z_2) - F(z_1)$$
If $\gamma$ is a closed curve, and $z_1 = z_2$, then the contour integral would be zero. 

In the case of $\gamma$ being a closed curve, we write the function as:
$$\oint _\gamma f(z)dz$$
