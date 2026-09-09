# FCIG Model XXVI — Charged Elliptic / Jacobi Spectral Determinant

> Citation policy: statements marked **Established** are attributed to the cited literature; statements marked **Derived here** are calculations in this note; **FCIG interpretation** labels the comparison with earlier FCIG models. The charged determinant is not identified with a Green--Schwarz term or with a gravitational equation.

## 1. Goal

Model XXV established a precise no-go: the gauge-blind elliptic threshold cannot see the Green--Schwarz gauge vectors or the charge/cocharacter lattice because no gauge-holonomy variable was present. The minimal typed extension is therefore a flat gauge connection on the elliptic fiber.

We take the area-one elliptic torus

\[
E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z),\qquad
\tau=u+iY,\quad Y>0,
\]

with

\[
ds^2=\frac{|dx+\tau dt|^2}{Y},\qquad (x,t)\sim(x+1,t)\sim(x,t+1).
\]

Let a field have integral charge \(q\) in the chosen normalization. Introduce flat holonomies \((\alpha,\beta)\in\mathbb R^2/\mathbb Z^2\) by

\[
\phi(x+1,t)=e^{2\pi i q\alpha}\phi(x,t),\qquad
\phi(x,t+1)=e^{-2\pi i q\beta}\phi(x,t),
\]

and define the elliptic holonomy coordinate

\[
\boxed{z=\alpha\tau+\beta.}
\]

This sign convention is chosen so that the shifted lattice is \(m\tau-n+qz\).

## 2. Exact charged spectrum — Derived here

The quasi-periodic Fourier modes are

\[
\phi_{m,n}(x,t)=
\exp\!\left(2\pi i[(m+q\alpha)x+(n-q\beta)t]\right),
\qquad (m,n)\in\mathbb Z^2.
\]

For the area-one metric,

\[
\boxed{
\lambda^{(q)}_{m,n}(\tau,z)
=\frac{4\pi^2}{Y}
|m\tau-n+qz|^2.
}
\]

Hence a zero mode occurs exactly on the divisor

\[
\boxed{qz\in\mathbb Z\tau+\mathbb Z.}
\]

Away from this divisor the twisted scalar Laplacian is invertible.

Large gauge transformations are elliptic translations

\[
z\mapsto z+r\tau+s,\qquad r,s\in\mathbb Z,
\]

and, for integral \(q\), simply relabel the Fourier lattice.

## 3. Zeta determinant from the second Kronecker limit formula

**Established.** The second Kronecker limit formula / Shintani regularized-product formula expresses the shifted two-dimensional Epstein product through the odd Jacobi theta function and the Dedekind eta function [KLF], [DLMF20]. In the present normalization, away from the zero divisor,

\[
\boxed{
D_q(\tau,z)
:=\det\Delta_{q,z}
=
\exp\!\left[-\frac{2\pi q^2(\operatorname{Im}z)^2}{Y}\right]
\left|\frac{\theta_1(qz\mid\tau)}{\eta(\tau)}\right|^2.
}
\]

The formula is the norm-square completion of the holomorphic theta/eta quotient. The Gaussian factor is essential; dropping it destroys elliptic/modular invariance.

### Zero-mode normalization check — Derived here

Use

\[
\theta_1(w\mid\tau)=2\pi\eta(\tau)^3w+O(w^3).
\]

As \(z\to0\),

\[
D_q(\tau,z)
=4\pi^2q^2|z|^2|\eta(\tau)|^4+O(|z|^4),
\]

while the small eigenvalue is

\[
\lambda^{(q)}_{0,0}
=\frac{4\pi^2q^2}{Y}|z|^2+O(|z|^3).
\]

Therefore

\[
\boxed{
\lim_{z\to0}
\frac{D_q(\tau,z)}{\lambda^{(q)}_{0,0}}
=Y|\eta(\tau)|^4
=\det{}'\Delta_\tau,
}
\]

recovering Model XIX with the same normalization.

## 4. Jacobi covariance

**Established background.** The theta and eta transformation laws are standard [DLMF20], [DLMF23]. The quotient

\[
\varphi_q(\tau,z)=\frac{\theta_1(qz\mid\tau)}{\eta(\tau)}
\]

has Jacobi weight zero and holomorphic index

\[
\boxed{m_q=\frac{q^2}{2}}
\]

(up to the standard multiplier system of \(\theta_1/\eta\)).

Under

\[
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb Z),
\qquad
(\tau,z)\mapsto
\left(\frac{a\tau+b}{c\tau+d},\frac{z}{c\tau+d}\right),
\]

and under elliptic translations \(z\mapsto z+r\tau+s\), the holomorphic factor acquires the usual Jacobi multiplier. The Gaussian completion cancels its absolute-value automorphy factor, giving

\[
\boxed{D_q(\gamma\tau,z/(c\tau+d))=D_q(\tau,z),}
\]

\[
\boxed{D_q(\tau,z+r\tau+s)=D_q(\tau,z).}
\]

Thus the real determinant descends to the universal elliptic curve with the appropriate flat-holonomy identifications.

## 5. Exact Jacobi curvature — Derived here

Away from the theta divisor, \(\log|\theta_1(qz|\tau)/\eta(\tau)|^2\) is pluriharmonic. Hence the entire Chern/Hessian response comes from the Gaussian completion.

Write

