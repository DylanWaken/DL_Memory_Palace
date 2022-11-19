----
#ProbabilityTheory
related knowledge : [[Conditional Probability]]

***Conditional Independence*** describes situations wherein an observation is irrelevant or redundant when evaluating the certainty of a hypothesis. in which:

$$P\left( A| B,C\right) = P\left( A| C\right)$$

where A is the hypothesis, and B, C are observations. In this case, the condition / obserbation B provides no contribution to the certainty of the hypothesis A.

In the form of [Joint Distributions](Joint%20Distribution.md), the same theorem can be rewritten as:

$$P\left( A,B| C\right) =P\left( A| C\right) P\left( B| C\right)$$

Conditonal Independence can be also happening between **random variables**. if random variable X and Y are conditionally independent given a third random variable Z if and only if "given any value of Z, the probability distribution of X is the same for all values of Y  and the probability distribution of Y is the same for all values of X"


## An visual example from Vikipedia:
----

Each cell represents a possible outcome. The events ![{\displaystyle \color {red}R}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9f01e253717901b8b00c959c34140b7305fa89ec), ![{\displaystyle \color {blue}B}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5cca068ce7654c7fecd8085bdbe7f3b72de5daa2) and ![{\displaystyle \color {gold}Y}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5a255a2578c3d9ba10e9b09bfe646669acf989be) are represented by the areas shaded red, blue and yellow respectively. The overlap between the events ![{\displaystyle \color {red}R}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9f01e253717901b8b00c959c34140b7305fa89ec) and ![{\displaystyle \color {blue}B}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5cca068ce7654c7fecd8085bdbe7f3b72de5daa2) is shaded purple.

![[StateExample.png]]

The purple shaded area is the [[joint distribution]] of R ann B. In both examples, R, B are conditionally independent by Y, because:

$$P\left( R,B| Y\right) =P\left( R| Y\right) \cdot P\left( B| Y\right)$$

However, they are not independent given the condition not Y, as

$$P\left( R,B| not Y\right) \neq P\left( R| notY\right) \cdot P\left( B| notY\right)$$


## Proof of conditional independence
----

Proof of the following equivalent definitions 

$P(A,B|C) = P(A|C)P(B|C)$

iff $\frac{P(A,B,C)}{P(C)} = (\frac{P(A,C)}{P(C)})(\frac{P(B,C)}{P(C)})$

iff $P(A,B,C) = \frac{P(A,C)P(B,C)}{P(C)}$

iff $\frac{P(A,B,C)}{P(B,C)} = \frac{P(A,C)}{P(C)}$

iff $P(A|B, C) = P(A|C)$

