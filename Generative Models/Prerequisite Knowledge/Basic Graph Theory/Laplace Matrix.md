----
#BasicGraphTheory 

Laplace matrix is a special representation of [[Graph]] in matrices.

## Discrete Laplace Operator

The discrete laplace operator is the [[Laplace Operator]] defined on a graph or discrete grid, instead of a continuous function.

For a [[Graph]] $\mathcal{G = \{V,E\}}$ , Let $\phi : V \rightarrow R$ be a function of the vertices taking values in a ring. Under such assumption, the Laplacian is defined as:
$$(\Delta\phi)(v) = \sum _{w:d(w,v)=1} [\phi(v) - \phi(w)]$$
- $d(w,v)$ is the distance between vertices $w,v$. For now, $w$ is the nearest neighbors of $v$ 

If the graph have the edges weighted, we have the weighting function $\gamma : V \rightarrow R$ , then the discrete laplacian is defined as:
$$(\Delta\phi)(v) = \sum _{w:d(w,v)=1} \gamma_{wv}[\phi(v) - \phi(w)]$$
- where $\gamma_{wv}$ is the weight on the edge $e\{w,v\} \in \mathcal{E}$  

## Laplace Matrix

For unweighted undirected graphs, the laplace matrix is defined as:
$$L_{i,j} := \begin{cases}deg(v_i)\quad \text{if}\quad i = j \\
-1 \quad \text{if} \quad i \neq j \,\,\text{and}\,\,v_i \,\,\text{is adjacet to } v_j
\\
0 \quad \text{otherwise}
\end{cases}$$
In the other form, it is:
$$L = D-A$$
- where $D$ is the [[Definite Matrix]] and $A$ is the [[Adjacency Matrix]]

Laplace Matrix is the linear transformation equivalent to the discrete laplace operation on grpahs, as given by the following process:

The original discrete laplacian is:
$$(\Delta\phi)(v) = \sum _{j \in N_i} [\phi(v_i) - \phi(v_j)]$$
And by further processing, we have:
$$(\Delta\phi)(v_i) = \sum _{j \in N_i} \phi(v_i) -  \sum _{j \in N_i} \phi(v_j) = d_i \phi(v_i) - \sum _{j \in N_i} \phi(v_j)$$
- where $d_i$ is the degree of $v_i$

Here we havd adjacency matrix as $A_{ij} = 1$ if $v_i$ and $v_j$ is connected with an edge, else 0. 
We define $A_{i:}$ as $[A_{i1}, A_{i2}, ... , A_{in}]$
we have the funciton as:
$$d_i \phi(v_i) - A_{i:} \phi(v_j)$$

And by incorporate this conclusion, we have the discrete laplace operation for every vertex as:
$$\Delta \phi(\mathcal{V}) = \begin{bmatrix}
\Delta \phi(\mathcal{v_1})\\
\Delta \phi(\mathcal{v_2})\\
...\\
\Delta \phi(\mathcal{v_n})\\
\end{bmatrix} = \begin{bmatrix}
d_1 \phi(v_1) - A_{1:} \phi(v_j)\\
d_2 \phi(v_2) - A_{2:} \phi(v_j)\\
...\\
d_n \phi(v_n) - A_{n:} \phi(v_j)\\
\end{bmatrix} =
diag(d_i) \phi(\mathcal{V} ) - A\phi(\mathcal{V})
$$
And with the simplification, we have:
$$\Delta \phi(\mathcal{V}) = (D-A) \phi(\mathcal{V}) = L\phi(\mathcal{V})$$
- where $L$ is the laplace matrix
