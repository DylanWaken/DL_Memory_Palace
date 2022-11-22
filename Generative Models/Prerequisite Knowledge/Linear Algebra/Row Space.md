----
#LinearAlgebra 

Row space is the vector space constructed by the rows in the matrix $A$:
$$A = \begin{bmatrix} 
 \quad r_1 \quad \\
 \quad r_2 \quad \\
 \quad r_3 \quad\\
 ...\\
 \quad r_n\quad
\end{bmatrix}$$
($r_n$ is the nth row)

in which row space is $\mathcal{R}(A) = span({r_1, r_2, ... , r_n})$    

- The dimensions of the row space is the [[Rank]] of the matrix 
- The row space of $A$ is the same as the [[Column Space]] of $A^T$ 

## [[Basis]]:

To find the [[Basis]] of a row space, we normally execute a row-echelon reduction process on the matrix $A^{m \times n}$:

$$A = \begin{bmatrix} 
a_{1,1} \quad a_{1,2} \quad ... \quad a_{1,n} \\
a_{2,1} \quad a_{2,2} \quad ... \quad a_{2,n} \\
...\\
a_{m,1} \quad a_{m,2} \quad ... \quad a_{m,n} \\
\end{bmatrix}
\rightarrow

\begin{bmatrix} 
1 \quad \_ \quad.... \quad\_ \\
0 \quad 1 \quad ... \quad \_ \\
...\\
0 \quad 0 \quad ... \quad \_
\end{bmatrix}$$
all the rows with a **pivot** (or a 1 in the row) is a [[Basis]] of the row space.

Note: the reduced rows with pivots are the set of [[Basis]] vectors, while the rows in the corresponding locations in the original matirx is also the set of [[Basis]] vectors.

The size of [[Basis]] vector seet $B$ or $||B||$ is the [[Rank]] of the matrix. 