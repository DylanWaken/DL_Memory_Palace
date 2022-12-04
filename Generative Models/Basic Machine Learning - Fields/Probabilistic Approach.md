-----------
#BasicMachineLearning 

Probabilistic machine learning is a general term for a large class of machine learning methods. They model the distribution of variables by means of probabilistic models with parameters. 

- Frequency learning approach wants to solve for parameter point estimates and make predictions using some optimal parameter. 

- The Bayesian approach wants to find the distribution of parameters (i.e., Bayesian inference) and on this basis derive a generative, discriminative or predictive model for the sample (i.e. Bayesian decision making).

What they have in common is that they use probabilistic models with parameters.

##  The Basic Tasks

For porbabilistic machine learning, there ae 3 primary categories:

- **Parameter estimation (point estimation)**: GIven the dataset $X$ amd the probabilistic model of unknown parameter $\theta$,  solve for the optimized parameter $\hat \theta$. 

- **Distribution Estimation:** Given the dataset $X$ and the probabilistic model of unknown parameter $\theta$, solve for the posterior distribution $p(\theta|X)$ of the parameter given the conditions of the dataset.

- **Distribution Sampling:** Given the parameter $\theta$ and model $p(X|\theta)$, solve for set of data samples $x^{(1)}, x^{(2)},...,x^{(N)}$ subjecting to the distribution

