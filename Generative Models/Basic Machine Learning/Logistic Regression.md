------
#BasicMachineLearning 
> ***Problem Type***: [[Classification Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $y^{(i)} \in \{0,1\}$ 
> SOLVE: parameters $\theta \in \mathbb{R}^{n}$ such that $\min_\theta J(\theta) = \frac{1}{N}\sum ^N _{i=1} (-y^{(i)} \log(\sigma(\theta^Tx^{(i)})) - (1-y^{(i)})\log(1-\sigma(\theta^Tx^{(i)})$
> ***Closed-form Solution***: $\theta_{t+1} = \theta_{t} - \alpha \frac{1}{N} \sum ^N _{i=1} (\sigma(\theta^Tx^{(i)}) - y^{(i)})x^{(i)}$ 

Logistic regression is designed for bisecting data as it maps a sigmoid curve to the output target variable, like this:

![[LogisticRegressionSample.png]]

We define our hypothesis function as:
$$h_\theta(x)^{(i)}) = \sigma(\theta^Tx^{(i)})$$
- where $\sigma$ stands for the sigmoid function

We assume the desired distribution in bernouili form:

$P(y = 1 | x ; \theta) = h_\theta(x)$
$P(y = 0|x;\theta) = 1 - h_\theta(x)$

And by combining the functions we have:
$$p(y|x;\theta) = (h_\theta(x))^y(1-h_\theta(x))^{1-y}$$
And we have the [[likelihood]] function as:
$$\mathcal{L}(\theta) = \prod _{i=1}^N (h_\theta(x^{(i)}))^{y^{(i)}} (1-h_\theta(x^{(i)}))^{1-y^{(i)}}$$
For the [[maximum likelihood estimation]], we use the log [[likelihood]] as:
$$\mathcal{l}(\theta) = \sum _{i=1} ^N y^{(i)} \log h(x^{(i)}) + (1-y^{(i)})\log(1-h(x^{(i)}))$$
and this log likehood is our optimization target.

To find the derivative of parameters, we have:

$\dfrac{\partial}{\partial \theta_j} \mathcal{l}(\theta) = (\dfrac{y}{\sigma(\theta^T x)} - \dfrac{1-y}{1-\sigma(\theta^T x)}) \dfrac{\partial}{\partial \theta_j} \sigma(\theta^T x)$ 

$= (...) \sigma(\theta^T x)(1-\sigma(\theta^T x))\dfrac{\partial}{\partial \theta_j}\theta ^T x$ 

$= (y(1-\sigma(\theta^T x)) - (1-y)\sigma(\theta^T x)) x_j$

$= (y-h_\theta(x))x_j$

And with the maximizing term defined we can use gradient descent (or ascent in this case) to approach our optimization target:
$$\theta_{t+1} = \theta_t + \alpha(y^{(i)} - h_\theta(x^{(i)}))x^{(i)}$$
