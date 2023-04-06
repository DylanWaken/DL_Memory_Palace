
----
#GenerativeModel 

A really good blog on the topic: https://huggingface.co/blog/encoder-decoder 

## Self Attention

Self attention is the variant of the old methodology of "**Exponential Dot Product Attention**" use in the field of contrastive learning and metric learning like [[Noise-Contrastive Estimation]].

Self attention is an operation that models the correlation between the different parts of the same piece of message. The output of self attention would be a matrix representing the correlation of every single time series data point upon othe points

The raw form of Self-Attention (or the key-value attention) is given as: $$\text{Attention(Q,K,V)} = softmax\left( \frac{QK^T}{\sqrt{ d_{k} }} \right) V$$
- $Q$ is the query matirx
- $K$ is the key matirx
- $V$ is the value matirx
- these matrices are of same dimensions

I will expand upon the details of these components in the later part of this blog.

Assume our data over time is concatinated into the rows of these matrices:
$$X = \begin{bmatrix}
-x_{t=1}- \\
-x_{t=2}- \\ 
\dots\\
-x_{t=n}-
\end{bmatrix}, X\in \mathbb{R}^{n\times m}$$
- $n$ is the length for time series data, normally called `seq_length`
- $m$ is the length for the data, normally called `d_model` or `model_dimension`

For easier understanding, lets assume that $Q=K=V=X$, and our formula is reduced to:
$$softmax (XX^T)X$$
The first component of the formula can be expressed as vector inner product:
$$(XX^T)_{i,j} = \sum_{k} x_{i,k} \cdot x_{k,j} = X_{i}(X_{j})^T$$
Since the second matrix is the transposed of the first matrix, the  outcome is equivalent of inner product for the $i$ th row and $j$ th row of the same matrix, which corresponds to the $i$ th and $j$ th data in the sequence.

Because inner product is the measure of similarities between vectors, the $XX^T$ operation here gives us a matrix showing the similarity between every single pair of data in the input sequence.

The softmax operation is applied by row on the resultant matrix, which can be shown as:
$$W:w_{i,j}= \frac{\exp(w_{ij})}{\sum_{k}^n\exp(w_{ik})}$$
- Since each row stands for a specifc data points, the normalized weight vector of this row would give the weighted value for how much this data point is related to other data points in the series as probability.

Now, the final step in self attention is to apply these weights, as:
$$WX = \begin{bmatrix}
w_{00}&w_{01}&\dots &w_{0n} \\
w_{10}&w_{11}&\dots&w_{1n} \\
\quad\dots \\
w_{n0}&w_{n1}&\dots& w_{nn}
\end{bmatrix} \begin{bmatrix}
- x_{t=1} - \\
-x_{t=2}- \\
\dots \\
-x_{t=n}-
\end{bmatrix}$$

For every row of new data in output matrix $X'$ , the data would be a the **weighted sum** of itself and other data in the time series, as we "encode" these data correlations into the data themselves.

The $Q,K,V$ matrices are named after this theorem. We applied linear transformations to the input data as:
$$Q =  X W_{Q}\quad K= X W_{K}\quad V=XW_{v}$$
- The right multiplication is just to keep the same with the books/papers on the topic.  It means that we are applying the transformations on "row vectors" of the matrix instead of column vectors in other models. 

The name query and key came fron the idea we mentioned above, the self-attention would compute the correlation of every "key" to the same "query", and store the output in the "value" as output.

The linear transformations are just learnable parameters to helf finding the attentions to pick between different parts of the time series data.

The final term $\sqrt{ d_{k} }$ is the normalizing term. Assume the original data in the rows and columns have variance 1 and mean 0, the add-multiply might blow up the vectors. The variance can be normalized to 1 through dividing the square root of the sequence length $n$, $\sqrt{ d_{k} } = \sqrt{ n }$

Note that self attention is, pretty obviously, position independent, which means the order of the sequence does not influence the correlation of the correlation computation between query and keys. 

//TODO: ad the probabilistic understandong of self attention 

## Multi-Headed Attention

