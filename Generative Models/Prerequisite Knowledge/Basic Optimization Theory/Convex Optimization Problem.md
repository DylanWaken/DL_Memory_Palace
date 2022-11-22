------
#BasicOptimizationTheory 

Convex optimization problem is a specific form of [[Optimization Problem]], in which the objective function is a convex function contains one and only one local minimum. 

The basic shape is the same as normal optimization:
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0 \quad h_j(x) =0$$
- $x \in \mathbb{R}^n$ is the optimization variable
- The objective function $f:\mathcal{D} \subset \mathbb{R}^n \rightarrow \mathbb{R}$  is a convex function
- The inequality constraint functions $g_i : \mathbb{R}^n \rightarrow \mathbb{R}$ are all convex functions
- The equality constraint functions $h_i : \mathbb{R}^n \rightarrow \mathbb{R}$ are affine transformations, which means the function is in form $h_i(x) = a_i \cdot x -b_i$ where $a_i$ is vector and $b_i$ is scalar. 

In the definition, the convex optimization problem is seeking to find a point $\hat{x} \in C$ in the feasible set of solutions such that:
$$\inf\{f(x):x\in C\}$$
- Both the objective function and the feasible solution set $C$ is convex

The special properties of convex optimizations:

- Every local minimum of objective function is the global minimum
- The optimal set is also convex
- If the objective function is strictly convex, the problem would have at most one optimal point

## Conditions for being convex:

A set is convex if for all members $x,y\in S$ and  $\theta \in [0,1]$, the following satisfies:
$$\theta \cdot x +(1-\theta)\cdot y \in S$$
- Any points on the line connecting any two members of the set is within the set

A function is convex if for all values $x,y$ in its domain an $\theta \in [0,1]$, the following satisfies:
$$f(\theta x + (1-\theta)y)\leq \theta f(x) + (1-\theta) f(y)$$
- Any function output of the input values betweem $x$ and $y$ is above the line connecting $x$ and $y$ 