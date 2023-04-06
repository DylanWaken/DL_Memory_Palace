
----
#GenerativeModel 

Reference: DDPM paper

![[Screenshot from 2023-04-06 09-56-47.png]]

A diffusion probabilistic model (which we will call a “diffusion model” for brevity) is a parameterized Markov chain trained using variational inference to produce samples matching the data after finite time. 

> Diffusion models are called diffusion models because they are inspired by the physical process of diffusion. In the context of modeling, diffusion is a process where particles or information spread from areas of high concentration to areas of low concentration over time, eventually reaching a state of equilibrium. --GPT4

Note that is note only covers the unconstrainted / unconditional diffusion models. In the future blogs I would cover guided diffusion models with UNet and ControlNet.

## Forward Diffusion Process

The diffusion model is separated into time steps, as we said earlier, in the forward diffusion process, we linearly combine the image with some gaussian noise, as:  $$x_{t} = \sqrt{ 1-\beta_{t} }x_{t-1} + \sqrt{ \beta_{t}} \epsilon_{t-1}$$
- $x_{t},x_{t-1}$ is the image at current and previous time steps
- $\epsilon_{t-1}$ is the gaussian noise we achieved from previous time step, where epsilon is $$\epsilon \sim \mathcal{N}(0_{n}, I_{n})$$ the epsilons are defined as I.I.Ds or independently and identically distributed

- $\beta_{t}$ is the variance of the appended noice. In the common practice there exists a noise schedule that controls this parameter in the forward diffusion process

To actually have the reversed diffusion posterior being possible to get estimated, we define the posterior distribution $q$ of time step t given the timestep $t-1$ as:
$$q(x_{t}|x_{t-1}) = \mathcal{N}(\sqrt{ 1-\beta_{t}}x_{t-1}, \beta_{t}I)$$
- This is a multivariate gaussian distribution
- The first term is the mean of the distribution, the second term is variance
- This distribution is extremely important, in which in the future we will use it to minimize KL divergence

#### Closed form formula for noised images

To compute the noised images at each step faster, we derived a closed form formula as follows:
$$x_{t} = \sqrt{ \bar{\alpha}_{t} }x_{0} + \sqrt{ 1-\bar{\alpha}_{t}} \epsilon$$
- $\bar{\alpha}_{t}$ is the cumulative product of all linear conbination parameters (source image weights) before and include the time step $t$
- $\epsilon$ is the gaussian noise $\epsilon \sim \mathcal{N}(0_{n}, I_{n})$

The derivation of this closed form formula is shown below:

![[diffusion.jpg]]

- Note: the reparameterization trick is the application of the normal distribution properties. This trick is also used in the derivation of parameter update law for [[Variational Autoencoder (VAE)]]

## Variational Posterior Approximation with Reversed Diffusion

Assume we have $T$ time steps

Now, we know that the distribution of the final sample is the marginal distribution for the joint distribution of all 
intermediate samples, as:
$$P_{\theta}(x_{0}) = \sum_{x_{1}:x_{T}} P_{\theta}(x_{0},x_{1},\dots,x_{T})$$
Here we assume that every time step of the sampling process preserved local markov property (in which the next time step is independet from the previous time step given the current time step), in which we can expand this joint distribution using [[Markov Models]]:
$$P_{\theta}(x_{0}:x_{T} ) = P(x_{T}) \prod_{t=1}^T p_{\theta}(x_{t-1}|x_{t})$$

- Note that the first reversed timestep $P(x_{_{T}}) = \mathcal{N} (x_{T} ; 0, I)$ is just a gauss noise

The model assums that this reversed transition process is also in some gaussian distribution, as:
$$p_{\theta}(x_{t-1}|x_{t}) := \mathcal{N}(x_{t-1};\mu_{\theta}(x_{t},t),\Sigma_{\theta}(x_{t}, t))$$
- Note that $\mu_{\theta}$ is predicted by an neural network from the time step $x_{t}$

Like traditional generative models, we are trying to minimize the divergence between model distribution and data distribution, as:
$$\begin{align}
D_{KL}(P(x_{0}) | | P_{\theta}(x_{0})) &= \sum_{x_{0}} P(x_{0}) \log \frac{P(x_{0})}{P_{\theta}(x_{0})} = C -  \sum_{x_{0}} P(x_{0} )\log P_{\theta}(x_{0}) 
\end{align}$$
- $C$ is some constant term decided by the distribution of real world data

