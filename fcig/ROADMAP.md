# FCIG Research Roadmap

**Current target:** v0.6 — differential-cohomology / determinant-holonomy synthesis  
**Updated:** 2026-09-09

The roadmap is ordered so that each mathematical mechanism is tested before it is used in a gravitational interpretation. A failed extrapolation is recorded as a no-go result rather than repaired by changing definitions after the fact.

---

## Milestone v0.3 — principally polarized abelian varieties — COMPLETE

The flat ppav laboratory established:

\[
\boxed{
\dim H^0(A_\Omega,L^k)=k^g,
}
\]

\[
\boxed{
F_{\det\mathcal H_k}
=-\frac{k^g}{2}F_{\lambda_H},
}
\]

an exact Poisson-resummed Bergman lattice formula with exponential shortest-vector suppression, and finite Weil/metaplectic descent with explicit nontrivial flat holonomy.

Sources and derivations:

- `abelian-model.md`
- `abelian-bergman.md`
- `abelian-weil.md`

The v0.3 conclusion is specific to the flat polarized-abelian laboratory and its metric conventions.

---

## Milestone v0.4 — compact hyperbolic genus-\(g\ge2\) curves — COMPLETE

Work with a compact hyperbolic Riemann surface

\[
X=\Gamma\backslash\mathbb H,
\qquad g\ge2,
\]

and the canonical polarization \(K_X^k\).

### Gate F — explicit curved family — PASS

\[
\mathcal H_k(X)=H^0(X,K_X^k),
\qquad
\dim\mathcal H_k=(2k-1)(g-1).
\]

### Gate G — nonzero local curvature sector — PASS

\[
\boxed{
\rho_k^{\mathrm{loc}}
=
\frac{2k-1}{4\pi}
=
\frac{k}{2\pi}-\frac1{4\pi}.
}
\]

### Gate H — independent global sector — PASS

The exact hyperbolic Bergman formula contains

\[
\boxed{
\sum_{\gamma\in\mathfrak G_p}
\cosh^{-2k}\!\left(\frac{\ell(\gamma)}2\right)
\cos(2\pi k\alpha_\gamma),
}
\]

which depends on geodesic-loop lengths and Chern holonomy rather than local constant curvature alone.

### Gate I — determinant/Hodge comparison — PASS WITH NO-GO

\[
\boxed{
\lambda_k
\simeq
\lambda_1^{\otimes(6k^2-6k+1)}.
}
\]

Hence the flat ppav rank/2 determinant coefficient is not universal.

Source and sanity checker:

- `hyperbolic-model.md`
- `hyperbolic-loop.py`

---

## Milestone v0.5 — Quillen / analytic-torsion refinement — COMPLETE

Work on the same determinant-of-cohomology line

\[
\lambda_k=\det R\pi_*K^k
\]

with two metrics: ordinary \(L^2\) and Quillen.

### Gate J — same line, two metrics — PASS

With holomorphic analytic torsion

\[
\mathcal T_k
=
\sum_{q=0}^{1}(-1)^q q\log\det{}'\Delta_{0,q}^{(k)},
\]

fix the convention

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2}.
}
\]

Equivalently,

\[
\|\cdot\|_Q=e^{\mathcal T_k/2}\|\cdot\|_{L^2}.
\]

Primary background: Quillen; Bismut–Gillet–Soulé.

### Gate K — curvature decomposition — PASS

For \(F_h=-\partial\bar\partial\log h\),

\[
\boxed{
F_Q-F_{L^2}
=-\partial\bar\partial\mathcal T_k.
}
\]

Using the established compact-curve local index theorem,

\[
\boxed{
c_1(\lambda_k,h_Q)
=
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}},
}
\]

so

\[
\boxed{
c_1(\lambda_k,h_{L^2})
=
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}}
+
\frac{i}{2\pi}\partial\bar\partial\mathcal T_k.
}
\]

