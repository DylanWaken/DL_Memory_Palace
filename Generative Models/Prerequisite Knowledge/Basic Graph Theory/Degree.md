-----
#BasicGraphTheory 

Degree is the measure of adjacency for a vertex in the [[Graph]]. For vertex $V_i$ in [[Graph]] $\mathcal{G}$ , the degree of $V_i$ is defined as its frequency of adjacency to neighbors:

$$d(V_i) = \sum _{V_i \in \mathcal{V}} \mathbb{l}_\mathcal{e}({V_i,V_j})$$
with:
$$\mathbb{l}_\mathcal{e}(V_i,V_j) =  \begin{cases} 1 \quad\text{  if } \, (V_i,V_j) \in \mathcal{E} \\ 0 \quad \text{  if } \, (V_i,V_j) \notin \mathcal{E} \end{cases}$$
The same operation can be also done from the [[Adjacency Matrix]] of the [[Graph]] by:

$$d(V_i) = \sum _{j=1}^N A(i.j)$$
since the row of [[Adjacency Matrix]] contains all the edges that connects to the given vertex. The theoritical maximum degree for all nodes is the twice of the edge count for the [[Graph]]

$$\sum _{V_i \in \mathcal{V}} d(v_i) = 2 \cdot |\mathcal{E}|$$
