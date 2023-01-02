----
#BasicMachineLearning 
> ***Problem Type***: [[Probabilistic Approach]] ,[[Unsuprevised Learning]], 
> ***Solution Type***: Iterative solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , joint distribution $p(x,z;\theta)$ , the posterior distribution of the implicit variable $p(z|x;\theta)$
> SOLVE: The optimal parameters $\theta^*$  to maximized the observed log likelihood:
> $\max_\theta\log L(\theta) = \sum _{i=1} ^N \log \int_z p(x^{(i)},z;\theta)dz$
> ***Iterative Solution:*** 
> initialize the parameters $\theta_0$ 
> Estimation: $ELBO(\theta_{t+1}|\theta_t) = E_{z\sim p(x,z;\theta_t)}[\log p(x,z;\theta_t)]$ 
> Maximization: $\theta_{t+1}= \arg \max_{\theta} ELBO(\theta|\theta_t)$
> Calculate $\log L(\theta_{t+1})$, and repeat the above two steps until convergence 

In many cases, there exists implicit variables that influnece the distribution of data. The observed distribution $p(x)$ is the integral of the [[Joint Distribution]] between observed variable $x$ and other implicit variables $z$ :
$$p(x) = \int_z p(x,z)dz$$
However, if we can model the influence of implicit variables on our observed variables, or in the other words, we can ge the joint distribution of implicit variable and observed variable, and allowing the parameters within it to be unknown, as:
$$p(x;\theta) = \int_z p(x,z;\theta)dx$$
- Here, $p(x;\theta)$ is the [[Marginal Distribution]] of the $p(x,z;\theta)$

And this is the objective for the Expectation Maximization (E-M) algorithm. The algorithm will be searching for the parameter set $\theta$ that maximize the log likelihood among all samples:
$$\max_\theta\log L(\theta) = \sum _{i=1} ^N \log \int_z p(x^{(i)},z;\theta)dz$$
The E-M approach based on the following conclusion:
$$\log \int_z p(x,z;\theta)dz \geq \int_z \log \frac{p(x,z;\theta)}{q(z)}q(z)d(z), \forall \theta, \forall\int_z q(z)dz = 1$$
and we have the relationship between the distribution of $z$ as:
$$q(z)= p(x|z;\theta), \forall q, z$$

## Jensen Inequality Proof:

Assert arbitrary probabilistic distribution of implicit variables $p(z)$ satisfies:
$$\int_z q(z) dz= 1$$
There exists the constant equality:
$$p(x;\theta) = \int_z q(z) \frac{p(x,z;\theta)}{q(z)}dz, \quad\forall\theta,q$$
And by this we can get the log [[Likelihood]] of $\theta$ as:
$$\log L(\theta|x) = \log \int_z q(z) \frac{p(x,z;\theta)}{q(z)}dz\quad\forall\theta,q$$
The right side of the equation can be represented as expectation:
$$\log L(\theta) = \log E_{z\sim q}[\frac{p(x,z;\theta)}{q(z)}]\quad\forall\theta,q$$
Because of [[Jensen Inequality]], the logrithm of expectation is greater than the expectation of logrithm:
$$\log L(\theta) \geq E_{z\sim q}[\log \frac{p(x,z;\theta)}{q(z)}], \quad\forall \theta, q$$
- The left side of the equation can be also represented as (if we also multiply the left side by $q(z)$):
$$\log L(\theta) = \log \int_z p(x,z;\theta)dx = \log(E_{z\sim q}[ \frac{p(x,z;\theta)}{q(z)}])$$
In this case, since the right side of the inequality is always smaller than the left side for arbitrary $\theta$, we call the right side the **Evidence Lower Bound (ELBO)**.

Because of Jensen Inequality, If we have the terms inside the expectation to be a constant, the inequality woule be equal on both side. 
$$\log[E[C]] = \log(C) = E[\log(C)]$$
we replace the terms inside expectation constant $C$ , as:
$$\frac{p(x,z;\theta)}{q(z)} = C, \forall z$$
And therefore we have:
$$q(z) = \frac{1}{C} p(x,z;\theta)$$
If we integral relative to $z$ on both side:
$$\int_z q(z)dz = \int_z\frac{1}{C}p(x,z;\theta)dz = \frac{1}{C}p(x;\theta)=1$$
And therefore we have the following relationship:
$$q(z) = \frac{p(x,z;\theta)}{p(x;\theta)} = p(x|z;\theta), \forall z$$
Which means that the distribution of implicit variable is equal to the parameterized conditional distribution  of our observed variable $x$ given the implicit variable $z$.

## KL Divergence Proof

