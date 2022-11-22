----
#BasicOptimizationTheory 

Karush-Kuhn-Tucker Conditions (KKT) is the first derivative test (or first order necessary conditions) for solving non-linear [[Optimization Problem]] provided the constraints are satisfied.  The KKT conditions is the generalized [[Lagrange Multiplier]] methods that allows operations beyond equality constraints. 

## Karush-Kuhn-Tucker Theorem

For the [[Optimization Problem]] as follow:
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0 \quad h_j(x) =0$$
where $x \in X$ is the optimization variable chosed from a convex subset of $\mathbb{R}^n$ 
We define the Lagrangian of this problem as:
$$\mathcal{L}(x, \mu,\lambda) = f(x) + \mu^Tg(x) + \lambda^Th(x)$$
- $\mu$ is the inequality constraint KKT multipliers, $g(x) = [g_1(x), ..., g_m(x)]$ 
- $\lambda$ is the equality constraint Lagrange multipliers, $h(x) = [h_1(x),...,h_l(x)]$

The ***Karush-Kuhn-Tucker Theorem*** states that: If $(x^*, \hat{\mu})$ is a ***saddle point*** of Lagrangian function $\mathcal{L}(x, \mu)$ in $x \in X$, $\mu \geq 0$, then $x^*$ is an optimal vector for the above [[Optimization Problem]]. 

The proof of KKT Theorem used hyperplane separation theorem, since the definition is the same as finding a supporting hyperplane on the feasible set $\Gamma = \{x \in X : g_i(x) \leq 0, i=1...m\}$ 

## KKT Conditions

For the optimization problem: 
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0 \quad h_j(x) =0$$
- $f : \mathbb{R}^n \rightarrow \mathbb{R}$ , $g_i : \mathbb{R}^n \rightarrow \mathbb{R}$ , $h_j : \mathbb{R}^n \rightarrow \mathbb{R}$   
   
 If $x^*$ is a local optimum and the optimization problem satisfies the constraints, then there exists constants $\mu_i (i=1,...,m)$ and $h_j (j=1,...,l)$ , called KKT multipliers, such that the following groups of conditions holds:

  - Stationary: For minimizing:$$\partial f(x^*) + \sum _{j=1} ^l \lambda_j\partial h_j(x^*) + \sum _{i=1} ^m \mu_i \partial g_i(x^*) = 0$$
  - Stationary: For maximizing:$$-\partial f(x^*) + \sum _{j=1} ^l \lambda_j\partial h_j(x^*) + \sum _{i=1} ^m \mu_i \partial g_i(x^*) = 0$$
  - Primal feasibility: 
 
	$h_j(x^*) = 0$  for $j=1,...,l$
	$g_i(x^*) \leq 0$ for $i = 1,...,m$

- Dual feasibility:

	$\mu_i \geq 0$, for $i = 1,..,m$ 

- Complementarity:
$$ \mu_i g_i (x^*) = 0$$
In the complementarity condition, there are only two cases:

$\mu_i = 0$ and $g_i(x^*) \neq 0$ , meaning the constraint is not active
$\mu_i \neq 0$ and $g_i(x^*) = 0$ , meaning the constraint is active (on the boarder of feasible set) 

A graphical explanation can be found below:
![[KKT.png]]
## Proof of Dual Feasibility

The reason for KKT multipliers to be greater than 0 is as following:

Since for $x^*$ to be the optimal solution for the inequality constraints
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0$$
we have:
$$\partial f(x^*)  + \sum _{i=1} ^m \mu_i \partial g_i(x^*) = 0$$
And in the gradient form:
$$\nabla_x f(x^*) + \sum _{i=1} ^m \mu_i\nabla_xg_i(x^*) = 0$$
Where we have:
$$-\nabla_x f(x^*) = \sum _{i=1} ^m \mu_i\nabla_xg_i(x^*)$$
Assume we have two active constraints which $g_1(x^*) = 0$ and $g_2(x^*) = 0$, then $x^*$ must be on the intersection of $g_1(x^*)$ and $g_2(x^*)$. Since  $-\nabla_x f(x^*)$ is the linear combination of constraint gradients, they must be on the same plane as follows:

![[KKTDuality.png]]

And for $x^*$ to be the optimal solution, the direction of gradient of $f(x^*)$ must be between the gradient of the constraints (or $f(x)$ can be further minimized without break the constraints).

And to have the linear combination work as we expected, we have:
$$-\nabla_x f(x^*) = \mu_1\nabla_xg_1(x^*) + \mu_2\nabla_xg_2(x^*)\quad \mu_1 \geq 0, \mu_2 \geq 0$$
By expanding this to the broader dimensions, we have the dual feasibility. 

A detailed proof can be found here:
https://zhuanlan.zhihu.com/p/26514613 