# FCIG: Bergman–BLS Response Reconstruction

**Status:** exact Slater response + Kähler-angle gate + \(L^2\)/Quillen firewall

**Date:** 2026-09-12

**Depends on:** [BLS position transport](bls-position-transport.md), [Hermitian Born–Fisher completion](hermitian-born-fisher.md), [antisymmetric-response selector](antisymmetric-response-chirality-selector.md).

> **Claim policy.** Quantum geometric tensors, Berry/Chern curvature, and determinant connections are established. The FCIG result is their typed merger with the transported Bergman DPP. Probability-only phase recovery and equality of the \(L^2\) and Quillen connections are not claimed.

Citation audit: [bergman–BLS response audit](bergman-bls-response-reconstruction-citation-audit.md).

---

## 0. Result

Let \(B\) be a real surface and \([\Psi_q]:B\to\mathbb P(\mathscr F_q)\) the normalized Slater ray of

\[
\mathscr H_{q,b}=H^0(X_b,K_{X_b}^q).
\]

Using the ambient BLS connection, define

\[
Q_q(X,Y)=\langle D_X^\perp\Psi_q,D_Y^\perp\Psi_q\rangle,
\quad
g_q=\operatorname{Re}Q_q,
\quad
\Omega_q=2\operatorname{Im}Q_q.
\tag{0.1}
\]

Then \(g_q\) is the Plücker/Fubini–Study metric and, after fixing the simultaneous Berry/Chern sign convention,

\[
\boxed{\Omega_q=iF_{\det\mathscr H_q}^{L^2}.}
\tag{0.2}
\]

If \(g_q>0\) and \(\Omega_q\ne0\), the response theorem constructs

\[
\boxed{
J_q=
\frac{g_q^{-1}\Omega_q}
{\sqrt{-\tfrac12\operatorname{tr}((g_q^{-1}\Omega_q)^2)}}.
}
\tag{0.3}
\]

For the projectively holomorphic family, \(\Omega_q=2\omega_{g_q}\), so this recovers the Teichmüller complex structure. Together with the transported Bergman-DPP identity,

\[
\boxed{
Q_q=
\frac14\bigl(I_q^{KE}+J^*I_q^{KE}\bigr)
+\frac{i}{2}\Omega_q.
}
\tag{0.4}
\]

Symmetric Fisher response and antisymmetric Berry response are therefore two parts of one Slater quantum geometric tensor.

---

## 1. Determinant-line response

Write

\[
D_X^\perp\Psi_q
=(1-|\Psi_q\rangle\langle\Psi_q|)D_X\Psi_q.
\tag{1.1}
\]

\(Q_q\) is gauge invariant under \(\Psi_q\mapsto e^{i\chi}\Psi_q\), while Hermitian symmetry makes its imaginary part alternating.

### Proposition 1.1

\(\Omega_q\) is the real curvature of the induced unitary connection on

\[
L_q^{\rm Sl}\cong\det\mathscr H_q,
\]

up to the declared convention, and

\[
F_{\det\mathscr H_q}^{L^2}
=\operatorname{Tr}F_{\mathscr H_q}^{L^2}.
\tag{1.2}
\]

#### Proof

The projected connection of a normalized ray has local one-form proportional to \(\langle\Psi_q,D\Psi_q\rangle\). Exterior differentiation and antisymmetrization remove the vertical gauge term and give twice the imaginary part of the horizontal inner product. Exterior powers identify the Slater line with the determinant line, whose curvature is the trace curvature. \(\square\)

\[
\boxed{\text{Fisher measures distinguishability; Berry measures oriented phase circulation.}}
\]

---

## 2. Kähler-angle gate

Positivity of \(Q_q\) implies

\[
\boxed{
|\Omega_q(X,Y)|
\le
2\sqrt{g_q(X,X)g_q(Y,Y)-g_q(X,Y)^2}.
}
\tag{2.1}
\]

Define the absolute Kähler-angle ratio

\[
|\kappa_q|
=
\frac{|\Omega_q(X,Y)|}
{2|\operatorname{vol}_{g_q}(X,Y)|}
\le1.
\tag{2.2}
\]

- \(|\kappa_q|=1\): the ray tangent plane is complex and the Kähler relation is saturated.
- \(0<|\kappa_q|<1\): response orients the surface but is not its FS area.
- \(\kappa_q=0\): the family is Berry-isotropic and cannot select chirality.

The BLS determinant ray is projectively holomorphic:

\[
D_{JX}^\perp\Psi_q=iD_X^\perp\Psi_q.
\tag{2.3}
\]

Hence it saturates (2.1), and the selector from \((g_q,\Omega_q)\) equals the supplied moduli \(J\). This is a reconstruction theorem, not yet an orientation-free genesis theorem: (2.3) already uses \(J\).

---

## 3. Probability and phase

The BLS transport theorem gives

\[
g_q(X,Y)
=
\frac14\left[I_q^{KE}(X,Y)+I_q^{KE}(JX,JY)\right].
\tag{3.1}
\]

The antisymmetric part is instead phase holonomy:

\[
\operatorname{Hol}_{\gamma}(L_q^{\rm Sl})
=
\exp\!\left(i\oint_\gamma\mathcal A_q\right),
\qquad d\mathcal A_q=\Omega_q.
\tag{3.2}
\]

Ordinary Bergman-DPP probabilities determine (3.1), not (3.2). Phase-changing lifts can preserve the Born density. Probability alone still cannot select chirality; the BLS connection is essential extra data.

---

## 4. Hyperbolic asymptotic and integrality

The existing BLS calculation gives

\[
g_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1).
\tag{4.1}
\]

Projective holomorphicity therefore gives

\[
\boxed{
\Omega_q
=
\frac{q-1}{2\pi}\omega_{\rm WP}+O(1),
}
\tag{4.2}
\]

with the same WP and Berry conventions. Hence \(\Omega_q\) is nonzero for sufficiently large \(q\) on compact positive-WP loci. Integrality concerns the exact curvature rather than its truncated leading term:

\[
\boxed{
\left[\frac{\Omega_q}{2\pi}\right]
=c_1(L_q^{\rm Sl})
}
\tag{4.3}
\]

after matching conventions.

---

## 5. \(L^2\) versus Quillen

The Berry line carries the finite-dimensional \(L^2\) determinant metric. The Quillen metric also contains analytic torsion. Where the underlying determinant-of-cohomology line is identified,

\[
\boxed{
F_q^Q
=
F_q^{L^2}-\partial\bar\partial\log\tau_q^2,
}
\tag{5.1}
\]

with sign depending on the definition of \(\tau_q\). Thus the connections need not coincide. Wan–Zhang asymptotics used elsewhere in FCIG make the torsion-curvature correction lower order in the relevant high-power curve regime; they do not give exact connection equality.

Even curvature equality leaves the flat ambiguity

\[
H^1(B;U(1)).
\tag{5.2}
\]

The final comparison must be made in differential cohomology, not merely de Rham cohomology.

---

## 6. Gate ledger

- **BBR-A — PASS:** the BLS Slater QGT supplies \(g_q\) and \(\Omega_q\) simultaneously.
- **BBR-B — PASS:** \(\Omega_q\) is the \(L^2\) determinant/Slater curvature, hence its exact class is integral.
- **BBR-C — PASS:** projective holomorphicity saturates the Kähler-angle bound and reconstructs \(J\).
- **BBR-D — PASS (asymptotic):** response is nondegenerate for large \(q\) on compact positive-WP loci.
- **BBR-E — NO-GO:** Bergman-DPP probabilities alone do not determine Berry holonomy.
- **BBR-F — NO-GO:** projective holomorphicity reconstructs a supplied \(J\); it does not generate its sign orientation-free.
- **BBR-G — OPEN:** construct an orientation-free dynamical protocol for the response sign.
- **BBR-H — OPEN:** compare the \(L^2\) Berry and Quillen differential characters, including torsion and flat holonomy.

\[
\boxed{
\text{Fisher is the metric shadow; Berry is the oriented shadow; the Slater ray is their common source.}
}
\]

---

## References

- [PV80] J. P. Provost and G. Vallée, “Riemannian Structure on Manifolds of Quantum States,” *Communications in Mathematical Physics* 76 (1980), 289–301.
- [Qui85] D. Quillen, “Determinants of Cauchy–Riemann Operators over a Riemann Surface,” *Functional Analysis and Its Applications* 19 (1985), 31–34.
- [BGS88] J.-M. Bismut, H. Gillet and C. Soulé, “Analytic Torsion and Holomorphic Determinant Bundles III,” *Communications in Mathematical Physics* 115 (1988), 301–351.
- [WZ21] X. Wan and G. Zhang, high-power \(L^2\)/Quillen curvature comparison, as audited in the companion FCIG notes.
- [Var24] D. Varolin, BLS fields and Chern connections, as audited in the BLS transport note.
