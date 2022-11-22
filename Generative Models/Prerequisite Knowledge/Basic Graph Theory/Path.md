----
#BasicGraphTheory 
![[identify-walk-trail-path-graph-example.png]]
A path is a [[Walk]] with no repeating nodes in the [[Graph]].
A path must be a [[Trail]]

### shortest path

for $v_s,v_t \in \mathcal{V}$ in [[Graph]] $\mathcal{G}$ , the shortedt path between $V_s, V_t$ is defined as:

$$p^{sp} _{s,t} = argmin _{p \in P_{s,t}} |p|$$
- $P_{s,t}$ is the collection of all paths from $V_s$ to  $V_t$
- $|p|$ is the length of the path
- $p^{sp} _{s,t}$ is the shorted path from $V_s$ to  $V_t$

