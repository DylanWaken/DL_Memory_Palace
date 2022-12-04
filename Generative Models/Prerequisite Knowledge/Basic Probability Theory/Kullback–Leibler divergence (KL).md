----
#ProbabilityTheory 

For the discrete probabilistic distribution $P$ and $Q$ in the smae probabilistic space, the KL divergence of them is defined as:
$$D_{KL}(P ||Q) = \sum _{x\in \Omega} P(x) \log(\frac{P(x)}{Q(x)})$$
Which is equivalent to:
$$D_{KL}(P ||Q) = -\sum _{x\in \Omega} P(x) \log(\frac{Q(x)}{P(x)})$$
In other word, the KL divergence  it is the expectation of the logarithmic difference between the probabilities $P$ and $Q$, where the expectation is taken using the probabilities $P$.

The KL Divergence is designed to measure how different a distribution is different from another distribution.

The KL Divergence is also referred as relative [[entropy]].

For continuous random variables, the KL divergence is defined as:
$$D_{KL}(P||Q) =\int _x p(x)\log(\frac{p(x)}{q(x)})dx$$
Note: the KL divergence between distributions would always yield a positive value or zero.
Proof:

for $\forall a \geq 0$, the following relationship always holds:
$$\log(a) \leq a-1$$
We can easily prove $-D_{KL}(P||Q) \leq 0$ , which is the same as the original property:
$$\begin{align}
&-D_{KL}(P||Q) = -\int_x p(x) \log \frac{p(x)}{q(x)}dx\\
&\quad\quad\quad\quad\quad\quad = \int_x p(x) \log \frac{q(x)}{p(x)}dx\\
&\quad\quad\quad\quad\quad\quad \leq \int_x p(x) (\frac{q(x)}{p(x)}-1)dx\\
&\quad\quad\quad\quad\quad\quad = \int_xq(x)dx - \int_xp(x)
dx = 1-1=0
\end{align}$$
Which means that:
$$-D_{KL}(P||Q) \leq 0$$
