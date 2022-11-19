----
#BasicMachineLearning 
> ***Problem Type***: [[Regression Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N$ 
> SOLVE: parameters $\theta \in \mathbb{R}^{n}$ such that $\min_\theta J(\theta) = \frac{1}{2} || X\theta - y ||^2 + \lambda||\theta||$ 
> ***Iterative Solution***: $\theta_{(t+1)} = \theta_{(t)} - \alpha(\sum _{i=1}^N (\theta^Tx^{(i)} - y^{(i)})x_j ^{(i)} + sign( \theta_j))$  

[[LASSO]] Regression is the implementation of [[L1 Regularization]] in Linear Regression

$$J(\theta)= \frac{1}{2}|| X\theta - y||_2^2 + \lambda||\theta||$$

By taking derivative we have:

$$\dfrac{\partial J(\theta)}{\partial\theta_j} = \sum _{i = 1} ^N(\theta^Tx^{(i)}-y^{(i)})x^{(i)} _j + sign(\theta_j)$$

Then we can simply plug this formula into the iterative process
