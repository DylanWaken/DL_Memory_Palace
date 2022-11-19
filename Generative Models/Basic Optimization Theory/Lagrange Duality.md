----
#BasicOptimizationTheory 

Duality Principle is the relation ship between a pair of primal and dual problems. The objective of both problems have inversed direction, in which if the primal problem is minimizing, then the dual problem will be maximizing.

Any feasible solution to the primal problem (minimizing) is  at least as large as the feasible solution for the dual problem (maximizing).

- **Weak Duality** : There exists a non-zero gap between the primal and dual solutions
- **Strong Duality** : The primal and dual solutions are equal (gap is zero)

The Lagrange Duality is the part of the duality principle that process non-linear optimization problems, as:
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0 \quad h_j(x) =0$$
And the Lagrangian is defined with KKT multipliers ([[Karush–Kuhn–Tucker Conditions]]) as:
$$\mathcal{L}(x, \mu, \lambda) = f(x) + \sum _{i=1} ^m \mu_i g_i(x) + \sum _{j=1} ^l \lambda_jh_j(x)$$
And with $\mu$ and $\lambda$ called the dual variables. The Lagrange dual function is defined as:
$$g(\mu,\lambda) = \inf _{x \in \mathcal{D}} \mathcal{L}(x, \mu, \lambda)$$
- $\inf _x$ stands for the maximum value of x in the given set (infimum)
-  $\mathcal{D}$ is the domain of x with non-empty interior. 

In the dual problem. $g$ will be the new objective function.

## Convex Problems

For the special case of [[Convex Optimization Problem]] with inequality constraints:
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0 $$
The lagrange dual problem is:
$$\max_x \inf_x(f(x) + \sum _{i=1} ^m \mu_i g_i(x)) \quad s.t. \quad \mu_i \geq 0 ,i=1,..,m$$
For the convex function $f(x)$ and $g_i(x)$ , the infimum is achieved when the gradient is equal to zero, and the problem is derived as:

$$\max_{x, \mu} f(x) + \sum _{i=1} ^m \mu_i g_i(x) $$
$$ s.t. \quad \mu_i \geq 0 ,i=1,..,m \quad \nabla f(x) + \sum _{i=1} ^m \mu_i \nabla g_i(x) = 0$$

