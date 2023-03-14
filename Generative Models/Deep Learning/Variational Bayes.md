----
#ProbabilityTheory 

Variational Bayesian methods are a set of techniques to approximate posterior distributions in Bayesian Inference. ([[Bayes Rule]]).  As given a model, we're trying to find distributions for the unobserved variables (either parameters or latent variables since they're treated the same). Variational bayes methods would help to estimate that posterior distribution we are looking for.

This note focuses on the traditional mean-field version of the variational bayes.
https://bjlkeng.github.io/posts/variational-bayes-and-the-mean-field-approximation/ 

## KL Divergence as Infromation Gain

Normally, we define [[Entropy]] as the average amount of information or "surprise" for a probability distribution. Entropy is defined as for both discrete and continuous distributions: $$\begin{align}
&H(P) := E_{P}[I_{P}(X)] = - \sum_{i=1} ^n P(x_{i}) \log P(x_{i}) \\
&H(P) := E_{P}{[I_{P}(X)]} = - \int _{\infty} ^\infty p(x) \log(p(x)) \, dx 
\end{align}$$
Note that: when the entropy of a distribution is higehr, the more average the distribution is, and the more randomness would arise from the distribution. Therefore, the required message length to describe the distribution would increase. 

When we are using a distribution $Q$ to model the variables sampled from another distribution $P$, we are looking for our average message length (entropy) to use the parameters of $Q$ to estimate $P$. Under the ideal case when two distributions are identical, they should have the same entropy. 

When we are encoding a "message" from $P$ distribution using $Q$'s code, there would be an extra average message length required for doing so. The measure is given as:
$$H(P,Q) := E_{P}[I_{Q}(X)] = E_{P}[-\log(Q(X))]$$
- This is called the **cross entrop**y between two distributions. 
- This value is alwaus greater than $H(P)$ when $P \neq Q$, since $$H(P,Q) = - \sum_{x} P(x) \log ( Q(x))$$
and the minimum value of the expression above is achieved when P(x) = Q(x). The proof can be found in KL divergence proof

Therefore, the [[Kullback–Leibler divergence (KL)]] is actually a measure of the extra average message length required, which we can write as:
$$D_{KL}(P||Q) = H(P,Q) - H(P) = \sum_{i=1} ^n P(x_{i}) \log \frac{Q(x_{i})}{P(x_{i})}$$

KL Divergence have two directions, which is Forward $D_{KL}(P||Q)$ and Reversed $D_{KL}(Q||P)$. 

- In forward KL, when $P$ is large and $Q\to 0$ the logarithm blows up. Using forward KL as optimization target would encourage the new distribution to cover the range of $P$, which will result in mode averaging. 
- In reversed KL, If $P$ is small, we want $Q$ to be (proportionally) small too or the ratio might blow up. Using reversed KL on multimodel distribution $P$ would encourage the new distribution to fit one of the peaks.

This note uses reversed KL for easier computations.

## Variational Free Energy

In a standard bayesian inference problem, we are looking at the following problem:
$$p(\theta |X) = \frac{P(X,\theta)}{P(X)} = \frac{P(X|\theta)P(\theta)}{\sum_{\theta} P(X|\theta) P(\theta)}$$
- Here $\theta$ are the  latent variables or distribution parameters
- $X$ are the observed data 

The marginal likeliood is also named "evidence"

Our original equation above for bayesian inference can bet translated as: $$
P(\theta |X) = \frac{P(X,\theta)}{P(X)} = \frac{P(X|\theta)P(\theta)}{\sum_{\theta} P(X|\theta) P(\theta)} = \frac{{\text{likelihood} \cdot\text{prior}}}{\text{evidence}}
$$
- $P(\theta|X)$ is the posterior distribution of the parameters given the observed data. This is primarily the end goal of our optimizations, but directly solving for it is normally impossible since the distribution of observed data $P(X)$ is unknown.

Therefore, we are serching for the distribution $Q$ that would minimized the reversed KL divergence between our inference target. The $Q$ distribution is normally shaped with some known distributions like gaussian, and we can wrote this optimization target as:
$$\begin{align}
D_{KL}(Q || P) &= \sum_{\theta|X} Q(\theta) \log \frac{Q(\theta|X)}{P(\theta|X)} \\
&=\sum_{\theta} Q(\theta|X) \log \frac{Q(\theta|X)}{P(\theta,X)} + \sum_{\theta} Q(\theta) \log  P(X) \\
&=\sum_{\theta} Q(\theta|X) \log \frac{Q(\theta|X)}{P(\theta,X)} + \log (P(X))
\end{align}$$
Now our function looks like this:
$$\log P(X) = D_{KL}(Q || P) - E_{Q} [\log \frac{Q(\theta|X)}{P(\theta,X)}] = D_{KL}(Q ||P) + \mathcal{L}_{F}(Q)$$
Where $\mathcal{L}_{F}$ is the **variational free energy**, which is the term that we are trying to maximize. Note that since the left hand side $\log P(X)$ is a constant given the same model, therefore maximize free energy woule be equivalent to minimize the KL divergence. 

## Evidence Lower Bound (ELBO)

Another understanding is to use what we called the **Evidence Lower Bound**. in the origianl kl divergence, we deduced that the KL term can be written as: $$D_{KL}(Q || P) = \sum_{\theta} Q(\theta|X) \log \frac{Q(\theta|X)}{P(\theta,X)} + \log (P(X))$$
Since KL divergence is always a term greater than zero, we have the following relationship:
$$\log P(X) \geq -E_{Q} [\log \frac{Q(\theta|X)}{P(\theta,X)}]$$
And by further expanding, we have:
$$\begin{align}
\log P(X) &\geq -E_{Q} [\log \frac{Q(\theta|X)}{P(\theta,X)}] \\
&= E_{Q}[\log P(\theta,X) -\log Q(\theta|X)] \\
&= E_{Q}[\log P(X|\theta) + \log P(\theta) -\log Q(\theta|X)] \\
&= E_{Q}[\text{likelihood} - \text{prior} + \text{approx.posterior}] = ELBO
\end{align}$$
And this term on the right hand side is the Lower Bound for the evidence term. Maximizing the ELBO is equivalent to minimizing the KL divergence (Since minimizing negative of ELBO would decrease KL).

This is a type of variational inference, like the approach in [[Estimation Maximization (E-M algorithm)]]. We do not have to compute the evidence term, instead we just have to minimize the free energy term. 

This approach is called variational bayes. 

The exact details of this algorithm can be found in the blog post linked above for Mean Field Approximation




