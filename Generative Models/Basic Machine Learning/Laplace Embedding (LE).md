----
#BasicMachineLearning 

Laplace Embedding function similar to [[Locality Preserving Projection (LPP)]] to optimized on the weighted distance between data samples. However, the optimization target for Laplace Embedding is directly on the distance after projection.
$$J(Y) = \frac{1}{2} \sum _{i=1} ^N \sum _{j=1} ^N w_{ij}||y^{(i)}-y^{(j)}||^2 $$
- where $w_{ij}$ is the weight between samples before embedding , or between $x^{(i)}$, $x^{(j)}$

To have the weight function corresponding to distance, we construct the [[K-Nearest-Neighbors Graph (KNNG)]]. We find the k nearest neighbors of $x^{(i)}$, and use the [[Radical Basis Function (RBF)]] to construct the weights (like in LPP):
$$w_{ij} = \exp(-\frac{||x^{(i)} - x^{(j)}||^2}{\sigma^2})$$
We expand the oprimization target as follows:
$$\begin{align}
&J(Y)= \frac{1}{2} \sum _{i=1} ^N \sum _{j=1} ^N w_{ij}||y^{(i)}-y^{(j)}||^2 \\
&\quad\quad= \frac{1}{2} \sum _{i=1} ^N \sum _{j=1} ^N  w_{ij} (y^{(i)} - y^{(j)})^T(y^{(i)}-y^{(j)})\\
&\quad\quad=\frac{1}{2} \sum _{i=1} ^N \sum _{j=1} ^N  w_{ij} ({y^{(i)}}^Ty^{(i)} + {y^{(j)}}^Ty^{(j)} -2{y^{(i)}}^Ty^{(j)})\\
& \quad\quad=\sum_{i=1}^Nd_{ii}({y^{(i)}}^Ty^{(i)}) - \sum _{i=1} ^N \sum _{j=1} ^N w_{ij} ({y^{(i)}}^Ty^{(j)})\\
&\quad\quad = tr(Y^TYD-Y^TYW)\\
&\quad\quad = tr(Y^TY(D-W))\\
&\quad\quad = tr(YLY^T)
\end{align}$$
- $D$ is the degree matrix of the original graph
- $W$ is the weight matrix of the original graph
- $L$ is the [[laplace matrix]]

Because $Y$ is scale free, we add a scale constraint to prevent zero scales:
$$YDY^T = 1$$
And our optimization target became:
$$\begin{align}
&\min _Y J(Y) = tr(YLY^T) \\
&s.t. \quad YDY^T = I
\end{align}$$
Us the [[Lagrange Multiplier]] to get the optimization function:
$$\mathcal{L}(Y,\Lambda) = tr(YLY^T) + tr(\Lambda(YDY^T-I))$$
Solve for zero partial derivative:
$$\begin{align}
&\frac{\partial\mathcal{L}}{\partial Y} = 2YL - 2YD\Lambda = 0\\
&YL = \Lambda YD\\
&YLD^{-1} = Y\Lambda D
\end{align}$$
Where the row vectors of $Y$ is the eignevectors of $LD^{-1}$. To minimize the optimization targetm we pick the $k$ minimal eigenvalue's correspondign eigenvectors to form $Y$. 