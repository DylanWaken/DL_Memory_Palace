----
#BasicMachineLearning

> ***Problem Type***: [[Regression Problem]], [[Supervised Learning]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $y \in \mathbb{R}^N$ 
> SOLVE: parameters $\theta \in \mathbb{R}^{n}$ such that $\min_\theta J(\theta) = \frac{1}{2} || X\theta - y ||^2$ 
> ***Closed-form Solution***: $\theta^* = (X^TX)^{-1}X^Ty$ 

In linear regression, the data we are given is the set of data vectors $x^{(i)} \rightarrow \mathbb{R}^n : i \in [1,N]$ and set of labels $y^{(i)} \rightarrow \mathbb{R} : i \in [1,N]$ . we assume that the labels are distributed in a linear relation relative to input features.

The very nature of Linear regression is to solve the linear equation such that:

$$X\theta = y$$
since we do not have the ability to directly solve the equation, we are looking for the set of parameters $\theta$ such that:

$$argmin_\theta ||(X\theta - y)||^2$$

We assign each input feature $x_i$ a weight parameter of $\theta_i$ . we also assign the zero-th input feature entry $x_0 = 1$ to have $\theta_0$ to work as the intercept term. The hypothesis function looks like this:

$$h(x) = \sum_{i=0}^n \theta_i x_i = \theta^T x$$
And in order to have the hypothesis funciton approaching the desired function, we define a cost function using the [[least mean squares]] (LMS) algorithm, as:

$$J(\theta) = \frac{1}{2} \sum _{i=1}^N || \theta^T x^{(i)} - y^{(i)} ||^2$$


Proof of Loss:
---

We assume the labels are in a roughly linear relationship to the input features with some noise that are independently and identically distributed (IID), that is:

$$y^{(i)} = \theta^T x^{(i)} + \epsilon^{(i)}$$

We assume that noises are in a [[Gaussian Distribution]]:

$$p(\epsilon^{(i)}) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(\epsilon^{(i)})^2}{2\sigma^2})$$
And by replacing epsilon we have:

$$p(y^{(i)}|x^{(i)};\theta) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(y^{(i)} - \theta^Tx^{(i)})^2}{2\sigma^2})$$
This is the distribution of every $y$ given a specific input feature of $x$ parameterized by the weights of $\theta$

To get the best parameter set of $\theta$, we are using the [[Maximum Likelihood Estimation]] approach among all of our training set:

$$\mathcal{L}(\theta) = \mathcal{L}(\theta;X,\vec{y}) = p(\vec{y}|X;\theta)$$
Using the conditional independence rule ( IID assumption of $\epsilon$ ) to rewrite the [[Likelihood]] into cumulative products:

$$\mathcal{L}(\theta) = \prod _{i=1} ^N p(y^{(i)}|x^{(i)};\theta)$$
$$\mathcal{L}(\theta) = \prod _{i=1} ^N \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(y^{(i)} - \theta^Tx^{(i)})^2}{2\sigma^2})$$
To simplify the maximizing task, we apply the log [[Likelihood]] transform $\mathcal{l}(\theta) = \log (\mathcal{L}(\theta)) \newline$:

$$\mathcal{l}(\theta) = \log(\prod _{i=1} ^N \frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(y^{(i)} - \theta^Tx^{(i)})^2}{2\sigma^2}))$$
$$= \sum _{i=1} ^N \log(\frac{1}{\sqrt{2\pi\sigma^2}} \exp(-\frac{(y^{(i)} - \theta^Tx^{(i)})^2}{2\sigma^2}))$$
$$= n \log(\frac{1}{\sqrt{2\pi\sigma^2}}) - \frac{1}{2\sigma^2} \sum _{i=1} ^N (y^{(i)} - \theta^Tx^{(i)})^2$$
And by removing constants and scaling values we get the optimization target:

$$argmin_\theta \frac{1}{2} \sum _{i=1} ^N (y^{(i)} - \theta^Tx^{(i)})^2$$

Solution:
----
 The original LMS algorithm is an iterative solution process that uses [[gradient descent]] to approach the optimal parameters. 
 
  Since this is a quadratic function, the convex optimizing techniques can be implemented. we can use the normal equation to directly solve the optimal state. We first convert J($\theta$) to a vector form (given that for vecter z we have $z^Tz = \sum _{i}z_{i}^2$):

$$ \frac{1}{2} \sum _{i=1} ^N (y^{(i)} - \theta^Tx^{(i)})^2 = \frac{1}{2} (X\theta-\vec{y})^T(X\theta-\vec{y})$$
Because $J(\theta) : \mathbb{R}^n \rightarrow \mathbb{R}$ , we can solve for the point where gradient (partial derivative of J relative to all the $\theta$ ), that is: 

$$\nabla _{\theta} J(\theta) = \begin{bmatrix}
\dfrac{\partial J(\theta)}{\partial \theta_0} \\
\dfrac{\partial J(\theta)}{\partial \theta_1} \\
...\\
...\\
\dfrac{\partial J(\theta)}{\partial \theta_n} 
\end{bmatrix}

\quad X\theta - \vec{y} =  \begin{bmatrix}
(x^{(1)})^T\theta - y^{(1)} \\
(x^{(2)})^T\theta - y^{(2)}  \\
...\\
...\\
(x^{(n)})^T\theta - y^{(n)}  
\end{bmatrix}$$

$\nabla _{\theta} J(\theta) = \nabla_{\theta} \frac{1}{2} (X\theta-\vec{y})^T(X\theta-\vec{y})$ 

$= \frac{1}{2} \nabla_{\theta}((X\theta)^TX\theta - (X\theta)^T\vec{y} - \vec{y}(X\theta) + \vec{y}^T\vec{y})$ 

$= \frac{1}{2} \nabla_{\theta}(\theta^T(X^TX)\theta - 2(X^T\vec{y})^T \theta)$ 

$= \frac{1}{2} (2(X^TX)\theta - 2X^Ty)$

And thus we derived:

$$X^TX\theta = X^T\vec{y}$$
$$\theta = (X^TX)^{-1}X^T\vec{y}$$
