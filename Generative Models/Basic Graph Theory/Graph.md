----
#BasicGraphTheory

A graph is a set of nods (vertices) and edges: normally $\mathcal{V}$ denotes the set of all nodes, and $\mathcal{E}$ denotes the set of all edges. For example:

![[Graph.png]]

This is the example of a graph, in which $V_1, V_2$ denotes 2 vertices and $\mathcal{e}(V_1,V_2)$ is the edge between them (if there exists one). In this case, $V_1, V_2 \in \mathcal{V}$ and $\mathcal{e}(V_1,V_2) \in \mathcal{E}$.

We define a graphs as the set of all its vertices and edges, as:

$$\mathcal{G} = \{\mathcal{V}, \mathcal{E}\}$$
Or written in the definition form:

$$\mathcal{G} \{\mathcal{V}, \mathcal{E}\}$$

Graphs can be categorized into two versions, Directed graph and Undirected graph.

In ***directed graphs***, each edge between two vertices is a single-directional connection, and the permutation of vertices in the edge definition matters, whichi is:

$$\mathcal{e}(V_1, V_2) \neq \mathcal{e}(V_2, V_1)$$

In ***Undirected graphs***, in which all connections are dual-directional, and there exists no difference for the edge between two vertices regarding the permutation of the vertices in the edge definition:

$$\mathcal{e}(V_1, V_2) = \mathcal{e}(V_2, V_1)$$

The example shown below is the two graph types:

![[DirectedAndUndirected.png]]

In a graph, if there exists an edge between two vertices, we say that the vertices are ***adjacent*** to each others.

