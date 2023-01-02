-----
#StatisticalMechanics

The generalized paritition function defined for a distribution is given as:
$$Z(\beta) = \sum _{x_i} \exp (-\sum_k\beta_kH^{(k)}(x_i)) $$
- $\beta$ is the vector of Lagrange Multiplier / inverse temperature (thermodynamics) in [[Canonical Ensemble]]
- $H^{(k)}$ is the function applied to $x_i$ (specific values taken by random variable $X$)
- The sum over $x_i$ stands for each possible value can be taken by variable $X$, or all the possible microstates the system can be in.

## Proof

In a thermodynamic system with finite [[Microstate]]s, we can express every macrostate variable as the expectation of all its microstates, as:
$$\langle B^{(k)} \rangle = \sum_i B^{(k)} _iP_i$$
- Where $B^{(k)} _i$  can be viewed as the k-th thermodynamic variable picking value from a ramdom variable $B^{(k)}(x_i)$. 

Because of the [[Principle of Equal a Priori Probabilities]], find the equalibrium is the same as solving the following optimization problem is constraints:
$$\begin{align}
&\min_P S_G = k_B\sum_iP_i\log P_i \\
&s.t. \quad \langle B^{(k)} \rangle = \sum_i B^{(k)} _iP_i,\quad 1=\sum_iP_i
\end{align}$$
- The first constraint is the expecation of microstate variables equal to the macrostate variables, and the second constraint is the property of [[Probability Mass]]

Here we use [[Lagrange Multiplier]] to solve the problem:
$$\begin{align}
&L(\{P_i\}, \lambda_0,\{\lambda_k\}) = -k_B\sum_i P_i \log P_i-k_B\lambda_0(\sum_iP_i-1)- \\
&\quad\quad\quad\quad\quad\quad k_B \sum_k\lambda_k(\sum_iB^{(k)}_iP_i-B^{(k)})
\end{align}$$
- Here we maximize the negative information instead of minimize positive information
- we multiply all multipliers by $k_B$ for easier computation

Here we solve:
$$\nabla L(\{P_i\}, \lambda_0,\{\lambda_k\}) = 0$$
To expand, we have the form:
$$\begin{align}
&\dfrac{\partial L}{\partial P_j} = -k_B\log P_j - k_B -k_B\lambda_0 -k_B \sum_k \lambda_kB^{(k)}_j = 0 \\
& \log(P_j) = - (\lambda_0+1) - \sum _k \lambda_kB^{(k)} _j\\
& P_j = \frac{\exp( - \sum _k \lambda_kB^{(k)} _j)}{\exp(\lambda_0+1)} \quad(1.1)
\end{align}$$
We define $\Phi = \lambda_0+1$

Since we have the probability mass constraint, we can derive the following:
$$\sum_j P_j = 1 = \sum_j \frac{\exp( - \sum _k \lambda_kB^{(k)} _j)}{\exp(\Phi)} = \frac{1}{e^{\Phi}} \sum_j \exp( - \sum _k \lambda_kB^{(k)} _j)$$
And by then we have the constant term derived as:
$$Z = e^\Phi = \sum_j \exp( - \sum _k \lambda_kB^{(k)} _j)$$
Therefore, $Z$ or $e^{\Phi}$ is what we defined as the general partition function. 
Here, we have noted in the conclusion (1.1) $Z$ being the denominator of the probability of the system being at a specific configuration. $Z$ is indeed the term that makes the entire thing subject to the probability mass constraints (sum to 1). 