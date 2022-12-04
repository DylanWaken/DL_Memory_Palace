----
#StatisticalMechanics 

![[Heat_engine.png]]

In thermodynamics, we define a **heat engine** a device that converts heat to mechaical energy (work). The heat engine operates between 2 temperature reservoirs ($T_H$ and $T_L$). Heat is extracted from the high temperature tank to the low temperature tank. The total work output of a heat engine can be calculated as:
$$W = Q_H - Q_L$$
And there exists a reversed deivce called **Heat Pump**. It takes in mechanical energy (work) and converts it to heat, as it extract heat from lower tank and return it to the higher tank,  as:
$$Q_L + W = Q_H$$
There are few properties in this cycle:

- 1: **The Kelvin-Planck Statement** :  It is impossible to construct a device which operates on a cycle and produces no other effect than the transfer of heat from a single body in order to produce work. (a heat engine cannot produce work by transfering heat form a tank to itself)

- 2: **The Clausius Statement:**  It is impossible to construct a device which operates on a cycle and produces no other effect than the transfer of heat from a cooler body to a hotter body. (it is impossible for a heat engine to produce work by transfer heat from lower tank to higher tank)

## Carnot Theorem:

The carnot theorem is as follows:

 **No heat engine operating between two heat reservoirs can be more efficient than a reversible heat engine operating between the same two reservoirs.**

A reversable engine stands for the heat engine that utilize all its work it prodced when reverted to work as a heat pump.
$$W_0 = Q_H - Q_L,\quad Q_L+W_1 = Q_H,\quad W_0 = W_1$$
The above theorem also proved 2 properties:

- 1: **All reversible heat engines operating between the same two heat reservoirs must have the same efficiency.**

- 2: **The efficiency of a reversible heat engine is a function only of the respective temperatures of the hot and cold reservoirs. It can be evaluated by replacing the ratio of heat transfers $Q_L$ and $Q_H$ by the ratio of temperatures $T_L$ and $T_H$ of the respective heat reservoirs.**

Where we can wrtie the thermal efficiency of a reversable heat engine $\eta$ as:
$$\eta = \frac{W}{Q_H} = \frac{Q_H-Q_L}{Q_H} = 1 - \frac{Q_L}{Q_H} = 1-\frac{T_L}{T_H}$$



