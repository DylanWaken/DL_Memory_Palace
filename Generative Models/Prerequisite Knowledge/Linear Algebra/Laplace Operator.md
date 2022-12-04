----
#LinearAlgebra 

Laplace operator or laplacian is defined as the [[Divergence]] of the gradient of a scalar function in the Euclidean space.

For a scalar-value function $f: \mathbb{R}^n \rightarrow \mathbb{R}$, the laplace operator is defned as:
$$\Delta f = \nabla ^2f = \nabla \cdot \nabla f$$
Since we ave the definitions:
$$\nabla = \begin{bmatrix}
\dfrac{\partial }{\partial x_1}
\dfrac{\partial }{\partial x_2}
...
\dfrac{\partial }{\partial x_n}
\end{bmatrix}^T
\quad
\nabla f = \begin{bmatrix}
\dfrac{\partial f }{\partial x_1}
\dfrac{\partial f}{\partial x_2}
...
\dfrac{\partial f}{\partial x_n}
\end{bmatrix}^T
$$
The laplacian of $f$ is given as:
$$\nabla^T\nabla f = \sum _{i=1} ^n \dfrac{\partial^2f}{\partial x^2}$$
By intuition, the continuous Laplacian operator measures how a function changes “on average” as you move away from a given point
