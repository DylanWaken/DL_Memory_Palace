----
#BasicMachineLearning 
> ***Problem Type***: [[Regression Problem]], [[Supervised Learning]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $y \in \mathbb{R}^N$ 
> SOLVE: parameters $\theta \in \mathbb{R}^{n}$ such that $\min_\theta J(\theta) = \frac{1}{2} || X\theta - y ||^2 + \frac{\lambda}{2}||\theta||^2$ 
> ***Closed-form Solution***: $\theta^* = (X^TX + \lambda I)^{-1}X^Ty$ 

Original details can be found here: [[Ridge Regression Paper.pdf]]

A modified version of [[Linear Regression]] with [[L2 Regularization]]

Deriving the optimal solution:

$\nabla _{\theta} J(\theta) =  \nabla_{\theta} \frac{\lambda}{2} \theta^T\theta +\frac{1}{2} (X\theta-\vec{y})^T(X\theta-\vec{y})$ 

$= \lambda I\theta + \frac{1}{2} \nabla_{\theta}((X\theta)^TX\theta - (X\theta)^T\vec{y} - \vec{y}(X\theta) + \vec{y}^T\vec{y})$ 

$= \lambda I\theta + \frac{1}{2} \nabla_{\theta}(\theta^T(X^TX)\theta - 2(X^T\vec{y})^T \theta)$ 

$= \lambda I\theta + \frac{1}{2} (2(X^TX)\theta - 2X^Ty)$

We have the gradients to be zero, and:

$$(\lambda I + X^TX)\theta = X^Ty$$






