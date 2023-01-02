----
#StatisticalMechanics 

A **microstate** is a specific microscopic configuration of a thermodynamic system that the system may occupy with a certain probability in the course of its thermal fluctuations. 

In statistical mechanics, the macrostate (observed properties like entropy, energy...) is the sum over all microstates in the system multiplied by the probability of system in that specific configuration. 

Normally we represent the total amount of microstates in the system as $\Omega$ .

For all the thermodynamic variables in the system, the macrostate variables can be expressed as the expectation of all its microstates. For example, the internel energy of the system is represented by its microstates as:
$$U := \sum _{i=1} ^ \Omega p_iE_i$$
- $E_i$ is the energy of the system at that microstate

In normal cases, the energy $E_i$ for all microstates shoule be the same. (there are exceptions depending on specific setups)

In [[The First Law of Thermodynamics]], we have the relationship defined as:
$$dU = \delta W + \delta Q$$
Then we expand with the quantom definition of work and heat as:
$$\delta W = \sum _{i=1} ^N p_idE_i \quad \delta Q = \sum _{i=1} ^N E_i dp_i$$
- The reason for this step is that, in quantom mechanics, the adiabatic theorem states that the internal energy of the system only changes due to a change of the system's energy levels.

## Example of MicroState

Consider a system with $N$ particles that are identical from each-others. and k pieces of energy $k * \Delta E$.

With the law of energy conservation, the energy of the system $U = k * \Delta E$. The total energy of the system would be a constant.

Assume the system is in the following configuration that only one particle among the $N$ particles have all the energy, as:
$$E_1 = k * \Delta E, E_2 = 0,...,E_n = 0$$
This is a **Macrostate** of the system

Since the particles are identical to each other, the permutation of particles on the same energy level does not matter (undistinguishable Microstate)

There exists $N$ cases ($E_1$ or $E_2$ or ... or $E_n$) in which a specific partical takes all the energy, and therefore, the **Macrostate** discribed above would have $N$ **Microstates**, or $\Omega = N$

The number is calculated by $N!/(N-1)! = N$ 

In the general formula, our computation is done by:
$$\Omega = \frac{N!}{n_1!n_2!...n_i!}$$
- $N!$ is the total possible permutations of $N$ particles 
- $n_1!$ is the number of particles with the same energy level or $i$ th same $\Delta E$ (given the specific macrostate) 

