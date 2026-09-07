# FCIG Explicit Model III: Higher-Dimensional Abelian Varieties and Hodge–Determinant Scaling

**Status:** worked generalization / v0.3 draft  
**Date:** 2026-09-08

> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are calculations carried out in this FCIG note. Statements marked **FCIG interpretation/conjecture** are not attributed to the cited literature.

The purpose of this note is to test whether the exact elliptic mechanism survives for principally polarized abelian varieties of arbitrary complex dimension.

The first result is affirmative at the level of the exact theta-state Gram determinant and local Hodge/determinant curvature.

---

## 1. Siegel-space family

Let

\[
\Omega=X+iY\in\mathfrak H_g,
\qquad
\Omega^T=\Omega,
\qquad
Y=\operatorname{Im}\Omega>0,
\]

and define the principally polarized complex torus

\[
\boxed{
A_\Omega
=
\mathbf C^g/(\mathbf Z^g+\Omega\mathbf Z^g).
}
\]

The description of principally polarized complex abelian varieties by period matrices in Siegel upper half-space and the associated theta theory are standard; see [Mum83; BL04; FC90].

Write points in the fundamental parallelepiped as

\[
z=x+\Omega t,
\qquad
x,t\in[0,1)^g.
\]

Use the normalized translation-invariant Kähler form

\[
\boxed{
\omega_\Omega
=
\frac{i}{2}
\sum_{a,b=1}^g
(Y^{-1})_{ab}
\,dz_a\wedge d\bar z_b.
}
\]

With this normalization,

\[
\frac{\omega_\Omega^g}{g!}
=
 dx_1\cdots dx_g\,dt_1\cdots dt_g
\]

on the chosen fundamental domain, so

\[
\int_{A_\Omega}\frac{\omega_\Omega^g}{g!}=1.
\]

The fiber metric is flat.

---

## 2. Level-\(k\) theta states

Let \(L\to A_\Omega\) denote the principal theta line. For

\[
\mathbf j\in(\mathbf Z/k\mathbf Z)^g
\]

choose a representative \(\mathbf j\in\{0,\ldots,k-1\}^g\), and define

\[
\boxed{
 s_{\mathbf j}^{(k)}(z,\Omega)
=
\sum_{n\in\mathbf Z^g}
\exp\!\left[
\pi i k
\left(n+\frac{\mathbf j}{k}\right)^T
\Omega
\left(n+\frac{\mathbf j}{k}\right)
+
2\pi i k
\left(n+\frac{\mathbf j}{k}\right)^Tz
\right].
}
\tag{2.1}
\]

**Established background.** These are the standard level-\(k\) theta functions for the principal polarization. They form a basis of \(H^0(A_\Omega,L^k)\); see [Mum83; BL04]. In particular,

\[
\boxed{
N_k
=
\dim H^0(A_\Omega,L^k)
=
k^g.
}
\tag{2.2}
\]

Thus the FCIG capacity entropy is

\[
\boxed{
S_k^{\mathrm{cap}}
=
g\log k.
}
\]

The terminology “capacity entropy” is FCIG terminology; the dimension formula is standard.

---

## 3. Hermitian metric

On the universal cover, use the translation-compatible metric

\[
\boxed{
\|f(z)\|_{h_k}^2
=
|f(z)|^2
\exp\!\left[
-2\pi k
(\operatorname{Im}z)^T
Y^{-1}
(\operatorname{Im}z)
\right].
}
\tag{3.1}
\]

Since

\[
\operatorname{Im}z=Yt,
\]

the Gaussian factor is

\[
\exp(-2\pi k\,t^TYt).
\]

This is the higher-dimensional analogue of the metric used in Explicit Model I.

---

## 4. Exact \(L^2\) Gram matrix

Define

\[
\langle s,r\rangle_{L^2}
=
\int_{A_\Omega}
 h_k(s,r)
\frac{\omega_\Omega^g}{g!}.
\]

### Proposition 4.1 — exact orthogonality and norm

For

\[
\mathbf j,\mathbf m\in(\mathbf Z/k\mathbf Z)^g,
\]

one has

\[
\boxed{
\left\langle
s_{\mathbf j}^{(k)},
 s_{\mathbf m}^{(k)}
\right\rangle_{L^2}
=
\delta_{\mathbf j\mathbf m}
\det(2kY)^{-1/2}.
}
\tag{4.1}
\]

**Derived here.** The exact normalization in (4.1) is obtained below for the conventions of this note. It is not being attributed to [Mum83] or [BL04].

### Proof

Put

\[
q_n=n+\frac{\mathbf j}{k}.
\]

The \(x\)-dependence of a product of two theta terms is

\[
\exp\left[
2\pi i
\left(k(n-m)+\mathbf j-\mathbf m\right)^Tx
\right].
\]

Integrating over \(x\in[0,1)^g\) forces

\[
k(n-m)+\mathbf j-\mathbf m=0.
\]

