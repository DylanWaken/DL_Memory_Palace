-----
#ProbabilityTheory 

Bayesian Network is a directed and non-cyclistic [[Graph]]. 

Bayesian Networks are also refered as belief networks.

The directed edges encodes the conditional dependence relationships. 

For any two random varianbles $X_1$ and $X_2$ in a Bayesian network that is connected by an edge from $X_1$ to $X_2$, the joint distribution is represented as: 
$$P(X_1,X_2) = P(X_1)P(X_2|X_1)$$
## Cases

1: Branching:

![[Screenshot from 2022-12-08 12-09-28.png]]

In the case of a branching network, the joint distribution of the network is given as:
$$P(Y,X_1,...,X_n) = P(Y) \prod _{i=1} ^n P(X_n|Y)$$

2: Converging:

![[Screenshot from 2022-12-08 12-09-38.png]]

In this case of a branching network, the joint distribution of the nework is:
$$P(Y,X_1,...,X_n) = P(Y|X_1,...,X_n) \prod _{i=1} ^n P(X_n)$$
This is similar to the approach of [[Logistic Regression]] (with log likelihood)

## Properties

- 1: Each variable is conditionally independent of its **non-descendent** given is parents 
- 2: Each variable is conditionally independent of any other variable given its [[Markov Random Fields (MRF)]] transformed neighbors (**Markov blanket**).
 