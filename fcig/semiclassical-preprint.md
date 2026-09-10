# A Semiclassical Atlas for Holomorphic Discrete-Series Matrix Coefficients in FCIG

## Consolidated preprint draft

**Status: 2026-09-10.**

This paper consolidates the FCIG semiclassical branch into theorem-oriented form. The classical Airy, Bessel, Hermite, Jacobi, and coalescing-saddle mechanisms are not claimed as novel. The FCIG-specific content is the normalization, derived saddle/caustic geometry, boundary scalings, and matching of canonical charts.

## Abstract

Let \(M_{m,n}^{(q)}(t)\) be a radial K-type matrix coefficient in the holomorphic discrete series associated with q-differentials. In the FCIG normalization it has an exact Jacobi-polynomial representation. We analyze \(q\to\infty\) with \(m/q\to\alpha\ge0\) and \(n/q\to\beta\ge0\). The coefficient-extraction phase has two caustic sheets
\[
t_-=|u_\alpha-u_\beta|,\qquad t_+=u_\alpha+u_\beta,
\qquad \cosh u_\alpha=1+\alpha,\quad\cosh u_\beta=1+\beta.
\]
The intermediate chamber is oscillatory and the exterior chambers have real decaying saddles governed by explicit rate functions. Simple caustics have Airy normal forms. The two failures of separated-fold uniformity occur at \(q|\alpha-\beta|=O(1)\) and \(q\min(\alpha,\beta)=O(1)\); direct double scaling gives respectively Bessel and Hermite--Gaussian/parabolic-cylinder charts. Their large-order turning regions match the generic Airy charts. This yields a leading semiclassical atlas for the radial matrix coefficients. A stronger unrestricted all-derivatives Harish--Chandra-Schwartz theorem is not asserted.

---

# 1. Introduction

The holomorphic discrete series provides the representation-theoretic side of the FCIG hyperbolic information construction. Earlier FCIG notes identified an exact transported Bergman/coherent-state kernel, a cyclic relative trace, and a strict distinction between matrix coefficients, orbital integrals, and Harish--Chandra characters. Here we isolate the semiclassical behavior of radial K-type matrix coefficients when the representation parameter and K-type labels may grow together.

The exact coefficient is a Jacobi polynomial with simultaneously varying degree and parameters. The FCIG task is to derive the exact phase, determine its caustic surface, normalize the boundary charts, and verify their overlaps without identifying unrelated spectral variables. Generic points are governed by nondegenerate saddles, simple folds by Airy functions, the identity/near-diagonal boundary by Bessel functions, and the lowest-K sheet merger by Hermite--Gaussian functions.

After \(\alpha+1=\cosh u_\alpha\), \(\beta+1=\cosh u_\beta\), the allowed chamber is
\[
|u_\alpha-u_\beta|<t<u_\alpha+u_\beta.
\]
This is an exact algebraic statement about the saddle discriminant, not a separate geometric hyperbolic-triangle theorem.

---

# 2. Exact representation and conventions

For \(n\ge m\), in the frozen radial convention of `phase-convention.md`,
\[
\boxed{M_{m,n}^{(q)}(t)=\mathcal N_{m,n}(q)\left(\cosh\frac t2\right)^{-2q}\left(\tanh\frac t2\right)^{n-m}P_m^{(n-m,2q-1)}\left(1-2\tanh^2\frac t2\right)}
\]
with
\[
\mathcal N_{m,n}(q)=\left(\frac{m!\Gamma(2q+n)}{n!\Gamma(2q+m)}\right)^{1/2}.
\]
The opposite ordering is obtained through
\[
\boxed{M_{m,n}^{(q)}(-t)=\overline{M_{n,m}^{(q)}(t)}.}
\]
Thus invariant radial statements may be written using the ordered pair \(\max(m,n),\min(m,n)\). Compact K-phases are excluded from the radial theorem and are not transferred to the orbital orientation convention.

Set \(r=\tanh(t/2)\), \(m=\alpha q+o(q)\), \(n=\beta q+o(q)\). Coefficient extraction gives
\[
\boxed{\Psi_{\alpha,\beta,r}(z)=\beta\log(z+r)-(\beta+2)\log(1+rz)-\alpha\log z.}
\]
The saddle equation is
\[
\frac{\beta}{z+r}-\frac{r(\beta+2)}{1+rz}-\frac{\alpha}{z}=0,
\]
or
\[
r(\alpha+2)z^2+Bz+\alpha r=0,\qquad B=(\alpha-\beta)+(\alpha+\beta+2)r^2.
\]

---

# 3. Main results

## Theorem A — exact caustic surface