Multi-headed Attention is the mechanisom borrowed from the multi convolution kernels from traditional CNNs. 

In the multi-headed attention computation, the same input data is applied to multiple weighted linear transformations for constructing $Q,K,V$ vectors. The computation looks like this:
$$\begin{align}
&H_{i } = \text{Attention}(XW_{i}^Q, XW_{i}^K, XW_{i}^V) \\
&X' = \text{Concat}(H_{1},\dots,H_{h})W^O
\end{align}$$
- Here $h$ is the number of parallel self-attention blocks at the same time.

The dimensions of the weight matrices are given as:
$$\begin{align}
&W_{i}^Q \in \mathbb{R} ^{m\times d_{k}}, W_{i}^K \in \mathbb{R} ^{m\times d_{k}}, W_{i}^V \in \mathbb{R}^{m\times d_{v}}, W^O \in \mathbb{R} ^{hd_{v} \times m} \\
&H_{i} \in \mathbb{R}^{n\times d_{v}} , Concat(H_{1},\dots,H_{n}) \in \mathbb{R}^{n \times d_{v}h}
\end{align}$$
- $m$ is the length of the data.
- $d_{k}$ is the dimension for the query/key computation, we normally set $d_{k}<n$ to have the dimension reduction effect to save some computational power. A tradition is to have $d_{k} = \frac{n}{h}$
- $d_{v}$ is the desired output dimension for each self-attention component of the multi-headed attention. in tradition we have $d_{v}=d_{k}$ 

Note, through the multi-headed attention process, the dimensionality of the data remains the same. The final matrix $W^O$ linear transforms the concatinated data to combine these attention results.

## Feed Forward Layers

The archiecture includes a feed forward linear structure for each datapoint after the multi-headed attention segment. The linear transformations and activation runs on the row vectors to process each data piece individually:
$$FFN(X) = ReLU(xW_{1} +b_{1})W_{2}+b_{2}$$
- These layers are used as some sort of feature extraction over data, the original paper did not give an official explanation on this part.
- The layer size in the middle of the 2 layered structure can be different from data length $m$, normally denoited as `d_ff`

## Positional Encoding

Since we mentioned above, the self-attention is a topological model that only learns the inter-correlation between data points, and these similarity weights are computed independent from the location or time step the data point belongs to.

For modeling a time series, the information about relative location in time is still crucial. Therefore, we need a way to embed this information into the data points given to self attention blocks.

The position encoding in the original work is defined as:
$$\begin{align}
&PE_{1}(pos,2i) = \sin(pos/10000^{2i/m}) \\
&PE_{2}(pos,2i+1) = \cos(pos/10000^{2i/m})
\end{align}$$
- $i$ is the dimension id of the input data, as $X_{pos,i}$. This term is just for garentee the data mean after positional encoding remains around 0 and variation around 1.
- $pos$ is the position of the data point in the sequence, as $t=pos$ in $X$ or $X_{pos}$

The matrix produced from running this operation on each input matrix location would be directly added to the input matirx.

- Positional encoding is periodic, which means it gives infromation about the relative location of data in the sequence 
- Positional encoding also have the effect of damping out data that is farther away from a specific data point. it acts as a constraint for the attention computation. 
- Positional encoding is easy to extrapolate for long sequences since it is a determinastic function.

## Residual Connections

