----
#LinearAlgebra 

***Overdetermined*** : more equations than needed to solve a linear combination, e.g:

$$\begin{bmatrix}
a_1 \quad a_2 \\
b_1 \quad b_2 \\
c_1 \quad c_2
\end{bmatrix}
\begin{bmatrix}
X \\
Y 
\end{bmatrix}
=
\begin{bmatrix}
a_3\\
b_3\\
c_3
\end{bmatrix}$$
such system corresponds to 3 equations of 2 variables, and soving systens like this may lead to the folowing cases:

![[OD-case1.jpg]]  ![[OD-case2.jpg]]  ![[OD-case3.jpg]]

- 1: Non-intersecting lines : no solution
- 2: Multple local solutions, no global solution for the system
- 3: Exists a unique solution for all equation