Define \(\alpha+1=\cosh u_\alpha\), \(\beta+1=\cosh u_\beta\). Then
\[
\boxed{\Delta_{\rm sad}=(\alpha+\beta+2)^2(r^2-r_-^2)(r^2-r_+^2)}
\]
with
\[
r_-=\tanh\frac{|u_\alpha-u_\beta|}{2},\qquad r_+=\tanh\frac{u_\alpha+u_\beta}{2}.
\]
Consequently
\[
\boxed{t_-=|u_\alpha-u_\beta|,\qquad t_+=u_\alpha+u_\beta.}
\]
The chambers are inner forbidden, oscillatory, and outer forbidden as \(t\) crosses \(t_-\) and \(t_+\).

## Theorem B — generic saddle and Airy charts

For \(\alpha\ge\beta>0\), let \(\Delta=B^2-4\alpha(\alpha+2)r^2\). The real decaying saddles are
\[
z_{\rm in}=\frac{-B-\sqrt\Delta}{2r(\alpha+2)},\qquad z_{\rm out}=\frac{-B+\sqrt\Delta}{2r(\alpha+2)}.
\]
With
\[
s(\gamma)=\frac12[(\gamma+2)\log(\gamma+2)-\gamma\log\gamma-2\log2],
\]
define
\[
\Phi_{\alpha,\beta}(t;z)=2\log\cosh\frac t2+s(\alpha)-s(\beta)-\beta\log|z+r|+(\beta+2)\log|1+rz|+\alpha\log|z|.
\]
Then \(\Phi_-:=\Phi(t;z_{\rm in})>0\) in \(0<t<t_-\), and \(\Phi_+:=\Phi(t;z_{\rm out})>0\) in \(t>t_+\), with vanishing at the corresponding caustic.

