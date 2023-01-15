-----
#StatisticalMechanics 

In the [[Entropy]] section, we defined the [[Gibbs Entropy]] as:
$$S_G = -k_B \sum P_i \log P_i$$
Where we can also write it in terms of information:
$$S = -I(P)$$
From the [[Generalised Partition Function]] section, we have the definition:
$$ P_j = \frac{\exp( - \sum _k \lambda_kB^{(k)} _j)}{e^{\Phi}}$$
Where probability $P$ of every microstate can be represented by the potential parameter values scaled by lagrange multipliers devided by the partition function.

If we plug this definition into the Gibbs Entropy, we have:
$$\dfrac{S}{k_B} = \Phi + \sum_k \lambda_k \langle B^{(k)} \rangle$$
And for the change of entropy relative to constant constrainted variables, we have:
$$\frac{dS}{k_B} = - \sum _k\lambda_k 
\langle \dfrac{\partial B^{(k)}}{\partial\alpha^{(j)}} \rangle d\alpha^{(j)}  + \sum_k \lambda_k d\langle B^{(k)} \rangle$$

## Entropy wrt constant variables

In the original [[Microstate]] section, there are some variables $\alpha$ that we wished to be maintained constant, and therefore we introduced the constant constraint as:
$$\delta(\alpha^{(j)} _i - \alpha^{(j)}) = 0$$
- This constraint will assure the constant variables to not change among microstates.

Here we can calculate the partial derivative of the entropy $S$ relative to $\alpha^{(j)}$ :
$$\frac{1}{k_B} \dfrac{\partial S}{\partial\alpha^{(j)}} = \dfrac{\partial \Phi}{\partial \alpha^{(j)}} + \sum_k \dfrac{\partial\lambda_k}{\partial \alpha^{(j)}} \langle B^{(k)} \rangle + \sum_k \lambda_k \dfrac{\partial\langle B^{(k)} \rangle}{\partial \alpha^{(j)}}$$
And by multiply the change of alpha on both side of the equation, we get the relationship between the change of quantities:
$$\frac{dS}{k_B} = d\Phi + \sum_k  \langle B^{(k)} \rangle d\lambda_k + \sum_k \lambda_k d\langle B^{(k)} \rangle \quad(1.0)$$
Since $\Phi$ is the logrithm of the generalized partition function, we can derive the first term as:
$$\begin{align}&\dfrac{\partial \Phi}{\partial \alpha^{(j)}} = \dfrac{\partial}{\partial \alpha^{(j)}}[\log(\sum_i \exp( - \sum _k \lambda_kB^{(k)} _i))]\\
&\quad\quad\quad= -\frac{1}{e^{\Phi}}\sum_i\sum_k \dfrac{\partial \lambda_kB^{(k)} _i}{\partial \alpha^{(j)}}\exp( - \sum _k \lambda_kB^{(k)} _i)
\end{align}$$
By rearranging the sum operations and use the product rule, we can get the following function:
$$-\sum_k\dfrac{\partial \lambda_k}{\partial \alpha^{(j)}}\sum_i B_i^{(k)} \frac{\exp( - \sum _k \lambda_kB^{(k)} _i)}{e^{\Phi}}  -\sum_k\lambda_k\sum_i \dfrac{\partial B_i^{(k)}}{\partial\alpha^{(j)}} \frac{\exp( - \sum _k \lambda_kB^{(k)} _i)}{e^{\Phi}}$$
Or in a simpler form:
$$-\sum_k\dfrac{\partial \lambda_k}{\partial \alpha^{(j)}}\sum_i B_i^{(k)} P_i  -\sum_k\lambda_k\sum_i \dfrac{\partial B_i^{(k)}}{\partial\alpha^{(j)}} P_i$$
And by bring this back into the original entropy delta function (1.0), we have:
$$d\Phi = -\sum_k \langle B^{(k)} \rangle d\lambda_k - \sum _k\lambda_k 
\langle \dfrac{\partial B^{(k)}}{\partial\alpha^{(j)}} \rangle d\alpha^{(j)} $$
And since the first term will cancel out the second term in the original function (1.0):
$$\frac{dS}{k_B} = - \sum _k\lambda_k 
\langle \dfrac{\partial B^{(k)}}{\partial\alpha^{(j)}} \rangle d\alpha^{(j)}  + \sum_k \lambda_k d\langle B^{(k)} \rangle \quad(1.1)$$
And this is the amount of the change in entropy relative to the constant variables. 
