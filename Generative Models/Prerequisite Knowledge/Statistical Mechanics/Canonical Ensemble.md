----
#StatisticalMechanics 

Canonical Ensemble is a special case in statistical mechanics. It place the system into a "heat bath" that allows the system to reach different energy levels and thus occupy [[Microstate]] with different energy levels. 

If all the variables else than energy are fixed, we can get the probability of every state by computing:
$$ P_j = \frac{\exp(-\beta H(x_j,p_j))}{Z_C}\quad \beta=\frac{1}{k_BT}$$
- $H$ is the hamiltonian for computing energy.
- $Z_C$ is the Canonical partition function here

And we can also simplify it as:
$$P = e^{(F-E)/k_BT}$$
or
$$P = \frac{1}{Z_C}e^{-E/k_BT}\quad Z_C = e^{F/k_BT} = \sum_j \exp(-\beta E)$$
- $j$ is all the states the systme can be in
- $F$ is the helmholtz free energy term: $F = E -TS = -k_BT\log Z_C$

## Proof

In the original [[Generalised Partition Function]] , we have the conclusion that:
$$ P_j = \frac{\exp( - \sum _k \lambda_kB^{(k)} _j)}{Z}$$
Where we denoted $B^{(k)}_j$ being a thermodynamic variable taking value on the value $x_j$ produced by random variable $X$.  

Here, we have the energy calculated from the **Hamiltonian** as :
$$\langle E \rangle = H(x_j,p_j)$$
And we can simplify the above function as:
$$P_j = \frac{\exp(-\beta H(x_j,p_j))}{Z}$$
With the partition function itself also rewrite as:
$$Z = \sum_j \\exp(-\beta H(x_j,p_j))$$
Here if we bring back our [[Change of Entropy]] formula, we have:
$$\frac{dS}{k_B} = - \sum _k\lambda_k 
\langle \dfrac{\partial B^{(k)}}{\partial\alpha^{(j)}} \rangle  + \sum_k \lambda_k d\langle B^{(k)} \rangle$$
Note: since our $\alpha$ is marked for only constant variables

As an example, we use the ideal gas as our object and use volume as the constant variable, we can swap in the terms for volume and energy as:
$$\frac{dS}{k_B} = - \beta 
\langle \dfrac{\partial H}{\partial V} \rangle dV  + \beta  d\langle H \rangle$$
Here we introduce [[The First Law of Thermodynamics]] :
$$dE = TdS -PdV$$
And we can easiy derive:
$$dS = \frac{1}{T}dE +\frac{1}{T}PdV$$
Since we already have the definition for $\frac{dS}{k_B}$ , we can reach the conclusion:
$$\beta = \frac{1}{k_BT}$$
This is the so called inverse [[temperature]] constant in [[Generalised Partition Function]]

## Helmholtz Free Energy

If we replace the variables in the entropy definition function:
$$\dfrac{S}{k_B} = \Phi + \sum_k \lambda_k \langle B^{(k)} \rangle$$
with the energy terms, we have:
$$\dfrac{S}{k_B} = \Phi +   \frac{ E}{k_BT}$$
also written as:
$$k_BT\Phi = -(E-TS)$$
- The right side is the definition of Helmholtz free energy $F$
$$F = -k_BT\log Z_C = E-TS$$
