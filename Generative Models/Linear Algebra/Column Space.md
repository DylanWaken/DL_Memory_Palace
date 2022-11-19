----
#LinearAlgebra 

Column space is the vector space constructed by the columns of a matrix. 
$$A = [c_1, c_2, ...,c_n]$$
($c_n$ is the nth column)

in which column space $\mathcal{C}(A) = span({c_1, c_2, ... , c_n})$    

- The dimensions of the column space is also the [[rank]] of the matrix 
- The column space of $A$ is the same as the [[row space]] of $A^T$ 

## [[Basis]]:

To find the [[basis]] of a column space, we normally execute a ***reduced-row-echelon*** reduction process on the matrix $A^{m \times n}$:

$$A = \begin{bmatrix} 
a_{1,1} \quad a_{1,2} \quad ... \quad a_{1,n} \\
a_{2,1} \quad a_{2,2} \quad ... \quad a_{2,n} \\
...\\
a_{m,1} \quad a_{m,2} \quad ... \quad a_{m,n} \\
\end{bmatrix}
\rightarrow

\begin{bmatrix} 
1 \quad 0 \quad.... \quad 0 \\
0 \quad 1 \quad ... \quad 0 \\
...\\
0 \quad 0 \quad ... \quad 0
\end{bmatrix}$$
For every row, we need to find the position of the leading element (pivot) that is 1 (the leftmost element in each row that is not zero). The columns containing the leading elements are [[linearly independent]] to each others, and thus are the [[basis]] of the column space.

The [[basis]] is the original columns with leading elements in RREF(row reduced echelon form) matrix. 

The dimensions of the column space is the [[rank]] of the matrix.