For the [[Marginal Distribution]], we follow the [[Bayes Rule]]:
$$p(x;\theta) = \frac{p(x,z;\theta)}{p(z|x;\theta)}, \forall z, \theta$$
We take the logrithm on both side, and have:
$$\log p(x;\theta) = \log p(x,z;\theta) - \log p(z|x;\theta), \forall z, \theta$$
Assume the distribution $q$ of $z$ satisfies:
$$\int_z q(z)dz = 1$$
And we will obtain the equality:
$$\log p(x;\theta) = \frac{\log p(x,z;\theta)}{q(z)} - \frac{\log p(z|x;\theta)}{q(z)}, \forall z,q, \theta$$
- In this step, we subtract a $q(z)$ on the first right term and add $q(z)$ on the second right term, because of log properties we can write these as divisions.

We take expectation relative to $z$ on both side:
$$E_{z\sim q}[\log p(x;\theta)] = E_{z \sim q} [\log \frac{\log p(x,z;\theta)}{q(z)}] + E_{z\sim q}[ - \frac{\log p(z|x;\theta)}{q(z)}] $$
The left side have no relation to $z$, and we can remove expectation:
$$\log p(x;\theta) = \log L(\theta) = \int_z q(z)\log \frac{\log p(x,z;\theta)}{q(z)}dz + \int_z -q(z)  \frac{\log p(z|x;\theta)}{q(z)}dz$$
The second term on the right side is by definition the [[Kullback–Leibler divergence (KL)]] of the two distributions, where:
$$D_{KL}[q(z)||p(z|x;\theta)] = \int_z -q(z)  \frac{\log p(z|x;\theta)}{q(z)}dz$$
And since KL divergence is the measure of difference between distributions (cannot be used as distance due to asymmetry).  This term is always non-negative.

Which gives the first term being the lower bound (ELBO) for the likelihood:
$$\log L(\theta) \geq \int_z q(z)\log \frac{\log p(x,z;\theta)}{q(z)}dz \quad\forall q, \theta$$
And the equality condition remains (when KL Divergence is zero):
$$q(z) = \frac{p(x,z;\theta)}{p(x;\theta)} = p(x|z;\theta)$$
## Simplification of ELBO

Since our original equation is:
$$\log L(\theta) \geq \int_z q(z)\log \frac{\log p(x,z;\theta)}{q(z)}dz \quad\forall q, \theta$$
We can rewrite as:
$$\log L(\theta) \geq \int_z q(z)\log p(x,z;\theta)dz - \int_zq(z)\log q(z)dz$$
And the write term is by definition the **Shannon entropy** of the distribution, which is non-negative and is independent from $\theta$ :
$$H[q(z)] =- \int_zq(z)\log q(z)dz $$
and therefore the final ELBO can be written as:
$$\log L(\theta) \geq \int_z q(z)\log p(x,z;\theta)dz\quad\forall\theta, q$$
## Iterative Solution:

In the above sections, we have proved the equality condition and ELBO. 
We are looking for $\theta$ such that it maximize the log likelihood:
$$\max_\theta\log L(\theta) = \sum _{i=1} ^N \log \int_z p(x^{(i)},z;\theta)dz$$
We start by initialize parameters as $\theta_0$ , have the posterior distribution $p(z|x;\theta_0)$ for the implicit variable, and set it the same as distribution of implicit variable $q(z)$. By doing this, we have the ELBO as a function of $\theta$:
$$\log L(\theta) = ELBO(\theta|\theta_0) = \int_z p(z|x;\theta_0)\log \frac{\log p(x,z;\theta)}{p(z|x;\theta_0)}dz$$
Where we have the property of ELBO, that the function minimum can only be achieved when $\theta = \theta_0$ , else the log likelihood would achieve greater values. 

Therefore, we need to find the better parameter for the ELBO as:
$$\theta_1 = \arg \max_\theta ELBO(\theta|\theta_0)$$
Then the corresponding log likelihood would be also better than current version:
$$\log L(\theta_1) = ELBO(\theta_1|\theta_0) \geq ELBO(\theta_0|\theta_0) = \log L(\theta_0)$$
Here we remove the shannon entropy term, and have the final optimization target as:
$$\arg \max_{\theta_{t+1}} \int_z p(z|x;\theta_t)\log p(x,z;\theta_{t+1})dz$$
And this is our iterative optimiziong target. The iteration will be conducted until the objective likelihood funciton converges. 

## Summary

For the **Estimation** step, we solve for ELBO, or the expectation of the log joint distribution with respect to the implicit variable:
$$ELBO(\theta_{t+1}|\theta_t) =  \int_z q(z)\log p(x,z;\theta_t)dz = E_{z\sim p(x,z;\theta_t)}[\log p(x,z;\theta_t]$$

For the **Maximization** step: we solve for the maximum parameters for ELBO:
$$\theta_{t+1}= \arg \max_{\theta} ELBO(\theta|\theta_t)$$
