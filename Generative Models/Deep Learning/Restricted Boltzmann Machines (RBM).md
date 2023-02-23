------
#GenerativeModel 

The restricted boltzmann machine is the variant of the original [[Boltzmann Machines]]. In the RBM architecture, units are separated into hidden and visible layers, while all connections between units in the same layer have been dropped or removed. 

The most important consequence for this bipartite architecutre is that **The hidden node activations are mutually independent given the visible unit activations**. This theorm also holds reversely as the activation of every visible units are independent to each others given the hidden units.

The energy function definition of RBM is defined as:
$$E(v,h) = - \sum_{i} a_{i}v_{i} - \sum_{j} b_{j}h_{j} - \sum_{ij} w_{ij} v_{i} h_{j}$$
- $a_{i}$ is the bias terms for the $i$ th visible node $v_{i}$
- $b_{j}$ is the bias term for the $j$ th hidden node $h_{j}$
- $w_{ij}$ is the bi-directional weight connecting the $i$ th visible node and $j$ th hidden node.

In the matrix vector notation, the same relationship can be written as:
$$E(v,h) = -a^Tv -b^T h-v^TWh$$
Using the boltzmann distribution to convert energy to probability, we have the probability for every visible state the network stops with:
$$P(v) = \sum_{\{h\}} \frac{1}{Z} \exp(-E(v,h))$$
- $\{ h \}$ is the set of all hidden states

The property of conditional independence between visible and hidden units gives an extremely neat alternatie in calculating the probabilities:
$$P(v|h) = \prod_{i} P(v_{i}|h),\quad P(h|v) = \prod_{j} P(h_{j}|v)$$
Like in the boltzmann machine note, we compute the difference of energy $\Delta E$ as:
$$E(v_{i} = 1 | h) - E(v_{i} = 0 | h) = a_{i} + \sum_{j} w_{ij}h_{j}$$
And our relation from boltzmann distribution still holds:
$$\Delta E_i = k_BT \log(p_{v_{i}=1} ) - k_BT\log (p_{v_{i}=0})$$
Therefore, we can derive the probability difference as:
$$P(v_{i}=1|h) = \frac{1}{1+ \exp(-\frac{\Delta E_i}{k_BT})}$$
Note for the ease of annotation, we would merge the term for boltzmann constant into temperature.
Here, we can replace the function with sigmoid, and written it as:
$$P(v_{i}=1|h) = \sigma \left(\frac{1}{T} (a_{i} + \sum_{j} w_{ij}h_{j}) \right)$$
And the formula is the same for hidden units respect to visible units. When $T=1$, the function would be a standard sigmoid. 

## Contrastive Divergence

The contrastive divergence was build upon an idea of arbitrary energy based models with $x$ as the visible nodes and parameterized by some $W$. 

The Contrastive Divergence optimization treats the model distribution as the infinitely far step of an markov chain converging toward it, and we run finite steps on the model to extimate the model distribution. We clamp the data into the model, and update the model using Gibbs sampling by its parameters.

