----
#LinearAlgebra 

Divergence is the derivative of vector-output-functions ($\mathbb{R}^n \rightarrow \mathbb{R}^n$) with scalar output . Gradient is the derivative of a scalar-output-vector-function ($\mathbb{R}^n \rightarrow \mathbb{R}$) that produce a vector. 

Divergence is defined on the [[Vector Field]], producing a scalar giving the quantity of the vector field's source at each point.

>More technically, the divergence represents the volume density of the outward flux of a vector field from an infinitesimal volume around a given point.

Intuitively speaking, if the vectors around a region is pointing away from the regin, the divergence achieves a positive value. In contrary, if the vectos are pointing toward the given region, the divergence of the region would have a negative value.

![[Divergence.png]]

## Definition

In Cartesian coordinates, the divergence is defined on a n dimension constinously differentiable vector field constructed based on vector function:
$$F(x) = [f_1(x_1...x_n),f_2(x_1...x_n)...f_n(x_1...x_n)]$$
The divergence of $F$ is:
$$div (F) =\nabla \cdot  F = \begin{bmatrix}
\dfrac{\partial }{\partial x_1} 
\dfrac{\partial }{\partial x_2} 
... 
\dfrac{\partial }{\partial x_n}
\end{bmatrix}
\cdot
\begin{bmatrix}
F_{x_1} \,
F_{x_2}
...
F_{x_n}
\end{bmatrix}
= \sum_{i=1}^n \dfrac {\partial F}{\partial x_i}$$
## Properties

The divergence also follows the linear properties, as:
$$div(aF +bG)  = a \cdot div(F) + b\cdot div(G)$$
The product rule is given as:
$$div(\phi F) = (\nabla \phi)F + \phi (div(F))$$
- Where $\phi$ is a scalar-value funtion $\phi : \mathbb{R}^n \rightarrow \mathbb{R}$ 

