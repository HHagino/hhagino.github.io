# FCIG Explicit Model IV: Compact Hyperbolic Curves, Local Curvature, and Geodesic Sectors

**Status:** v0.4 worked model  
**Date:** 2026-09-08

> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are deductions made from those established formulas in the conventions stated below. Statements marked **FCIG interpretation** are not attributed to the cited literature.

This note tests the FCIG local/global split after leaving the flat abelian laboratory. The curved model is a compact hyperbolic Riemann surface

\[
X=\Gamma\backslash\mathbb H,
\qquad
\operatorname{genus}(X)=g\ge2,
\]

with hyperbolic metric of Gaussian curvature \(-1\), and the polarization is the canonical line bundle \(K_X\) with its hyperbolic Hermitian metric.

The key point is that the curved model has an exact Bergman formula in which a nonzero local curvature contribution and a genuinely global geodesic-loop contribution occur in the same expression.

---

## 1. State space and normalization

For \(k\ge2\), consider

\[
\mathcal H_k(X)=H^0(X,K_X^k).
\]

By Riemann--Roch,

\[
\boxed{
N_{g,k}
=
\dim H^0(X,K_X^k)
=
(2k-1)(g-1).
}
\tag{1.1}
\]

The hyperbolic area is

\[
\boxed{
\operatorname{Area}(X)=4\pi(g-1).
}
\tag{1.2}
\]

These identities will provide a global normalization check for the Bergman density.

---

## 2. Established exact Bergman formula

Let \(\rho_k(p)\) denote the diagonal Bergman density for \(K_X^k\) in the hyperbolic metric. For each point \(p\in X\), let \(\mathfrak G_p\) denote the set of nontrivial oriented geodesic loops based at \(p\). Write \(\ell(\gamma)\) for the length of a loop and

\[
\operatorname{Hol}_{K_X}(\gamma)
=
e^{2\pi i\alpha_\gamma}
\]

for the Chern-connection holonomy.

**Established.** In the normalization used here, Sun proves the exact formula for compact complex-hyperbolic manifolds; in complex dimension one it specializes to [Sun26]

\[
\boxed{
\rho_k(p)
=
\frac{2k-1}{4\pi}
\left[
1+
\sum_{\gamma\in\mathfrak G_p}
\cosh^{-2k}\!\left(\frac{\ell(\gamma)}{2}\right)
\cos(2\pi k\alpha_\gamma)
\right]
}
\tag{2.1}
\]

for the stated range of \(k\). The same paper records the relation to periodization formulas on the universal cover. General periodization of positive-line-bundle Szeg\H{o}/Bergman kernels over deck groups is established by Lu--Zelditch [LZ16]. Exponentially small remainders in constant-curvature Riemann-surface settings were established earlier by Berman [Ber12].

Equation (2.1) is **not** claimed as an FCIG derivation.

---

## 3. Exact local/global split

Define

\[
\rho_k^{\mathrm{loc}}
=
\frac{2k-1}{4\pi}
=
\frac{k}{2\pi}-\frac1{4\pi}
\tag{3.1}
\]

and

\[
\mathcal G_k(p)
=
\sum_{\gamma\in\mathfrak G_p}
\cosh^{-2k}\!\left(\frac{\ell(\gamma)}{2}\right)
\cos(2\pi k\alpha_\gamma).
\tag{3.2}
\]

Then (2.1) becomes

\[
\boxed{
\rho_k(p)
=
\rho_k^{\mathrm{loc}}
\left(1+\mathcal G_k(p)\right).
}
\tag{3.3}
\]

### 3.1 Local curvature sector

The first term is polynomial in \(k\):

\[
\boxed{
\rho_k^{\mathrm{loc}}
=
\frac{k}{2\pi}-\frac1{4\pi}.
}
\tag{3.4}
\]

The nonzero constant term is the curved analogue of the subprincipal scalar-curvature coefficient in the Tian--Zelditch--Lu expansion [Zel98; Lu00; MM07]. In constant curvature, all local curvature invariants are fixed by the hyperbolic geometry, and the exact formula packages the local polynomial sector into the factor (3.4).

### 3.2 Global geodesic sector

The second term depends on

- lengths of nontrivial based geodesic loops;
- line-bundle holonomy along those loops;
- the global quotient group \(\Gamma\).

It is therefore not determined by the scalar curvature at \(p\). The factor

\[
\cosh^{-2k}\!\left(\frac{\ell}{2}\right)
=
\exp\!\left[-2k\log\cosh\left(\frac{\ell}{2}\right)\right]
\tag{3.5}
\]

shows its nonperturbative character in \(1/k\). Berman's constant-curvature estimates give exponential control in terms of the injectivity radius [Ber12], while off-diagonal hyperbolic estimates make the dependence on distance/injectivity radius explicit [AM20].

**FCIG interpretation.** The natural curved decomposition is therefore

\[
\boxed{
\text{Bergman state density}
=
\text{local curvature sector}
+
\text{global geodesic/holonomy sector},
}
\tag{3.6}
\]

where the second term is beyond every finite power series in \(1/k\).

---

