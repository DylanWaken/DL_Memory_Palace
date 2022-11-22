----
#BasicGraphTheory 

A Walk is a sequence of nodes and edges (starting from a node and end at a node). Each edge in the walk must ***incident*** with the node preceeding and following it:
![[identify-walk-trail-path-graph-example.png]]
- nodes and edges in a walk can be repeated

For a [[Graph]] $\mathcal{G}\{\mathcal{V},\mathcal{E}\}$ , if we say $A^n$ is the n th power of the [[Adjacency Matrix]] $A$ , then $A^n[i.j]$ would represent the number of $v^i \text{ to } v^j$  walks of length $n$. Proof:

$$A_{ij} ^{k+1} = \sum _{h=1} ^{N} A^k_{ik} \cdot A _{kj}$$
- since this is a cumulative product, $A^{k+1} _{ij}$ would only be non-zero if a edge exist such that $\mathcal{e(v_i,v_h)} \in \mathcal{E}$  and $\mathcal{e(v_h,v_j)} \in \mathcal{E}$
