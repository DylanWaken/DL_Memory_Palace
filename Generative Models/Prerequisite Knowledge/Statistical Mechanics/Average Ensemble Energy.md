-----
#StatisticalMechanics 

Except from the direct definition in [[Microstate]], the [[Ensemble Average]] of energy can also be calculated from the following manner:
$$\langle E\rangle = k_BT^2 (\dfrac{\partial \log Z}{\partial T}) =  - \dfrac{\partial \log Z}{\partial \beta}$$
## Proof:

In the [[Canonical Ensemble]], we have the partition function defined as:
$$Z_C = e^{F/k_BT} = \sum_j \exp(-\frac{1}{k_BT} E_j)$$
And since we have the system energy equal to the sum of its microstates times probabilities, we have
$$\langle E\rangle = \sum _{j} E_jP_j \quad P_j=\frac{e^{-E_j/k_BT}}{Z}$$
Here, if we take the derivative of $\log Z$ with respect to [[temperature]] $T$ :
$$\dfrac{\partial \log Z}{\partial T} = \frac{1}{k_BT^2} \sum_j \frac{E_j e^{-E_j/k_BT}}{Z}$$
- Note: the summation term of the function is exactly the same as the definition for the [[Ensemble Average]] of the energy.

Therefor we have a conclusion:
$$\langle E \rangle = k_BT^2 (\dfrac{\partial \log Z}{\partial T})$$
Another approach is to take derivative of $\log Z$ with respect to $\beta$: 
$$\dfrac{\partial \log Z}{\partial \beta} = -\sum_j \frac{E_je^{-\beta E_j}}{Z}$$
And we have the conclusion:
$$\langle E \rangle = - \dfrac{\partial \log Z}{\partial \beta}$$
