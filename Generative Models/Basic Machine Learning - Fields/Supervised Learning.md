----
#BasicMachineLearning 

Supervised learning is a class of machine leanring problems that attempts to learn a functional relationship between the input features and target outputs. 

Supervised learning tasks have the following components:

- Input features, normally denoted as $x^{(i)}$ 
- Output or Target variable, normally denoted as $y^{(i)}$
- Training examples, includes input and correct target (label), normally represented in the form: $(x^{(i)}, y^{(i)})$ 
- Training set of size n : $\{(x^{(i)}, y^{(i)}) : i \in [1,n]\}$
- space of input features : $\mathcal{X}$ , space of output variables : $\mathcal{Y}$ 
- Hypothesis function : $h : \mathcal{X} \rightarrow \mathcal{Y}$  

Supervised learning is an iterative process of optimizing the hypothesis function such that the output of $h (x^{(i)})$ will be approaching $y^{(i)}$