For representatives \(\mathbf j,\mathbf m\in\{0,\ldots,k-1\}^g\), this implies

\[
\mathbf j=\mathbf m,
\qquad
n=m.
\]

Hence all off-diagonal theta labels are orthogonal.

For a diagonal term, combining the theta modulus with the Hermitian Gaussian gives

\[
\exp\!\left[
-2\pi k(q_n+t)^TY(q_n+t)
\right].
\]

Therefore

\[
\begin{aligned}
\|s_{\mathbf j}^{(k)}\|_{L^2}^2
&=
\sum_{n\in\mathbf Z^g}
\int_{[0,1)^g}
\exp\!\left[
-2\pi k(q_n+t)^TY(q_n+t)
\right]dt\\[1mm]
&=
\int_{\mathbf R^g}
\exp(-2\pi k\,u^TYu)\,du.
\end{aligned}
\]

Using

\[
\int_{\mathbf R^g}e^{-\pi u^TAu}\,du
=(\det A)^{-1/2}
\]

for positive-definite \(A\), with \(A=2kY\), gives

\[
\boxed{
\|s_{\mathbf j}^{(k)}\|_{L^2}^2
=
\det(2kY)^{-1/2}.
}
\]

This proves (4.1). \(\square\)

The orthonormal basis is therefore

\[
\boxed{
\widehat s_{\mathbf j}^{(k)}
=
\det(2kY)^{1/4}
 s_{\mathbf j}^{(k)}.
}
\tag{4.2}
\]

---

## 5. Determinant of the theta-state bundle

Let

\[
\mathcal H_k\to\mathfrak H_g
\]

be the rank-\(N_k=k^g\) theta-state bundle, locally framed by all

\[
s_{\mathbf j}^{(k)}.
\]

Let

\[
\Sigma_{g,k}
=
\bigwedge_{\mathbf j\in(\mathbf Z/k\mathbf Z)^g}
 s_{\mathbf j}^{(k)}
\]

be the determinant frame.

Since the Gram matrix is scalar diagonal,

\[
G_{g,k}
=
\det(2kY)^{-1/2}I_{k^g},
\]

we obtain

\[
\boxed{
\|\Sigma_{g,k}\|^2
=
\det(2kY)^{-k^g/2}.
}
\tag{5.1}
\]

Equivalently,

\[
\log\|\Sigma_{g,k}\|^2
=
-\frac{k^g}{2}\log\det Y
-
\frac{gk^g}{2}\log(2k).
\]

---

## 6. Hodge line over Siegel space

Let

\[
\mathbb E
=
\pi_*\Omega^1_{\mathcal A/\mathfrak H_g}
\]

be the rank-\(g\) Hodge bundle and

\[
\lambda_H=\det\mathbb E.
\]

The Hodge bundle and its determinant are standard objects on the moduli space of principally polarized abelian varieties; see [FC90]. Over Siegel space a holomorphic frame is

\[
\eta
=
 dz_1\wedge\cdots\wedge dz_g.
\]

Up to a positive convention-dependent constant, the natural Hodge metric satisfies

\[
\boxed{
\|\eta\|_H^2
\propto
\det Y.
}
\tag{6.1}
\]

Hence the constant drops out of the Chern curvature and

\[
\boxed{
F_{\lambda_H}
=
-\partial\bar\partial\log\det Y.
}
\tag{6.2}
\]

The relation of the Hodge bundle to Siegel modular forms is standard in the moduli theory; see [FC90].

---

## 7. Exact Hodge–determinant scaling

Using (5.1),

\[
\begin{aligned}
F_{\det\mathcal H_k}
&=
-\partial\bar\partial
\log\|\Sigma_{g,k}\|^2\\
&=
\frac{k^g}{2}
\partial\bar\partial\log\det Y.
\end{aligned}
\]

Together with (6.2):

### Theorem 7.1 — FCIG abelian determinant identity

Under the metric and volume conventions of this note,

\[
\boxed{
F_{\det\mathcal H_k}
=
-\frac{k^g}{2}F_{\lambda_H}.
}
\tag{7.1}
\]

Since

\[
N_k=\operatorname{rank}\mathcal H_k=k^g,
\]

this can be written as

\[
\boxed{
F_{\det\mathcal H_k}
=
-\frac{N_k}{2}F_{\lambda_H}.
}
\tag{7.2}
\]

**Derived here.** Equation (7.1) follows from the exact Gram determinant in this note. The general theories of theta bundles, Hodge bundles, and determinant lines provide context; they are not cited as the source of this normalization-dependent coefficient.

For \(g=1\), (7.1) reduces exactly to the elliptic identity

\[
F_{\det\mathcal H_k}
=-\frac{k}{2}F_{\lambda_H}.
\]

Thus the elliptic coefficient is not isolated: in this normalization it generalizes as **one half of the state-bundle rank**.

