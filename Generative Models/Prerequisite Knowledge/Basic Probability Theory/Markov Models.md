----
#ProbabilityTheory 

Markov model is designed on the assumption:

**The past is independent of the future given the present**

Or, in the [[Time Series]] data of $x_1,...,x_n$ , the above hypothesis can also be represented as  the following formula:
$$p(x_{t-1},x_{t+1}|x_t) = p(x_{t}|x_{t-1})p(x_{t+1}|x_t)$$
And if we want to get the [[Joint Distribution]] of all moments, we can write:
$$p(x_1,...,x_n) = p(x_1)\prod _{t=2} ^n p(x_t|x_{t-1})$$
You can get the probability distrib of the next state just from the current state, as:
$$p(x_{t+1}) = \sum _{x_t} p(x_t)p(x_{t+1}|x_t)$$
- where the sum is over all possible cases of $x_t$, since we are solving for the marginal distribution