## 4. Global normalization check

If the geodesic-loop correction is integrated over the surface, the total Bergman density must equal the dimension of the state space:

\[
\int_X\rho_k\,dA=N_{g,k}.
\tag{4.1}
\]

The local factor alone already gives

\[
\begin{aligned}
\int_X\rho_k^{\mathrm{loc}}\,dA
&=
\frac{2k-1}{4\pi}\,4\pi(g-1)\\
&=(2k-1)(g-1)\\
&=N_{g,k}.
\end{aligned}
\tag{4.2}
\]

Hence

\[
\boxed{
\int_X
\rho_k^{\mathrm{loc}}\mathcal G_k(p)\,dA(p)=0.
}
\tag{4.3}
\]

**Derived here.** Equation (4.3) follows from the established exact formula, Riemann--Roch, and Gauss--Bonnet normalization. It shows that the global loop sector redistributes the local state density without changing the total number of states.

This is already qualitatively different from treating entropy as a scalar function whose gradient alone is supposed to encode geometry.

---

## 5. A shortest-loop scale

At a fixed point \(p\), define

\[
\ell_{\min}(p)
=
\inf_{\gamma\in\mathfrak G_p}\ell(\gamma).
\tag{5.1}
\]

Every individual loop contribution is bounded in absolute value by

\[
\cosh^{-2k}\!\left(\frac{\ell_{\min}(p)}2\right).
\tag{5.2}
\]

The sum requires growth control on the number of loops; this is precisely why the established exponential Bergman estimates are cited rather than replacing them with a naive termwise bound [Ber12; LZ16; AM20].

For a compact surface, the injectivity radius is positive, so the global sector is exponentially small as \(k\to\infty\), uniformly away from degeneration. When a family approaches the Deligne--Mumford boundary, short closed geodesics appear and this suppression can fail uniformly.

**FCIG interpretation.** The natural degeneration parameter is no longer the lattice shortest-vector scale \(\mu(\Omega)\) of v0.3; it is replaced by hyperbolic short-geodesic / injectivity-radius data.

---

## 6. Period map and the Hodge line

Let

\[
\pi:\mathcal C_g\to\mathcal M_g
\]

be the universal smooth curve, locally on an appropriate cover, and set

\[
\lambda_1
=
\det \pi_*K_{\mathcal C_g/\mathcal M_g}.
\tag{6.1}
\]

This is the Hodge determinant line. Under the Torelli/period map

\[
\mathcal M_g\longrightarrow\mathcal A_g,
\]

it is the pullback of the Hodge determinant line on principally polarized abelian varieties. The Hodge-bundle side is standard moduli theory; see [FC90; HM98].

For \(k\ge2\), define the determinant-of-cohomology line

\[
\lambda_k
=
\det R\pi_*K_{\mathcal C_g/\mathcal M_g}^{k}.
\tag{6.2}
\]

---

## 7. Mumford isomorphism: the flat rank/2 law does not survive

**Established.** On the smooth moduli space, the Mumford isomorphism gives [Eri08]

\[
\boxed{
\lambda_k
\simeq
\lambda_1^{\otimes c_k},
\qquad
c_k=6k^2-6k+1.
}
\tag{7.1}
\]

Compare this with the state rank

\[
N_{g,k}=(2k-1)(g-1).
\tag{7.2}
\]

The exponent \(c_k\) is quadratic in \(k\), whereas \(N_{g,k}\) is linear in \(k\) for fixed genus.

Therefore the v0.3 identity

\[
F_{\det\mathcal H_k}
=-\frac{N_k}{2}F_{\lambda_H}
\tag{7.3}
\]

cannot be promoted to a universal determinant/Hodge law for curved canonical families.

**Derived here / no-go statement.** The curved canonical family falsifies the simplest universal extrapolation of the flat ppav rank/2 scaling. What survives is the existence of a precise determinant/Hodge relation, but its coefficient is the Mumford polynomial \(6k^2-6k+1\), not one half of the state rank.

This is a useful failure, not a defect to be hidden.

---

## 8. Quillen curvature benchmark

The determinant line carries the Quillen metric. For compact hyperbolic Riemann surfaces, the local family index theorem of Zograf--Takhtajan gives, in their normalization [ZT87],

\[
\boxed{
c_1(\lambda_k,\|\cdot\|_Q)
=
\frac{6k^2-6k+1}{12\pi^2}
\,\omega_{\mathrm{WP}}.
}
\tag{8.1}
\]

For \(k=1\),

\[
\boxed{
c_1(\lambda_1,\|\cdot\|_Q)
=
\frac{1}{12\pi^2}\omega_{\mathrm{WP}}.
}
\tag{8.2}
\]

so (8.1) is the curvature form compatible with the Mumford exponent (7.1).

This section is used only as a benchmark in v0.4. The systematic comparison between ordinary \(L^2\) determinant metrics, Quillen metrics, analytic torsion, and holonomy remains the explicit target of v0.5.

---

## 9. What survives from v0.3 and what fails

The comparison is now sharp.

### Survives

1. **State counting remains geometric.**  
   \(N_{g,k}=(2k-1)(g-1)\) is a global index/state-count quantity.

