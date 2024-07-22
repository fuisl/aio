# Matrix inverse example

Example in 1.5

$$
A = \left[
\begin{array}{cc}
-2 & 6 \\
8 & -4
\end{array}
\right]
$$

we observe that the determinant of $A$ is $det(A) = ad - bc = -40 \neq 0$ so $A$ is invertible.

$$
A^{-1} = \frac{1}{\text{det}(A)} \left[
\begin{array}{cc}
-4 & -6 \\
-8 & -2
\end{array}
\right]
$$

$$
A^{-1} = \frac{1}{-40} \left[
\begin{array}{cc}
-4 & -6 \\
-8 & -2
\end{array}
\right]
$$

$$
A^{-1} = \left[
\begin{array}{cc}
0.1 & 0.15 \\
0.2 & 0.05
\end{array}
\right]
$$

# Eigenvector example

Example 2.1
$$
A = \left[
\begin{array}{cc}
0.9 & 0.2 \\
0.1 & 0.8
\end{array}
\right]
$$

$$
\mathbf{A} \in \mathbb{R}^{2 \times 2}, \mathbf{I} \in \mathbb{R}^{2 \times 2}, \mathbf{v} \in \mathbb{R}^2
$$

Eigenvalues: $det(A - \lambda I) = 0$

$$
\left|
\begin{array}{cc}
0.9 - \lambda & 0.2 \\
0.1 & 0.8 - \lambda
\end{array}
\right| = 0
$$

$$
(0.9 - \lambda)(0.8 - \lambda) - 0.2 \times 0.1 = 0
$$

$$
\lambda^2 - 1.7\lambda + 0.62 = 0
$$

$$
\lambda = \frac{1.7 \pm \sqrt{1.7^2 - 4 \times 0.62}}{2}
$$

$$
\lambda = \frac{1.7 \pm \sqrt{-0.79}}{2}
$$

Eigenvecotrs: $(A - \lambda I)v = 0$

$$
\left[
\begin{array}{cc}
0.9 - \lambda & 0.2 \\
0.1 & 0.8 - \lambda
\end{array}
\right]
\left[
\begin{array}{c}
v_1 \\
v_2
\end{array}
\right] = 0
$$

Solve for $\lambda$: 