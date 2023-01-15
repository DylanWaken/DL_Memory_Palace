----
#GenerativeModel 

![[Screenshot from 2023-01-10 18-58-52.png]]

The Wake-Sleep algorithm is basically treating the model as 2 reversely directional sigmoid belief network combined with different purposes, namely Pattern Generation and Pattern Recognition networks.

All variables marked with $G$ means it belongs to the generative SBN, while all variabels marked with $R$ means it belongs to the recognition SBN

## The Algorithm

1: Zero initialized the parameters
2: The wake phase:
       Set the data layer to observed data, and sample all the explanary layers according to the conditional probabilities of the recognition network 
       Update the generative network according to the gradient with respect to Holmholtz Free Energy:
       $$\begin{align}
&\nabla _{W_{G}}E_{G} = -(s_l - \sigma(w^G_{l}s_{l+1}+b^G_{l})) (s_{l+1})^T \\ 
&\nabla _{b_{G}}E_{G} = -(s_l - \sigma(w^G_{l}s_{l+1}+b^G_{l}))  
\end{align}$$
3: The sleep phase:
     Sample the top-most hidden layer according to the bias, and sample every layer all the way to the data layer according to the weights of the generative network
     Update the recognitive network according to the gradient with respect to the KL divergence term:
     $$\begin{align}
&\nabla _{W_{R}}\log P_{R}(h|v) = -(s_l - \sigma(w^R_{l}s_{l-1}+b^R_{l})) (s_{l-1})^T \\ 
&\nabla _{b_{R}}\log P_{R}(h|v) = -(s_l - \sigma(w^R_{l}s_{l-1}+b^R_{l}))  
\end{align}$$
4: Repeate until the KL divergence between generative and recognition distributions approach zero

## Pattern Generation 

In arbitrary [[Sigmoid Belief Networks (SBN)]], the relationships between nodes and its parents is modeled through conditional probability relationship, in which:
$$P(H_{l,i}|H_{l+1})=\sigma(w_{l+1} H_{l+1} + b_{l+1})$$
- The fundation layer that models the real-world data is refered as "data layer"
- The other layers functioning as explanations is refered as "hidden layer"

For the top layer of the generative network, the probability of a specific layer state is only dependent on the bias of the neurons in the layer, as:
$$P_{G}(s_{k}) = \prod_{i} (s_{k,i})^{s_{k,i}}[1-P_{G}(s_{k,i})]^{1-s_{k,i}}$$
where:
$$P_{G}(s_{k}) = \sigma(b_{k}^G)$$
- here $k$ is just the layer label following the figure.

And for any other layers, the probability is considered a conditional probability:
$$P_{G}(s_{l} |s_{l+1}) = \prod_{i} P_{G}(s_{l,i}|s_{l+1})^{s_{l,i}}[1-P_{G}(s_{l,i}|s_{l+1})^{s_{l,i}}]^{1-s_{l.i}}$$
where:
$$P_{G}(s_{l,i}|s_{l+1}) = \sigma\left( \sum _{j=1} ^{n_{l+1}} w_{ij}^G y_{j} + b^G _{i} \right)$$
With these calculations defined, we can bring in the law of [[Boltzmann Distribution]].


## Pattern Recognition

When we run the recognition SBN network, the structure is a little bit different.

The first layer is the input data, and there is no bias applied or probabilities for sampling calculated.

The calculation for other layers is identical as the generative pass:
$$P_{R}(s_{l} | s_{l-1}) = \prod _{i} P_{R}(s_{l,i})^{s_{l,i}}[1-P_{R}(s_{l,i})^{1-s_{l,i}}]$$
Where:
$$P_{R}(s_{l,i}|s_{l-1}) = \sigma\left( \sum _{j=1} ^{n_{l-1}} w_{ij}^R y_{j} + b^R _{i} \right)$$


## Free Energy

For easier notation, we define $K$, $J$ and $I$ as the vector state of the three layers we shown above in figure 1. The rules we deduced can apply to arbitrarily depth networks though

Given a fixed external data $I$, we are able to write the corresponding probability of the hidden layer states as:
$$P_{G} (K,J|I) = \frac{{P_{G}(K,J,I)}}{P_{G}(I)} =  \frac{{P_{G}(K,J,I)}}{\sum_{KJ} P_{G}(K,J,I)}$$
And this is exactly the same form in [[Canonical Ensemble]].  Here we can replace the joint distributions with an energy definition that:
$$E_{KJI} = - \log P_{G}(K,J,I)$$
And rewrite the original function as:
$$P_{G} (K,J|I)  = \frac{\exp[-E_{KJI}]}{\sum_{KJ}\exp[-E_{KJI}]}$$
- Note: here we set temperature to 1 for easier steps
- The partition function here is just the probability of the specific state of data layer (predicted by the model)

Since our primary learning objective is to have the probability of generated data $P_G(I)$ to be as close as the probability of the real world conterpart $P(I)$, we would use again [[Kullback–Leibler divergence (KL)]] as our primary optimization target by minimizing the following function:
$$\phi(G) = D_{KL}[P(I),P_{G}(I)] = \sum_{I} P(I) \log {P(I)} - \sum_{I} P(I) \log P_{G}(I)$$
Since the first term is a constant (the [[Gibbs Entropy]]), we are just looking at the second term. The optimization target would become minimizing:
$$- \log P_{G}(I)$$
- Which, without surprise, is exactly the same as maximizing log likelihood of observed data

Through a few steps of simple derivation, we would have:
$$\begin{align}
&-\log P_{G}(I)  \\
&= - \left[ \sum_{KJ} p_{G} (K,J|I) \right] \log P_{G}(I)\\  
&= - \sum_{KJ} P_{G}(K,J|I) \log P_{G}(K,J,I) +\sum_{KJ} P_{G}(K,J|I)\log P_{G}(K,J|I) \\
&=  \sum_{KJ} P_{G}(K,J|I) E_{KJI} - S_{KJI} = \langle E_{KJI} \rangle _{KJ|I} - S_{KJ|I}
\end{align}$$
- Where $S_{KJI}$ is the Gibbs Entropyof the distribution

And since the difination of **HelmHoltz Free Energy** is average energy minus entropy times temperature:
$$F = \langle E\rangle - TS\quad F_{G} = -\log P_{G}(I) = \langle E_{KJI} \rangle _{{KJ|I}}^G- S_{KJ|I}$$
Our optimization target is exactly the search for minimal Helmholtz free energy.

## Variational Free Energy

If we directly solve for partial derivatives of the parameters relative to the free energy, it is extremely hard for calculation. Therefore, variational techniques are applied:

We take the recognition explanatory distribution $P_{R}(KJ|I)$, and if we compute the [[Kullback–Leibler divergence (KL)]] of this distribution with respect to $P_{G}(KJ|I)$
$$\begin{align}
&D_{KL}[P_{R}(K,J|I),P_{G}(K,J|I)]  = \sum_{KJ} P_{R} (K,J|I) \log \frac{{P_{R}(K,J|I)}}{P_{G}(K,J|I)}\\
&= \sum_{KJ}  P_{R} (K,J|I) \log  P_{R} (K,J|I) - \sum_{KJ}  P_{R} (K,J|I) \log  P_{G} (K,J,I) + \sum_{KJ}  P_{R} (K,J|I)\log P_{G}(I) \\
&= -S_{K,J|I} ^R + \langle E_{KJI} ^G \rangle_{KJ|I} ^R - F_{G} (I)
\end{align}$$
And by rewriting the above formula, we would get a definition of free energy with respect to the recognition distributions:
$$F_{G}(I) = \langle E_{KJI} ^G\rangle^R _{KJ|I} - S_{KJ|I}^R - D_{KL}[P_{R}(K,J|I),P_{G}(K,J|I)]$$
Since the KL divergence is always positive, we would have the relationship:
$$F_{G}(I) \leq  \langle E_{KJI}\rangle^R _{KJ|I} - S_{KJ|I}^R$$
And we can represent our variational free energy as:
$$F_{G}^R (I) = F_{G}(I) +  D_{KL}[P_{R}(K,J|I),P_{G}(K,J|I)]$$


## Wake Phase

The wake phase would preform trainings on the generative SBN.
In the wake phase, we would look for the gradient of Helmholtz Free Energy:
$$F^R_{G}(I) = \sum_{KJ} P_{R}(K,J|I) E^G _{KJI} - S^R _{KJ|I}$$
Since we are taking the gradients relative to the generative weights and biases, the second term is a constant for now and can be ignored.

And to figure out the gradients relative to weights and biases, we have
$$\nabla _{G} F^R_{G} (I) = \sum_{KJ} P_{R}(K,J|I) \nabla _{G} E^G _{KJI} $$
And the same equation can be rewritten as:
$$\nabla _{G} E^G _{KJI} = -\nabla _{G}\log P(K,J,I) = -\nabla _{G} \log P(K)-\nabla _{G} \log P(J|K) - \nabla _{G} \log P(I|J)$$
- This decomposition is because of the conditional dependency properties of [[Kullback–Leibler divergence (KL)]]

**In this step, we can calculate the posterior probability that is used in the generative network, this is exactly why we are training the generative net though actually using the recognition data, we are estimating these posterior probabilities.**

And now we can write out the general form.langle
Where, if we take a look at definition of the layered conditional probabilities, we would have:
$$\log P_{G} (s_{l}|s_{l+1}) = \log \prod_{i} P_{G}(s_{l,i}|s_{l+1})^{s_{l,i}}[1-P_{G}(s_{l,i}|s_{l+1})^{s_{l,i}}]^{1-s_{l.i}}$$
In which:
$$P_{G}(s_{l,i}|s_{l+1}) = \sigma\left( \sum _{j=1} ^{n_{l+1}} w_{ij}^G s_{j} + b^G _{i} \right)$$
And we can expand the formula as:
$$\log P_{G} (s_{l}|s_{l+1}) = \sum_{i}s_{l,i}\log P(s_{l.i}|s_{l+1}) -\sum_{i}(1-s_{l.i})\log (1- P(s_{l.i}|s_{l+1}))$$
And the partial derivatives can be easily solved (exact steps check paper [[Koeln - Helmholtz Machine Explained.pdf#page17]])
$$\begin{align}
&\frac{{\partial \log P_{G} (s_{l}|s_{l+1})}}{\partial b^G _{l,i}} =s_{l,i} - P_{G}(s_{l,i}|s_{l+1})  =  s_{l,i} - \sigma\left( \sum _{j=1} ^{n_{l+1}} w_{ij}^G s_{j} ^{l+1} + b^G _{i} \right) \\ 

&\frac{{\partial \log P_{G} (s_{l}|s_{l+1})}}{\partial w^G _{l,ij}} = (s_{l,i} - P_{G}(s_{l,i}|s_{l+1})) \cdot s_{l+1,j} 
\end{align}
$$
And  this is fundamentally the algorithm, written in vector form:
$$\begin{align}
&\nabla _{W_{G}}E_{G} = -(s_l - \sigma(w^G_{l}s_{l+1}+b^G_{l})) (s_{l+1})^T \\ 
&\nabla _{b_{G}}E_{G} = -(s_l - \sigma(w^G_{l}s_{l+1}+b^G_{l}))  
\end{align}$$
- Note for the top layer with no weigths, we conly need to calculate bias
And this is our update rule.

## Sleep Phase

The sleep phase works similar to the generative training process, but the subject becamed the recognition SBN

In the sleep phase, we use the variational free energy as well:
$$F_{G}^R (I) = F_{G}(I) +  D_{KL}[P_{R}(K,J|I),P_{G}(K,J|I)]$$
However, since this original Free energy is hard to calculate the gradients, we would use a approximation of that energy, as:
$$\tilde F_{G}^R (I) = F_{G}(I) +  D_{KL}[P_{G}(K,J|I),P_{R}(K,J|I)]$$
- Note: The KL divergence on two directions is not the same (which means you can not use it as a distance)

The first term is not related to recognition netwrok, so it is ignored.
And Following the exactly same steps as above, we can rewrite the function as:
$$\nabla _{R} F_{G}^R = \nabla _{R} D_{KL}[P_{G}(K,J|I),P_{R}(K,J|I)] = - \sum_{KJ} P_{G}(K,J|I) \nabla _{R} \log P_{R}(K,J|I) $$
- Note: the $K$ and $J$ vectors came from the generative distributiuon, which is exactly the opposite as for the wake phase

And our optimization objective is again 
$$\nabla _{R} \log P_{R}(K,J|I) = \nabla _{R} \log P_{R} (J|I) + \nabla _{R} \log P_{R}(K|J)$$
Note that the direction of our calculation is exactly reversed compared to the wake phase

Now we are moving back to the general formula
Through the definition of Recognition SBN, we have:
$$P_{R}(s_{l} | s_{l-1}) = \prod _{i} P_{R}(s_{l,i})^{s_{l,i}}[1-P_{R}(s_{l,i})^{1-s_{l,i}}]$$
And follow exactly the same steps of derivition, we would have the final update rule as:
$$\begin{align}
&\nabla _{W_{R}}\log P_{R}(h|v) = -(s_l - \sigma(w^R_{l}s_{l-1}+b^R_{l})) (s_{l-1})^T \\ 
&\nabla _{b_{R}}\log P_{R}(h|v) = -(s_l - \sigma(w^R_{l}s_{l-1}+b^R_{l}))  
\end{align}$$
- Here $h$ and $v$ stands for hidden neurons given visible neurons.

In the sleep phase, the data layer is generated by the explanation layers before we actually adjust any of the weights. We are training the recognition weights based on the data generated from generative distribution.