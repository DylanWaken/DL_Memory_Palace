-----
#BasicGraphTheory 

KNN is a technique in constructing adjacency graph given a data set within the same [[Normed Vector Space]]. The process in constructing such graph is as follows:
$$d_{ij} = ||x^{(i)} - x^{(j)}||$$
In a new graph $\mathcal{G} = \{\mathcal{V},\mathcal{E}\}$,  we give each data sample a vertex reprersentation.

Then we construct a edge $e = \{v_i,v_j\}$ if and only if $d_{ij}$ is among the $k$ shourtest distances (norms) between $v_i$ and any other nodes $v_j \in \mathcal{V}/v_i$

The graph from KNN is directed