----
#StatisticalMechanics 

Gibbs Entropy is a special definition came from information theory. 

From [[Boltzmann Entropy]], we have the entropy for the system defined as:
$$S = k_B\log\Omega$$
However, not every state of $\Omega$ can be separated from each others from experiment measurements. 

Therefore we separate the [[Microstate]]s into $i$ batches each with $\Omega_i$ elements. Experiment measurements can tell whether the system is in one of the batches, but it cannot seperate individual states in the batches.

The probability of the system within a batch is:
$$P_i = \Omega_i/\Omega\quad S_i = k_B\log \Omega_i$$
Because we cannot seperate individual states from batches, $S_i$ cannot be measured.

Therefore, the entire unmeasurable part of the entropy can be written as:
$$S_U = \sum _{i} P_iS_i = k_B \sum_i p_i\log \Omega_i$$
If we need the entropy for the measurable sections of the system, we need to exclude this term out:
$$S_G = S-S_U = k_B\log\Omega - k_B \sum_i P_i\log \Omega_i$$
To simplify, we have:
$$S_G = k_B \sum _{i}P_i(\log\Omega-\log\Omega_i)$$
And since $\log\Omega - \log\Omega_i = -\log(\Omega/\Omega_i) = -\log P_i$ , the final definition for Gibbs entropy is:
$$S_G = -k_B \sum P_i \log P_i$$