Like the traditional residual CNN (Resnet), the residual connections are also introduced in the model to prevent gradient vanishing problem as multiple modules of multihead attentions and FFNs are stacked upon each others. For all sublayers (MA or FFN), an residual connection is introduced as:
$$X' = sublayer(X) + X$$
In the original work, a dropout is included to prevent overfitting as:
$$X' = dropotu(sublayer(X)+X)$$
To prevent the addition process from causing the network activations to blow up (since it shifts the mean of the data, and grow the data exponentially across following sublayers), a layered normalization is included:
$$X_{out} = \gamma \left[ \frac{{X'_{i}-\mu_{X'_{i}}}}{\sigma _{X'_{i}}} \right] + \beta$$
- $\beta$ and $\gamma$ are learnable parameters like in batch normalization, $\beta\in \mathbb{R^n}$, $\gamma \in \mathbb{R}^n$
- here every row of $X'$ or $X'_{i}$ is subtracted by the mean of the row and divided by the standard deviation of the row

## AutoEncoding Self-Attention

The self attention autoencoder is designed for the sequence generation problems. That is, given an existing sequence of data:
$$X_{1:n} = \{ x_{1},\dots,x_{n} \}$$
We are looking for a mapping to a sequence of output data:
$$f:X_{1:n}\to Y_{1:k} $$
#### Encoder

The transformer encoder is a **self-attention** block that maps data to the same dimensions, as: $$f_{enc} : X_{1:n} \to X'_{i:n}$$
The architecutre is shown below by stacking multiple residual multi-headed attention layers and residual FFN layers, which is normally called **The Bidirectional Encoder for Transformers - BERT** 

(it is bidirectional because each data point in the sequence will be computed attention scores relative to all other data points in the sequence, there is no constraints on time steps). 

![[Screenshot from 2023-03-15 14-36-06.png]]

In the encoder below, only the self attention blocks are used.

![[Deep Learning/Assets/Screenshot from 2023-03-15 14-34-49.png]]

**The encoder will encode each data point with the network weighted intercorrelations with othre data points in the sequence, and store it back into the data point itself. Note: This is just a theory, the exact reason for why BERT works remains unknown.**

#### Decoder

The decoder part of this autoencoder involves a little bit more complexity

Similar to RNN-based encoder-decoder models, the transformer-based encoder-decoder models define a conditional distribution of target vectors $Y_{1:k}$​ given an input sequence $X_{1:n}$. $$p_{\theta_{dec}}(Y_{1: k}|X_{1:n})$$ (￼￼without main diagnal￼￼)
And by the Bayes rule we can expand this as: $$p_{\theta_{dec}}(Y_{1: k}|X_{1:n}) = \prod _{i=1} ^k p_{\theta_{dec}}(y_{i }|Y_{i-1}, X_{1:n})$$
Note: this formula says that the probability of a specific output at a time step is only conditionally dependent on the preceeding time steps, and the data points beyond this time step should not be involved in the prediction process. This is extremely important in the definnition of the decoder.

To prevent the network from "using data points in the furture", the decoder attention block is designed to be **Uni-Directional**. Every data point $y_{i}$ in the generator self attention only have access to data points that came before it. $y_{1} ,\dots,y_{i-1}$ . 

![[Screenshot from 2023-03-16 10-36-07.png]]

The decoder includes the uni-directional self ttention and a cross-attention structure between the decoded data and the encoder inputs.

The uni-directional self-attention is defined as:$$Y'' = softmax\left( LT( \frac{QK^T}{\sqrt{ d_{k} }}) \right) V +Y'_{0}$$ 
- Here $LT$ stands for taking the lower triangle of the attention score. This operation is also called **masking** in some papers
- By taking the upper triangular part of attention score, the linitselfear transformation will only add attention weighted preceding data points in the output sequence to the current data point. 

Which in graphical representation, is shown as:

![[Screenshot from 2023-03-16 11-03-28.png]]

The **Cross Attention** is following the self attention layer, it is defined as the attention process among the input sequence $X_{1:n}$ and the output sequence $Y$, and then apply this attention score on the values matrix of $X$, which is defined as:
$$Y''' = softmax\left( \frac{Q_{y}K_{x}^T}{\sqrt{ d_{k_{x}} }} \right) V_{x} + Y''$$
The graphical representation is:

![[Screenshot from 2023-03-16 11-14-32.png]]

The encoder output's participation in the decoder can be also understood as a "control signal" of the decoder behaviors. This architecture is originally designed for the purpose of translation in NLP, therefore the cross attention is for the measure of similarity in representation between the source language and target language. 

This is the fundamental structure of self-attention autoencoders. There exists many training algorithms/ loss design for different purposes, check the notes links to this note. 

The whole architecture can be viewed below:

![[eAKQu.png]]