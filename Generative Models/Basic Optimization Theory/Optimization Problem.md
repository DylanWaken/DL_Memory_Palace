-----
#BasicOptimizationTheory 

Optimization problem is the problem of finding the best (optimal) solution in the feasible set of solutions:

The problem is usually set to solve for optimal solutions within specific conditions or constraints. For continuous optimization problems, the form is normally in the following shape:
$$\min _x f(x) \quad s.t. \quad g_i(x) \leq 0 \quad h_j(x) =0$$
- $f:\mathbb{R}^n \rightarrow \mathbb{R}$ is the objective function to minimize ($x$ is a n dimensional vector)
- $g_i(x) \leq 0$ is called inequity constraints, $i\in[1,m] \quad m\geq 0$ 
- $h_j(x) = 0$ is called equity constraints, $j \in [1,q] \quad q \geq 0$ 
- if $m = 0$ and $q=0$ , the problem is an unconstrainted optimization problem

