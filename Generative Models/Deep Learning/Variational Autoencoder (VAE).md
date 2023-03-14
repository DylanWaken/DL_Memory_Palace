------
#GenerativeModel 

https://bjlkeng.github.io/posts/variational-autoencoders/

## Decoder 

![[Screenshot from 2023-03-12 20-29-42.png]]

^ The decoder part of the VAE architecture.

The primary objective of the decoder is to sample latent variables from a known destribution, and then using the learned information of the real data distribution to sample data that satisfies the real-world distribution.

To write out the variational decoder out, we have the following terms:$$
\begin{align}
&X_{i} \sim \mathcal{N} (\mu_{i}, \sigma^2 * I) \\
&\mu_{i} \sim g(Z_{1,\dots,K}; \theta) \\
&Z_{k} \sim \mathcal{N} (0,I)
\end{align}$$
- $X_{i=1,\dots,N}$ are the normally distributed observed dat
- $\mu_{\mathbf{i}..,N}$ are the means of the observed variables given the specific latent variables
- $\sigma^2$ is the hyperparameter for variance
- $I$ is the identity matrix
- $g(Z_{1,\dots,K};\theta)$ is the deterministic function parameterized by $\theta$ 
- $Z_{i=1,\dots,K}$ are standard isotrophic normally distributed random variables. it is a k dimensional vector

Here, $X$ is our observed variable, and $Z$ is our implicit latent variable

In this model, the probability of observe a single sample $x$ is:
$$\begin{align}
P(X=x) &= \sum_{z} P(X=x, Z=z) \\
&= \sum_{z} P(X=x |z;\theta) P(z) \\
&= \sum_{z} P_{N} (x;g(z;\theta), \sigma^2 *I)P_{N}(z;0,I) \\
&\approx \frac{1}{M} \sum_{m}^M P_{N}(x;g(z_{m};\theta),\sigma^2 *I)
\end{align}$$
Note: The probability of a single sample is just the joint probability of our given model marginalizing out $Z$. Since we does not have the probability mass function, we are approximating by averaging over $M$ samples form $Z$

Therefore, we can defined our optimization target is the log likelihood function:
$$\log P(X) \approx \sum_{i=1}^N\log \left( \frac{1}{M} \sum_{m}^M P_{N}(x_{i};g(z_{m};\theta),\sigma^2 * I) \right)$$
The problems of this optimization is given as:

- Since $z_{m}$ is a k dimensional vector, the approximation of the marginal distribution would require the sampling through a massive number possible $z$. However, most of the $z_m$ would contribute little to the likelihood sicne most samples from the latent would not yield desirable data.

The solution to this problem is directly sample from posterior $P(z|X=x_{i})$ directly and only use $z$ values that have significant contribution to the function. This approach is similar our approach of [[Sigmoid Belief Networks (SBN)]] 

## Variational Bayes for the Posterior (Encoder)

Since directly solving for the posterior is extremely hard, we would use the variational approach to estimate it. The solution for VAE is the [[Variational Bayes]]. We denote the estimated posterior as $Q(Z|X)$, and therefore our KL divergence term can be written as:
$$\begin{align}
D_{KL} (Q(z|X)||P(z|X)) &= \sum_{z} Q(z|X) \log \frac{Q(z|X)}{P(z|X)} \\
&= E_{z \sim Q}[\log Q(z|X) - \log P (z|X)] \\
&= E_{z\sim Q} [\log Q(z|X) + \log P(X) -\log P (X|z)-\log P(z)] \\
&= E_{z\sim Q} [\log Q(z|X) - \log P (X|z) - \log P(z)]+ \log P(X)
\end{align}$$
Since $P(X)$ is not dependent on $z$, we pull it out of the expectation: $$\log P(X) - D_{KL} (Q(z|X)||P(z|X)) = E_{z \sim Q}[\log P(X|z)] - D_{KL}(Q(z|X)|| P(z))$$
On the left hand side, we have the equations as our optimization objective:

- $\log P(X)$ : maximizing the log likelihood
- $D_{KL} (Q(z|X)||P(z|X))$ : Minimize the KL divergence between estimated and actual posterior

On the right hand side, we have an explicit objective where we know all the pieces, and thus can be maximized by using gradients:

- $P(X|z)$ : the original implicit generative model
- $Q(z|X)$ : approximated posterior destribution
- $P(z)$ : prior distribution of latent variable, already defined

And here, we roughly defined the two components of an VAE: $P(X|z)$ decodes latent samples to reconstruct observed data, and $Q(z|X)$ encodes observed data into latent variables.

## Define the Variational Autoencoder

![[Screenshot from 2023-03-12 20-59-02.png]]

To have an actually operative autoencoder, we have to explicitly define $Q(z|X)$ with a mean and covariance matrix. These components are defined by the encoder network parameters $\phi$ , and the covariance matrix is usually constrained to be diagonal for simplified computation.

Therefore, we have: $$
\begin{align}
&z|X \approx \mathcal{N}(\mu_{z|X}, \Sigma_{z|X}) \\
&\mu_{z|X}, \Sigma_{z|X} = g_{z|X}(X; \phi)
\end{align}$$
- $z|X$ is the approx posterior distribution is multvariate normal distribution
- $\mu_{z|X}$ is a vector of means for the normal
- $\Sigma_{z|X}$ is the diagonal co-variance matrix for the normal
- $g_{z|X}$ is the function approximator
- $\phi$ is the network parameter

