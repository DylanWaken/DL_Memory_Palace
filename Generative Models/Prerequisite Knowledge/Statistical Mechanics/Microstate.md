----
#StatisticalMechanics 

A **microstate** is a specific microscopic configuration of a thermodynamic system that the system may occupy with a certain probability in the course of its thermal fluctuations. 

In statistical mechanics, the macrostate (observed properties like entropy, energy...) is the sum over all microstates in the system multiplied by the probability of system in that specific configuration. 

Normally we represent the total amount of microstates in the system as $\Omega$ .

For all the thermodynamic variables in the system, the macrostate variables can be expressed as the expectation of all its microstates. For example, the internel energy of the system is represented by its microstates as:
$$U := \sum _{i=1} ^ \Omega p_iE_i$$
- $E_i$ is the energy of the system at that microstate

In [[The First Law of Thermodynamics]], we have the relationship defined as:
$$dU = \delta W + \delta Q$$
Then we expand with the quantom definition of work and heat as:
$$\delta W = \sum _{i=1} ^N p_idE_i \quad \delta Q = \sum _{i=1} ^N E_i dp_i$$
- The reason for this step is that, in quantom mechanics, the adiabatic theorem states that the internal energy of the system only changes due to a change of the system's energy levels.

