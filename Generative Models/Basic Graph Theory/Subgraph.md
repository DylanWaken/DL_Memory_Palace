----
#BasicGraphTheory 

A subgraph $\mathcal{G}'\{ \mathcal{V}', \mathcal{E}'\}$   of a given [[graph]] $\mathcal{G}\{ \mathcal{V}, \mathcal{E}\}$ is a [[graph]] formed with a subset of nodes $\mathcal{V' \subset V}$ and a subset of edges $\mathcal{E' \subset E}$. The subset of vertices must contain all of the nodes involved in the subset of edges.

### Connectivity

A subgraph $\mathcal{G}'\{ \mathcal{V}', \mathcal{E}'\}$ is said to be the connected component of a given [[graph]] $\mathcal{G}\{ \mathcal{V}, \mathcal{E}\}$ is there is at least one [[path]] between any pair of nodes in the subgraph, and the nodes in $\mathcal{V}'$ are not adjacent to any nodes in $\mathcal{V}/\mathcal{V}'$ 

![[ConnectedCompSample.png]]

//sample: the set of red nodes and edges is the connnected component of the [[graph]]

A [[graph]] $\mathcal{G}\{ \mathcal{V}, \mathcal{E}\}$ is said to be connected [[graph]] if ther e is exactly one connected component.


