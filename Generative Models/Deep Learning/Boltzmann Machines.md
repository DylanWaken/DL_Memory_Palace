----
#GenerativeModel 

The paper introdicing this model is [[Hinton - Learning of Boltzmann Machines.pdf]]

Boltzmann Machines work like [[Ising Model]]. its component is also binary states. The hamiltonian of the model is given as:
$$E = -\sum _{i<j}  w_{ij}s_is_j - \sum _{i} \theta_i s_i \quad(Eq.0)$$
- The first term is the model between the vertices, and the second term remains to be the influence from externel field. 
- $w_{ij}$ is the connection strength between the two vertices (weight), $\theta_i$ is the bias term, and $s_i \in \{0,1\}$
- Unlike Ising model running on lattice, the boltzmann machine is a fully connected [[Graph]], and the weights are in the symmetric matrix $W$ with the diagnol being zero. 

## Unit States

The influence of switching one unit $s_i$ on ($1$) or off ($0$) can be represented through the change of total energy in the system:
$$\Delta E_i = \sum _{j\neq i}  w_{ij}s_j+ \theta_i \quad (Eq .1)$$

or can be also be represented as:
$$\Delta E_i = E_{i=1} - E_{i=0}$$
If we implement the correlation between energy difference and probability ratio from [[Boltzmann Distribution]] and replace the original equation as:
$$\Delta E_i = k_BT \log(p_{i=1} ) - k_BT\log (p_{i=0})$$
Here we can derive the function for the probability of the $i$ th unit being on or off as:
$$\begin{align}
&\frac{\Delta E_i}{k_BT} = \log(\frac{p_{i=1}}{p_{i=0}}) \\
&\frac{\Delta E_i}{k_BT} = \log(\frac{p_{i=1}}{1-p_{i=1}}) \\
&-\frac{\Delta E_i}{k_BT} = \log(\frac{1}{p_{i=1}-1})\\
&\exp(-\frac{\Delta E_i}{k_BT}) = \frac{1}{p_{i=1}-1}
\end{align}$$
And therefore we have the conclusion:
$$p_{i=1} = \frac{1}{1+ \exp(-\frac{\Delta E_i}{k_BT})}$$
Where $T$ is the temperature property of the system. We normally merge the term $k_{B}$ into $T$

Note here, when $\Delta E$ is 0, the chance for the unit on both state ($s_{i} = 1, s_{i}=0$) is equal. However, if $\Delta E < 0$ (which means the system energy is greater when the unit is turned off), the probability of turning on would be greater $p_{i=1} > 0.5$ 

And therefore, because of the [[Boltzmann Distribution]], the entire system would be tending toward minimum energy. When the network can no longer reduce its energy, it is said to be at thermal equilibrium wit175 Billion ;h maximum entropy.

## Learning algorithm for Boltzmann Machines

In real world applications, the units for Boltzmann machine is segregated into visible units $V$ and hidden units $H$.

>"during training all the visible units are clamped into specific states by the environment; when testing for completion ability, any subset of the visible units may be clamped. The hidden units, if any, are never clamped by the environment and can be used to explain underlying constraints in the ensemble of input vectors that cannot be represented by pairwise constraints among the visible units."

The learning of Boltzmann machine is aimed to configure all the weights $w_{ij}$ such that the entire network to have the perfect model of the environment. In the formal definition:

>**The network will be said to have a perfect model of the environment if it achieves exactly the same probability distribution over these $2^v$ states when it is running freely at thermal equilibrium with all units unclamped so there is no environmental input.**

- In the other word, this means that the probability of the network collapsing into a specific microstate should be the same as the probability of the microstate of the original system.

