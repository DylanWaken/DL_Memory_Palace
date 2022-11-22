-----
#BasicMachineLearning 
> ***Problem Type***: [[Classification Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N, y^{(i)} \in \{-1,1\}$ 
> SOLVE: parameters $w \in \mathbb{R}^{n}, b$ such that $\min_{w,b} \frac{1}{2} w^T w + C\sum _{i=1} ^N \xi_i$ subject to  $y^{(i)} (w^Tx^{(i)} + b) \geq 1 - \xi$ for $\xi_i \geq 0$ and $i \in {1,..., N}$ 
> ***Iterative Solution***: [[Pegasos Algorithm]], [[Sequential Minimal Optimization]]

- [[Support Vector Machines]]

In the non-linear separable binary classification problems, the algorithm solves for the hyperplane with the maximized minimal margin, but allows sample points to exist within the minimal margins of train set. 

This methodology can also be used to prevent outliers from influence the results and causing overfit.

![[SVMOverfit.png]]

We introduced a soften variable $\xi \geq 0$ into the constraints:
$$y^{(i)}(w^Tx^{(i)} + b) \geq 1 - \xi_i$$
And make minimizing it part of our objective function:
$$\min _{w,b} \frac{1}{2} w^Tw + C\sum _{i=1} ^N \xi_i$$
This is the same approach as implementing a [[L1 Regularization]] to the problem. And together, the [[Optimization Problem]] is converted to:
$$\min _{\xi,w,b} \frac{1}{2} ||w||^2 + C\sum _{i=1} ^N \xi_i \quad s.t. \quad y^{(i)}(w^Tx^{(i)} + b) \geq 1 - \xi_i, \xi_i\geq0$$
The Lagrangian form is also given as:
$$\mathcal{L}(w,b,\xi,\alpha, \beta) = \frac{1}{2}w^Tw + C\sum _{i=1} ^N \xi_i- \sum _{i=1} ^N \alpha_i[y^{(i)}(w^Tx^{(i)}+b)-1 + \xi_i] - \sum_{I=1}^N\beta_i\xi_i $$

Through [[Lagrange Duality]] and setting $\nabla w$ and $\partial b$ to zero, we have the dual problem as:
$$\max _\alpha \sum_{i=1} ^N \alpha_i -  \frac{1}{2} \sum _{i,j=1} ^N y^{(i)} y^{(j)} \alpha_i \alpha_j <x^{(i)}, x^{(j)}> \quad s.t. \quad 0\leq\alpha\leq C, \sum_{i=1} ^N \alpha_iy^{(i)}=0$$
Under this case, the [[Karush–Kuhn–Tucker Conditions]] (dual-complementarity) are:

$\alpha_i = 0 \rightarrow y^{(i)}(w^Tx^{(i)} + b) \geq 1$
$\alpha_i = C \rightarrow y^{(i)}(w^Tx^{(i)} + b) \leq 1$
$0 < \alpha_i < C \rightarrow y^{(i)}(w^Tx^{(i)} + b) = 1$

Proof:

if we have the Lagrangian:
$$\mathcal{L}(w,b,\xi,\alpha, \beta) = \frac{1}{2}w^Tw + C\sum _{i=1} ^N \xi_i- \sum _{i=1} ^N \alpha_i[y^{(i)}(w^Tx^{(i)}+b)-1 + \xi_i] - \sum_{i=1}^N\beta_i\xi_i $$
And we set the derivative with respect to $\xi_i$ to be zero,  we have:
$$\alpha_i + \beta_i = C \quad \forall i \in \{1,...,N\}$$
Since the KKT duality condition requires:
$$\mu_ig_i(x^*) = 0$$
We have:
$$\alpha_i[y^{(i)}(w^Tx^{(i)}+b)-1+\xi_i] = 0\quad \beta_i \xi_i =0$$
And we can derive the following cases:

Case 1: $\alpha_i = 0$ : train sample outside of functional margin $\hat{\gamma} = 1$ 
$$\alpha_i=0 \Rightarrow \beta_i = C \Rightarrow \xi_i = 0 \Rightarrow y^{(i)}(w^Tx^{(i)}+b) \geq 1$$
Case 2: $0 < \alpha_i < C$ : train sample on the functional margin  $\hat{\gamma} = 1$ 
$$0 < \alpha_i < C \Rightarrow 0 < \beta_i < C \Rightarrow \xi_i = 0 \Rightarrow y^{(i)}(w^Tx^{(i)}+b) = 1$$
Case 3: $\alpha=C$ : train sample within the functional margin:
$$\alpha_i=C \Rightarrow \beta_i = 0 \Rightarrow \xi_i \geq 0 \Rightarrow y^{(i)}(w^Tx^{(i)}+b) \leq 1$$
This technique is also used in the SMO algorithm
