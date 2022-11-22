-----
#BasicMachineLearning 

Sequential Minimal Optimization (SMO) is the [[Support Vector Machines]] solver using the [[Coordinate Descent]] process.

In the original [[Soft-Margin SVM]], we have the dual optimization problem being:
$$\max _\alpha \sum_{i=1} ^N \alpha_i -  \frac{1}{2} \sum _{i,j=1} ^N y^{(i)} y^{(j)} \alpha_i \alpha_j <x^{(i)}, x^{(j)}> \quad s.t. \quad 0\leq\alpha\leq C, \sum_{i=1} ^N \alpha_iy^{(i)}=0$$
In the traditional cord descent, we select one varible to optimize at a time. However, this approach will not function as intended, as in the constraints:
$$\alpha_1y^{(1)} =-\sum _{i=2} ^N \alpha_iy^{(i)} \quad \alpha_1 = - y^{(1)} \sum _{i=2} ^N \alpha_iy^{(i)}  $$
If all the $\alpha$ are under the constraint, we can not make any progress since the params are locked together.

The workaround for the problem above is to extract 2 params at once, as we have:
$$\alpha_1y^{(1)} + \alpha_2y^{(2)} = -\sum_{i=3} ^N \alpha_iy^{(i)}$$
Since the righthand-side is fixed (as we treat $\alpha_3 ... \alpha_N$ as constants), we have:
$$\alpha_1y^{(1)} + \alpha_2y^{(2)} = \zeta$$
This function acts as a constraint for our optimization of $\alpha_1, \alpha_2$, as shown below:

![[SMOStructure.png]]

- The line indicates the relationship of $\alpha_1y^{(1)} + \alpha_2y^{(2)} = \zeta$
-  $L\leq\alpha_2\leq H$
- $L$ and $H$ are the possible range for $\alpha_2$ given the range of $\alpha_1$
- There may be values of $\alpha_1$ such that $\alpha_1$ and $\alpha_2$ can not exist within the constraints

We can derive $\alpha_1$ as a function of $\alpha_2$, in which:
$$\alpha_1 = (\zeta-\alpha_2y^{(2)})y^{(1)}$$
## Derive SMO Algorithm

>Warning: This part is extremely complex, feel free to skip if you don't need to understand and code this in detail!!! 

For easier deriving, we convert the original maximizing problem into a minimizing problem:

$$\min _\alpha  \frac{1}{2} \sum _{i,j=1} ^N y^{(i)} y^{(j)} \alpha_i \alpha_j <x^{(i)}, x^{(j)}> - \sum_{i=1} ^N \alpha_i  \quad s.t. \quad 0\leq\alpha\leq C, \sum_{i=1} ^N \alpha_iy^{(i)}=0$$

If we pick out $\alpha_1, \alpha_2$ from the original objective function and we plug them back in separately, we will have this long objective funtion, as:

$L(\alpha_1, \alpha_2) = \frac{1}{2}[ y^{(1)} y^{(1)}\alpha_1 \alpha_1 <x^{(1)},x^{(1)}> + 2\cdot y^{(1)} y^{(2)}\alpha_1 \alpha_2 <x^{(1)},x^{(2)}>$  

$\quad \quad \quad \quad + y^{(2)} y^{(2)}\alpha_2 \alpha_2 <x^{(2)},x^{(2)}> + 2 \cdot \sum _{j=3} ^N y^{(1)} y^{(j)}\alpha_1 \alpha_j <x^{(1)},x^{(j)}>$

$\quad\quad\quad\quad +  2 \cdot \sum _{j=3} ^N y^{(2)} y^{(j)}\alpha_2 \alpha_j <x^{(2)},x^{(j)}> + \sum _{i,j=3} ^N  y^{(i)} y^{(j)} \alpha_i \alpha_j <x^{(i)}, x^{(j)}>]$

$\quad\quad\quad\quad - \alpha_1 - \alpha_2 - \sum _{i=3} ^N \alpha_i$


Here we define the inner product $<x^{(i)}, x^{(j)}>$ to be the linear kernel matrix $K_{ij}$ 
And we remove the constant terms $\sum _{i,j=3} ^N  y^{(i)} y^{(j)} \alpha_i \alpha_j <x^{(i)}, x^{(j)}>$  and $- \sum _{i=3} ^N \alpha_i$
Note that $y^{(i)} \cdot y^{(i)} = 1$ , since $1^2 = (-1)^2 = 1$

Simplify the formula and we have:

