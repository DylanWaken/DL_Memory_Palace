-----
#BasicMachineLearning 
>  ***Problem Type***: [[CLassification Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $y = [y^{(1)} ... y^{(N)}] \in \mathbb{R}^{c \times N}$ 
> SOLVE: parameters $\theta \in \mathbb{R}^{n \times c} = [\theta_1, \theta_2,...,\theta_c]$ such that $\min _\theta E(\theta) = \frac{1}{N} \sum _{i=1} ^N \sum _{j=1} ^c y_{ji} \log f_j(x^{(i)})$ in which: $f(x) = [f_1(x),...,f_c(x)]^T$, $f(x)$ is the sofrmax operation
> ***Iterative Solution***:  $\theta_k := \theta_k + \alpha \sum _{i=1} ^N y_{ki} (1-f_k(x^{(i)})) x^{(i)}$

Softmax regression is designed for multiple-class classification with $c$ classes. In the other word, the target variable $y$ can take values $y \in [1,c]$  

//In actual computation $y$ will be a vector with one-hot class label, but we set it to integers for our GLM process.

To parameterize this multinomial over the $c$ possible outcomes, we use a set of parameters $W = [w_1, w_2, ... , w_n]$ with each $w_i \in \mathbb{R}^n$ for each output across all inputs. In the actuall prediction stage, each set of parameter will be responsible for the probability of one class. 
$$h_W(x^{(i)}) = W^Tx^{(i)}$$
The output of the hypothesis is also a vector $\phi = [\phi_1, \phi_2, ... \phi_c]$ in which $\phi_i$  represents the probability of the $i^{th}$ output given the inputs. Since these outputs are probabilities, we have $\sum _{i=1} ^c \phi_i = 1$, and knowing $\phi_1$ to $\phi_{c-1}$ would be enough to get all probabilities, making $\phi_c$ not independent from other outputs, and thus be redundant. Where we have the final output $\phi_c = 1 - \sum _{i=1} ^{c-1} \phi_i$ 

Here we derive from [[Generalized Linear Models]]. 
$$p(y;\eta) = b(y) \exp(\eta^T T(y) - \alpha(\eta))$$

To map the exponential family to the higher dimension, we define $T(y) \in \mathbb{R}^{c-1}$ as:

$$T(1) = \begin{bmatrix}
1 \\
0 \\
0 \\
... \\
0
\end{bmatrix}

\quad T(2) = 
\begin{bmatrix}
0 \\
1\\
0\\
...\\
0
\end{bmatrix}

\quad...\quad

T(c-1)=\begin{bmatrix}
0 \\
0 \\
0\\
...\\
1
\end{bmatrix}

\quad T(c) = \begin{bmatrix}
0\\
0\\
0\\
...\\
0
\end{bmatrix}
$$

Note: ${l\{y=1\}}$ produce 1 if y=1, else 0 
We can define the probability of $y$ given $\phi$ as:
$$p(y;\phi) = \phi_1 ^{l\{y=1\}} \phi_2 ^{l\{y=2\}} ... \phi_c^{l\{y=c\}}$$
Swap out the final term we have:
$$p(y;\phi) = \phi_1 ^{(T(y))_1} \phi_2 ^{(T(y))_2} ... \phi_c^{1 - \sum _{i=1} ^{c-1} (T(y))_i}$$
To get the general formula of exponential family, we take the exponents:
$$\exp((T(y))_1\log(\phi_1)+(T(y))_2\log(\phi_2)+...+(1 - \sum _{i=1} ^{c-1} (T(y))_i)\log(\phi_c))$$
Expand the final term, we have:
$$\exp((T(y))_1\log(\phi_1/\phi_c)+(T(y))_2\log(\phi_2/\phi_c)+...+log(\phi_c))$$
By setting this as the exponential family formula, we can easily derive:
$$\eta = \begin{bmatrix}
\log(\phi_1/\phi_c) \\
\log(\phi_2/\phi_c) \\
...\\
...\\
\log(\phi_{c-1}/\phi_c)
\end{bmatrix}$$$$\alpha(\eta) = -\log(\phi_c), b(y)=1$$
For convenience, we also define the final term $\eta_k = \log(\phi_c/\phi_c) = 0$ 

From the derivation, since $\phi_i$ is our linear predictor, the link function for GLM is:
$$\eta_i = \log(\frac{\phi_i}{\phi_k})$$
With a little bit of derivation, we can yield:

$e^{\eta_i} = \dfrac{\phi_i}{\phi_c}$ 

$\phi_c e^{\eta_i} = \phi_i$

$\phi_c \sum ^c _{i=1} e^{\eta_i} = \sum ^c _{i=1} \phi_i = 1$

and where we can solve that  $\phi_c = 1 / \sum _{i=1} ^{c} e^{\eta_i}$

With a little substitution in the original function we have:
$$\phi_i = \frac{ e^{\eta_i} }{\sum _{i=1} ^{c} e^{\eta_i}}$$
And by replacing the $\eta$ with the linear terms, we can get:
$$P(y=i|x;\theta) = \phi_i = \phi_i = \frac{ e^{\theta_i^Tx} }{\sum _{i=1} ^{c} e^{\theta_i^Tx}}$$
- This function would output the brobability of $y = i$ for each class given the specific input $x$

The optimization is also based on [[Maximum Likelihood Estimation]] with the log likelyhood being:

$$\mathcal{l}(\theta) = \sum _{i=1} ^N \log(\prod _{j=1} ^c (\frac{ e^{\theta_j^Tx} }{\sum _{i=1} ^{c} e^{\theta_i^Tx}})^{l{\{y^{(i)}=j\}}})$$
- The cumulative product produce only one probability since all $l\{y^{(i)} \neq l\}$ will be zeros and make other terms 1

From this, we can derive the iterative solution as:
$$\mathcal{l}(\theta) = \sum _{i=1} ^N \sum _{j=1} ^c l\{y^{(i)}=j\} \log(\frac{ e^{\theta_j^Tx} }{\sum _{i=1} ^{c} e^{\theta_i^Tx}}) $$
If we turn $y$ into the one hot matrix versions, we will have:
$$\mathcal{l}(\theta) =  \sum _{i=1} ^N \sum _{j=1} ^c y_{ji} \log(\frac{ e^{\theta_j^Tx} }{\sum _{i=1} ^{c} e^{\theta_i^Tx}})$$
Where we can rewrite in the form of:
$$\mathcal{l}(\theta)=\sum _{i=1} ^N \sum _{j=1} ^c y_{ji} \log f_j(x^{(i)})$$
In order to solve for the point with maximum likelyhood, we take the derivative of the function:
$$\nabla _{\theta_k} l(\theta) = \sum _{i=1} ^N \sum _{j=1} ^c y_{ji} \nabla _{\theta_k} \log(f_j(x^{(i)}))$$
For the second summation, the terms would be zero for any $k \neq j$ .With further deriving we have:
$$\nabla _{\theta_k} l(\theta) = \sum _{i=1} ^N y_{ki} \frac{1}{f_k(x^{(i)})} \nabla _{\theta_k} f_k(x^{(i)})$$
We can solve the derivative of $f_k(x^{(i)})$ :
$$\nabla_{\theta_k}  \frac{ e^{\theta_k^Tx} }{\sum _{i=1} ^{c} e^{\theta_i^Tx}}
= \frac{ e^{\theta_k^Tx} (\sum _{i=1} ^{c} e^{\theta_i^Tx} -e^{\theta_k ^Tx})}{(\sum _{i=1} ^{c} e^{\theta_i^Tx})^2} =  \frac{ e^{\theta_k^Tx} }{\sum _{i=1} ^{c} e^{\theta_i^Tx}} \times \frac{\sum _{i=1} ^{c} e^{\theta_i^Tx} -e^{\theta_k ^Tx}}{\sum _{i=1} ^{c} e^{\theta_i^Tx}}$$
Which can be simplified as:
$$\nabla _{\theta_k} f_k(x^{(i)}) = f_k(x^{(i)})(1-f_k(x^{(i)})) x^{(i)}$$
And our iterative solution is:
$$\theta_k := \theta_k + \alpha \sum _{i=1} ^N y_{ki} (1-f_k(x^{(i)})) x^{(i)}$$

