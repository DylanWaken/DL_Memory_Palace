-----
#StatisticalMechanics 

The Boltzmann distribution is a distribution measuring the probability of system settle on a specific [[Microstate]] as a function of the state's [[temperature]] and energy. 

![[Boltzmann Distribution.png]]
The distribution formula is given as:
$$P_i = \frac{e^{-\beta E_i}}{Z} = \frac{e^{-E_i/k_BT}}{\sum_i ^Ne^{-E_i/k_BT}}$$
- The function is basically [[Canonical Ensemble]] but with $E_i$ of the specific microstate being a variable.
- $k_B$ is the Boltzmann constant and $T$ is the absolute [[temperature]] of the system.

Note, this equation would subject to the constraint that the macrostate energy of the system remains constant.

## Properties:

1: Boltzmann distribution is a distribution that maximizes the [[Gibbs Entropy]]:
$$H(p_1,p_2,...,p_n) = -\sum _{i=1} ^N p_i \log p_i$$
subject to the normalization constraint (probability sum to one) and the constraint that $\sum E_i p_i$ equals a particular mean energy value.

2: The ratio of probability being at any two microstates can be calculated through:
$$\frac{p_i}{p_j} = e^{(E_i-E_j)/k_BT}$$
Which is only related to the differences between the state energies. 

3: The [[Softmax Regression]] can be also derived from Boltzmann distribution, as:
$$(p_1,...,p_n)=softmax(-E_1/(k_BT),...,-E_n/k_BT)$$
## Proof

From the definition of [[Gibbs Entropy]] (or information entropy), we can derive that for $n$ random events each with probability of $p_1,p_2,...,p_n$, the gibbs entropy of the events is defined as:
$$H_n = -k_B p_i \log p_i$$
