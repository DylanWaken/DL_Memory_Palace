----
#BasicMachineLearning 

## Radical function

A Radical Function is a real-value function $\phi$ with the only value dependent on the distance between the input vector and a specific point, in which:
$$\phi = \hat\phi||x-c||$$
- The distance is normally Euclidean distance

The radical function $\phi : [0,\infty) \rightarrow \mathbb{R}$ 
When paired with a norm $||\cdot|| : V \rightarrow [0:\infty)$ , a radical function $\phi = \hat\phi||x-c||$ is said to be a **radical kernel** centered at $c$

The Radical function is said to be a radical basis function if for the given set of nodes $\{x_k\}_{k=1} ^n$ satisfy the following conditions: 

- The kernels $\phi_{x_1}, \phi_{x_2}, ... ,\phi_{x_n}$ are linearly independent
- The kernels $\phi_{x_1}, \phi_{x_2}, ... ,\phi_{x_n}$ have a non-singular interpolation matrix:
$$\begin{bmatrix}
\phi||x_1-x_1||\quad \phi||x_1-x_2|| \quad ... \quad \phi|x_1-x_n||\\
\phi||x_2-x_1||\quad \phi||x_2-x_2|| \quad ... \quad \phi|x_2-x_n||\\
....\\
\phi||x_n-x_1||\quad \phi||x_n-x_2|| \quad ... \quad \phi|x_n-x_n||\\
\end{bmatrix}$$



