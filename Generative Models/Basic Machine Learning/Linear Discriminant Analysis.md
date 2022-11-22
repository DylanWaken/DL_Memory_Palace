----
#BasicMachineLearning 
> ***Problem Type***: [[Classification Problem]], [[Supervised Learning]], [[Generative Learning]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N$ 
> SOLVE: Gaussian distribution parameters $\mu_i$ for each class, covariance matrices for all classes $\Sigma$ , and class probabilities $p(y=i)$
> ***Closed Form Solution: 
> $p(y=i) = \frac{1}{N} \sum _{j=1} ^N \mathbb{1} \{y^{(j)}=i\}$
> $\mu_i = \dfrac{\sum_{j=1} ^N \mathbb{1}\{y^{(j)} = i\} x^{(j)}}{\sum_{j=1} ^N \mathbb{1}\{y^{(j)} = i\}}m \quad i \in \{1,2,...,C\}$
> $\Sigma = \dfrac{1}{N} \sum _{i=1} ^N (x^{(i)} - \mu_{y^{(i)}})(x^{(i)} - \mu_{y^{(i)}})^T$ 

Linear Discriminant Analysis (LDA) is the generalized form of [[Fisher Linear Discriminant Analysis]]
The LDA algorithm would try to build the distribution of the samples, and use [[Bayes Rule]] to determine the class probability of a new sample, the decision boundry is implicit.  

In LDA problems, the following assumptions are made:

- **Independence**: The variables are distributed independent to each others
- **Multivariate Normallity**: Variables are distributed in [[Multivariate Gaussian Distribution]]
- **Homogeneity of Covariance**: All variables have the same convariance matrix. If this condition does not satisfy, another approach of Quadratic Discriminant Analysis (QDA) will be used  (since the decision boundry will be parabolic instead of hyperplane in that case)
- **Multicollinearity**:  The predictor performance would decrease when classes are distributed nearby

This problem is also a part of Gaussian Discriminant Analysis (GDA), which includes LDA and QDA

## Two class LDA

![[LDA.png]]

The two class is designed based on the assumption that:
$$y \sim Bernoulli(\phi) \quad x|y=0 \sim \mathcal{N}(\mu_0,\Sigma)\quad x|y=1 \sim \mathcal{N}(\mu_0, \Sigma)$$
And the distributions can be written as:

$p(y) = \phi^y(1-\phi)^{1-y}$

$p(x|y=0)= \dfrac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}\exp(-\dfrac{1}{2}(x - \mu_0)^T \Sigma^{-1}(x-\mu_0))$

$p(x|y=1)= \dfrac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}\exp(-\dfrac{1}{2}(x - \mu_1)^T \Sigma^{-1}(x-\mu_1))$

And here we can still use the maximum [[likelihood]] estimation approach to find the parameters for the normal distributions. 

We have the log likelyhood of the joint distribution to all parameters defined as:
$$l(\phi,\mu_0, \mu_1, \Sigma) = \log \prod _{i=1} ^N p(x^{(i)},y^{(i)}; \phi, \mu_0, \mu_1, \Sigma)$$

$$l(\phi,\mu_0, \mu_1, \Sigma) = \log \prod _{i=1} ^N p(x^{(i)}|y^{(i)}; \phi, \mu_0, \mu_1, \Sigma) p(y^{(i)};\phi)$$
And by some simple deriving process (not shown here), we can fin the optimal parameters to be:

$\phi = \dfrac{1}{N} \sum _{i=1} ^N \mathbb{1}\{y^{(i)} = 1\}$

$\mu_0 = \dfrac{\sum_{i=1} ^N \mathbb{1}\{y^{(i)} = 0\} x^{(i)}}{\sum_{i=1} ^N \mathbb{1}\{y^{(i)} = 0\}}$

$\mu_0 = \dfrac{\sum_{i=1} ^N \mathbb{1}\{y^{(i)} = 1\} x^{(i)}}{\sum_{i=1} ^N \mathbb{1}\{y^{(i)} = 1\}}$

$\Sigma = \dfrac{1}{N} \sum _{i=1} ^N (x^{(i)} - \mu_{y^{(i)}})(x^{(i)} - \mu_{y^{(i)}})^T$

By solving the problem, we have normal distributions, and we can make predictions based on the following rule:
$$p(y|x) = \frac{p(x|y)p(y)}{p(x)}$$
- where $p(x) = p(x|y=1)p(y=1) + p(x|y=0)p(y=0)$ is the distrib of all $x$ 

And the constant denominator can be ignored, since we are judging with
$$\arg \max _y p(y|x) = \arg \max _y \frac{p(x|y)p(y)}{p(x)} = \arg \max_y p(x|y)p(y)$$
## Multiclass LDA

In the multi-calss case, all the other assumptions holds true, with the only difference being the way  $p(y)$  
is distributed, since traditional bernoulli distribution only works for 2 classes.

The original bernoulli distribution came from the combination of the following two functions:

$p(y=1) = \phi$

$p(y=0) = 1 - \phi$

Following the same rule, we can assign the class probabilities to each class as:
$$p(y=i) = \frac{1}{N} \sum _{j=1} ^N \mathbb{1} \{y^{(j)}=i\}$$
With the mean for each class and total covariance as:

$\mu_i = \dfrac{\sum_{j=1} ^N \mathbb{1}\{y^{(j)} = i\} x^{(j)}}{\sum_{j=1} ^N \mathbb{1}\{y^{(j)} = i\}}m \quad i \in \{1,2,...,C\}$

$\Sigma = \dfrac{1}{N} \sum _{i=1} ^N (x^{(i)} - \mu_{y^{(i)}})(x^{(i)} - \mu_{y^{(i)}})^T$

And the prediction rule is the same as the multiclass bayes rule as:
$$p(y|x) = \frac{p(x|y)p(y)}{\sum_{i=1} ^{c} p(x|y=i)p(y=i)}$$
And since the denominator is constant,
$$p(y|x) = p(x|y)p(y)$$ 