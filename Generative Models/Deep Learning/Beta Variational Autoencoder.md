----
#GenerativeModel 

Beta Autoencoder is the variation of the original [[Variational Autoencoder (VAE)]]. The primary objective is to apply the ideas in disentangled unsupervised learning (the process which different latent variables are corresponding to the representation of different information in the input data).

> We propose augmenting the original VAE framework with a single hyperparameter β that modulates the learning constraints applied to the model. These constraints impose a limit on the capacity of the latent information channel and control the emphasis on learning statistically independent latent factors. β-VAE with β = 1 corresponds to the original VAE framework. With β > 1 the model is pushed to learn a more efficient latent representation of the data, which is disentangled if the data contains at least some underlying factors of variation that are independent.

In the beta-VAE framework, we assume real world data to be composed of facters:
$$\mathcal{D} = \{ X,V,W \}, \quad x \in \mathbb{R}^N, v\in\mathbb{R}^K, w\in \mathbb{R}^H$$
- $x$ is the raw image data sampled from real world.
- $v$ is the real world generation factors, conditionally independent: $\log P(v|x) = \sum_{k} \log p(v_{k}|x)$ 
- $w$ is the real wold generation factors that are conditionally dependent on each others.

The idea is that every $x$ came from specific generation factors, as: $$p(x|v,w)$$
The primary objective of the beta-VAE is to develop the unsupervised learning algorithm that using only data samples from $X$ to produce a set of generative latnet factors $z \in \mathbb{R}^M$ such that the following relationship satisfies:
$$p(x|z) \approx p(x|v,w)$$
In the original VAE approach, the latent distribution configuration is generated through the inference network with the function approximator $g_{z|x} (x; \phi)$ (which can be also understood as the distribution $q(z|x;\phi)$).  

The isotropic distribution $p(z)$ is used as the prior distribution in VAE latent sampling, which assumes that the different dimensions of the latent variables are statistically independent and equally likely. 

By matching the posterior distribution $p(x|z)$ to this prior, the model is encouraged to learn a representation where the different generative factors are statistically independent of each other, which makes it easier to manipulate the data and understand how the different factors affect the output.

Therefore, the paper imposed a constraint on the VAE optimization target, as:
$$\max_{\phi,\theta} E_{x \sim D} [E_{q_{\phi}(z|x)}(\log p_{\theta}(x|z))] \quad s.t. \quad D_{KL}(q(z|x)|| p(z)) < \epsilon$$
- Note that though the KL divergence here is originally a part of the VAE optimization target itself, but now it is forces to be limited under a pre-defined minimum.

And therefore, we can use [[Lagrange Multiplier]] and [[Karush–Kuhn–Tucker Conditions]] to rewrite this optimization target into:
$$E_{x\sim D}[E_{z \sim Q}[\log p(x|z)] - \beta D_{KL}(q(z|x)|| P(z))]$$
Now, when $\beta = 1$, the function behaves like traiditional VAE
When $\beta > 1$, a strong latent bottleneck for the VAE factors, encourage the network's latent factors to be more conditional independent from each others.

