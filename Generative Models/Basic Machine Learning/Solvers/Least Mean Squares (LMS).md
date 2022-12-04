----
#BasicMachineLearning 

Least Mean Squares, or LMS algorithm, is a common practice in solving [[linear regression]] problems. It is base on the loss function that: 

$$J(\theta) = \frac{1}{2} \sum _{i=1}^N ( \theta^T x^{(i)} - y^{(i)}）^2$$

or written in vector form:
$$J(\theta) = \frac{1}{2} || X\theta - \vec{y} ||^2$$
- $J(\theta)$ is the loss function with $\theta \in \mathbb{R}^n$ as parameters
- input featurs $X \in \mathbb{R}^{n \times N}$ , labels $\vec{y} \in \mathbb{R}^N$  
 
The solution to the problem is a iterative process using [[Gradient Descent]]:
$$\theta_{t+1} = \theta_{t} -\alpha (\theta^Tx^{(i)}-y^{(i)})x^{(i)}$$
and to iteratie through the entire dataset at once, which is normally called Batch [[Gradient Descent]]:
$$\theta_{t+1} = \theta_{t} -\alpha \sum _{i=1}^N(\theta^Tx^{(i)}-y^{(i)})x^{(i)}$$
The algorithm will continuously function until convergence.

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