2. **A local/global Bergman split survives.**  
   The exact hyperbolic formula separates a polynomial local factor from exponentially small geodesic-loop corrections.

3. **Global information survives beyond local curvature.**  
   Loop lengths and holonomies remain even though the local curvature is constant.

4. **Determinant/Hodge geometry remains structured.**  
   The period-map/Hodge sector is controlled by a precise line-bundle relation.

### Fails or deforms

1. **Flat local sector does not survive.**  
   The hyperbolic model has a nonzero subprincipal term \(-1/(4\pi)\).

2. **The ppav lattice invariant is replaced.**  
   \(\mu(\Omega)\) is replaced by injectivity-radius / closed-geodesic data.

3. **The rank/2 determinant coefficient is not universal.**  
   The canonical family is governed by the Mumford polynomial \(6k^2-6k+1\).

4. **A single line bundle cannot encode all sectors.**  
   Fiber Bergman density, Hodge/period geometry, geodesic data, and determinant/Quillen geometry are distinct objects linked by explicit maps, not literal identifications.

---

## 10. FCIG v0.4 synthesis

The curved laboratory supports the refined hierarchy

\[
\boxed{
\begin{aligned}
\text{state capacity}
&:\quad (2k-1)(g-1),\\[1mm]
\text{local curvature density}
&:\quad \frac{k}{2\pi}-\frac1{4\pi},\\[1mm]
\text{global geodesic sector}
&:\quad
\sum_{\gamma}
\cosh^{-2k}\!\left(\frac{\ell(\gamma)}2\right)
\cos(2\pi k\alpha_\gamma),\\[1mm]
\text{Hodge/determinant sector}
&:\quad
\lambda_k\simeq\lambda_1^{6k^2-6k+1},\\[1mm]
\text{Quillen moduli curvature}
&:\quad
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}}.
\end{aligned}
}
\tag{10.1}
\]

**FCIG interpretation.** The evidence now favors a multi-sector theory of information geometry:

\[
\boxed{
\text{local asymptotics}
\oplus
\text{global geodesic/holonomy data}
\oplus
\text{determinant/index geometry}
\oplus
\text{moduli curvature}.
}
\tag{10.2}
\]

It does **not** support identifying gravity with a single entropy gradient.

---

## 11. Status of the v0.4 gates

- **Gate F — explicit curved family:** PASS. Compact hyperbolic genus-\(g\ge2\) curves with \(K_X^k\).
- **Gate G — local curvature sector:** PASS. Exact local factor \((2k-1)/(4\pi)\), with nonzero subprincipal term.
- **Gate H — independent global sector:** PASS. Exact geodesic-loop/holonomy correction in (2.1), with exponential injectivity-radius control from the literature.
- **Gate I — determinant/Hodge comparison:** PASS WITH A NO-GO. Mumford's quadratic exponent replaces the flat ppav rank/2 coefficient.

The next milestone is therefore **v0.5: systematic \(L^2\) vs Quillen / analytic-torsion refinement**.

---

## 12. Reproducibility note

`hyperbolic-loop.py` checks:

1. the local-density integral against the Riemann--Roch dimension;
2. exponential suppression of a finite list of geodesic-loop terms;
3. the difference between linear state-rank scaling and quadratic Mumford scaling.

The code does not attempt to re-prove Sun's theorem or enumerate the complete loop spectrum of a compact surface.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[Sun26]** J. Sun, *On the Bergman Kernel of Complex Hyperbolic Manifolds*, arXiv:2511.16240, v3 (2026).
- **[Ber12]** R. J. Berman, *Sharp Asymptotics for Toeplitz Determinants and Convergence Towards the Gaussian Free Field on Riemann Surfaces*, IMRN (2012).
- **[LZ16]** Z. Lu and S. Zelditch, *Szegő Kernels and Poincaré Series*, J. Anal. Math. 130 (2016).
- **[AM20]** A. Aryasomayajula and P. Majumder, *Estimates of the Bergman Kernel on a Hyperbolic Riemann Surface of Finite Volume II*, Ann. Fac. Sci. Toulouse 29 (2020).
- **[Zel98]** S. Zelditch, *Szegő Kernels and a Theorem of Tian*, IMRN (1998).
- **[Lu00]** Z. Lu, *On the Lower Order Terms of the Asymptotic Expansion of Tian--Yau--Zelditch*, AJM (2000).
- **[MM07]** X. Ma and G. Marinescu, *Holomorphic Morse Inequalities and Bergman Kernels*, Birkhäuser (2007).
- **[ZT87]** P. G. Zograf and L. A. Takhtajan, *A Local Index Theorem for Families of \(\bar\partial\)-Operators on Riemann Surfaces*, Russian Math. Surveys 42:6 (1987).
- **[Eri08]** D. Eriksson, *A Deligne--Riemann--Roch Isomorphism*, Thèse d'Orsay (2008), §6.5.
- **[FC90]** G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Springer (1990).
- **[HM98]** J. Harris and I. Morrison, *Moduli of Curves*, Springer (1998).
