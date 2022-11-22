-----
#BasicMachineLearning 
>***Problem Type***: [[Classification Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N, y^{(i)} \in \{0,1\}$  
> SOLVE: parameters $w \in \mathbb{R}^{n}, b$ such that  $y^{(i)} = g(w^Tx^{(i)} + b)$ where $i \in \{1,...,N\}$ and $g(z) = z \geq 0 ? 1: 0$  
> ***Iterative Solution***: if $y^{(i)} = 1,$  $w := w +x^{(i)}, b:= b+1$ 
> if $y^{(i)} = 0,$  $w := w - x^{(i)}, b:= b-1$ 

Perceptron Algorithm is one of the earliest binary classification algorithm in the field of machine learning.

For the binary linear-separable data, the decision boundry of a perceptron is given as:
$$w^Tx + b = 0$$
The learning algorithm looks like this:

if $y^{(i)} = 1$ and $w^Tx + b < 0$, then:
$$w := w +x^{(i)}, b:= b+1$$
if $y^{(i)} = 0$ and $w^Tx+b \geq 0$, then:
$$w := w - x^{(i)}, b:=b-1$$
Proof:

Here we combine $b$ into the weights called $w_0$, and we have $x_0$ always equal to 1

When $y^{(i)} = 1$,  we want the value of $w^Tx^{(i)} > 0$ , which because of the following relationship:
$$\cos \alpha = \frac{ w^Tx^{(i)}}{||w||\cdot||x^{(i)}||} \propto w^Tx^{(i)}$$
We want the angle $\alpha$ between $w$ and $x^{(i)}$ to be below 90 degress to have $w^T x^{(i)} \geq 0$ 

Since the direction of $w$ is normal to the decision boundry, In the case of miss classification, if we add the misclassified vector $x^{(i)}$ to the weights vector, we have the effect of rotating the decision boundry in the direction of the missclassified sample.

![[Perceptron.png]]