Thus elementary \(L^2\) determinant curvature and Quillen curvature are related by an explicit torsion correction and must not be conflated.

### Gate L — global spectral/geodesic expression — PASS

For compact hyperbolic surfaces, zeta-regularized Laplacian determinants are expressed through Selberg-zeta data. A convention-safe scalar benchmark is

\[
\boxed{
\det{}'\Delta_0=C_g Z_X'(1),
}
\]

while D'Hoker–Phong give tensor/spinor-weight determinant formulas in terms of special Selberg-zeta values. Their operator conventions are kept explicit rather than silently identified with the FCIG \(\bar\partial\)-Laplacian.

### Gate M — compare with Bergman global sector — PASS WITH NO-GO

The v0.4 Bergman correction is a pointwise based-loop functional on \(X\). Analytic torsion is a global regularized spectral functional on the family/moduli parameter. They share hyperbolic geodesic/trace input but are not literally the same functional.

\[
\boxed{
\text{common geodesic geometry}
\not\Rightarrow
\text{identical global functional}.
}
\]

Source and sanity checker:

- `quillen-refinement.md`
- `quillen-refinement.py`

### v0.5 synthesis

The determinant sector is now separated as

\[
\boxed{
\lambda_k
\oplus
h_{L^2}
\oplus
\mathcal T_k
\oplus
h_Q,
}
\]

with

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2}.
}
\]

This closes the metric-refinement ambiguity left open in earlier FCIG drafts.

---

## Milestone v0.6 — differential-cohomology / determinant-holonomy synthesis — ACTIVE

The next task is to package curvature and global holonomy into one geometric object rather than treating them as unrelated outputs.

The natural target is a determinant line with connection represented in differential cohomology,

\[
\boxed{
(\lambda,\nabla)
\rightsquigarrow
\widehat c_1(\lambda,\nabla)
\in
\widehat H^2(B;\mathbf Z).
}
\]

### Gate N — fix the differential-cohomology object

Choose a precise model for degree-two differential cohomology and state the maps to

\[
c_1(\lambda)\in H^2(B;\mathbf Z),
\qquad
F_\nabla\in\Omega^2_{\mathrm{cl}}(B),
\qquad
\operatorname{Hol}_\nabla:\text{loops}\to U(1).
\]

**Pass condition:** one convention is fixed and cited; no informal identification of curvature with the whole anomaly class.

### Gate O — Quillen/Bismut–Freed connection

Place the Quillen determinant connection of the curved family into the chosen differential-cohomology model.

**Pass condition:** curvature is matched to the family index theorem, while loop holonomy is matched to the established Bismut–Freed/eta-invariant framework where applicable.

### Gate P — compare flat and curved anomaly sectors

Compare:

1. flat metaplectic holonomy from v0.2–v0.3;
2. curved Quillen/determinant holonomy from v0.4–v0.5.

**Pass condition:** determine what is genuinely common at the level of differential characters and what is model-specific.

### Gate Q — pre-closure no-go audit

Before any gravitational interpretation, list all remaining type mismatches:

- moduli-base curvature vs spacetime curvature;
- determinant-line \(U(1)\) data vs tangent/frame-bundle curvature;
- Euclidean/Kähler data vs Lorentzian causal structure;
- state-count entropy vs horizon entropy functional.

**Pass condition:** the repository contains a precise map or an explicit unresolved obstruction for every mismatch.

---

## Gravity Closure gate — NOT ACTIVE

No claim that FCIG derives gravity should be made until v0.6 passes.

The closure target remains

\[
\boxed{
\text{local state-density/index data}
+
\text{global holonomy/spectral data}
+
\text{causal thermodynamics}
\Longrightarrow ?
\text{Lorentzian field equation}.
}
\]

A successful closure must specify:

1. the physical spacetime object;
2. the map from Kähler/moduli data to Lorentzian variables;
3. tensor-type matching;
4. the entropy/information functional varied;
5. the limit reproducing established gravitational dynamics;
6. a falsification route.
