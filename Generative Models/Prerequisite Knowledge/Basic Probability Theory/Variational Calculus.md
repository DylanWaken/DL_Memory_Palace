----
#ProbabilityTheory 

This blog goes through things in detail : https://bjlkeng.github.io/posts/the-calculus-of-variations/

For an arbitrary differentiable function $F:\mathbb{R} \to \mathbb{R}$, the tiny change over $F$ can be represented as the little nudge of change given the small change in the variable:
$$dF = F(y_{1}+dy)-F(y_{1}) = \frac{dF}{dy} |_{y_{1}} dy$$
And if the function is scalar values but with vector input of $\mathbb{R}^n$, the function can be represented as:
$$dF = \frac{{\partial F}}{\partial y_{1}}|_{y_{1}^1} dy_{1} + \dots + \frac{{\partial F}}{\partial y_{n}} |_{y_{n}^1}dy_{n}$$
Now, if we regard that $y_{1},\dots,y_{n}$ as the output uniformly sampled from a specific function $y :\mathbb{R} \to \mathbb{R}$ over some finite interval $[a,b]$. As the sample size increases toward infinity, the function $F$ would become a **"Function of a function"**.  We call $F$ a **Functional**

The formfacor of the actual function is given as:
$$dF  =\sum _{{i}}^N \frac{{\partial F}}{\partial y_{i}}|_{y_{i}^1} dy_{i} = \sum_{i} ^N F(y_{i}^1+dy_{i})-F(y_{i}^1)$$
And when the sample count $N \to \infty$, the function would become an indegral:
$$dF = \int _{a} ^b \frac{δF}{δy(x)} |_{y^1 (x)} δy(x)\, dx \quad(1.0)$$
The general (most common form) of a functional is defined as:
$$F[y(x)] = \int _{a} ^b L(x,y(x), y'(x)) \, dx $$
- The function $y$ takes a number and output a number
- The funtion $F$ takes $y(x)$ as input and output a number

In an simpler way of explanation:

**The change in $F$ is proportional to the sum of all changes in the funtion $y(x)$ represented by $δy(x)$ (step size) multiplied by the derivative for each direction $\frac{δF}{δy(x)}$ (slope)

For the function above, we define its functional derivative (the change in a functional ($F$) to the change in a function ($y(x)$) which $F$ dependes) as:
$$\frac{{\delta F}}{\delta y(x)}$$
This is analogous to the derivative at each of the "independent variables" $y(x)$, which is the same concept as the gradient for multivariate functions.

Equation $(1.0)$ then becomes a directional derivative, where we can interpret as the rate of change of $F$ as we are moving through "point" $y_{1}(x)$ in the direction of $\delta y (x)$. 

Using the analogy of directional derivatives from above, if we have the functional derivative at the multivariate "point" $y(x)$ moving in the multivariate "direction" of an arbitrary function $\eta (x)$ then we can formulate the limit as:
$$\lim_{ \epsilon \to 0} \frac{{F[y(x) + \epsilon \eta(x)] - F[y(x)]}}{\epsilon} = \int \frac{\delta F}{\delta y(x)} \eta(x) \, dx  $$
which would be the same as the equation $(5.0)$

Where we can get $\delta F$ or $dF$ as:
$$dF = F[y+\delta y] -F[y]$$
## Euler-Lagrange Equation
F[y(x)] = \int _{a} ^b L(x,y(x), y'(x)) \, dx 
Eular-Lagrange Equation is a shortcut in computing the functional derivatives in variational calculus, which the theorem states:
$$F[y] = \int _{a} ^b L(x,y(x), y'(x)) \, dx $$
Has the functional derivative given by:$
$$\frac{{\partial F}}{\delta y(x)} = \frac{\delta L}{\delta y} - \frac{d}{dx} \frac{\partial L}{\partial y'}$$
Proof:

We set the original $y(x)$ between bundries $y(a) = A$ and $y(b) = B$ and which extremizes the functional, Let $g(x) = y(x) + \epsilon \eta(x)$ be the new function with $\eta(x)$ such that $\eta(a) = \eta(b) = 0$, and we define:
$$J = \int _{a}^b L(x, g(x), g'(x)) \, dx  = \int _{a}^b  L\, dx $$ And we are solving the total derivative (partial derivative for every single argument) of $J$ with respect to $\epsilon$:
$$\frac{{\partial J}}{\partial \epsilon} = \int _{a} ^b \frac{dL}{d \epsilon} \, dx $$
Using the rules of total derivatuve that:
$$\begin{align}
\frac{dL}{d \epsilon} &= \frac{\partial L}{\partial x} \frac{dx}{d \epsilon} + \frac{\partial L}{\partial g} \frac{dg}{d \epsilon} + \frac{\partial L}{\partial g'} \frac{dg'}{d\epsilon}  \\
&=\eta(x) \frac{\partial L}{\partial g}  + \eta'(x) \frac{\partial L}{\partial g'} 
\end{align}$$
Note the first term is ignored since $dx/de$ is zero, the original derivative can be rewritten as:
$$\frac{dJ}{d \epsilon} =\int _{a}^b  \eta(x) \frac{\partial L}{\partial g}  + \eta'(x) \frac{\partial L}{\partial g'}\, dx$$
And whwen we have $\epsilon \to 0$ (as we assume the function is appraching extreme value), $g(x)$ would be approaching $f(x)$.  so our function becames the follwoing equation:
$$\frac{dJ}{d \epsilon} = \int _{a} ^b \left[ \eta(x)\frac{{\partial L}}{\partial f} +  \eta'(x) \frac{\partial L}{\partial f'}\right] \, dx $$
And through integrating by parts, we would have the following conclusion:
$$\frac{dJ}{d \epsilon} = \left[ \eta(x) \frac{{\partial L}}{\partial f'}\right]_{a}^b + \int _{a} ^b  \eta(x)\frac{{\partial L}}{\partial f} -\eta(x) \frac{d}{dx}\frac{{\partial L}}{\partial f'} \, dx $$
Since $\eta(x)$ have both end be zero, the first term is discarded, and the final form of the formula would be:
$$\frac{dJ}{d \epsilon} = \int _{a} ^b \left[\frac{\delta L}{\delta y} - \frac{d}{dx} \frac{\partial L}{\partial y'}\right] \,\eta(x) dx $$
If we look at the definition of the functional derivative by limit, this is exatly the same form, and we have proved the equality.

## Extrema

When unconstrainted, the extrema can be found by solving the point where the functional derivative is zero.

To find the extrema of a functional $H[y]$ subjecting to specific constraints $G[y]$, the technique of [[Lagrange Multiplier]] is commonly used. GIven a function named by:
$$G[y] = \int _{a} ^b M(x,y, y') \, dx =C$$
We an apply an Lagrangian form of this function as another functional:
$$H[y] = \int _{a} ^b (L(x,y, y') - \lambda M(x,y, y')) \, dx $$
And we can solve for function $y$ and $\lambda$ given the above conditions. 
