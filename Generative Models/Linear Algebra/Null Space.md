----
#LinearAlgebra 

Null space of a mtrix is the set of vectors $v$ such that:
$$Av = 0$$
which can be also seen as:

$$\begin{bmatrix}
  r_1\cdot v\\
    r_2\cdot v\\
    ...\\
      r_n\cdot v\\

\end{bmatrix} = 0$$
Since vector $v$ is executing an inner product to every row of matrix $A$,  the only condition that allows the matrix vector multiplication to produce $<r,v> = 0$ is  $v \perp \forall r \in R(A)$. 

As the rows are included in the row space, the condition is simplified as $v$ being [[orthogonal]] to every [[basis]] vector of the row space $R(A)$ .  The null space is labeled as $N(A)$

By the [[rank]]\-nullity theorem:
$$rank(A) + null(A) = dim(A)$$
(the null space is the nullity complement to the linear transformation represented by A)

And since we have the ranks defined as size of row / col space, we have
$$dim(R(A)) +dim(N(A)) = dim(A)$$