Therefore our optimization target term became:
$$\arg\min_{\theta}\mathbb{E}[-\log P_{\theta}(x_{0})]$$

Directly optimizing this target function will be inpractical because we will have to iterate through all possible time step sampls at each step according to the joint distribution we have above. 

This distribution$$P_{\theta}(x_{0:T-1} | x_T)$$
Is not tractable.

#### Derive the variational lower bound

The method get around with this issue is to use some distribution to estimate this untractable distribution through a variational lower bound (like in [[Variational Autoencoder (VAE)]]). We define a new distribution $q(x_{0:T-1}|x_{t})$ to estimate $P_{\theta}(x_{0:T-1}|x_{t})$. 

NOTE: Here we call $q$ the IDEAL reconstruction distribution we are looking for since it is the actual forward posterior, and we are actually using $p_{\theta}$ to estimate $q$:
$$\begin{align}
D_{KL} (q(x_{0:T-1}|x_{T}) | | P_{\theta}(x_{0:T-1}|x_{T}))
\end{align}$$
Since KL divergence is always greater than zero, we have the following expression:
$$\mathbf{E}[-\log P_{\theta}(x_{0})] \leq \mathbb{E}[-\log P_{\theta}(x_{0})] + D_{KL} (q(x_{0:T-1}|x_{T}) | | P_{\theta}(x_asy{0:T-1}|x_{T})) \quad(1.0)$$

By unpacking the KL divergence:
$$E[-\log P_{\theta}(x_{0})] \leq E[-\log P_{\theta}(x_{0})] + \sum_{x_{0:T-1}} q(x_{0:T-1}|x_{T}) \log \frac{q(x_{0:T-1}|x_{T})}{P_{\theta}(x_{0:T-1}|x_{T})} $$
Then we do the decomposing the last log term:
$$E_q\left[\log\frac{P_{\theta}(x_{0:T-1} | x_T)}{q(x_{0:T-1} | x_T)}\right] = E_q\left[\log P_{\theta}(x_{0:T-1} | x_T) - \log q(x_{0:T-1} | x_T)\right]$$
And we have $$E_q\left[\log P_{\theta}(x_{0:T-1} | x_T) - \log q(x_{0:T-1} | x_T) + \log P_{\theta}(x_T) - \log P_{\theta}(x_T)\right]$$
Note that if we combine the first three terms,we will have, because of our markov chain assertion, $P_{\theta}(x_{0:T-1}|x_{t})$  multiplied with $P_{\theta}(x_{t})$ will give us $P_{\theta}(x_{0:t})$:
$$E_q\left[\log \frac{P(x_{0:T})}{q(x_{0:T-1} | x_T)} - \log P(x_T)\right]$$
Apply a negative sign on this term we can cancel out the first term in the original inequality (1.0) as:
$$\mathbb{E}[-\log P_{\theta}(x_{0})] \leq E_q\left[-\log \frac{P(x_{0:T})}{q(x_{0:T-1} | x_T)}\right]\quad(1.1)$$
This is our variational lower bound.
Now we have to rewrite our RHS to get a working optimization target.

#### Derivation of Optimization target

First, we can split the expression within the expectation (divide by a common term on both side of the division and split it using log property):
$$E_q\left[\log \frac{P_{\theta}(x_{0:T})}{P_{\theta}(x_T)} - \log \frac{q(x_{0:T-1} | x_T)}{P_{\theta}(x_T)}\right]$$

Now, let's rewrite $P(x_{0:T})$ using the Markov model definition:
$$P_{\theta}(x_{0:T}) = P_{\theta}(x_0) \prod_{t=1}^{T} P_{\theta}(x_t | x_{t-1})$$
Substitute this back into the expression:

$$E_q\left[\log \frac{P_{\theta}(x_0) \prod_{t=1}^{T} P_{\theta}(x_t | x_{t-1})}{P_{\theta}(x_T)} - \log \frac{q(x_{0:T-1} | x_T)}{P_{\theta}(x_T)}\right]$$

