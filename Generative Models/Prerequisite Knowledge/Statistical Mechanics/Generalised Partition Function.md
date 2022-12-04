-----
#StatisticalMechanics

In a thermodynamic system with finite [[Microstate]]s, we can express every macrostate variable as the expectation of all its microstates, as:
$$B^{(k)} = \sum_i B^{(k)} _iP_i$$
- Where $B^{(k)}$  can be viewed as the k-th thermodynamic variable. 

Because of the [[Principle of Equal and Priori Probabilities]], find the equalibrium is the same as solving the following optimization problem is constraints:
$$\begin{align}
&\min_P S_G = k_B\sum_iP_i\log P_i \\
&s.t. \quad B^{(k)} = \sum_i B^{(k)} _iP_i,\quad 1=\sum_iP_i
\end{align}$$
- The first constraint is the expecation of microstate variables equal to the macrostate variables, and the second constraint is the property of [[Probability Mass]]

