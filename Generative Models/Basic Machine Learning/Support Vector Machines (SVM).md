-----
#BasicMachineLearning 
> ***Problem Type***: [[Classification Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N, y^{(i)} \in \{-1,1\}$ 
> SOLVE: parameters $w \in \mathbb{R}^{n}, b$ such that $\min_{w,b} \frac{1}{2} w^T w$ subject to  $y^{(i)} (w^Tx^{(i)} + b) \geq 1$ for $i \in [1, N]$ 
> ***Iterative Solution***: [[Pegasos Algorithm]], [[Sequential Minimal Optimization (SMO)]]

Support vector machine (SVM) is the algorithm that search for the optimal boarder between the given classes. 

![[SVM.png]]
For linearly divisible binary classification problems, we can consider the optimal linear classifier to be the one that separates the two classes and to the hyperspace with the largest minimum interval of all samples plane.

## Margins

In the support vector machine, we define the hypothesis function as:
$$h_{w,b} = g(w^Tx +b), \quad g(z) = z \geq 0 \, ? \, 1: -1$$
In this case, the decision boundry is defined as the hyperplane where $w^Tx + b = 0$ 

Given a training example $(x^{(i)}, y^{(i)})$, the **functional margin** for w, b is defined as:
$$\hat{\gamma}^{(i)} = y ^ {(i)}(w^Tx^{(i)} + b)$$
The $y^{(i)} \in \{1,-1\}$ gives the direction of the margin, and $(w^Tx^{(i)} + b)$ need to be as large as possible to achieve the maximum functional margin. The functional margin will always be positive given correct predictions.

For a training set $S = \{(x^{(i)}, t^{(i)});i=1,...,n\}$, the functional margin of the set is defined as:
$$\hat{\gamma} = \min _{i,...,n} \hat{\gamma}^{(i)}$$
- Note: the functional margin is sensitive to the scaling of weights and biases

The **Geometric Margin** $\gamma$ of the sample is defined as the geometric distance between the sample data to the decision boundry.  

- The unit weight vector $w/||w||$ gives the normal direction to the decision boundry 
- The sample point is represented by $x^{(i)}$
- The point where geometric margin contact decision boundry is given as $x^{(i)} - \gamma^{(i)} \cdot w/||w||$

Hence we have the equation:
$$w^T(x^{(i)}-\gamma^{(i)}\frac{w}{||w||}) + b = 0$$
And solve for the equation yields the geometric margin as:
$$\gamma^{(i)} = \frac{w^Tx^{(i)}+b}{||w||} = (\frac{w}{||w||})^T x^{(i)} + \frac{b}{||w||}$$
However, since $\gamma$ defined as this will take negative values, we refine the definition as:
$$\gamma^{(i)} = y^{(i)} ((\frac{w}{||w||})^T x^{(i)} + \frac{b}{||w||})$$
And the geometric margin of the training set is still:
$$\gamma = \min _{i,...,n} \gamma^{(i)}$$
## The Optimal Margin Problem

Since we are looking for the maximum geometric margin, we have the [[Optimization Problem]]:
$$\max_{\gamma,w,b} \gamma \quad s.t. \quad y^{(i)}(w^Tx^{(i)} + b) \geq \gamma, i=1,...,N \quad ||w|| = 1$$
- $||w||=1$ is the constraint such that the functional margin would be as close a geometric margin

And if we directly optimize the functional margin, we can convert the problem as:
$$\max_{\hat{\gamma},w,b} \frac{\hat{\gamma}}{||w||} \quad s.t. \quad y^{(i)}(w^Tx^{(i)} + b) \geq \gamma, i=1,...,N$$
Since the scaling of functional margin does not influence geometric margin, we can define the optimal functional margin $\hat{\gamma} = 1$ and the problem became the following:
$$\min _{w,b} \frac{1}{2} ||w||^2\quad s.t. \quad y^{(i)}(w^Tx^{(i)} + b) \geq 1, i=1,...,N$$
Here we can rewrite the constraint into the standard forms:
$$g_i(w)=-y^{(i)}(w^Tx^{(i)}+b)+1 \leq 0$$
Note: due to the [[Karush–Kuhn–Tucker Conditions]] (The dual and complementarity conditions), since the geometric margin of the training set is the minimum geometic margin among all samples, only the training samples with functional margin $\hat{\gamma} = 1$ (saddle points of the set) will satisfy the KKT theorem. 

Note: the traning samples on the $\hat{\gamma} = 1$ line (dashed line in the graph) are the only points define the decision boundry, they are called **Support Vectors**.

Note: in the entire Lagrangian function, only the support vectors can have non-zero $\alpha$ , since they satisfy the KKT conditions and have possible KKT multipliers.

![[SVMOptimizer.png]]

To solve the optimal weights, we derive the Lagrangian form with KKT multipliers:
$$\mathcal{L}(w,b,\alpha) = \frac{1}{2}||w||^2 - \sum _{i=1} ^N \alpha_i[y^{(i)}(w^Tx^{(i)}+b)-1]$$
Here [[Lagrange Duality]] comes into play. To find the dual problem, we neet the minimize $\mathcal{L}(w,b,\alpha)$ with respect to $w,b$ , where we can solve for the optimals that:
$$\nabla _w \mathcal{L}(w,b,\alpha) = w - \sum _{i=1} ^N \alpha_i y^{(i)}x^{(i)} = 0$$
which solved to be 
$$w = \sum _{i=1} ^N \alpha y^{(i)}x^{(i)}$$
And if we looks at b, we get
$$\dfrac{\partial \mathcal{L}}{\partial b} = \sum _{i=1} ^N \alpha_iy^{(i)} = 0$$
 If we replace the definition of $w$ into the primal problem, $b$ as the constraint, and set the Lagrangian as the new objective function, we have the dual problem:
 $$\max_\alpha \sum_{i=1} ^N \alpha_i -  \frac{1}{2} \sum _{i,j=1} ^N y^{(i)} y^{(j)} \alpha_i \alpha_j <x^{(i)}, x^{(j)}> \quad s.t. \quad \alpha_i\geq0, \sum _{i=1} ^N \alpha_iy^{(i)} = 0 $$
Because the  support vectors  satisfy $w^Tx^{(i)} + b = \pm 1$. We have   $\max_{i:y^{(i)}=-1}(w^{*})^Tx^{(i)} + b= -1$    and $\min_{i:y^{(i)}=1}(w^*)^Tx^{(i)} + b = 1$. By combining the functions, the optimal intercept term $b^*$ can be found as a function of optimal $w^*$:
$$b^*=-\frac{\max_{i:y^{(i)}=-1}(w^{*})^Tx^{(i)}+\min_{i:y^{(i)}=1}(w^*)^Tx^{(i)}}{2}$$

  Bu using the support vectors and definition of weights, we can directly using $\alpha$ terms for support vectors to preform prediction, as:
  $$w^Tx + b = \sum _{i=1} ^N \alpha_iy^{(i)}<x^{(i)},x> + b$$
  