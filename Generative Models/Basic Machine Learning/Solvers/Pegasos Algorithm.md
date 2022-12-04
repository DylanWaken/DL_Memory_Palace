----
#BasicMachineLearning 
> ***Problem Type***: [[Classification Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N, y^{(i)} \in \{-1,1\}$ 
> SOLVE: parameters $w \in \mathbb{R}^{n}, b$ such that $\min_{w,b} \frac{1}{2} w^T w$ subject to  $y^{(i)} (w^Tx^{(i)} + b) \geq 1$ for $i \in [1, N]$ 
> ***Iterative Solution***: $w_{t+1} := (1-\frac{1}{t})w_t + \eta_t \mathbb{1}\{y^{(i)}(w^Tx+b) < 1\} y^{(i)}x^{(i)}$
> $b_{t+1} := (1-\frac{1}{t})w_t  + \eta_t\mathbb{1}\{y^{(i)}(w^Tx+b) < 1\} y^{(i)}$

Original Paper: [[PegasosMPB SVM Solving Algorithm.pdf]]
This is a solution to the [[Support Vector Machines (SVM)]]

In the origial SVM problem, we have the primal objective defined as:
$$\min _{w,b} \frac{1}{2} ||w||^2 \quad s.t. \quad y^{(i)}(w^Tx^{(i)} + b) \geq 1 $$
There is the alternative representation of the same problem with a minimizing function of no constraints,  as:
$$\min _{w,b} \frac{\lambda}{2} ||w||^2 + \frac{1}{N} \sum _{x,y\in S} \max \{0, 1-y(w^Tx + b)\}$$
- $\lambda \geq 0$ is the regulation strength
 
Where we convert the constraints into a punishment term that will equal to zero if the sample is correctly classified. Note: the term $1-y(w^Tx + b)$ will only be greater than zero if the sample is misclassified or is within the functional margin $\hat\gamma = 1$ . 
 
We can define a loss function based on this alternative problem, called the ***Hinge Loss***:

![[HingeLoss.png]]

The function for each sample form as below:
$$J(w,b)= \frac{\lambda}{2} ||w||^2 +  \max \{0, 1-y^{(i)}(w^Tx^{(i)} + b)\}$$
And by taking derivative of the loss function, we have the gradients:
$$\nabla_w J(w,b) = \lambda w - \mathbb{1}\{y^{(i)}(w^Tx+b) < 1\} y^{(i)}x^{(i)}$$
$$\dfrac{\partial J}{\partial b} = -  \mathbb{1}\{y^{(i)}(w^Tx+b) < 1\} y^{(i)}$$
And by repeating the above formulas with Stocastic [[Gradient Descent]], we would converge toward the optimal parameters.

In the original Pegasos Algorithm, we use a step size decreasing with respect to time, in which $\eta_t = 1/(\lambda t)$, and our update rule for $w$ and $b$ can be written as:
$$w_{t+1} := (1-\frac{1}{t})w_t + \eta_t \mathbb{1}\{y^{(i)}(w^Tx+b) < 1\} y^{(i)}x^{(i)}$$
$$b_{t+1} := (1-\frac{1}{t})w_t  + \eta_t\mathbb{1}\{y^{(i)}(w^Tx+b) < 1\} y^{(i)}$$
The versions for kernel SVMs and convergence proof can be found in [[pegasos explanation.pdf]]