Therefore, the full architecture is shown by the above image. The red boxes are the loss function of the model, as:
$$\begin{align}
&D_{KL} (\mathcal{N} (\mu_{z|X}), \Sigma_{z|X} || \mathcal{N}(0,I))\quad\text{Inference Loss} \\
&|| X-\mu_{X|z}||^2\quad\text{Reconstruction Loss}
\end{align}$$
The objectives for the Inference (encoder) is to minimize the difference between the generated $z$ distribution and the designed standard $z$ distribution,  while the reconstruction loss is trying to minimize the difference between input sample and mean of reconstructed sample. 

The naive forward pass is defined as:

- 1. Input sample of $X=x_{i}$
- 2. Computing the $\mu_{z|X}$ and $\Sigma _{z|X}$ from $g_{z|X}(X;\phi)$
- 3. Sample $z$ values from the Inference estimated posterior distribution: $\mathcal{N} (\mu_{z|X}, \Sigma _{z|X})$
- 4. Compute $\mu_{X|z}$ to produce the mean of the reconstructed output. 

**Note: This Mean here does not refer to the mean of the entire data distribution, but referes to the mean for the posterior distribution of the reconstructed data given a specific latent state.**

The problem in this design is that the gradients can not propagate through the stochastic sampling process of $z$, and therefore reconstruction gradients cannot optimize the encoder network.

Therefore, a parameterization trick is deployed in the architecture. Since we have the following properties for normal distributions:
$$\mathcal{N}( \mu_{z|X},\Sigma_{z|X}) = \mathcal{N}(0,1) * \Sigma_{z|X} + \mu_{z|X}$$
And this allows us to propagate gradient through the values, and exclude the stochastic sampling from back propagation.

The gradients for the encoder and decoder networks are given as:
$$\begin{align}
&\frac{\partial}{\partial \theta} (X-\mu_{X|z})^2 \\
&\frac{\partial}{\partial \phi} (X-\mu_{X|z})^2 \\
& \frac{\partial}{\partial \phi} D_{KL}(Q(z|X)|| P(z))
\end{align}$$
## Proof of Loss

In the previous section, we defined our optimization objective as:
$$\log P(X) - D_{KL} (Q(z|X)||P(z|X)) = E_{z \sim Q}[\log P(X|z)] - D_{KL}(Q(z|X)|| P(z))$$
However, since we do not have the distribution parameters for $P(z|X)$ and $P(X|z)$, we would optimize upon a single fused objective function and the data samples. 

We can rewrite the original objective as:
$$E_{X\sim D}[\log P(X) - D_{KL} (Q(z|X)||P(z|X))] = E_{X\sim D}[E_{z \sim Q}[\log P(X|z)] - D_{KL}(Q(z|X)|| P(z))]$$
- The expectation $E_{X\sim D}$ stands for the expectation over relavent variables (?)

Since directly estimating the RHS objective is not feasible, we took the approximation approach:
$$\begin{align}
RHS=E_{X\sim D}[E_{\epsilon \sim N(0,I)}[\log P(X|z=\mu_{z|X}(X) + \Sigma_{z|X}^{1/ 2}(X_{i})*\epsilon)] - D_{KL}(Q(z|X)|| P(z))]
\end{align}$$
This step is achieved by replacing our parameterization trick into the original distribution

Then, we will estimate the $E_{X \sim D}$ through taking $N$ data samples from real world distribution, and our objective is given as:
$$\approx\frac{1}{N} \sum _{x_{i} \in X} E_{\epsilon \sim N(0,I)}[\log P(x_{i}|z=\mu_{z|X}(x_{i}) + \Sigma_{z|X}^{1/ 2}(X_{i})*\epsilon)] - D_{KL}(Q(z|x_{i})|| P(z))$$
Each time we evaluate the network, we must explicitly sample a _new_ value $\epsilon$ from our isotropic normal distribution. We can simplify the internal expectation $E_{\epsilon \sim N(0,I)}$ by pair each observation $x_{i}$ with a bunch of samples from $N(0,I)$ to make a "full input" throughout the training process. $$
\approx\frac{1}{N} \sum _{x_{i} \in X} \log P(x_{i}|z=\mu_{z|X}(x_{i}) + \Sigma_{z|X}^{1/ 2}(x_{i})*\epsilon)- D_{KL}(Q(z|x_{i})|| P(z))
$$
And finally, using the definition of every term, we can simplify our optimization objective as:
$$\frac{1}{N} \sum_{x_{i}\in X} -\frac{1}{2\sigma^2} (x_{i}-\mu_{X|z})^2 - \frac{1}{2}( tr(\Sigma_{z|X}(x_{i}))+(\mu_{z|X}(x_{i}))^T(\mu_{z|X}(x_{i}))-k-\log \det(\Sigma_{z|X}(x_{i})))$$
- The first part of the equation is the MSE loss defined upon likelihood maximization of distribution $P(x_{i}|z)$
- The second part of the equation is the original KL divergence. It cames from the standard computation of the KL divergence between two multivariate normals.