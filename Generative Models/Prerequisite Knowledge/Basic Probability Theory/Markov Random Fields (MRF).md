-----
#StatisticalMechanics 

Markov Random Field is a class of of Undirected Graphical Models.

![[MRF2.png]]

The joint distribution of all random variables is given as the cumulative product of every maximal [[Clique]] potential functions devided by a [[Generalised Partition Function]].

Given a set of random variables $X : \{X_1,...,X_n\}$ , let $P(X=x)$ be a specific configuration of $x$ (value taken from the joint distribution) among set $X$. 

The same function above can be rewritten as:
$$P(X=x) = \frac{1}{Z} \prod _{c\in cl(G)}\phi_c(x_c)$$
- $Z$ is the partition function
- $\phi_c$ is the clique potential function for the [[Maximal Clique]] $c$
- $x_c$ is every node within the clique

Note: the potential function of actually referres to $\log(\phi_c)$ since this would be align with the statistical mechanic definition in [[Statistical Potential]]

## Bayes Net Transformation

Note: if you are considereing to convert a [[Bayesian Networks]] to MRF, then for each node, its neighbors would include its parents, children, and **children's parents**. as shown below:

![[Screenshot from 2022-12-08 12-27-55.png]]
![[Screenshot from 2022-12-08 12-27-55.png]]
![[Screenshot from 2022-12-08 12-29-40.png]]
![[Screenshot from 2022-12-08 12-35-11.png]]

- Note: in the final case, the **moralizing** process is done as if any node have several co-parents, these co-parents must be connected to each other in the converted MRF.

## Properties

- Any two non-adjacent variables are [[Conditional Independence]] to each others given all the  other variables (Pairwise Markov Property).
- Any variable is conditionally adjacent to all the variables in the same graph expect its neighbors (Local Markov Property)

