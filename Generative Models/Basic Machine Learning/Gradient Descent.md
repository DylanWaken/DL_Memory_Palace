----
#BasicMachineLearning 

A classic algorithm in machine learning that uses iterative process to approach the optimal parameters of the hypothesis functions. 

![[GradientDescentSample.png]]

The partial derivative of a loss function relative to the parameters represents the slope of the function at the given parameters. And by modifying the parameters according to the negative partial derivatives, the model will be going on the "fastest downhill direction" of the loss function. When running in a iterative process, this will approach the minimum of the loss function. 

The rule of parameter update:
$$\theta_j := \theta_j - \alpha \dfrac{\partial}{\partial \theta_j} J(\theta)$$
- $\alpha$ is the learning rate, it controls the step size to prevent gradient explosion



