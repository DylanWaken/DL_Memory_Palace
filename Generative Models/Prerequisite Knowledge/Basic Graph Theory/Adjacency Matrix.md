----
#BasicGraphTheory 
Required Knowledge: 
[[Graph]]

![[Adjacency Matrix.png]]

Adjacency matrix is a representation of connections within the [[Graph]] through the linear algebra methods. If we place all vertices into a vector:
$$V = [V_1, V_2, ... , V_n \in \mathcal{V}\,]^T$$
we can use a matrix of $\mathbb{R}^{n \times n}$ to display all the edges, as:
$$A = \begin{bmatrix}
\mathcal{e}_{1,1} \quad \mathcal{e}_{1,2} \quad ... \quad \mathcal{e}_{1,n}\\
\mathcal{e}_{2,1} \quad \mathcal{e}_{2,2} \quad ... \quad \mathcal{e}_{2,n}\\
...\\
...\\
\mathcal{e}_{n,1} \quad \mathcal{e}_{n,2} \quad ... \quad \mathcal{e}_{n,n}\\
\end{bmatrix}$$
Where $\mathcal{e}_{i.j}$ means an edge from vertex $V_i$ to $V_j$ 

- if there exists and edge, the value $\mathcal{e}_{i.j} = 1$ , else  $\mathcal{e}_{i.j} = 0$
- the vertex edge to itself does not exist : $\mathcal{e}_{i.i} = 0$
- In undirected graphs, $\mathcal{e}_{i,j} = \mathcal{e}_{j,i}$ , and the adjacency matrix must be symmetrical
- in weighted [[Graph]], the entry will be equal to the weight asigned to the edge

The adjacency matrix for a arbitrary undirected [[Graph]] looks like:

$$A = \begin{bmatrix}
0 \quad \mathcal{e}_{2,1} \quad ... \quad \mathcal{e}_{n,1}\\
\mathcal{e}_{2,1} \quad 0 \quad ... \quad \mathcal{e}_{n,2}\\
...\\
...\\
\mathcal{e}_{n,1} \quad \mathcal{e}_{n,2} \quad ... \quad 0\\
\end{bmatrix}$$
