----
#LinearAlgebra 

A vector field is an assignment of a vector for every give point in the subset of a space. 

![[Vector Field.png]]

To define a vector space, we define a vector-value function as:
$$f(x_1,...,x_n) = \begin{bmatrix}\
f_1(x_1,..,x_n) \\
f_2(x_1,...,x_n)\\
...\\
f_n(x_1,...,x_n)
\end{bmatrix}$$
- $x_1,...,x_n$ is the coordinate of every point in the space $S \in \mathbb{R}^n$
- $f$ is the vector-value function

This function would assign a $n$ dimensional vector to every point in $S$

If $f(x)$ is a linear function, such operation can be done in linear form:
$$f(x) = A\vec{x} + b$$
where $A \in \mathbb{R}^{n \times n}$ is a transformation matrix applied on every point vector $\vec{x}$ , and $b \in \mathbb{R}^n$ is the offset vector

## Vector Fields on Euclidean Space

Given a subset $S \in \mathbb{R}^n$, a vector field is represented by a vector function $V:S\rightarrow \mathbb{R}^n$ in Cartesian coordinates ($x_1,x_2,...,x_n$). The vector field is continuous if each component of $V$ is continuous. 

$V$ is a $C^k$ vector field of each component of $V$ is $k$ times continously differentiable

Vector fields follows the rule of linearity:
$$(fV)(p) := f(p)V(p), \quad (V+W)(p) = V(p) + W(p)$$
- $V,W$ are $C^k$ vector fields defined on $S \in \mathbb{R}^n$ 
- $f$ is a real-valued $C^k$ function defined on $S$ 