\[
v=\operatorname{Im}z.
\]

Then

\[
-\partial\bar\partial\log D_q
=\partial\bar\partial\left(\frac{2\pi q^2v^2}{Y}\right).
\]

A direct differentiation gives

\[
\boxed{
-\partial\bar\partial\log D_q
=
\frac{\pi q^2}{Y}
\left(dz-\frac{v}{Y}d\tau\right)
\wedge
\left(d\bar z-\frac{v}{Y}d\bar\tau\right).
}
\]

This is a rank-one semipositive Jacobi-invariant \((1,1)\)-form. At fixed \(\tau\),

\[
\boxed{
-\partial_z\partial_{\bar z}\log D_q
=\frac{\pi q^2}{Y}.
}
\]

The spectral geometry therefore reads the quadratic charge moment exactly.

## 6. Many charges and representations

For independent charged species with determinant weights \(\nu_a\) and charges \(q_a\), logarithms add. The holomorphic Jacobi index and the fiberwise curvature are controlled by

\[
\boxed{
\mathcal Q_2=\sum_a\nu_a q_a^2.
}
\]

In particular,

\[
m_{\rm total}=\frac12\mathcal Q_2,
\qquad
-\partial_z\partial_{\bar z}\log D_{\rm total}
=\frac{\pi}{Y}\mathcal Q_2.
\]

For a nonabelian Cartan holonomy \(z\), a weight \(\rho\) replaces \(qz\) by \(\rho(z)\), and the quadratic tensor becomes

\[
\sum_{\rho\in R}\rho\otimes\rho,
\]

which is the same representation-theoretic quadratic trace that defines the Dynkin index, once conventions are fixed.

## 7. First genuine common microscopic invariant with Green--Schwarz data

**Established.** For a single six-dimensional \(U(1)\) factor, the local anomaly equations can be written [TT18]

\[
\boxed{
a\cdot\widetilde b
=-\frac16\sum_{q>0}x_q q^2,
\qquad
\widetilde b\cdot\widetilde b
=\frac13\sum_{q>0}x_q q^4.
}
\]

Thus the quadratic charge moment appearing in the Jacobi spectral curvature is also the microscopic moment entering \(a\cdot\widetilde b\):

\[
\boxed{
\sum_q x_q q^2
\quad\text{appears in both the charged spectral geometry and the GS anomaly data.}
}
\]

This is the first typed bridge in the FCIG sequence where gauge-charge data enter both sides through the same microscopic invariant.

However,

\[
\boxed{
\text{common microscopic moment}
\neq
\text{equality of observables}.
}
\]

The determinant curvature is a metric on holonomy/moduli space; \(a\cdot\widetilde b\) is an anomaly-lattice pairing. Their coefficients, signs, determinant weights and field-content conventions differ unless a complete microscopic multiplet calculation is supplied.

The quartic moment

\[
\sum_qx_qq^4
\]

entering \(\widetilde b^2\) is **not** determined by the quadratic Jacobi curvature. It should first appear in higher holonomy response (for example fourth derivatives / four-point data), not be inferred from the two-derivative metric.

## 8. Global gauge-group / cocharacter sensitivity

Model XXV found that the gauge-blind threshold could not see the global gauge group. The charged determinant does.

The allowed holonomy space is the Cartan algebra modulo the cocharacter lattice. Equivalently, a shift \(z\mapsto z+\ell_1\tau+\ell_2\) is a gauge identification precisely when every allowed weight evaluates integrally on the corresponding cocharacter. Therefore changing the global form of the gauge group can change the allowed Jacobi translation lattice even when the Lie algebra is unchanged [MMP18].

This is a genuine new spectral channel for global gauge data.

## 9. What is established and what is new

**Established:**

- second Kronecker limit formula / regularized shifted lattice product [KLF];
- Jacobi theta and Dedekind eta transformation laws [DLMF20], [DLMF23];
- determinant-line / zeta-determinant framework [RS], [Qui85];
- 6d abelian anomaly relations involving \(\sum q^2\) and \(\sum q^4\) [TT18];
- global gauge/cocharacter quantization data in 6d anomaly coefficients [MMP18].

**Derived here:**

- the exact spectrum in the Model-XIX area-one convention;
- zero-mode matching to \(Y|\eta|^4\);
- the exact Jacobi curvature matrix
  \(\frac{\pi q^2}{Y}|dz-(\operatorname{Im}z/Y)d\tau|^2\);
- the explicit identification of the quadratic spectral charge moment with the same microscopic \(\sum x_qq^2\) that enters the 6d abelian anomaly equation, while keeping the observables distinct.

## 10. Scope and next gate

This model treats a flat background gauge connection and the parity-even determinant magnitude of charged Laplace-type modes. It does not yet include the full charged vector/hyper/tensor multiplet spin structure, background gauge curvature, nonabelian Weyl quotients, chiral determinant phases, or quartic holonomy response.

The next controlled task is therefore:

\[
\boxed{
\text{full charged multiplet determinant}
\longrightarrow
\text{Jacobi index matrix}
\longrightarrow
(a\cdot b_i,\ b_i\cdot b_j)\text{ comparison}
}
\]

with the quartic charge moment treated independently.

No anomaly cancellation, UV completion, Einstein equation or horizon law follows from the charged determinant alone.

## References

See `charged-jacobi.bib`.
