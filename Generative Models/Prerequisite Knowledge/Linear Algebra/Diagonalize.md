----
#LinearAlgebra 

If a matrix $A$ can be diagonalized is and only if the sum of the dimensions of its eigenspaces is equal to $n$, which is the same as if and only if there exists a basis matrix $F^{n \times n}$ consisting of eigenvectors of $A$. 

If such a basis has been found, we can form matrix $P$ have the basis vectors as columns, and the matrix $P^{-1}AP$ will be the matrix consisting of all the eigen-values for $A$

Where we have the equation:
$$\Lambda = P^{-1}AP$$
And for the property of eigen vectors, we have:
$$AP = P\Lambda$$
And if we inverse the function, we have:
$$A = P\Lambda P^{-1}$$
