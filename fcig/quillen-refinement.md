# FCIG Explicit Model V: Quillen Refinement, Analytic Torsion, and Spectral–Geodesic Separation

**Status:** v0.5 worked determinant-metric refinement  
**Date:** 2026-09-09

> **Citation policy.** Bracketed keys cite established results only. Statements marked **Derived here** are deductions in the conventions fixed below. Statements marked **FCIG interpretation** are not attributed to the cited literature.

This note refines the determinant sector of the compact hyperbolic model. The purpose is to separate three objects that were deliberately kept distinct in v0.4:

1. the ordinary \(L^2\) metric on the determinant of cohomology;
2. the Quillen metric on the same holomorphic line;
3. the analytic-torsion / Selberg-spectral factor relating the two.

The ambient family is a smooth family of compact genus-\(g\ge2\) hyperbolic curves

\[
\pi:\mathcal X\to B,
\]

with relative canonical line \(K_{\mathcal X/B}\). For \(k\ge2\), set

\[
\boxed{
\lambda_k
=\det R\pi_*K_{\mathcal X/B}^k.
}
\tag{0.1}
\]

Since \(H^1(X,K_X^k)=0\) for \(k\ge2\), the fiber is simply

\[
(\lambda_k)_X=\det H^0(X,K_X^k).
\]

The determinant-of-cohomology construction is standard; Quillen's original metric construction and the family curvature theorem are due to Quillen and Bismut–Gillet–Soulé [Qui85; BGS88].

---

## 1. The ordinary \(L^2\) determinant metric

Equip each hyperbolic fiber \(X\) with its constant-curvature metric and \(K_X^k\) with the induced Hermitian metric. Harmonic representatives give \(H^0(X,K_X^k)\) an \(L^2\) inner product.

If

\[
s_1,\ldots,s_N
\]

is a local holomorphic frame of \(H^0(X,K_X^k)\), with Gram matrix

\[
G_{ab}=\langle s_a,s_b\rangle_{L^2},
\]

then the determinant frame

\[
\Sigma=s_1\wedge\cdots\wedge s_N
\]

has squared norm

\[
\boxed{
 h_{L^2}(\Sigma,\Sigma)=\det G.
}
\tag{1.1}
\]

This is the direct curved analogue of the elementary determinant metrics used in the elliptic and ppav models.

---

## 2. Holomorphic analytic torsion and the Quillen metric

Let

\[
\Delta_{0,q}^{(k)}
\]

denote the Kodaira Laplacian on \((0,q)\)-forms with values in \(K_X^k\), with zero modes removed in the zeta-regularized determinant.

Adopt the convention

\[
\boxed{
\mathcal T_k(X)
=
\sum_{q=0}^{1}(-1)^q q\,\log\det{}'\Delta_{0,q}^{(k)}.
}
\tag{2.1}
\]

For a curve this reduces to

\[
\boxed{
\mathcal T_k(X)
=-\log\det{}'\Delta_{0,1}^{(k)}.
}
\tag{2.2}
\]

With this convention, the Quillen metric on the **same holomorphic line** \(\lambda_k\) is [Qui85; BGS88]

\[
\boxed{
 h_Q
=e^{\mathcal T_k}\,h_{L^2}.
}
\tag{2.3}
\]

Equivalently for norms,