This is the first structural extension beyond the elliptic toy model.

---

## 8. Corrected flat line

If \(N_k=k^g\) is even, define

\[
\boxed{
\mathscr A_{g,k}
=
\det\mathcal H_k
\otimes
\lambda_H^{N_k/2}.
}
\tag{8.1}
\]

Then

\[
\boxed{
F_{\mathscr A_{g,k}}=0.
}
\tag{8.2}
\]

If \(k\) is odd, then \(N_k=k^g\) is odd and the exponent \(N_k/2\) requires a square-root/metaplectic refinement. This is the direct higher-dimensional analogue of the parity phenomenon in Explicit Model II.

**FCIG interpretation.** The locally flat corrected line is a candidate carrier of a purely global modular anomaly sector. Equation (8.2) alone does not prove nontrivial holonomy; global descent and the finite Weil multiplier must be computed separately.

---

## 9. What has generalized successfully

The elliptic mechanism now has the following dimension-\(g\) form:

\[
\boxed{
\begin{aligned}
\operatorname{rank}\mathcal H_k
&=k^g,\\[1mm]
\|s_{\mathbf j}^{(k)}\|^2
&=\det(2kY)^{-1/2},\\[1mm]
F_{\det\mathcal H_k}
&=-\frac{k^g}{2}F_{\lambda_H},\\[1mm]
F_{\mathscr A_{g,k}}
&=0
\quad\text{(after the appropriate Hodge/metaplectic correction).}
\end{aligned}
}
\]

This passes the first functoriality test:

\[
\boxed{
\text{elliptic determinant/Hodge cancellation}
\longrightarrow
\text{principally polarized abelian varieties}.
}
\]

No claim of literature novelty is made here. The statement is that the FCIG normalization and interpretation extend coherently and admit an exact derivation.

---

## 10. Numerical cross-check

A direct truncated theta-sum integration was performed for a non-diagonal \(g=2\) period matrix with positive-definite imaginary part. For \(k=2\), the predicted diagonal norm

\[
\det(2kY)^{-1/2}
\]

agreed with the numerical integral to the displayed floating-point precision, while an off-diagonal theta-label inner product was numerically zero.

A reproducible verifier is included as `abelian-gram.py`.

This check is evidence for the convention bookkeeping; Proposition 4.1 is proved analytically above.

---

## 11. Next gate: multidimensional Bergman lattice formula

Because the fiber metric remains flat, every local positive-power curvature coefficient in the usual Bergman expansion vanishes.

The next target is therefore an exact multivariate Poisson-resummed expression of the schematic form

\[
\boxed{
B_{g,k}(z;\Omega)
=
k^g
+
\text{exponentially small Fourier modes of the period lattice}.
}
\]

The quantity controlling suppression should be a shortest-vector invariant of the normalized period lattice. The precise formula, phase convention, and uniformity near the boundary of Siegel space remain to be derived.

**Open problem.** Determine the exact dimension-\(g\) lattice formula and prove a bound

\[
B_{g,k}
=
k^g
\left[1+O_\Omega(e^{-c(\Omega)k})\right]
\]

on compact subsets away from degeneration.

---

## 12. Next gate: finite Weil transport

The modular group is now

\[
\operatorname{Sp}_{2g}(\mathbf Z),
\]

acting on Siegel space by fractional linear transformations. The associated theta states carry the standard finite Weil/metaplectic structure; see [Mum83] for theta theory and the general Weil framework referenced in the earlier FCIG modular note.

The FCIG task is convention-sensitive and therefore remains explicit:

1. choose a theta level structure;
2. write the finite generators acting on \((\mathbf Z/k\mathbf Z)^g\);
3. compute the determinant character;
4. combine it with the Hodge automorphy factor;
5. decide whether \(\mathscr A_{g,k}\) is globally nontrivial despite (8.2).

Passing this gate would establish the higher-dimensional version of

\[
\boxed{
\text{local curvature cancellation}
+
\text{residual global metaplectic holonomy}.
}
\]

---

## 13. Research consequence

The coefficient in the determinant/Hodge relation has become

\[
\frac{k^g}{2}
=
\frac12\dim H^0(A_\Omega,L^k).
\]

This suggests a sharper FCIG principle to test in broader families:

\[
\boxed{
\textbf{the local determinant response may scale with one half of the quantum-state rank.}
}
\]

At present this is **not** proposed as a universal theorem. It is an exact feature of the elliptic model and the principally polarized abelian model under the present metric conventions.

The next curved test at genus \(g\ge2\) will determine whether this scaling is special to flat abelian geometry.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[Mum83]** D. Mumford, *Tata Lectures on Theta I*, Birkhäuser (1983).
- **[BL04]** C. Birkenhake & H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer (2004).
- **[FC90]** G. Faltings & C.-L. Chai, *Degeneration of Abelian Varieties*, Ergebnisse der Mathematik 22, Springer (1990).
