----
#BasicMachineLearning 

LASSO stands for: ***Least Absolute Shrinkage and Selection Operator***

The original design of LASSO is to have the absolute value of all regression coefficients (or parameters) to be below a fixed threshold (the meaning for absolute shrinkage). It uses L1 norm to forcely limit the complexity of the model. The problem looks like this:
$$\min _{\beta, \beta_0} \sum _{i=1}^N (y_i - \beta_0 - x_i^T\beta)^2
\quad s.t. \quad \sum _{j=1}^n|\beta_j| \leq t$$
- $y_i$ is the target output
- $\beta_0$ is the constant coefficient
- $\beta$ is the parameter set

In the vector notation, we have:
$$\min _{\beta_0, \beta} || y - \beta_0 - X\beta||_2^2 \quad s.t.\quad ||\beta_j||_1 \leq t$$
$\beta_0$ can be solved independently to be $\hat{\beta_0} = \bar{y} - \bar{x}^T\beta$ , with the problem being:
$$\min _{ \beta} || y - X\beta||_2^2 \quad s.t.\quad -||\beta_j||_1 \geq -t$$
We can apply a [[lagrange multiplier]] to the restraint, and form the lagrangian form:
$$\min _{ \beta} || y - X\beta||_2^2 - \lambda||\beta||$$
This form of problem is also referred as [[L1 Regularization]]
