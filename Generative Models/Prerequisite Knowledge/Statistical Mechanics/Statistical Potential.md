-----
#StatisticalMechanics 

In the original [[Boltzmann Distribution]], we can measure the microstate probability directly from its energy as:
$$P_i = \frac{e^{-\beta E_i}}{Z} = \frac{e^{-E_i/k_BT}}{\sum_i ^Ne^{-E_i/k_BT}}$$
And in the properties, the ratio between the probabilities of two microstates can be calculated from:
$$\frac{p_i}{p_j} = e^{(E_i-E_j)/k_BT}$$
Here, note that we represent these ratio with a differnece in energy. 

A little tweak of the function will give us the energy from microstate probability as:
$$E_i = -k_BT\ln P_i-k_BT\ln Z$$

And therefore, we can reverse the function by defining the difference in energy through the ratio of microstate probabilities:
$$\Delta E = -k_BT \log \frac{P_i}{P_j}$$
- The $Z$ terms would cancel out in the division since the partition function would be exactly the same if these microstates are from the same system.

This quantity is defined as the **statistical potential** of microstate $x_i$ relative to $x_j$
