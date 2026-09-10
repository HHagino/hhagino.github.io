# BLS Transport — Research Interpretation

The transport calculation changes the FCIG information-closure question in a useful way.

The moving-fiber ambiguity is not removed by declaring a Bergman projection to be fixed. Instead, one works one level higher: the ambient \(L^2\) position measurement is transported geometrically, while the moving holomorphic subspace carries a nontrivial second fundamental form. Compression back to the Bergman space then produces an exact defect controlled by that same second fundamental form.

Thus the geometry has the schematic form

\[
\boxed{
\begin{array}{ccc}
\text{ambient position measurement} & \xrightarrow{\rm BLS/KE} & \text{parallel} \\
\downarrow\text{compress} && \downarrow \\
\text{Bergman/Toeplitz measurement} & \xrightarrow{} & \text{defect }\mathbb B \\
&& \downarrow \\
&& \operatorname{Tr}(\mathbb B^*\mathbb B)=g_{\rm Pl}
\end{array}}
\]

For the Slater state the actual Born position measurement occurs before this compression, in the ambient antisymmetric many-body space. This is why the DPP Fisher construction can remain covariant even though the compressed one-particle Toeplitz observable is not parallel.

The main asymptotic statement is therefore not “classical Fisher equals the full Quillen curvature.” It is the filtered statement

\[
\boxed{
I_{HBF,q}^{KE}
\sim
\mathfrak K_q
\sim
\frac{q-1}{4\pi}G_{WP},
}
\]

with the first quantity coming from a Born probability law, the second from the intrinsic Kodaira--Spencer resolvent response, and the common limit from moduli geometry. The full direct-image/Quillen curvature retains additional sectors and different leading orders.

This is the current FCIG information-geometry target for publication-level verification.