Now, using the markov model on $q$ (Note here that we assume $q$ preserves the local markov property on both sides, which means we can expand the terms in the reversed order),  $$\frac{q(x_{0:T-1} | x_T)}{P_{\theta}(x_T)} = \frac{q(x_0 | x_T)}{P_{\theta}(x_T)} \prod_{t=1}^{T} q(x_t | x_{t-1})$$
We have:
$$E_q\left[\log \frac{P_{\theta}(x_0) \prod_{t=1}^{T} P_{\theta}(x_t | x_{t-1})}{P_{\theta}(x_T)} - \log \frac{q(x_0 | x_T)}{P_{\theta}(x_T)} \prod_{t=1}^{T} q(x_t | x_{t-1})\right]$$

Applying the properties of logarithms and rearranging the terms:
$$E_q\left[-\log P_{\theta}(x_T) + \log \frac{P_{\theta}(x_0)}{q(x_0 | x_T)} + \sum_{t=1}^{T} \log \frac{P_{\theta}(x_t | x_{t-1})}{q(x_t | x_{t-1})}\right]$$
Finally, the term on the RHS of equation (1.1) can be rewritten as:
$$L:=E_{q} \left[ -\log P_{\theta}(x_{T}) - \sum _{t\geq 1}\log \frac{{P_{\theta}(x_{t-1}|x_{t})}}{q(x_{t} | x_{t-1})} \right]\quad (1.2)$$
**Here is where the magic came in.** Unlike SBNs or other stepwise sampling models, the "inference pass of the model" or the forward sampling from data into the model (commonly referred as the untractable posterior as $p(h|x)$ or latent given data), is already defined through another Markov chain, as:
$$q(x_{1:T}|x_{0}) = \prod_{t=1}^T q(x_{t}|x_{t-1})$$
Where $q$ is a distribution we defined earlier as: $$q(x_{t}|x_{t-1}) = \mathcal{N}(\sqrt{ 1-\beta_{t}}x_{t-1}, \beta_{t}I)$$
I did not fully understand these steps here, I will need further clarification on how the these steps works

Now, we can further derive our variational lower bound, as 
$$E_{q} \left[ -\log P_{\theta}(x_{T}) - \sum _{t\geq 2}\log \frac{{P_{\theta}(x_{t-1}|x_{t})}}{q(x_{t} | x_{t-1})} - \log \frac{P_{\theta}(x_{0}|x_{1})}{q(x_{1}|x_{0})} \right]$$
and using the markov definition of $q$, here we reverse the markov chain again, and we have:
$$E_{q} \left[ -\log P_{\theta}(x_{T}) - \sum _{t\geq 2}\log \frac{{P_{\theta}(x_{t-1}|x_{t})}}{q(x_{t-1} | x_{t},x_{0})} \cdot \frac{q(x_{t-1}|x_{0})}{q(x_{t}|x_{0})} - \log \frac{P_{\theta}(x_{0}|x_{1})}{q(x_{1}|x_{0})} \right]$$
Therefore, we can multiply out the term :
$$E_{q}\left[ -\log \frac{P_{\theta}(x_{T})}{q(x_{T}|x_{0})} - \sum _{t\geq 2}\log \frac{{P_{\theta}(x_{t-1}|x_{t})}}{q(x_{t} | x_{t-1},x_{0})}  - \log P_{\theta}(x_{0}|x_{1}) \right]$$
**And finally, we can rewrite this term as a KL divergence (from original paper):**
$$E_{q}\left[D_{KL}(q(x_{T}|x_{0}) | | P_{\theta}(x_{T}))+\sum_{t\geq 2} D_{KL}(q(x_{t-1} | x_{t},x_{0}) | | P_{\theta}(x_{t-1}|x_{t})) - \log P_{\theta}(x_{0}|x_{1})\right]\quad(1.4)$$
- The first term : $D_{KL}(q(x_{T}|x_{0}) | | P_{\theta}(x_{T}))$ is the KL divergence between gaussian noises, and therefore cannot help us minimizing the loss, and therefore is omitted.
- The first term in the summation $D_{KL}(q(x_{t-1} | x_{t},x_{0}) | | P_{\theta}(x_{t-1}|x_{t}))$ is the KL divergence between the reconstructed noise of the "ideal" reconstruciton distribution $q$ and our approximation $p$ . This is estimated stepwise!
- The second term in the summation $\log P_{\theta}(x_{0}|x_{1})$ is the reconstruction likelihood of the original image given the first time step.

## The tractable posterior

