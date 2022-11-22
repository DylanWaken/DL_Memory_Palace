-----
#BasicMachineLearning 

The traditional [[Gradient Descent]] would modify all parameters at the same time to travel in the fastest downhill direction through gradients. 

Coordinate Descent is the approach to a optimization process that we modify the parameters one by one. In the objective functions that parameters are inter-dependent, this approach will be efficient in optimizing one parameter based on the values of other parameters.

For example, if we are looking at:
$$\min_\alpha W(\alpha_1,...,\alpha_n)$$
We will do:
$$\text{For} \quad i=1,...,n \quad\{ a_i=\arg \min_\hat{\alpha_i}W(\alpha_1,..,\hat\alpha_i,...,\alpha_n)\}$$
until the problem converges.

A graphic overview of the algorithm is:

![[CoordinateDescent.png]]