$L(\alpha_1, \alpha_2) = \frac{1}{2}[\alpha_1^2 K_{11} + 2  y^{(1)} y^{(2)}\alpha_1 \alpha_2 K_{12} + \alpha_2^2 K_{22} + 2 \cdot \sum _{j=3} ^N y^{(1)} y^{(j)}\alpha_1 \alpha_j K_{1j}$

$\quad\quad\quad\quad + 2 \cdot \sum _{j=3} ^N y^{(2)} y^{(j)}\alpha_2 \alpha_j K_{2j}] - \alpha_1-\alpha_2$

And by replacing $\alpha_1$ as the function of $\alpha_2$ , we have:

$L( \alpha_2) = \frac{1}{2}[(\zeta-\alpha_2y^{(2)})^2 K_{11} + 2 y^{(2)}(\zeta-\alpha_2y^{(2)}) \alpha_2 K_{12}$

$\quad\quad\quad\quad + \alpha_2^2 K_{22} + 2 \cdot \sum _{j=3} ^N  y^{(j)}(\zeta-\alpha_2y^{(2)}) \alpha_j K_{1j} + 2 \cdot \sum _{j=3} ^N y^{(2)} y^{(j)}\alpha_2 \alpha_j K_{2j}]$

$\quad\quad\quad\quad -(\zeta-\alpha_2y^{(2)})y^{(1)} -\alpha_2$

Here we take the derivative:

$\dfrac{\partial L}{\partial \alpha_2} = \dfrac{1}{2}[-2y^{(2)}(\zeta-\alpha_2y^{(2)})^2 K_{11} + (2\zeta y^{(2)}K_{12}-4\alpha_2K_{12}) - 2 \sum _{i=3} ^N y^{(2)}\alpha_iy^{(i)}K_{1i}$

$\quad\quad\quad\quad 2\alpha_2K_{22} + 2\sum _{i=3}^N y^{(2)} \alpha_jy^{(j)}K_{2j}] + y^{(1)}y^{(2)} - 1$

And since we are soving for optimal:
$$\dfrac{\partial L}{\partial \alpha_2} = 0$$
By solving and simplifying the equations we have:

$\alpha_2(K_{11} + K_{22} - 2K_{12}) = y^{(2)}[y^{(2)}-y^{(1)} + \zeta K_{11} - \zeta K_{12} + \sum _{i=3} ^N\alpha_iu^{(i)}K_{1i} - \sum _{i=3} ^N \alpha_i y^{(i)}K_{2i}]$

With the original SVM KKT conditions, we have the conclusion that:
$$w = \sum _{i=1}^N \alpha_iy^{(i)}x^{(i)}$$
Since our prediction is $f(x) = w^Tx + b$, we can rewrite our prediction with $\alpha_1, \alpha_2$:
$$f(x) = (\alpha_1y^{(1)}x^{(1)}  + \alpha_2y^{(2)}x^{(2)} +  \sum _{i=3} ^N \alpha_i y^{(i)}x^{(i)})^Tx + b$$
And by setting $x = x^{(1)}, x^{(2)}$, we have:

$f(x^{(1)})-\alpha_1y^{(1)}K_{11} - \alpha_2y^{(2)}K_{12} - b =\sum _{i=3} ^N \alpha_i y^{(i)}K_{1i}$

$f(x^{(2)})-\alpha_1y^{(1)}K_{21} - \alpha_1y^{(1)}K_{22} - b =\sum _{i=3} ^N \alpha_i y^{(i)}K_{2i}$

by replacing the summation terms in the original function, we have：

