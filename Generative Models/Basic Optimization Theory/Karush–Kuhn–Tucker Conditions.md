----
#BasicOptimizationTheory 

Karush-Kuhn-Tucker Conditions (KKT) is the first derivative test (or first order necessary conditions) for solving non-linear optimization problem provided the constraints are satisfied.  The KKT conditions is the generalized [[Lagrange Multiplier]] methods that allows operations beyond equality constraints. 

## Karush-Kuhn-Tucker Theorem

For the optimization problem as follow:
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0 \quad h_j(x) =0$$
where $x \in X$ is the optimization variable chosed from a convex subset of $\mathbb{R}^n$ 
We define the Lagrangian of this problem as:
$$\mathcal{L}(x, \mu,\lambda) = f(x) + \mu^Tg(x) + \lambda^Th(x)$$
- $\mu$ is the inequality constraint KKT multipliers, $g(x) = [g_1(x), ..., g_m(x)]$ 
- $\lambda$ is the equality constraint KKT multipliers, $h(x) = [h_1(x),...,h_l(x)]$

The ***Karush-Kuhn-Tucker Theorem*** states that: If $(x^*, \hat{\mu})$ is a ***saddle point*** of Lagrangian function $\mathcal{L}(x, \mu)$ in $x \in X$, $\mu \geq 0$, then $x^*$ is an optimal vector for the above optimization problem. 

The proof of KKT Theorem used hyperplane separation theorem, since the definition is the same as finding a supporting hyperplane on the feasible set $\Gamma = \{x \in X : g_i(x) \leq 0, i=1...m\}$ 

## KKT Conditions

For the optimization problem: 
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0 \quad h_j(x) =0$$
- $f : \mathbb{R}^n \rightarrow \mathbb{R}$ , $g_i : \mathbb{R}^n \rightarrow \mathbb{R}$ , $h_j : \mathbb{R}^n \rightarrow \mathbb{R}$   
   
 If $x^*$ is a local optimum and the optimization problem satisfies the constraints, then there exists constants $\mu_i (i=1,...,m)$ and $h_j (j=1,...,l)$ , called KKT multipliers, such that the following groups of conditions holds:

  - Stationary: For minimizing:$$\partial f(x^*) + \sum _{j=1} ^l \lambda_j\partial h_j(x^*) + \sum _{i=1} ^m \mu_i \partial g_i(x^*) \ni 0$$
  - Stationary: For maximizing:$$-\partial f(x^*) + \sum _{j=1} ^l \lambda_j\partial h_j(x^*) + \sum _{i=1} ^m \mu_i \partial g_i(x^*) \ni 0$$
  - Primal feasibility: 
 
	$h_j(x^*) = 0$  for $j=1,...,l$
	$g_i(x^*) = 0$ for $i = 1,...,m$

- Dual feasibility:

	$\mu_i \geq 0$, for $i = 1,..,m$ 

- Complementary Slackness:
$$ \mu_i g_i (x^*) = 0$$
These conditions determines whether $x^*$ is the optimal solution
A graphical explanation can be found below:
![[KKT.png]]
A detailed proof can be found here:
https://zhuanlan.zhihu.com/p/26514613 