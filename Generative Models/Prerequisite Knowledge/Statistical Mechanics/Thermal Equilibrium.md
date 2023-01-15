----
#StatisticalMechanics 

Thermal Equilibrium is the state of the isolated system, that given a long enough time, there exists no heat exchange throughout the components of the system.

**The thermal equilibrium of an isolated system is achieved when the entropy $S$ of the system is maximized.** 

## Proof

In the standard thermodynamic definition of [[Entropy]]:
$$S = \frac{Q}{T} \quad dS = \frac{\delta Q}{T}$$
Given two segments of the system with temperatures $T_H$ and $T_C$ . According to [[The Second Law of Thermodynamics]], there must be an exchange of heat between the segments, as:
$$T_H > T_C$$
Assume the same piece of heat $\delta Q$ is flowing from the hotter segment to the cooler segment. The net entropy decreased on the hotter segment is less than the entropy created on the cooler segment, as:
$$dS_H = \frac{\delta Q}{T_H}\quad dS_C = \frac{\delta Q}{T_C}\quad dS_H < dS_C$$
Therefore, the only way for the system to be at thermal equilibrium (no heat exchange between segments) is when the system reaches the **maximum entropy**. 

## Other Properties

For a statistical mechanic system with [[Boltzmann Entropy]], the maximum entropy or thermal equilibrium is reached when the system have the maximum amount of [[Microstate]]s, that is:
$$\max S = \max k_B \log \Omega$$
- Since $k_B$ is the boltzmann constant