At either simple caustic the saddles coalesce at
\[
\boxed{z_*=-\sqrt{\frac{\alpha}{\alpha+2}}},\qquad
\boxed{\partial_t\Psi'(z_*,t_\pm)=-(\alpha+2).}
\]
The nonzero cubic term yields
\[
z-z_*=O(q^{-1/3}),\qquad t-t_\pm=O(q^{-2/3}),
\]
and a Chester--Friedman--Ursell Airy normal form. On the forbidden side, \(\Phi_\pm(t)\asymp C_\pm|t-t_\pm|^{3/2}\).

## Theorem C — identity/near-diagonal Bessel chart

If \(n-m=k\ge0\) is fixed, \(m/q\to\alpha>0\), and \(t=s/q\), then uniformly for bounded \(s\),
\[
\boxed{M_{m,m+k}^{(q)}(s/q)\longrightarrow J_k(\sqrt{\alpha(\alpha+2)}\,s)}
\]
up to the frozen compact phase. Moreover
\[
\boxed{\sqrt{\alpha(\alpha+2)}\,qt_-\to k,}
\]
so the large-order Bessel turning region matches the generic inner Airy chart.

## Theorem D — lowest-K Hermite--Gaussian chart

If the smaller K-type index is fixed, say \(n=\nu\ge0\), while \(m/q\to\alpha>0\), and
\[
t=u_\alpha+\frac{\tau}{\sqrt q},
\]
then
\[
\boxed{q^{1/4}M_{\nu,m}^{(q)}\left(u_\alpha+\frac{\tau}{\sqrt q}\right)\longrightarrow[\pi\alpha(\alpha+2)]^{-1/4}\frac{H_\nu(-\tau)}{\sqrt{2^\nu\nu!}}e^{-\tau^2/2}}
\]
or equivalently the corresponding parabolic-cylinder expression. The generic caustics satisfy
\[
\boxed{\tau_\pm\to\pm\sqrt{2\nu},}
\]
so large-order Hermite turning asymptotics recover the separated Airy folds.

## Corollary — semiclassical atlas

\[
\boxed{\begin{array}{ccl}
\text{generic forbidden bulk}&:&e^{-q\Phi_\pm}\times\text{saddle amplitude},\\
\text{generic allowed bulk}&:&\text{conjugate-saddle oscillation},\\
\text{simple caustic}&:&\operatorname{Ai},\\
q|\alpha-\beta|=O(1)&:&J_{|m-n|},\\
q\min(\alpha,\beta)=O(1)&:&\text{Hermite--Gaussian / }D_\nu.
\end{array}}
\]
with Bessel-to-Airy and Hermite-to-Airy overlaps. Thus
\[
\boxed{\textbf{SAC-A: PASS — leading semiclassical atlas closed.}}
\]

---

# 4. Proof architecture

Theorem A follows by exact factorization of the quadratic saddle discriminant. Theorem B follows from real-saddle selection in the two forbidden chambers and cubic reduction at a double saddle. Standard coalescing-saddle theory supplies the Airy canonical integral once the FCIG cubic and unfolding coefficients are nonzero on compact generic parameter sets.

Theorem C follows directly from the terminating Jacobi hypergeometric series: under fixed \(k=n-m\) and \(t=s/q\), the Gauss series contracts to \({}_0F_1\), and normalization converts it to the displayed Bessel function. Theorem D is also derived directly at the boundary: with fixed Jacobi degree and two large parameters, the rescaled Jacobi differential equation contracts to the Hermite equation, while Stirling/local-CLT normalization gives the Gaussian envelope.

Detailed algebra remains in the derivation notebooks listed in §7.

---

# 5. Relation to FCIG

The exact FCIG Sun/Bergman orbital kernel has transverse Fourier window centered at
\[
|\xi|\sim2q\tanh(L/2),
\]
while the representation-side saddle geometry is organized by \(r=\tanh(t/2)\). This is compatibility of scales, not identification:
\[
\boxed{\xi\neq t\neq n\neq\text{Harish--Chandra spectral parameter}.}
\]
Matrix coefficients, cyclic relative traces, orbital integrals, and Harish--Chandra characters remain different typed objects. A stronger representation/orbital equality requires an explicit transform theorem.

---

# 6. Scope and current gates

Closed here:
\[
\boxed{\textbf{JA-A1, RF-B1, RF-B2, RF-C, UR-A1, UR-A2, BC-A1, BC-A2, SAC-A: PASS.}}
\]
The old `JA-A2: OPEN` and `BC-A: OPEN` labels are historical and superseded.

Not claimed here: a single globally explicit all-orders remainder theorem across every stratum; unrestricted-K all-derivatives pointwise Harish--Chandra-Schwartz control (`UQ-A2`); equality of K-type, orbital Fourier, or Harish--Chandra spectral variables; an ordinary trace interpretation of the Harish--Chandra character; or novelty of the classical special-function mechanisms.

---

# 7. Derivation map and reproducibility

1. `jacobi-asymptotic-closure.md` — exact Jacobi formula and fixed-K estimates.
2. `proportional-k-type-rate-function.md` — coefficient-extraction phase.
3. `off-diagonal-rate-surface.md` — discriminant and caustic surface.
4. `two-sheet-airy-normalization.md` — cubic coefficients and Airy normalization.
5. `global-off-diagonal-rate-closure.md` — forbidden saddles and rates.
6. `uniform-remainder-closure.md` — generic uniformity and boundary scales.
7. `boundary-bessel-closure.md` — Bessel double scaling.
8. `lowest-k-hermite-closure.md` — Hermite--Gaussian double scaling.
9. `semiclassical-atlas-closure.md` — atlas assembly.
10. `phase-convention.md` — frozen publication phase/orientation convention.
11. `semiclassical-status-audit.md` — historical gate audit.

---

# 8. References

1. NIST Digital Library of Mathematical Functions, §15.9(i), Jacobi polynomial/hypergeometric representation.
2. NIST Digital Library of Mathematical Functions, §2.4(v) and Chapter 36, coalescing saddle points and canonical integrals.
3. NIST Digital Library of Mathematical Functions, §§10.19--10.20, large-order Bessel and Airy-uniform asymptotics.
4. NIST Digital Library of Mathematical Functions, §§18.7 and 18.15, Jacobi/Hermite limits and large-parameter asymptotics.
5. C. Chester, B. Friedman, and F. Ursell, *An extension of the method of steepest descents*, Proc. Cambridge Philos. Soc. **53** (1957), 599--611.
6. C. L. Frenzen and R. Wong, *A Uniform Asymptotic Expansion of the Jacobi Polynomials with Error Bounds*, Canadian J. Math. **37** (1985), 979--1007.
7. A. Gil, J. Segura, and N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss--Jacobi quadrature for large degree and parameters in terms of elementary functions*, J. Math. Anal. Appl. **494** (2021), 124642.
8. G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloquium Publications 23, 1975.

---

# 9. Claim firewall

1. The theorem concerns radial holomorphic-discrete-series matrix coefficients, not Harish--Chandra characters or ordinary traces.
2. Airy, Bessel, Hermite, and standard coalescing-saddle machinery are classical.
3. The FCIG-specific derived content is the normalization, saddle phase, caustic surface, rate selection, boundary scalings, and chart matching recorded above.
4. The triangle-inequality caustic chamber is an algebraic reparameterization of the saddle discriminant; no independent geometric triangle theorem is claimed.
5. `SAC-A: PASS` is a leading canonical-atlas result, not `UQ-A2`.
6. K-type phase conventions and cyclic/orbital orientation conventions remain separate typed choices.
