----
#LinearAlgebra 

Jacobian matrix is the derivative of the vector-valued funtion ($f:\mathbb{R}^n \rightarrow \mathbb{R}^m$). It produces a matrix with every function component $f_1 ... f_m$ of $f$ with respect to every element of input vector $x_1...x_n$.

Suppose we have the vector output $y \in \mathbb{R}^m$, for every element $y_i$ of $y$ , we can write its gradients given every input elements and the $i$ th function component of $f$ as:

$$\begin{bmatrix}
\dfrac{\partial y_i}{\partial x_0}\\
\dfrac{\partial y_i}{\partial x_1}\\
...\\
\dfrac{\partial y_i}{\partial x_n}\\
\end{bmatrix}
=
\begin{bmatrix}
\dfrac{\partial f_i(x)}{\partial x_0}\\
\dfrac{\partial f_i(x)}{\partial x_1}\\
...\\
\dfrac{\partial f_i(x)}{\partial x_n}\\
\end{bmatrix}
=
\nabla_xf_i(x)$$
Where we can apply this to every output and get the Jacobian matrix:
$$J_f(x) = 
\begin{bmatrix}
\nabla_xf_1(x)^T\\
\nabla_xf_2(x)^T\\
...\\
\nabla_xf_m(x)^T\\
\end{bmatrix}
=
\begin{bmatrix}
\dfrac{\partial f_1}{\partial x_1} \dfrac{\partial f_1}{\partial x_2}
...\dfrac{\partial f_1}{\partial x_n}\\
\dfrac{\partial f_2}{\partial x_1} \dfrac{\partial f_2}{\partial x_2}
...\dfrac{\partial f_2}{\partial x_n}\\
...\\
\dfrac{\partial f_m}{\partial x_1} \dfrac{\partial f_m}{\partial x_2}
...\dfrac{\partial f_m}{\partial x_n}\\
\end{bmatrix}
$$

The Jacobian matrix is viewed as the first order derivative matrix

Jacobian follows the chain rule of derivative:
given $f: \mathbb{R}^m \rightarrow \mathbb{R}^n$, $g:\mathbb{R}^n \rightarrow \mathbb{R}^k$ , $h(x) = g(f(x))$
$$J_h(x) = J_g(f(x)) \cdot J_f(x)$$\