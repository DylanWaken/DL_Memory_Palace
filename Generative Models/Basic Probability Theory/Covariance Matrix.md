----
#ProbabilityTheory
required knowledge: [[Covariance]]

Instead of representing multiple random wariables as a single multi-dimensional scalar function, we can also store these as a Ramdom Vector:

$$X = [X_1, X_2,...,X_n]^T$$

In this form facter, given $g(\vec{x})$ as a vector funcion $g : \mathbb{R}^n \rightarrow \mathbb{R}^n$ , the [[expectation]] is also an vector function that map every entry of the random vector to its [[expectation]] values:

$$g(x) = \begin{bmatrix}
g_1(x_1) \\
g_2(x_2) \\
. \\
. \\
g_n(x_n)

\end{bmatrix} \longrightarrow 
E[g(x)] = \begin{bmatrix}
E[g_1(x_1)] \\
E[g_2(x_2)] \\
. \\
. \\
E[g_n(x_n)]
\end{bmatrix}$$

WIth all random variables and expectations stored as matrix, we can calculate the [[covariance]] between all pairs of random variables, and store these as the [[covariance]] matrix or $\Sigma$

$$\Sigma = \begin{bmatrix}
Cov[X_1,X_1]\quad Cov[X_1,X_2] \quad ... \quad Cov[X_1,X_n]\\
Cov[X_2,X_1]\quad Cov[X_2,X_2] \quad ... \quad Cov[X_2,X_n]\\
... \\
... \\
Cov[X_n,X_1]\quad Cov[X_n,X_2] \quad ... \quad Cov[X_n,X_n]
\end{bmatrix}$$

Because the calculation of [[covariance]] is $E[(X-E[X])(Y-E[Y])]$

$Cov[X_i,X_j]=Cov[X_j,X_i]$
$Cov[X_i,X_i] = Var[X_i]$

This property makes the [[covariance]] matrix a symmetrical matrix with variances on the diagnol:

$$\Sigma = \begin{bmatrix}
Var[X_1]\quad Cov[X_2,X_1] \quad ... \quad Cov[X_n,X_1]\\
Cov[X_2,X_1]\quad Var[X_2] \quad ... \quad Cov[X_n,X_2]\\
... \\
... \\
Cov[X_n,X_1]\quad Cov[X_n,X_2] \quad ... \quad Var[X_n]
\end{bmatrix}$$

The calculation for the [[covariance]] matrix can be expressed in the form of vector outer product:

$$\Sigma  = E[XX^T] - E[XE[X]^T$$
$$\Sigma = E[(X-E[X])(X-E[X])^T]$$

