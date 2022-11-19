----
#ProbabilityTheory 
Required Knowledge: 
[[Likelihood]]

Maximum [[Likelihood]] Estimation (or often called MLE) is an algorithm that solves for the specific parameter(s) $\theta$ of a model or distribution that best fits the observed data. in the math terms, we are trying to have:

$$argmax_{\,\theta}(\mathcal{L}(\theta; \vec{y}))$$
- $\vec{y}$ is the set of observed data 

Since logrithm remapping do not change the point of maximum, optimizing log [[likelihood]] is the same problem. And by the dedinition of log [[likelihood]], we have:

$$argmax_{\,\theta}\mathcal{l}(\theta;\vec{y}) = argmax_{\,\theta} \sum _{i=1} ^n \log( p(y^{(i)};\theta))$$

By definition, the [[likelihood]] function have only one point of maximum, which makes a [[convex optimization problem]]. If we have the set of parameters $\theta$ being:

$$\theta = [\theta_1, \theta_2,...,\theta_k]^T$$

and $\mathcal{l}(\theta;\vec{y}) : \mathbb{R}^n \rightarrow \mathbb{R}$, we can solve for the point where:

$$\nabla_{\theta}\,\mathcal{l}(\theta;\vec{y}) = 
\begin{bmatrix}
\dfrac{\partial \mathcal{l}(\theta)}{\partial \theta_1} \\
\dfrac{\partial \mathcal{l}(\theta)}{\partial \theta_2} \\
.\\
.\\
\dfrac{\partial \mathcal{l}(\theta)}{\partial \theta_n}
\end{bmatrix}= 0$$

The derivative of all parameters relative to the [[likelihood]] function is 0

In many cases, the derivative could not be easily solved at once. In the usual apprach researchers will look for a iterative process and set the maximum [[likelihood]] as the loss function. Data will normally be feed into the algorithm in small batches and the model or distribution gradually fits the observed data. 

