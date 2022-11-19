------
#LinearAlgebra 

A Norm is defined as the measure of the size or length for vectors in vector spaces. 

let $V$ be a vector space in domain $\mathbb{F}$ , the function $||\cdot||$ acts on $V$ such that:

- 1: Positive Qualification: for $\forall x \in V$ , $||x|| \geq 0$ with $||x|| = 0$ iff $x = 0$
- 2: Homogeneous: for $\forall x \in V, \forall a \in \mathbb{F}$ , $||ax|| = ||a|| ||x||$
- 3. Trigonometric inequality: $\forall x, y \in V$ ,  $||x+y|| \leq ||x|| + ||y||$ 

then $||\cdot||$ is a norm of $V$, $V$ is the normed vector space of $||\cdot||$ 

The difference compared to [[metric space]]:

- metric is defined on any non-empty set, while norm is defined only on vector spaces
- In normed vector spaces, a norm can induce a metric, but inverse does not work. This means that normed vector space must be [[metric space]].
- Homogeneous property of normed vector spaces can be viewed as a reinforcement of the concept of distance or metric