With our primary objective defined, we can defined the loss using asymmetric divergence (which measures difference between distribs, general form of [[Kullback–Leibler divergence (KL)]]):
$$G = \sum_{\alpha} P(V _{\alpha})\log \frac{P(V_{\alpha})}{P'(V _{\alpha})} \quad(Eq.2)$$
- $P(V _{\alpha})$ stands for the probability of specific microstate $\alpha$
- $P'(V_{\alpha})$ stands for the probabilty of the same microstate resulting from the network when it is at thermal equilibrium

To find an algorithm to update the weights, we are building the relation between the log probabilities for the microstate with respect to single connection weigths.

When the network is free-running, the probability of the specific microstate for visible units is given as:
$$P'(V_{\alpha})=\sum _{\beta}P'(V_{\alpha} , H_{\beta}) = \sum _{\beta} \frac{e^{-E_{\alpha \beta}/T}}{{Z}_{\lambda\mu}}\quad(Eq.3)$$
- $\alpha$ stands for the arrangement of visible unit, and $\beta$ stands for all arrangement of hidden units. $E_{\alpha \beta}$ stands for the energy for configuration $\alpha \beta$  . Here we are looking at the [[Marginal Distribution]] of the visible state
- $V_{\alpha}$ is the vector for visible unit states, and $H_{\beta}$ is the vector for hidden unit states
 - $Z_{\lambda\mu}$ is the partition function for system states for all visible hidden combinations, as:
$$Z _{\lambda\mu} = \sum _{\lambda\mu} e^{-E_{\lambda \mu}/T}$$
The energy of state $\alpha \beta$ can be calculated by Eq 0:
$$E_{\alpha \beta}  = \sum _{i < j} w_{ij} s^{(\alpha \beta)}_{i}s^{(\alpha \beta)} _{j}$$
If we take derivative of Equation 3 with respect to connection strength $w_{ij}$, we have:
$$\dfrac{\partial e^{-E_{\alpha \beta}/T}}{\partial w_{ij}} = \frac{1}{T} s^{(\alpha \beta)}_{i} s^{(\alpha \beta)} _{j} e^{-E_{\alpha \beta}/T}$$
And hence:
$$\dfrac{\partial P'(V_{\alpha})}{\partial w_{ij}} = \frac{\frac{1}{T}\sum _{\beta} s^{(\alpha \beta)}_{i} s^{(\alpha \beta)} _{j} e^{-E_{\alpha \beta}/T}}{\sum_{\alpha \beta}e^{-E_{\alpha \beta}/T}} - \frac{\sum_{\beta}e^{E_{\alpha \beta}/T} \frac{1}{T}\sum_{\lambda \mu}e^{E_{\lambda \mu}/T}s^{(\lambda \mu)}_{i}s^{(\lambda \mu)}_{j}}{(Z _{\lambda \mu})^2}$$
Which can be simplified as:
$$=\frac{1}{T}\left[ \sum_{\beta}P'(V_{\alpha} , H_{\beta}) s^{(\alpha \beta)}_{i} s^{(\alpha \beta)} _{j} - P'(V_{\alpha})\sum _{\lambda \mu} P'(V_{\lambda} , H_{\mu})s^{(\lambda \mu)} _{i } s^{(\lambda \mu)}_{j}\right]$$
Given the loss defined in equation 2, we can find the gradient of the loss wrt weights by:
$$\dfrac{\partial G}{\partial w_{ij}} = - \sum _{\alpha} \frac{{P(V_{\alpha})}}{P'(V_{\alpha})} \frac{{\partial P'(V_{\alpha})}}{\partial w_{ij}}$$
Now we have by the [[Bayes Rule]]:
$$\begin{align}
&P(V_{\alpha} , H_{\beta}) = P(H_{\beta} | V_{\alpha}) P(V_{\alpha})
 \\ &P'(V_{\alpha} , H_{\beta}) = P'(H_{\beta} | V_{\alpha}) P'(V_{\alpha})
\end{align}$$
Here one of the most important properties of Boltzmann machines came into play:

**the equilibrium distribution is independent of the path followed in reaching equilibrium**

And therefore, the probability of a hidden state given some visible state must be the same in equilibrium whether the visible units were clamped in that state or arrived there by free-running:
$$P(H_{\beta} | V_{\alpha}) = P'(H_{\beta} | V_{\alpha})$$
Hence:
$$P'(V_{\alpha} , H_{\beta}) \frac{P(V_{\alpha})}{P'(V_{\alpha})} = P(V_{\alpha} , H_{\beta}) \quad\sum _{\alpha} P(V_{\alpha})=1$$
And by this substitution, we would have the final update rule:
$$\frac{{\partial G}}{\partial w_{ij}} = \frac{{1}}{T} [p_{{ij}} - p'_{ij}]$$
where:
$$\begin{align}
&p_{ij} = \sum_{\alpha \beta} P(V_{\alpha} , H_{\beta}) s^{(\alpha \beta)}_{i} s^{(\alpha \beta)} _{j} \\
&p'_{ij} = \sum _{\lambda \mu} P'(V_{\lambda} , H_{\mu})s^{(\lambda \mu)} _{i } s^{(\lambda \mu)}_{j}
\end{align}$$
in a simpler manner, the value $p_{ij}$ is also the measure of the probability for the connection to turn on (with both units on). In the training process we would directly sample this from network.

## Training Procedure

1: Initialized the network with zero weights

2: Run the estimation for $p_{ij}$ : (Positive phase)
- Each training vector (noised) is clamped into the visible units 
- For each vector, the network is allowed to reach equilibrium multiple times
- We calculate the frequency of every connectin been turning on as samples  

3: Run the estimation for $p_{ij}'$ : (Negative phase)
- The network is completely unclamped, and is allowed to reach equilibrium
- we do the exactly same amount of runs as we did in step 2, and sample frequency

4: Update the weights $w_{ij}$ :
- The weights are increased or decreased based on the sign of $p_{ij} - p_{ij}'$ . We can apply a constant learning rate for the network to take each step the same. 

There is also a detailed description for this process here: [[Neal - Connectionist learning of belief networks.pdf#page=6]]

## Applications

- Use as a autoencoder, as we have 2 groups of visible units. (details in the paper linked)