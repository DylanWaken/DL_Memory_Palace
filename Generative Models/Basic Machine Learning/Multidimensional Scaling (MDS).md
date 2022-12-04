-----
#BasicMachineLearning 
> ***Problem Type***: [[Embedding]]
> ***Solution Type***:  Closed-form Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$  
> SOLVE: The transformation $f(X)$ where  $f : \mathbb{R}^n \rightarrow \mathbb{R}^k$ such that $||x^{(i)} - x^{(j)}|| = ||f(x^{(i)}) - f(x^{(j)})||$  
> ***Closed-form Solution***:
> 1: Compute the distance matrix $D$ : $d_{ij} = ||x^{(i)} - x^{(j)}||$
> 2: Compute the inner product matrix $B$ of the embedded samples:
> $b_{ij} = -\frac{1}{2}(d^2 _{ij} - \frac{1}{N} \sum_{j=1} ^N d^2 _{ij} - \frac{1}{N}\sum_{i=1} ^N d^2_{ij} + \frac{1}{N^2} \sum_{i,j=1} ^N d^2_{ij})$
> 3: Run the diagonalization on matrix $B$ to get $B = P\Lambda P^T$ 
>  Take the greatest $k$ eigenvalues (columns) from $P$ to form $P_k$, with correspond eigenvalues $\Lambda_k$
>   The transformation will be $f(X) = P_k \Lambda _n ^{1/2} \in \mathbb{R}^{k \times N}$


The intention behind MDS is to keep the distances between data samples the same after the embedding or dimension reduction process.

Assume sample $X \in \mathbb{R}^{n\times N}$ , and the embedding process $f : \mathbb{R}^n \rightarrow \mathbb{R}^k$ functions as $f(X) = [z^{(1)}, z^{(2)},...,z^{(N)}]$ . We have the inner product matrix:
$$B = Z^TZ$$
Where $B_{ij} = <z^{(i)}, z^{(j)}>$

We define the distance matrix $D$ as we assume the distance between the original sample points as:
$$d_{ij} = ||x^{(i)} - x^{(j)}||$$
Since the distance between embedded and original samples are maintained constant, we have the constraints of:
$$d_{ij}^2 = ||z^{(i)} - z^{(j)}||^2$$
And with further deriving we have:
$$d_{ij}^2 = {z^{(i)}}^T z^{(i)} - 2 {z^{(i)}}^T z^{(j)} +  {z^{(j)}}^T z^{(j)} = b_{ii} - 2b_{ij} + b_{jj} \quad(1.1)$$
For easier computation, we assume $z$ is normalized:
$$\sum _{i=1} ^N z^{(i)} = 0$$
And therefore we derived the constraints for the inner product matrix:
$$\sum _{i=1} ^N b_{ij} = 0 \quad \sum _{j=1} ^N b_{ij} = 0$$
- Since the same row and column resulted from all embedded sample data multipling with the same sample data,  the sum of rows and columns must be zero for the above normalization condition to satisfy.

To solve for the optimal transformation, we take sum on both side of funciton (1.1)
$$\begin{align*}
d^2_{:j} =\sum_{i=1}^N d_{ij} ^2 = \sum _{i=1}^N ||{z^{(i)}}||^2 + ||z^{(j)}||^2 = tr(B) + Nb_{jj} \\
d^2_{i:} =\sum_{j=1}^N d_{ij} ^2 = \sum _{j=1}^N ||{z^{(i)}}||^2 + ||z^{(j)}||^2 = tr(B) + Nb_{ii} \\
d^2 _{::} = \sum _{i=1}^N \sum _{j=1}^N d^2 _{ij} =  \sum _{i,j=1}^N ||{z^{(i)}}||^2 + ||z^{(j)}||^2 = 2N tr(B)
\end{align*}$$
Bring this conclusion back into formula (1.1), we can solve for the inner product matrix $B$ (we use the above formulas to replace out $b_{ii}$ and $b_{jj}$):
$$\begin{aligned}
& b_{ij} = - \frac{1}{2}(d_{ij}^2 -b_{ii} -b_{jj})\\
& = - \frac{1}{2} (d_{ij}^2 - \frac{1}{N}(d^2 _{i:} -\frac{1}{2N}d^2_{::}))-\frac{1}{N} (d^2 _{:j} -\frac{1}{2N}d^2_{::}))\\
& = -\frac{1}{2}(d^2 _{ij} - \frac{1}{N}d^2 _{i:} - \frac{1}{N}d^2_{:j} + \frac{1}{N^2}d^2_{::})
\end{aligned}$$
And as long as we have the inner product matrix of the projected data, we can solve for the orthnormal basis. We use the [[Diagonalize]] process:
$$B = P \Lambda P^{-1} = P\Lambda P^T$$
- Here we used the property of [[Orthnormal Matrix]]

We use the top k largest eigen vectors as our new projection basis. 

The eigen vectors are represented as $P_k$
The corresponding eigen values are formed into the diagnol matrix $\Lambda_k$

By solving the following equation:
$$Z_k^TZ_k = P_k\Lambda P_k^{T}$$
we can find the projected data as:
$$X' = Z = P_k\Lambda _k ^{1/2} $$
