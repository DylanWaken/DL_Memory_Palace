----
#StatisticalMechanics 

 To have this cycle work as intended, we need to set the term $s_{N+1} = s_1$ 
For easier writing, we define $z(s_i) = s_i > 0 \quad ? \quad1 : -1$ and reset $s_i \in \{0,1\}$

The parition function is given as:
$$Z = \lambda_1^N + \lambda_2^N$$
where:
$$\lambda = e^{\beta J} \cosh(\beta H) \pm \sqrt{e^{2\beta J}\cosh^2(\beta H) -2\sinh(2\beta J)}$$
In the case without externel field $H=0$:
$$\lambda = e^{\beta J} \mp e^{-\beta J}\quad\lambda_1=2\cosh(\beta J)\quad\lambda_2=2 \sinh(\beta J)$$

## Proof

To derive the partition function, we need to rearrange the hamiltonian to the following form:
$$E = -\sum _{i=1}^N [Jz(s_i)z(s_{i+1}) + H \frac{z(s_i) +z(s_{i+1})}{2}]$$
And agian we used [[Canonical Ensemble]] partition function, and use the same tricks in [[Lattice Gases]] to write out the binary states of every atom:
$$Z = \sum _{s_1=0} ^1\sum _{s_1=0}^1...\sum _{s_n=0} ^1 \exp(\beta \sum _{i=1}^N [Jz(s_i)z(s_{i+1} )+ H \frac{z(s_i) + z(s_{i+1})}{2}])$$
And of course we can use the old tricks to expand exponential as products:
$$Z = \sum _{s_1=0} ^1\sum _{s_1=0}^1...\sum _{s_n=0} ^1 \prod _{i=1} ^N \exp(\beta  [Jz(s_i)z(s_{i+1}) + H \frac{z(s_i) +z(s_{i+1})}{2}])$$
The expanded form of this equation is complicated, since the individual terms are related to each other and we can not simply decompose the multiplication to individual summations multiplied together.

![[Ising Model Partition.png]]

- The final product is also two exponential terms

However, if we look closely to the final term in the expanded formula above, we can easily discover it is the result of trace on the result of matrix multiplication as:
$$tr(\begin{bmatrix}
e^{\beta(J+H)}\quad e^{-\beta J} \\
e^{-\beta J} \quad e^{\beta(J-H)}
\end{bmatrix}
\begin{bmatrix}
e^{\beta(J+H)}\quad e^{-\beta J} \\
e^{-\beta J} \quad e^{\beta(J-H)}
\end{bmatrix})$$
And actually, the entire formula can be written as the continuous multiplication of the identical transfer matrices. (The proof of this is extremely complicated so I will link to the proof later).
$$Z = \sum _{s_1=1}^1 \begin{bmatrix}
e^{\beta(J+H)}\quad e^{-\beta J} \\
e^{-\beta J} \quad e^{\beta(J-H)}
\end{bmatrix}^N$$

Here, we use the trick in [[Eigen Decomposition]] in solving the matrix powers, we have:
$$A^N = (V\Lambda V^{-1})^N = V\Lambda^NV^{-1}$$
And this property also indicated that the trace of any matrix to the power is the sum of its eigen values raised to the same power.
$$tr(A^N) = \sum _{i} \lambda_i^N$$
And therefore our partition function can be calculated as:
$$Z = \lambda_1^N + \lambda_2^N$$
with eigenvalues solved from the characteristic polynomial of the original transfer matrix:
$$(e^{\beta(J+H)}-\lambda)(e^{\beta(J-H)}-\lambda)-e^{-2\beta J} = 0$$
This can be rewrite as a quadratic formula:
$$(e^{2\beta J}-e^{-2\beta J}) -\lambda e^{\beta J}(e^{\beta H}+e ^{-\beta H})+\lambda^2 = 0$$
by replacing the first term with $2\sinh(2\beta J)$ and second term as $2\cosh(\beta H)$ 
and the solution is given as:
$$\lambda = e^{\beta J} \cosh(\beta H) \pm \sqrt{e^{2\beta J}\cosh^2(\beta H) -2\sinh(2\beta J)}$$
With some terms canceld we can simplify this as:
$$\lambda = e^{\beta J} \cosh(\beta H) \pm \sqrt{e^{2\beta J}\sinh^2(\beta H) + e^{-2\beta J}}$$
In the case when externel field $H = 0$, we can simplify this as:
$$\lambda = e^{\beta J} \mp e^{-\beta J}\quad\lambda_1=2\cosh(\beta J)\quad\lambda_2=2 \sinh(\beta J)$$
