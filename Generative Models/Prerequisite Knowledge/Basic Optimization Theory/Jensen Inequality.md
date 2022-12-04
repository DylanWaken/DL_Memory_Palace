----
#BasicOptimizationTheory 

For any given convex function $f$, if $\lambda \in [0,1]$, the following inequality satisfies:
$$\lambda f(x) + (1-\lambda)f(y) \geq f(\lambda x + (1-\lambda)y)$$
This is because since the function is convex, the function out between any two given points on the funciton curve must be below the straight line connecting the two points.

![[Jensen Inequality.png]]

For the concave case, the opposite would be true.

If we take a look closer, the "line" between the two poitns, or $\lambda f(x) + (1-\lambda)f(y)$ is actually the weighted average of $f(x)$ and $f(y)$ . By extending this definition, if we have an arbitrary convex function $g$ , and a series of variables $\alpha_1,\alpha_2,...,\alpha_n$ that sums to one, we have the following conclusion:
$$\sum _{i=1} ^n \alpha_ig(x_i) \geq g(\sum _{i=1} ^n \alpha_ix_i) $$
And if we have the $\alpha$ replace with a continuous function $p(x)$ that sums to one, we have:
$$\int p(x) g(x) dx \geq g(\int p(x)dx)$$

Since we have the [[Expectation]] defined as a function weighted by a probabilistic distribution, the above funtion stands for a new fact:
$$E[g(X)] \geq g(E[X])$$