In the traditional unsupervised learning with [[Maximum Likelihood Estimation]], the models would maximize the likelihood of train data. 
$$\mathcal{L}(W; X) = \frac{1}{N}\sum_{n}^N \log p(x_{n};W) = \langle \log p(x;W)\rangle _{0}$$
Using the definition of [[Boltzmann Distribution]], we are able to rewrite the same formula as:
$$p(x;W) = \frac{1}{Z(W)} \exp(-E(x;W)) \to \mathcal{L}=-\langle E(x;W) \rangle_{0} - \log Z(W)$$
Where:
$$Z(W) = \sum_{x} \exp(-E(x; W))$$
Deriving the first part can easily be done, but deriving the second part is a little compliex, shown below:
$$\begin{align}
\frac{{\partial \log Z(W)}}{\partial W} &= \frac{1}{Z(W)} \frac{{\partial Z(W)}}{\partial(W)} \\
&= \frac{1}{Z(W)} \sum_{x} \frac{\partial}{\partial x} \exp(-E(x;W)) \\
&= \sum_{x} \frac{1}{Z(W)}\exp(-E(x;W)) \frac{\partial}{\partial x} -E(x;W) \\
&= -\left\langle  \frac{{\partial E(x,W)}}{\partial W} \right\rangle _{\infty} 
\end{align}$$
And if we take the partial derivatives, we would have:
$$\frac{\partial\mathcal{L}}{\partial W} = -\left\langle  \frac{{\partial E(x,W)}}{\partial W} \right\rangle _{0} + \left\langle  \frac{{\partial E(x,W)}}{\partial W} \right\rangle _{\infty}$$
- $\langle.\rangle_{0}$ is the expectation over the data distribution $p_0$, this is found from data.
- $\langle . \rangle _\infty$ is the expectation over the model's distribution $p_\infty$. The infinity symbol here stands for the modeli's distribution as an infinitely far step for the markov chain.

The problem in this approach is that the partition function $Z(W)$ cannot be directly computed in a reasonable time complexity, and therefore must be approximated.

> The standard approach is to approximate the average over the distribution with an average over a sample from $p(x;W)$, obtained by setting up a Markov chain that converges to $p(x;W)$ and running the chain to equilibrium. it is typically very slow, since running the Markov chain to equilibrium can require a very large number of steps, and no foolproof method exists to determine whether equilibrium has been reached.

The MLE is trying to minimize the [[Kullback–Leibler divergence (KL)]] between the data distribution and model distribution of visible units, as:
$$\arg \min_{W} D_{KL}(p_{0} || p_{\infty}) = \arg \min _{W} \sum_{x} p_{0}(x) \log \left( \frac{p_{0}(x)}{p(x; W)} \right)$$
The alternative methods proposed by Hinton involves the following definition of **Contrastive Divergence**:
$$CD_{n } = D_{KL} (p_{0} || p _\infty) - D_{KL}(p_{n}| | p_{\infty})$$
Which, if we convert to our gradient expression, would stand for:
$$\frac{\partial CD}{\partial W} = -\left\langle  \frac{{\partial E(x,W)}}{\partial W} \right\rangle _{0} + \left\langle  \frac{{\partial E(x,W)}}{\partial W} \right\rangle _{n}$$
- Where $n$ is the steps we run on the markov chain starting from the data distribution. 

## Contrastive Divergence of RBM

Under the case of restricted boltzmann machines, the CD happens in an iterative manner. 

![[Contrastive Divergence.png]]

In the first step of $x_{0}$, we clamp data into the visible nodes, and gibbs sample our hidden units:
$$h_{t} \sim p(h|v_{t}) $$
After the hidden units are sampled, we reconstruct the data using the hidden units and the weight, taking a step forward in the model's distribution:
$$v_{t+1} \sim p(v|h_{t})$$
According to the assumptions in contrastive divergence, the repeating of this process would converge the visible units toward the model's equilibrium. 

What really interesting about this pattern is that, given enought steps in the alternative Markov Chain, the states of both visible and hidden units actually modeled the joint distribution of the model, as $P(v,h)$

After taking $n$ steps forward, we can utilize our update rule to figure out the gradients for the weigths and biases as:
$$\begin{align}
&\frac{{\partial \log P(v)}}{\partial w_{ij}} = P(h_{i}=1|v^{(0)})v_{j}^{(0)} - P(h_{i}=1|v^{(n)})v_{j}^{(n)} \\
&\frac{\partial \log P(v)}{\partial a_{i}} = v_{i}^{(0)} -v_{i}^{(n)} \\
& \frac{{\partial \log P(v)}}{\partial b_{j}}= P(h_{i}=1|v^{(0)}) - P(h_{i}=1|v^{(n)})
\end{align}$$
The proof is given below: