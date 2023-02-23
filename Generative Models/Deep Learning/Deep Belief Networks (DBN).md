-----
#GenerativeModel 

The Deep Belief Network (DBN) is a special network architecture that fused together [[Restricted Boltzmann Machines (RBM)]] and [[Sigmoid Belief Networks (SBN)]]. It actually uses RBMs as scafoldings for training deep sigmoid belief network in a layer by layer manner. 

## Complementary Priors 

To better understand the idea of Complementary Priors, we can imagine the alternative Gibbs sampling process of RBM as the inference of some infinitely deep sigmoid belief nets. 

All layers shares the same weights with repeating visual-to-hidden and hidden-to-visual cycles. In theory, we would get the equilibrium distribution of the weight matrix if we consider it as a markov chain when we traverse through all infinite many layers.

![[Deep Learning/Assets/Screenshot from 2023-02-21 11-03-09.png]]

Note, the inference pass goes in the reverse direction of the generative pass. However, in our assumption both pass shares the weights in the connections.

The following distributions are all defined by $W$ after reaching the equilibrium through the top-down Gibbs sampling of the infinite SBN.
$$P(h|v)\quad P(v|h)$$
we would also have samples for the joint distribution between the visible and hidden units:
$$P(v,h)$$
Now consider the joint distributiuon between visible and hidden units $p(v,h)$, we have a likelihood function defined as $p(v|h)$. By the [[Bayes Rule]] we have the expression that:
$$P(v,h) = P(h)P(v|h)$$
Here, we define the **model above** $P(h)$ as the **Complementary Prior**

![[Screenshot from 2023-02-22 15-57-02.png]]

Consider the nodes $i,j,k$ in the above figure:

If there exists no layers beyond $h_{0}$ and both $k,j$ are positively correlated to $i$, whie $i$ is turned on, the explaning away in the original SBN would start to cause problems. 


## Contrastive Wake-Sleep Algorithm