Note that, the expression in (1.4) is the computation of KL divergence is considered tractable since we directly defined:
$$q(x_{1:T}|x_{0}) = \prod_{t=1}^T q(x_{t}|x_{t-1})$$
And:
$$q(x_{t}|x_{t-1}) = \mathcal{N}(\sqrt{ 1-\beta_{t}}x_{t-1}, \beta_{t}I)$$
We also have the closed expression for $x_{t}$, as:
$$x_{t} = \sqrt{ \bar{\alpha}_{t} }x_{0} + \sqrt{ 1-\bar{\alpha}_{t}} \epsilon$$
Note tha from our earlier derivation using Bayes theorem, we have the following equivalence:
$$q(x_{t} | x_{t-1}) = q(x_{t-1} | x_{t},x_{0}) \frac{q(x_{t}|x_{0})}{q(x_{t-1}|x_{0})}$$
And therefore we have:
$$q(x_{t-1} | x_{t}, x_{0}) = q(x_{t} | x_{t-1}) \cdot \frac{q(x_{t-1}|x_{0})}{q(x_{t}|x_{0})} $$
Since we already have the stepwise definition of $q$, we only need to define an expression for $q(x_{t-1}|x_{0})$ and $q(x_{t}|x_{0})$. Here we use our closed form formula we derived before, Our definition cames as:
$$q(x_{t-1}|x_{0}) = \mathcal{N}(x_{t-1} | \sqrt{ {\bar{\alpha}_{t-1}}}x_{0} , (1-\bar{\alpha}_{t-1} ) I)$$
And for another term:
$$q(x_{t}|x_{0}) = \mathcal{N}(x_{t} | \sqrt{ {\bar{\alpha}_{t}}}x_{0} ,( 1-\bar{\alpha}_{t} )I)$$
By combining and reparameterization of the above distributions, we can express the final optimization target as:
$$q(x_{t-1} | x_{t}, x_{0}) = \mathcal{N} (x_{t-1}; \tilde\mu_{t}(x_{t}, x_{0}), \tilde \beta_{t}I )\quad(1.5)$$
Where:
$$\tilde \mu _{t} = \frac{{\sqrt{ \bar{\alpha}_{t-1} }\beta_{t}}}{1-\bar{\alpha}_{t}} x_{0} + \frac{\sqrt{ \bar{\alpha}_{t}}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_{t}}x_{t}\quad \tilde\beta_{t} = \frac{{1-\bar{\alpha}_{t-1}}}{1-\bar{\alpha}_{t}}\beta_{t}$$
## Learning algorithm of DDPM

Remember that, in the beginning of this derivation, we choosed our reversed distributino to be marked as:
$$p_{\theta}(x_{t-1}|x_{t}) := \mathcal{N}(x_{t-1};\mu_{\theta}(x_{t},t),\Sigma_{\theta}(x_{t}, t))$$
Like in the [[Variational Autoencoder (VAE)]], we assume there are no co-variances between individual data points (or pixels), we have the following definition that:
$$\Sigma_{\theta}(x_{t},t) = \sigma^2_{t} I$$
For easier computation, we unify the variances between $q$, and $p$, as:
$$\sigma^2_{t} = \beta_{t}$$
- Note that in the original paper, the author states that choosing $\beta_{t}$ or $\tilde\beta_{t}$ have basically no influence on the training outcomes

The first term in the expression or:
$$L_{T} = E_{q}[D_{KL}(q(x_{T}|x_{0}) | | P_{\theta}(x_{T}))]$$
is a constant, its the KL divergence between the forward noising (no learnable terms) and the pure gaussian noise at the start of our reversed diffusion process, and therefore we cannot optimize this term.

By removing non-optimizable terms from our optimization target, we have the loss defined as:
$$L:=E_{q}\left[\sum_{t\geq 2} D_{KL}(q(x_{t-1} | x_{t},x_{0}) | | P_{\theta}(x_{t-1}|x_{t})) - \log P_{\theta}(x_{0}|x_{1})\right]$$
Now, we need to decompose this expression into some stepwise formula. 
$$L_{t-1} := E_{q}\left[D_{KL}(q(x_{t-1} | x_{t},x_{0}) | | P_{\theta}(x_{t-1}|x_{t})) \right]$$
Here, remember we are trying to align the following gaussian distributions:
$$\begin{align}
&p_{\theta}(x_{t-1}|x_{t}) = \mathcal{N}(x_{t-1};\mu_{\theta}(x_{t},t),\beta_t I) \\
&q(x_{t-1} | x_{t}, x_{0}) = \mathcal{N} (x_{t-1}; \tilde\mu_{t}(x_{t}, x_{0}), \tilde \beta_{t}I )
\end{align}$$
These gaussian distributions have "identical" variances (it is considered identical due to our choice of parameterizationm, we can make them mathematically identical like mentioned above, but the current version yields similar results and less computational needs). 

