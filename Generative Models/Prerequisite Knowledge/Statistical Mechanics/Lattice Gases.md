-----
#StatisticalMechanics 

Lattice Gas is a theoritical model of statistical mechanics, with **non-interactive particles on a lattice** (grids). The model have constant temperature, volume and number of atoms.

The hamiltonian of this system is given as:
$$E = - \sum _{i=1} ^n s_i\mu H$$
- $E$ is the energy of a microstate, $n$ is number of atoms
- $\mu$ is the Magnetic moment, and $H$ is the magnetic field strength.
- $s_i$ is the states of spins, at two possible outcoms of $+1$ ot $-1$ 

This model is frequencly used in modeling spins of particles with respect to magnetic fields. In this model, the hamiltonian function have no relation between adjacent atoms.

The partition funciton of lattice gas is given as:
$$Z = 2^n\cosh^n (\beta\mu H) $$
And the relationship between energy and temperature is:
$$\langle E \rangle = -n\mu H\tanh(\beta\mu H)$$

## partition function:

 since each partical can have two possible spins, a new atom means the entire count of [[Microstate]]s would be multiplied by 2. And here when we plug this property into the canonical partition function ([[Canonical Ensemble]]), we would have:
 $$Z = \sum _{s_1=0} ^1 \sum _{s_2=0} ^1 ....\sum _{s_n=0} ^1\exp(\beta \sum _{i=1} ^n s_i\mu H)$$ Here we can convert the sum within the exponential as the product of exponentials:
 $$ \begin{align}
 &Z = \sum _{s_1=0} ^1 \sum _{s_2=0} ^1 ....\sum _{s_n=0} ^1 \prod _{i=1} ^n\exp(\beta  s_i\mu H)
 \\
 & = \sum_{s_1=0}^1 \exp(\beta  s_i\mu H)   \sum_{s_2=0}^1 \exp(\beta  s_i\mu H) ...  \sum_{s_0=n}^1 \exp(\beta  s_i\mu H) 
 \\
 &= [ \sum_{s_0=0}^1 \exp(\beta  s_i\mu H) ]^n  = [e^{+\beta\mu H} + e^{-\beta \mu H}]^n
 \\
 &=2^n\cosh^n (\beta\mu H) 
 \end{align}
 $$
 
## Average Energy:

In the [[Average Ensemble Energy]] section, we have the conclusion that 
$$\langle E\rangle =  - \dfrac{\partial \log Z}{\partial \beta}$$
Since our partition function is given as:
$$Z = 2^n\cosh^n (\beta\mu H) $$
Plug this definition into the above partial equation we have:
$$\langle E \rangle = - \frac{n \mu H \sinh(\beta\mu H)}{\cosh(\beta \mu H)} = -n\mu H\tanh(\beta\mu H)$$
This will give us the relationship between temperature and average energy.