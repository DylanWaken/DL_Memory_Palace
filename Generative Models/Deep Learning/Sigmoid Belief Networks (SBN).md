----
#GenerativeModel 

Original paper is [[Neal - Connectionist learning of belief networks.pdf]]

## Belief Networks

Belief network is also named as [[Bayesian Networks]], which models the conditional probability relationship between the nodes. 

Here our discussion of belief networks is focused only on two-valued nodes (like 0,1)

For the belief network with state $s$, $s_i$ stands for the state of the ith node. Since belief networks models conditional dependency between nodes, the probability of the entire network being at a specific state $s$ is the product of the probability of the state for all nodes given their preceding nodes states (parents), as:
$$P(S_{\alpha}) = \prod_{i}P(s_{i} ^{(\alpha)}| s_{j} ^{(\alpha)}:j<i)$$
This structure is refered to as **forward conditional probabilities**. 

Through a Gibbs sampling process, the network would be collapsing into equilibrium. The update process follows a specific proportionality:
$$\begin{align}
&P(s_{i}=x|s_{j} ^{(\alpha)} : i \neq j)  \\
& \propto P(s_{i}=x| s_{j} ^{(\alpha)} : j <i) \cdot \prod _{j>i} P(s_{j} ^{(\alpha)} | s_{i}=x,s_{k} ^{(\alpha)} : k < j)
\end{align}$$
## Sigmoid Belief Networks

![[Screenshot from 2023-01-09 19-22-06.png]]

Sigmoid belief network is a variant of traditional belief network, in which it resembles the structure of [[Boltzmann Machines]] considering its connections. The SBN model introduced weights to the directed edges of the network, as $w_{ij}$ represents the weight from i to j.

The lowest layer of the sigmoid belief network is used as visible nodes, or $X$  (Note: for other cases this is also represented as $V$)

In the sigmoid belief network, we define the posterior probability as:
$$P(s_{i}=1|s_{j} : j < i) = \frac{{1}}{1+\exp\left( -\sum _{j<i}w_{ij}s_{j} +b_{j}\right) }$$
Assuming the l th layer nodes are marked as $H_{l}$, the i th node marked as $H_{l,i}$, the posterior probability of a specific node can be represented as:
$$P(H_{l,i}=1|H;\theta) = \sigma(w^T_{l+1}H_{l+1} + b_{l+1})$$
- Here $\theta$ is the zipped parameter terms where $\theta = \{w,b\}$ 

If we incorporate the 0 case as well, we can combine evergything to form the Gibbs sampling update rule:
$$P(H_{l,i}|H;\theta) = \sigma((2H_{l,i}-1)(w^T_{l+1}H_{l+1}+b_{l+1}))$$
Note: the top layer of the network is not controlled by any other nodes.

And the [[Joint Distribution]] of the entire network, or the probability of the specific case, can be calculated by:
$$P(H,X;\theta) = \prod_{l=0} ^L \prod _{i=1} ^{n_{l}} P(H_{l,i}|H;\theta)$$
## SBN Learning Algorithm

The learning objective of the SBN network is to maximize the log [[Likelihood]] of the network with respect to the observed real-world data, since we are still looking to reconstruct the distribution of the real world data.

We take the log likelihood as our optimization objective and have:
$$\max _{\theta} \log P(X;\theta) = \log \sum _{H} P(H,X;\theta)$$
Because directly solving for a closed form solution is infeasible, we would derive an iterative gradient ascent process by find the derivatives:
$$\begin{align}
&\frac{\partial}{\partial \theta} \log P(X;\theta)  \\
&=\frac{{\frac{\partial}{\partial \theta}  P(X;\theta)}}{P(X;\theta)} \\
&=\frac{\frac{\partial}{\partial \theta}\sum_{H}P(X,H;\theta)}{P(X;\theta)} \\
&=\sum_{H} \frac{\frac{\partial}{\partial \theta}P(X,H;\theta)}{P(X;\theta)} \\
&=\sum_{H} P(H|X;\theta) \frac{\frac{\partial}{\partial \theta}P(X,H;\theta)}{P(X,H;\theta)}
\end{align}$$
And with respect to parameters, we have:
$$\begin{align}
&\frac{\partial}{\partial w_{l+1,i,j}}\log P(X;\theta)  \\
&= \sum _{H} P(H|X;\theta)\frac{\frac{\partial}{\partial w_{l+1,i,j}}P(X,H;\theta)}{P(X,H;\theta)} \\
&=\sum_{H}P(H|X;\theta)\frac{\frac{\partial}{\partial w_{l+1,i,j}}\prod^L_{l'=0}\prod^{n_{l'}}_{i'=1}P(H_{l',i'}|H;\theta)}{\prod^L_{l'=0}\prod^{n_{l'}}_{i'=1}P(H_{l',i'}|H;\theta)} \\
&=\sum_{H} P(H|X;\theta) \frac{\frac{\partial}{\partial w_{l+1,i,j}}P(H_{l,i}|H;\theta)}{P(H_{l,i}|H;\theta)}
\end{align}
$$
If we say that:
$$h_{l,i}  = ((2H_{l,i}-1)(w^T_{l+1}H_{l+1}+b_{l+1}))$$
We would have the original equation above as
$$\begin{align}
&=\sum_{H} P(H|X;\theta) \frac{\frac{\partial}{\partial w_{l+1,i,j}}P(H_{l,i}|H;\theta)}{P(H_{l,i}|H;\theta)} \\
&=\sum_{H} P(H|X;\theta) \frac{\frac{\partial}{\partial w_{l+1,i,j}}\sigma(h_{l.i})}{\sigma(h_{l,i})} \\
&= \sum_{H }P(H|X;\theta) \frac{\sigma(h_{l,i})\sigma(-s_{l,i})(2H_{l,i}-1)H_{l+1,j}}{\sigma(h_{l,i})} \\
&=\sum_{H} P(H|X;\theta) \sigma(-h_{l,i})(2H_{l,i}-1)H_{l+1,j}
\end{align}$$
Which is indeed our gradient. 
However, the parameter gradient in this form dependes on the conditional distribution if hidden units. Since the visibal layer and the hidden layers are connected in conditional dependency, they are not independent and it is infeasible to directly solve for. 

Therefore, the direct likelihood maximization is rarely used in sigmoid belief networks.

Therefore, we usually take another approach, or the [[Wake-Sleep Algorithm]]


