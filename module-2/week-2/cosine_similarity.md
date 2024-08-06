# Cosine similarity example

Example 3.1

$$
\mathbf{x} = \left[
\begin{array}{c}
1 \\
2 \\
3 \\
4
\end{array}
\right]
\mathbf{y} = \left[
\begin{array}{c}
1 \\
0 \\
3 \\
0
\end{array}
\right]
$$

$$
\mathbf{x} \in \mathbb{R}^4, \mathbf{y} \in \mathbb{R}^4
$$

$$
\mathbf{x} \cdot \mathbf{y} = 1 \times 1 + 2 \times 0 + 3 \times 3 + 4 \times 0 = 10
$$

$$
\|\mathbf{x}\| = \sqrt{1^2 + 2^2 + 3^2 + 4^2} = \sqrt{30}
$$

$$
\|\mathbf{y}\| = \sqrt{1^2 + 0^2 + 3^2 + 0^2} = \sqrt{10}
$$

$$
\cos(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\| \|\mathbf{y}\|} = \frac{10}{\sqrt{30} \times \sqrt{10}} = \frac{10}{\sqrt{300}} = \frac{10}{10\sqrt{3}} = \frac{1}{\sqrt{3}}
$$