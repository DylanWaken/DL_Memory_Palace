----
#StatisticalMechanics 

Statistical mechanics defines temperature based on a system's fundamental degrees of freedom.

Here we define temperature $T$ as:
$$\frac{1}{k_BT} = \frac{d\log \Omega}{dE}$$
- $k_B$ is the Boltzmann constant.

## Proof:

If we consider two systems that can transfer heat between each-others but are isolated from environment. The macrostate energy are $E_1$, $E_2$ that satisfies the conservation of total energy $E = E_1 + E_2$. 

Assume the [[Microstate]] count for both systems at each moment are $\Omega(E_1), \Omega(E_2)$ , then the total amont of microstates in the entire system is $\Omega(E_1)\Omega(E_2)$.

Since heat exchanging is allow between both systems, the systems will reach a heat equilibrium after a certain period of time. With the basic ideas of statistical mechanics, we have the following assumptions:

- 1: **Equal probabilities**: All independent microstates have equal probabilities.
- 2: **Continuity:** The change between microstates is a continuous process
- 3: **Ergodic Hypothesis:** given a long enough time, the system will iterate all its microstates with the duration the same for all the microstates.

These assumptions implies that the system should be reach heat equilibrium at the macrostate of maximum amount of microstates. 

To solve for the maximum point of microstates, we have the following equation:
$$\frac{d}{dE_1} \Omega_1(E_1)\Omega_2(E_2) = 0$$
Using chain rule to expand:
$$\frac{d\Omega_1(E_1)}{dE_1}\Omega_2(E_2) + \Omega_1(E_1)\frac{d\Omega_2(E_2)}{dE_2} \frac{dE_2}{dE_1} = 0$$
Since $E_1 + E_2 = E$ is constant, so $dE_1 = -dE_2$
$$\frac{1}{\Omega_1} \frac{d\Omega_1}{dE_1} - \frac{1}{\Omega_2} \frac{d\Omega_2}{dE_2} = 0$$
Which is the same as:
$$\frac{d \log \Omega_1}{dE_1} = \frac{d \log \Omega_2}{dE_2}$$
Because the systems at heat equilibrium have the same temperature, we define temperature upon this funtion:
$$\frac{1}{k_BT} = \frac{d\log \Omega}{dE}$$
