----
#BasicMachineLearning 
> ***Problem Type***: [[Embedding]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$  
> SOLVE: orthnormal basis $u_1,u_2,...,u_k$ such that the weighted projection distance is minimized:
> $J(A = tr(A^TX^TLXA)$ 
> ***Closed-form Solution***: The new basis are the $k$ minimal eigenvectors of $(X^TDX)^{-1}X^TLX$  

LPP is designed based on the ideas behind [[Principal Component Analysis (PCA)]], but  LPP maximizes the weighted distance between projected sample points.

The computation begin with constructing data into a **adjacency graph**, normally through:

- $\epsilon$-neighbors: Node $i$ and $j$ are connected if $||x^{(i)} - x^{(j)}||^2 < \epsilon$ 
- [[K-Nearest-Neighbors Graph (KNNG)]]: Node $i$ and $j$ are connected if $i$ is among the $k$ nearest neighbors of $j$ and $j$ is among the $k$ nearest neighbors of $i$.

In the construction of the graph, the weights are calculated by the **Heat Kernel**, as:
$$W_{ij}=\exp(-\frac{||x^{(i)}-x^{(j)}||^2}{\sigma^2})$$
- This kernel is a [[Radical Basis Function (RBF)]]
- The wights are higher when the data samples are closer

## Optimal Linear Embedding

Since we are projecting a weighted graph $G$ to a lower dimensional vector, we are looking for the mapping that would minimize the distance between nearby data samples. Let $y$ be the mapping, we are looking for:
$$\min \sum _{i,j} ||y^{(i)}-y^{(j)}||^2 W_{ij}$$
The function incorporates a high penalty if neighboring points $x^{(i)}$ and $x^{(j)}$ are mapped far apart. We are looking for the mapping such that $y^{(i)}$ and $y^{(j)}$ are close when $x^{(i)}$ and $x^{(j)}$ are close. 

Suppose $A$ is the transformation matrix, that is:
$$y^{(i)} = Ax^{(i)}$$
- the i th column vector of $X$ is $x^{(i)}$.

With some simple deriving process:

$\dfrac{1}{2} \sum _{ij}^N ||y^{(i)} - y^{(j)}||^2W_{ij} = \dfrac{1}{2} \sum _{ij} ||Ax^{(i)} - Ax^{(j)}||^2W_{ij}$ 

$=\dfrac{1}{2} \sum_{i,j} ^N W_{ij} (Ax^{(i)} - Ax^{(j)})^T(Ax^{(i)} - Ax^{(j)})$

$= \dfrac{1}{2} \sum_{i,j} ^N W_{ij} (x^{(i)})^T A^T Ax^{(i)} + (x^{(j)})^T A^T Ax^{(j)} - 2(x^{(i)})^T A^T Ax^{(j)}$

$= \sum_{i} ^N d_{ii} (x^{(i)})^TA^TAx^{(i)} - \sum_{i,j} ^N W_{ij} (x^{(i)})^TA^TAx^{(j)}$

$= tr(A^TX^T(D-W)XA)$

$= tr(A^TX^TLXA)$

where $L$ is the [[Laplace Matrix]]

Since projection matrix $A$ can be arbitrarily scaled, we have a projection norm length constraint for the optimization problem (like the unit vector constraint in PCA):
$$A^TX^TDXA = I$$
And the final problem is:
$$ \min_AJ(A) = tr(A^TX^TLXA) \quad s.t. \quad A^TX^TDXA = I$$
Using the [[Lagrange Multiplier]], we convert the source problem to:
$$\mathcal{L}(A, \Lambda) = tr(A^TX^TLXA) + tr(\Lambda(A^TX^TDXA-I))$$
Followed by solving zero partial derivative:
$$\dfrac{\partial \mathcal{L}}{\partial \Lambda} = 2X^T LXA - 2X^TDXA \Lambda = 0$$
And finally by simplify:
$$(X^TDX)^{-1} X^TLXA = A \Lambda$$
In which, we have every column vector of $A$ being the eigenVector of matrix $(X^TDX)^{-1} X^TLX$ . The following dimension reduction process will be the same as for [[Principal Component Analysis (PCA)]]