$\alpha_2(K_{11} + K_{22} - 2K_{12}) = y^{(2)}[y^{(2)}-y^{(1)} + \zeta K_{11} - \zeta K_{12} + f(x^{(1)})-\alpha_1y^{(1)}K_{11} - \alpha_2y^{(2)}K_{12} - b$
$\quad\quad\quad\quad - f(x^{(2)})+\alpha_1y^{(1)}K_{21} + \alpha_1y^{(1)}K_{22} + b$

Since this is a iterative function and the term $\zeta$ holds constant through the algorithm, we can use the $\alpha$ from previous step and have:
$$\zeta = \alpha_1 ^{old}y^{(1)} + \alpha_2 ^{old}y^{(2)}$$
And by swap the terms into the above function and simplify:

$\alpha_2 ^{new}(K_{11} + K_{22} - 2K_{12}) = y^{(2)}[y^{(2)} - y^{(1)} + \alpha_2 ^{old}y^{(2)}K_{11} + f(x^{(1)}) - 2\alpha _2 ^{old} y^{(2)}K_{12}$

$\quad\quad\quad\quad - f(x^{(2)}) + \alpha_2^{old}y^{(2)}K_{22}]$

and with some further simplification:
$\alpha_2 ^{new}(K_{11} + K_{22} - 2K_{12}) = y^{(2)}[(f(x^{(1)})-y^{(1)}) - (f(x^{(2)})-y^{(2)}) + \alpha_2 ^{old} y^{(2)}(K_{11} + K_{22} - 2K_{12})]$
By defining several variables as in the original SMO paper, we have:

$E_1 = (f(x^{(1)})-y^{(1)})$

$E_2 = (f(x^{(2)})-y^{(2)})$

$\eta = K_{11} + K_{22} - 2K_{12}$

And the SMO update rule can be written as:

$$\alpha_2 ^{new} = \alpha_2^{old} + \frac{y^{(2)}(E_1 - E_2)}{\eta}$$
## Clipping of the solution

Since we have the constraints for $\alpha_2$ as $L \leq \alpha_2 \leq H$, we need to solve for the lower and upper bounds of the solution.

The conditions we have:
$$\alpha_1 \in [0, C] \quad \alpha_2 \in [0,C] \quad \alpha_1y^{(1)} + \alpha_2y^{(2)} = \zeta$$
- Case 1: $y^{(1)} \neq y^{(2)} \Rightarrow \alpha_1 - \alpha_2 = k = \pm \zeta$:

because $\alpha_1 \in [0,C], \alpha_2 = \alpha_1 - k$  

So $\alpha_2 \in [-k, C-k] \quad \alpha_2 \in [\alpha_2 - \alpha_1, C + \alpha_2 - \alpha_1]$

with $\alpha_2 \in [0,C]$

we have:
$$L = \max(0, \alpha_2 ^{old}-\alpha_1^{old}), H=\min(C, C+\alpha_2^{old} - \alpha_1^{old})$$
- Case 2: $y^{(1)} = y^{(2)} \Rightarrow \alpha_1 + \alpha_2 = k$

because $\alpha_1 \in [0,C], \alpha_2 = k - \alpha_1$  

So $\alpha_2 \in [k-C, k] \quad \alpha_2 \in [\alpha_2 + \alpha_1 - C, \alpha_2 + \alpha_1]$

with $\alpha_2 \in [0,C]$

we have:
$$L = \max(0, \alpha_2^{old} + \alpha_1^{old} - C), H = \min(C,  \alpha_2^{old} + \alpha_1^{old})$$
And when we are updating the $\alpha_2^{new}$, we take the value $L$ if $\alpha_2^{new} < L$, and we take $H$ if $\alpha_2 ^{new} > H$ 

## Update Rule of the Algorithm

To update the SVM, we first look for points that violates the KKT Conditions (from [[Soft-Margin SVM]]):

$\alpha_i = 0 \rightarrow y^{(i)}(w^Tx^{(i)} + b) \geq 1$
$\alpha_i = C \rightarrow y^{(i)}(w^Tx^{(i)} + b) \leq 1$
$0 < \alpha_i < C \rightarrow y^{(i)}(w^Tx^{(i)} + b) = 1$

And set our $\alpha_1$ to it.

And then we choose another point $\alpha_2$ with maximum $E_1 - E_2$:
do the optimization above

Then we need to update bias $b$:

- When $0 < \alpha_1 ^{new} < 1$, we need $y^{(1)}(w^Tx^{(1)} + b) = 1$ 

since $\sum ^N _{i=1}\alpha_iy^{(i)}K_{i1} + b = y^{(1)}$

We have the update rule:
$$b_1^{new} = y^{(1)} - \sum ^N _{i=1}\alpha_iy^{(i)}K_{i1}$$
With the definition of $E_1$, we can replace the function and have:
$$b_1^{new} = -E_1 - y_1K_{11}(\alpha_1^{new} - \alpha_1^{old}) - y_2K_{21}(\alpha_2^{new} - \alpha_2^{old}) + b^{old}$$
- When $0 < \alpha_2 ^{new} < 1$ , we have similarly:
$$b_2^{new} = -E_2 - y_1K_{12}(\alpha_1^{new} - \alpha_1^{old}) - y_2K_{22}(\alpha_2^{new} - \alpha_2^{old}) + b^{old}$$
And we have 
$$b^{new} = \frac{b_1^{new} + b_2 ^{new}}{2}$$
