-----
#BasicMachineLearning 
> ***Problem Type***: [[Embedding]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$  
> SOLVE: Regression parameters: $W \in \mathbb{R}^{N \times N}$ satisfying $\min _W J(W)= \sum _{i=1} ^N ||x^{(i)} - \sum _{j \in N(i)} w_{ji} x^{(j)}||^2$
> Embedding vectors $Y \in  \mathbb{R}^{k\times N}$ sich that:
> $\min_Y J(Y) = \sum _{i=1} ^N (y^{(i)} - \sum _{j\in N(i)} w _{ji}y^{(j)})$
> ***Closed-form Solution***: 
> 1. Use KNN to construct the nearest neighbor graph for original samples
> 2. Calculate the meighbor variance $C_i = (x^{(i)}-x^{(j)})^T(x^{(k)} - x^{(i)})$ pre sample
> 3. Calculate the regression parameter: $w_i = \frac{C_i \mathbb{1}_N}{\mathbb{1}_N C_i\mathbb{1}_N}$
> 4. Take the $k$ eigenvectors of minimal eigenvalues from $(W-I)^T(W-I)$, and combine these into the new data matrix

Locally Linear Embedding is the more general form of [[Locality Preserving Projection (LPP)]]. This is a form of non-linear dimension reduction algorithm that put more attention on preserving local attributes on the data samples. (minimizing the distance between nearby sample points)

The key assertion in LLE is that every sample in the dataset can be represented as the linear combination of adjacent samples.

If we have sample $X \in \mathbb{R}^{n \times N}$, we can contruct an nearest neighbor graph with [[K-Nearest-Neighbors Graph (KNNG)]] . Assume we have parameter matrix $[w_1,w_2,...,w_N] = W \in \mathbb{R}^{N\times N}$ . We use $w_i$ to represent the $i$ th column of the matrix. if $x^{(i)}$ and $x^{(j)}$ are not adjacent to each other, then $W_{ij} = 0$ 

 we can approximate each vertex as the linear combination of adjacent vertices, as:
$$x^{(i)} = \sum _{j=1} ^N w_{ji}x^{(j)} = Xw_i$$
We have the constraint:
$$\sum _{j=1} ^N w_{ji} = 1$$
- The constraint is for easier computation in construction of the optimization problem

Here, we can use the optimizer of [[Least Mean Squares (LMS)]] to compute the optimal parameters:
$$\min _W J(W)= \sum _{i=1} ^N ||x^{(i)} - \sum _{j \in N(i)} w_{ji} x^{(j)}||^2$$
- $N(i)$ is the set of all subscripts that are adjacent to the vertex $x^{(i)}$

We begin by consider the loss for the individual data sample $i$. Here, because of our ealier constraint in summing each row of weights to $1$, we can derive as follows:
$$\begin{align}
& J_i(W) = ||x^{(i)} - \sum _{j =1}^N w_{ji} x^{(j)}||^2 \\
& \quad\quad\quad = ||\sum_{j=1} ^N w_{ji} (x^{(i)} - x^{(j)}) ||^2 \\
& \quad\quad\quad = \sum _{j=1} ^N \sum_{k=1} ^Nw_{ji} w_{ki}(x^{(i)}-x^{(j)}) ^T(x^{(k)} - x^{(i)}) \\
& \quad\quad\quad = \sum _{j=1} ^N \sum _{k=1} ^N w_{ji} w_{ki} c _{jk} \\
& \quad\quad\quad = w_i^TC_iw_i
\end{align} 
$$
- where $C_i$ is the difference matrix were $c_{jk} =(x^{(i)}-x^{(j)}) ^T(x^{(k)} - x^{(i)})$

Assume $\mathbb{1}_N$ stands for the $N$ dimensional vector with all element of $1$ , our constraint is:
$$\mathbb{1}_N^Tw_i = 1$$
We have the optimization problem as:
$$\begin{align}
& \min_{w_i} J(w_i) = w_i^TC_iw_i \\
& \,s.t. \quad \mathbb{1}_N^Tw_i = 1
\end{align}$$
Applying [[Lagrange Multiplier]], we have:
$$\mathcal{L}(w_i, \lambda) = w_i^TC_iw_i + \lambda(\mathbb{1}^T_Nw_i-1)$$
And by solving thw zero derivative, we have:
$$\dfrac{\partial \mathcal{L}}{\partial w_i} = 2C_iw_i + \lambda \mathbb{1}_N$$
and we solve for $w_i$:
$$w_i = - \frac{\lambda}{2} C_i\mathbb{1}_N$$
And we normalize with the constraints to get rid of $\lambda$:
$$w_i = \frac{C_i \mathbb{1}_N}{\mathbb{1}_N C_i\mathbb{1}_N}$$
And we have the downscaled sample being $y^{(i)}$, and we have the same optimization target of LMS. But this time since $W$ is fixed, we run our optimization on the new variable $Y$:
$$\min_Y J(Y) = \sum _{i=1} ^N (y^{(i)} - \sum _{j\in N(i)} w _{ji}y^{(j)})$$
Because $Y$ can be scaled without influence the output, we add the constraint to $Y$:
$$\frac{1}{N} YY^T = 1$$
And we take advantage of that constraint again, rewrite the objective function as:
$$\begin{align}
&J(W) = \sum _{i=1} ^N ||y^{(i)} - \sum _{j\in N(i)} w _{ji}y^{(j)}||^2\\
& \quad\quad\quad = \sum _{i=1} ^N ||y^{(i)} - Yw_i||^2 \\
& \quad\quad\quad = \sum _{i=1}^N (y^{(i)} - Yw_i)^T(y^{(i)} - Yw_i) \\
& \quad\quad\quad = tr(Y^TY) + tr(W^TY^TYW) - 2(Y^TYW)  \\
& \quad\quad\quad = tr((W-I)^TY^TY(W-I))
& \end{align}$$
And by this conclusion we have the optimization target being:
$$\begin{align}
&\min_Y J(Y) = tr((W-I)^TY^TY(W-I)) \\
&s.t. \quad \frac{1}{N} YY^T = 1
\end{align}$$
By applying Lagrange Multipliers, we have:
$$\mathcal{L}(Y,\lambda) = tr((W-I)^TY^TY(W-I)) + \lambda(YY^T- NI)$$
Solve for zero derivative:
$$\dfrac{\partial \mathcal{L}}{\partial Y} = 2Y(W-I)(W-I)^T + 2\lambda Y = 0$$
And by simplify we have the solution:
$$Y(W-I)(W-I)^T = \lambda Y$$
We can do a [[Eigen Decomposition]] on matrix $(W-I)(W-I)^T$. Where the optimal $Y$ will be the $k$ (k is the target dimension) minimum eigenvalues' corresponding eigenvectors. 