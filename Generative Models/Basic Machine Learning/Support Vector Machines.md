-----
#BasicMachineLearning 
> ***Problem Type***: [[Classification Problem]], [[Supervised Learning]]
> ***Solution Type***:  Iterative Solution
> *GIVEN:* input featurs $X \in \mathbb{R}^{n \times N}$ , labels $Y \in \mathbb{R}^N$ 
> SOLVE: parameters $w \in \mathbb{R}^{n}, b$ such that $\min_{w,b} \frac{1}{2} w^T w$ subject to  $y^{(i)} (w^Tx^{(i)} + b) \geq 1$ for $i \in [1, N]$ 
> ***Iterative Solution***: Multiple in existance  

Support vector machine (SVM) is the algorithm that search for the optimal boarder between the given classes. 

![[Svm_max_sep_hyperplane_with_margin.png]]
For linearly divisible binary classification problems, we can consider the optimal linear classifier to be the one that separates the two classes and to the hyperspace with the largest minimum interval of all samples plane.


