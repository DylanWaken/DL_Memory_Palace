----
#BasicMachineLearning 
> ***Problem Type***: [[Classification Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N$ 
> SOLVE: parameters $w \in \mathbb{R}^{n}, b$ such that $\min_{w,b} \frac{1}{2} w^T w$ subject to  $y^{(i)} (w^T \phi(x^{(i)}) + b) \geq 1$ for $i \in [1, N]$ 
> ***Iterative Solution***: [[Pegasos Algorithm]], [[Sequential Minimal Optimization (SMO)]]

- [[Support Vector Machines (SVM)]]

![[KernelSVM.png]]

[[Kernel]] SVM used feature maps for addressing non-linear separable problems. Through projecting the data point into a higher dimension that they are linear-separable in, the algorithm will be finding optimal hyperplane for remapped data.

In the [[kernel]] problem, we are looking for:
$$\min _{w,b} \frac{1}{2} ||w||^2\quad s.t. \quad y^{(i)}(w^T\phi(x^{(i)}) + b) \geq 1, i=1,...,N$$
And through the Lagrangian and [[Lagrange Duality]] (The process of proof is the same as the Support Vector Machine, just replace $x^{(i)}$ with $\phi(x^{(i)})$  ), we have:
$$\max_\alpha \sum_{i=1} ^N \alpha_i -  \frac{1}{2} \sum _{i,j=1} ^N y^{(i)} y^{(j)} \alpha_i \alpha_j K(x^{(i)}, x^{(j)}) \quad s.t. \quad \alpha_i\geq0, \sum _{i=1} ^N \alpha_iy^{(i)} = 0 $$
Here, the original inner product is replaced with a [[Kernel]]

Normal kernels that are commonly used:

- Linear Kernel -> $K(x,z) = x^Tz$
- Polynomial Kernel -> $K(x,z) = (\gamma x^Tz + c)^k$ 
- Gaussian/[[Radical Basis Function (RBF)]] Kernel -> $K(x,z) = exp(\dfrac{||x-z||^2}{2\sigma^2})$ 



