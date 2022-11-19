----
#BasicOptimizationTheory 

Lagrange multiplier is the method used in optimization problems that converts the equality constraints to the components of the objective function. With such conversions in place, the derivative methods used in finding optimal values can be applied. 

The ***lagrange multiplier theorem*** states that for the given problem:
$$\min _x f(x) \quad s.t. \quad g(x) =0$$
For objective function $f:\mathbb{R}^n \rightarrow \mathbb{R}$ and equality constraint $g : \mathbb{R}^n \rightarrow \mathbb{R}^c$. Lex $\hat{x}$ be an optimal solution for the [[optimization problem]] such that $rank(Dg(\hat{x})) = c < n$ (where $Dg(\hat{x}))$ denotes the matrix of partial derivatives $[\partial g_j / \partial x_k]$)

The there exists a specific lagrange multiplier $\hat{\lambda}$ such that:
$$Df(\hat{x}) = \hat{\lambda}^TDg(\hat{x})$$
>The Lagrange multiplier theorem states that at any local maxima (or minima) of the function evaluated under the equality constraints, if constraint qualification applies, then the gradient of the function (at that point) can be expressed as a linear combination of the gradients of the constraints (at that point), with the Lagrange multipliers acting as coefficients. 
> Or still, saying that the directional derivative (gradient) of the function is 0 in every feasible direction.

With the above theorem, we can convert the original problem into the following form:
$$L(x, \lambda) = f(x) + \lambda g(x)$$
- This function is called ***Lagrangian Function*** or ***Lagrangian of the problem***. 

A detialed walkthrough, explanations and samples can be found on this wikipedia link:
https://en.wikipedia.org/wiki/Lagrange_multiplier

The version of Lagrange Multiplier that works for non-equality constraints is called the [[Karush–Kuhn–Tucker Conditions]]


## Single Constraint

In the problem of optimizing ($x$ is the n-dimensional vector):
$$\min _x f(x) \quad s.t. \quad g(x) =0$$
When we derive the function into its Lagrangian function (the minus sign is just for easier processing):
$$L(x, \lambda) = f(x) - \lambda g(x)$$
If there exists $f(x_0)$  being the maximum of function $f(x)$ for the constrainted [[optimization problem]] and $\nabla g(x) \neq 0$ , then there exists a value $\lambda_0$ making the point $(x_{0_0} ... x_{0_n}, \lambda_0)$ a stationary point for the Lagrangian function (where  the first partial derivatives of $L$ are zero). This is the necessary condition for achieve optimal solutions

To solve for that point, we incorporate it into the equation to solve:
$$\nabla_{x, \lambda} L(x, \lambda) = 0$$
- Note that $\nabla _\lambda L(x, \lambda) = 0$ if and only if $g(x) = 0$ 

And where we can derive the alternative form of the equation that:
$$\nabla_xf(x) = \nabla_x\lambda g(x)$$
And where we can solve for the unknown vector $x$ 

## Multiple Constraints

For multiple equality constraints, the problem is in the form 
$$\min _x f(x) \quad s.t. \quad g_i(x) =0 \quad i \in \{1,2,..,m\}$$
And it lagrangian form will be:
$$L(x, \lambda_1....\lambda_m) = f(x) - \sum ^m _{i=1} \lambda_ig_i(x)$$
And the problem is still solving:
$$\nabla _{x,\lambda_1...\lambda_m}L(x, \lambda_1....\lambda_m) = 0$$