\[
\boxed{
\|\cdot\|_Q
=e^{\mathcal T_k/2}\|\cdot\|_{L^2}
=(\det{}'\Delta_{0,1}^{(k)})^{-1/2}\|\cdot\|_{L^2}.
}
\tag{2.4}
\]

Equation (2.4) fixes the convention used throughout this note. Other papers sometimes package the same determinant with the inverse determinant line or a differently normalized Laplacian, so literal powers should not be transplanted without matching conventions.

**Gate J — PASS.** The \(L^2\) and Quillen metrics are now written explicitly on the same \(\lambda_k\).

---

## 3. Curvature decomposition

Use the Chern-curvature convention

\[
F_h=-\partial\bar\partial\log h
\]

for a Hermitian line metric \(h\). From (2.3),

\[
\begin{aligned}
F_Q
&=-\partial\bar\partial\log h_Q\\
&=-\partial\bar\partial(\mathcal T_k+\log h_{L^2})\\
&=F_{L^2}-\partial\bar\partial\mathcal T_k.
\end{aligned}
\]

Hence

\[
\boxed{
F_Q-F_{L^2}
=-\partial\bar\partial\mathcal T_k.
}
\tag{3.1}
\]

In first-Chern-form normalization

\[
c_1(\lambda_k,h)=\frac{i}{2\pi}F_h,
\]

this becomes

\[
\boxed{
c_1(\lambda_k,h_Q)
-
c_1(\lambda_k,h_{L^2})
=
-\frac{i}{2\pi}\partial\bar\partial\mathcal T_k.
}
\tag{3.2}
\]

**Derived here.** Equations (3.1)–(3.2) are the immediate metric consequence of the established Quillen definition in the convention (2.3).

The family local index theorem computes the left-hand Quillen curvature from characteristic forms [BGS88]. For the compact hyperbolic curve family, Zograf–Takhtajan give [ZT87]

\[
\boxed{
c_1(\lambda_k,h_Q)
=
\frac{c_k}{12\pi^2}\omega_{\mathrm{WP}},
\qquad
c_k=6k^2-6k+1.
}
\tag{3.3}
\]

Combining (3.2) and (3.3) gives the exact bookkeeping identity

\[
\boxed{
c_1(\lambda_k,h_{L^2})
=
\frac{c_k}{12\pi^2}\omega_{\mathrm{WP}}
+
\frac{i}{2\pi}\partial\bar\partial\mathcal T_k.
}
\tag{3.4}
\]

This is the central correction to any attempt to identify the elementary \(L^2\) determinant curvature directly with the Quillen/Weil–Petersson curvature.

**Gate K — PASS.** Analytic torsion supplies exactly the metric-curvature difference.

---

## 4. The Mumford polynomial remains metric-independent

The holomorphic line relation from v0.4 is

\[
\boxed{
\lambda_k\simeq\lambda_1^{\otimes c_k},
\qquad
c_k=6k^2-6k+1.
}
\tag{4.1}
\]

This is a statement about determinant lines, not about a particular Hermitian metric [Eri08]. The Quillen curvature formula is compatible with it because

\[
c_1(\lambda_k,h_Q)=c_k\,c_1(\lambda_1,h_Q).
\]

The ordinary \(L^2\) metric does not automatically turn the Mumford isomorphism into an isometry; the analytic-torsion factor measures part of the metric discrepancy.

**FCIG interpretation.** The hierarchy should therefore distinguish

\[
\boxed{
\text{holomorphic determinant line}
\neq
\text{choice of determinant metric}
\neq
\text{connection/curvature data}.
}
\tag{4.2}
\]

---

## 5. Spectral determinant and Selberg geometry

For a compact hyperbolic surface, zeta-regularized Laplacian determinants are controlled by Selberg zeta functions. This is classical. D'Hoker–Phong compute determinants for tensor/spinor weights in terms of special values of Selberg zeta functions, with explicit genus/weight constants [DP86]. Sarnak gives the scalar determinant relation and related formulas [Sar87].

A convention-safe scalar benchmark is

\[
\boxed{
\det{}'\Delta_0
=C_g\,Z_X'(1),
}
\tag{5.1}
\]

where \(C_g\) depends only on the genus in the chosen hyperbolic normalization [Sar87].

For tensor weight \(n>1/2\), D'Hoker–Phong obtain formulas of the schematic form

\[
\boxed{
\det{}'\Delta_n
=
Z_{\varepsilon_n}(s_n)\,e^{-c_n\chi(X)},
}
\tag{5.2}
\]

with \(s_n\), the multiplier sector \(\varepsilon_n\), and \(c_n\) explicit in their operator conventions [DP86]. Their formulas include, for example, a zero-mode-subtracted tensor Laplacian determinant expressed through a Selberg-zeta value at the tensor weight.

We do **not** identify their \(\Delta_n\) symbol with \(\Delta_{0,1}^{(k)}\) without the Kähler/operator normalization map. What is invariant for the present purpose is:

\[
\boxed{
\text{analytic torsion is a global spectral functional, and on a hyperbolic surface that spectrum is encoded by Selberg/geodesic data.}
}
\tag{5.3}
\]

The Selberg zeta function itself has an Euler product over primitive closed geodesics. Thus the torsion correction in (2.3) is globally sensitive to the closed-geodesic spectrum, not merely to local curvature.

**Gate L — PASS.** The scalar benchmark is explicit, and the tensor-weight extension is cited with its convention warning rather than silently shifting indices.

---

## 6. Bergman loops versus analytic torsion: a precise non-identification

The v0.4 Bergman density contains the established pointwise loop sector [Sun26]

\[
\mathcal G_k(p)
=
\sum_{\gamma\in\mathfrak G_p}
\cosh^{-2k}\!\left(\frac{\ell(\gamma)}2\right)
\cos(2\pi k\alpha_\gamma).
\tag{6.1}
\]

By contrast, analytic torsion is obtained from a global zeta-regularized spectral determinant, equivalently from Selberg-trace/zeta data in the hyperbolic case [DP86; Sar87].

These two global sectors have related geometric input but are **not the same functional**:

| Bergman geodesic sector | Analytic-torsion sector |
| --- | --- |
| pointwise function of \(p\in X\) | scalar function on the family/moduli parameter |
| based geodesic loops | primitive closed-geodesic / spectral data |
| carries pointwise line holonomy phase | enters through regularized eigenvalue determinant / Selberg factors |
| exact correction integrates to zero in the v0.4 normalization | torsion changes the determinant metric globally |

The v0.4 result gave

\[
\int_X\rho_k^{\mathrm{loc}}\mathcal G_k\,dA=0.
\tag{6.2}
\]

There is no analogous requirement that \(\mathcal T_k\) vanish or have zero moduli variation.

**Derived here / no-go.** The Bergman loop correction cannot be literally identified with analytic torsion: they live on different spaces and satisfy different normalization constraints. Similar geodesic sums are evidence of a common trace/covering geometry, not proof of equality.

A legitimate future question is whether a heat-kernel or trace transform maps one sector to the other after suitable integration; that would require a separate theorem.

**Gate M — PASS WITH NO-GO.** Coexistence is established; literal identification is rejected.

---

## 7. Revised FCIG determinant architecture

The determinant sector now has four logically distinct layers:

\[
\boxed{
\begin{aligned}
\lambda_k
&=\det R\pi_*K^k
&&\text{holomorphic determinant line},\\[1mm]
h_{L^2}
&&&\text{elementary state-space metric},\\[1mm]
\mathcal T_k
&&&\text{global spectral / analytic-torsion correction},\\[1mm]
h_Q=e^{\mathcal T_k}h_{L^2}
&&&\text{Quillen metric with local-index curvature}.
\end{aligned}
}
\tag{7.1}
\]

The curvature hierarchy is

\[
\boxed{
F_{L^2}
\xrightarrow{\;-\partial\bar\partial\mathcal T_k\;}
F_Q
\xrightarrow{\text{family local index}}
\frac{c_k}{12\pi^2}\omega_{\mathrm{WP}}.
}
\tag{7.2}
\]

The arrow notation denotes a relation, not a dynamical flow.

This resolves an ambiguity present in early FCIG drafts: determinant-line curvature obtained from the Quillen/family-index framework must not be substituted for an elementary \(L^2\) Gram-determinant curvature unless the torsion correction has been accounted for.

---

## 8. What v0.5 changes in the broader program

### Survives

- determinant lines remain the natural abelianized anomaly carriers;
- local curvature and global holonomy/spectral data remain distinct;
- family index theory supplies the Quillen curvature direction;
- the Mumford polynomial controls the canonical curve determinant line.

### Is corrected

- an \(L^2\) determinant metric and a Quillen metric are not interchangeable;
- analytic torsion is not an optional decoration: it is exactly the metric correction;
- a geodesic-looking term in a Bergman kernel is not automatically the same object as Selberg/analytic torsion;
- the flat ppav rank/2 coefficient remains a special exact model result, not a general determinant law.

### Remains open

- the complete differential-cohomology class of the Quillen determinant connection, including global holonomy, in the curved family;
- a direct comparison between Bismut–Freed holonomy/eta data and mapping-class-group holonomy in the FCIG convention;
- degeneration asymptotics near the Deligne–Mumford boundary;
- any Lorentzian/gravitational closure.

---

## 9. Status of v0.5 gates

- **Gate J — same line, two metrics:** PASS, equations (2.3)–(2.4).
- **Gate K — curvature decomposition:** PASS, equations (3.1)–(3.4).
- **Gate L — global spectral/geodesic expression:** PASS, scalar Selberg benchmark plus tensor-weight theorem with convention boundary.
- **Gate M — FCIG sector comparison:** PASS WITH NO-GO; Bergman loops and analytic torsion coexist but are not literally identical.

The natural next milestone is **v0.6: differential-cohomology / holonomy synthesis of the determinant connection**, before any Gravity Closure attempt.

---

## 10. Reproducibility note

`quillen-refinement.py` checks algebraic coefficient identities and illustrates, with a finite truncated Selberg product, that a spectral/geodesic functional has a different dependence on length data from the pointwise Bergman-loop weight. The finite product is a sanity illustration only; it is not a computation of the determinant of a specific compact surface.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[Qui85]** D. Quillen, *Determinants of Cauchy–Riemann Operators over a Riemann Surface*, Funct. Anal. Appl. 19 (1985).
- **[BGS88]** J.-M. Bismut, H. Gillet, C. Soulé, *Analytic Torsion and Holomorphic Determinant Bundles III: Quillen Metrics on Holomorphic Determinants*, Comm. Math. Phys. 115 (1988).
- **[ZT87]** P. G. Zograf and L. A. Takhtajan, *A Local Index Theorem for Families of \(\bar\partial\)-Operators on Riemann Surfaces*, Russian Math. Surveys 42:6 (1987).
- **[DP86]** E. D'Hoker and D. H. Phong, *On Determinants of Laplacians on Riemann Surfaces*, Comm. Math. Phys. 104 (1986).
- **[Sar87]** P. Sarnak, *Determinants of Laplacians*, Comm. Math. Phys. 110 (1987).
- **[Sun26]** J. Sun, *On the Bergman Kernel of Complex Hyperbolic Manifolds*, arXiv:2511.16240 (2026).
- **[Eri08]** D. Eriksson, *A Deligne–Riemann–Roch Isomorphism*, Thèse d'Orsay (2008).