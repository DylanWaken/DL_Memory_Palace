----
#BasicMachineLearning 
> ***Problem Type***: [[Classification Problem]], [[Supervised Learning]], [[Generative Learning]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N$ 
> SOLVE: Fisher Linear Discriminant Direction $w^* \in \mathbb{R}^n$ such that $\max_w J_F(w)$ 
> ***Closed Form Solution: $w^* = S_w^{-1} (\mu_1 - \mu_2)$

![[FLD_sample.png]]

For a binary classification problem, Fisher Linear Discriminant seaches for the optimal projection line, such that the sample points have minimal in-class distance and maximum cross-class distance on the  **Fisher Linear Discriminant Direction**

To solve for it, we have the means of the classes as:
$$\mu_i = \frac{\sum_{x\in \Omega_i}x}{\Omega_i}$$
- where $\Omega_i$ is the ith class's samples

And we can calculate the class [[Covariance Matrix]] as:
$$S_i = \sum _{x \in \Omega_i}(x-\mu_i)(x- \mu_i)^T$$
The universal covariance matrix can be calculated as:
$$S_w = S_1 + S_2$$
And the inter-class convatiance matrix:
$$S_b = (\mu_1-\mu_2)(\mu_1-\mu_2)^T$$
If we have vector $w$ satisfying $w^Tw=1$, then the projection length of sample $x$ on $w$ is
$$\frac{w^Tx}{||w||}=w^Tx$$
By using this property, we can calculate the mean and convariance by:
$$\hat\mu_i = \frac{\sum_{x\in \Omega_i} w^Tx}{\Omega_i}= w^T\mu_i$$
$$\hat S_i =  \sum _{x\in \Omega_i} (w^Tx - \hat \mu_i)^2$$
$$\hat S_w = \hat S_1 + \hat S_2$$
$$\hat S_b = (\hat \mu_1 - \hat \mu_2)^2$$
Because we want the greatest inter-class distance and minimal in-class distance, we want to maximize the inter-class covariance $\hat S_b$ and minimize both in-class covariances $\hat S_w$ .

We can define the Fisher loss function:
$$J_F(w) = \frac{\hat S_b}{\hat S_w} = \frac{(\hat \mu_1 - \hat \mu_2)^2}{\hat S_1 + \hat S_2}$$
## Solving Fisher LDA

 In the original problem we have the objective
$$\max_w J_F(w) = \max_w  \dfrac{(\hat \mu_1 - \hat \mu_2)^2}{\hat S_1 + \hat S_2}$$
and by exbanding the problem and replace the distance mean, cov with original sample mean, cov,  we have:
$$=\frac{(w^T(\mu_1-\mu_2))((\mu_1-\mu_2)^Tw)}{w^T[\sum_{i=1,2}\sum_{x\in \Omega_x}(x-\mu_i)(x-\mu_i)^T]w} = \frac{w^TS_bw}{w^TS_ww}$$
Because the norm length would cancel itself out in the final formula, we do not maintain the constraint for $||w|| = 1$. To ensure the denominator to be non zero, we set the denominator to be a constant, and include it as a constraint for the problem:
$$\max _w w^TS_bw \quad s.t. \quad w^TS_ww = c$$
Using [[Lagrange Multiplier]] to get the Lagrangian form:
$$\mathcal{L}(w, \lambda) = w^TS_b w + \lambda(w^TS_ww-c)$$
To solve for the maximum of the function, we solve the zero derivative:
$$\nabla_wL(w,\lambda) = 2S_bw + 2\lambda \cdot S_ww = 0$$
And by solving it:
$$S_w^{-1}S_b w^*= \lambda w^* $$
From the source definition, we have
$$S_bw^* = (\mu_1-\mu_2)(\mu_1-\mu_2)^Tw^*=R\cdot(\mu_1-\mu_2)$$
proved that $S_bw^*$ is on the same direction of $(\mu_1-\mu_2)$  scaled by $R = (\mu_1-\mu_2)^Tw^*$
Because the norm or magnitude of $w$ does not influence it direction, we ignore the scaling term:
$$w^* = S_w^{-1} (\mu_1 - \mu_2)$$
For prediction, we fit two distributions onto the projection lengths and use [[Bayes Rule]] to classify the data points, like in [[Gaussian Discriminant Analysis]]

