----
#LinearAlgebra 

The Gram Matrix of a set of vectors $\{v_1,...,v_n\}$ in an [[Inner Product Space]] is the square matrix with every element being the corresponding vector's inner products, in which:
$$G_{ij} = v_i^Tv_j = <v_i,v_j>$$
## Properties:

1: The Gram Matrix is always symmetric.
$$v_i^Tv_j = v_j^Tv_i$$
2: The Gram Matrix is positive-semidefinite ([[Definite Matrix]]):
$$x^TGx = \sum _{i,j} <x_iv_i, x_jv_j> = <\sum_{i,j}x_iv_i, \sum_{i,j} x_jv_j> = ||
\sum _{i,j} x_iv_i||^2 \geq0$$
3: The set of vectors $\{v_1,...,v_n\}$ is linearly independent to each others if and only if the determinent of their Gram matrix $G$ is nonzero.

## Constructing an orthnormal basis

Given a set of linearly independent vectors $\{v_i\}$ with the Gram matrix $G$, the orthnormal basis can be constructed through the following approach: 
$$w_i = \sum_j(G^{-1/2})_{ij} v_j$$
