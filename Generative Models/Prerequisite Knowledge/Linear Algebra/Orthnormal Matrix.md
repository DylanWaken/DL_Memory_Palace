----
#LinearAlgebra 

Orthnormal matrix are real square matrices whose columns and rows are orthnormal vectors.
The orthnormal matrix satisfies the following condition:
$$Q^TQ = I \Longrightarrow Q^{-1} =Q^T$$
- Orthnormal vectors are [[Orthogonal]] unit vectors

The reason is that, for any row $q^T_i$ in matrix $Q^T$ and any column $q_j$ in matrix $Q$, we have:
$$q^T_iq_j = 0 : i \neq j, q^T_iq_j = 1 : i =j$$
- Since all vectors with $i \neq j$ are orthogonal to each others with dot product of zero. and when the same unit vector dot product with itself ($i=j$), the result is 1

The orthnormal matrix would preserve all vector dot products, as:
$$u\cdot v = (Qu) \cdot(Qv) = u^TQ^TQv =u^TIv $$