Since KL divergence measures the difference between distributions, the only difference between these distributions are the means, so we can change our optimization target to be minimizing the MSE of the mean values for these distributions, as:
$$L_{t-1} = E_{x_{0},\epsilon}\left[  \frac{1}{2 \sigma^2_{t}} \left\lVert \tilde\mu_{t}(x_{t}, x_{0}) -\mu_{\theta}(x_{t},t) \right\rVert^2 \right]$$
We need some intermediate steps to process the first term, as:
$$\tilde \mu _{t} = \frac{{\sqrt{ \bar{\alpha}_{t-1} }(1-\alpha_{t})}}{1-\bar{\alpha}_{t}} x_{0} + \frac{\sqrt{ \bar{\alpha}_{t}}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_{t}}x_{t}$$
Note that in the beghinning, we defined $x_{t}$ in a closed formula from $x_{0}$, as:
$$x_{t} = \sqrt{ \bar{\alpha}_{t} }x_{0} + \sqrt{ 1-\bar{\alpha}_{t}} \epsilon$$
 we can define $x_{0}$ as some reversely noised term from $x_{t}$ as:
$$x_{0} = \frac{1}{\sqrt{ \bar{\alpha} }_{t}}(x_{t} - \sqrt{  1-\bar{\alpha}_{t}}\epsilon_{t})$$
By replacing $x_{0}$ as $x_{t}$ using the equation above, we have:
$$\tilde \mu _{t} = \frac{1}{\sqrt{ \bar{\alpha} }} \left( x_{t}  - \frac{1-\alpha_{t}}{\sqrt{ 1-{\bar{\alpha}_{t}} }} \epsilon_{t}\right)$$
With the definitions of $x_{0}$ and $x_{t}$, we can cancel out some terms and get:
$$E_{E_{x_{0},\epsilon}} \left[  \frac{1}{2 \sigma^2_{t}}  \left\lVert \frac{1}{\sqrt{ \bar{\alpha} }} \left( x_{t}  - \frac{1-\alpha_{t}}{\sqrt{ 1-{\bar{\alpha}_{t}} }} \epsilon_{t}\right)-\mu_{\theta}(x_{t},t) \right\rVert^2 \right]$$
To align the formulas, the author of the original paper decided to use an reparameterization as the estimation of the mean, as
$$\mu_{\theta}(x_{t},t)  := \frac{1}{\sqrt{ \bar{\alpha} }} \left( x_{t}  - \frac{1-\alpha_{t}}{\sqrt{ 1-{\bar{\alpha}_{t}} }} \epsilon_{\theta}(x_{t},t)\right)$$
- 

And by some simple factoring out common terms, we would have:
$$L_{t-1}= E_{E_{x_{0},\epsilon}} \left[  \frac{(1-\alpha_{t})^2}{2 \alpha_{t} (1-\bar{\alpha}_{t})\sigma^2_{t}}  \left\lVert\epsilon_{t}\ - \epsilon_{\theta}(x_{t},t) \right\rVert^2 \right]$$
And since the factored term is simply a constant, we can ignore it, and write our stepwise final optimization target as:
$$L_{t-1}= E_{E_{x_{0},\epsilon}} \left[  \left\lVert\epsilon_{t}\ - \epsilon_{\theta}(x_{t},t) \right\rVert^2 \right]$$
- We do this loss function on every single timestep within the model (asynchronously while stochastically choose time step to optimize)
- The final reconstruction term is replaces with $L_{0}$, since in the experiments this yields better results (no theoritical explanation given)
- Note here we have an really interesting conclusion. **The final optimization objective is actually trying to minize the difference between the actual noise we added to the image at a specific timestep, and the network predicted noise given the current timestep.** When we predict the noise accurately, we are actually canceling out noise through the reversed sampling process and achieve images we have seen before.

## Training procedure

See the graph below, its clear:

![[Screenshot from 2023-04-06 15-20-37.png]]

