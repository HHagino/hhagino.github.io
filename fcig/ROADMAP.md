# FCIG Research Roadmap

**Current target:** v0.5 — \(L^2\) vs Quillen / analytic-torsion refinement  
**Updated:** 2026-09-08

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

The family, metric, line bundle, state space and normalization are fixed explicitly:

\[
\mathcal H_k(X)=H^0(X,K_X^k),
\qquad
\dim\mathcal H_k=(2k-1)(g-1).
\]

### Gate G — nonzero local curvature sector — PASS

The established exact hyperbolic Bergman formula gives the local factor

\[
\boxed{
\rho_k^{\mathrm{loc}}
=
\frac{2k-1}{4\pi}
=
\frac{k}{2\pi}-\frac1{4\pi}.
}
\]

Thus the curved model has a nonzero subprincipal local term. Its normalization is tied to the hyperbolic metric and is cited to the exact formula / Bergman literature rather than imported from v0.3.

### Gate H — independent global sector — PASS

The same exact formula contains

\[
\boxed{
\sum_{\gamma\in\mathfrak G_p}
\cosh^{-2k}\!\left(\frac{\ell(\gamma)}2\right)
\cos(2\pi k\alpha_\gamma),
}
\]

which depends on geodesic-loop lengths and Chern holonomy. This is independent of the local constant scalar curvature and is exponentially small away from degeneration.

The local factor already integrates to the Riemann--Roch state count, so the global loop sector has zero total integral and redistributes state density spatially.

### Gate I — determinant/Hodge comparison — PASS WITH NO-GO

For

\[
\lambda_k=
\det R\pi_*K^k,
\qquad
\lambda_1=
\det\pi_*K,
\]

the established Mumford isomorphism gives

\[
\boxed{
\lambda_k
\simeq
\lambda_1^{\otimes(6k^2-6k+1)}.
}
\]

This supplies the required determinant/Hodge comparison and gives a clean no-go result:

\[
\boxed{
\text{the flat ppav rank/2 determinant coefficient is not universal.}
}
\]

For fixed genus, the state rank grows linearly in \(k\), whereas the Mumford exponent grows quadratically.

The established Quillen-curvature benchmark is

\[
\boxed{
c_1(\lambda_k,\|\cdot\|_Q)
=
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}}.
}
\]

The detailed comparison between this Quillen metric and the ordinary \(L^2\) determinant metric is deliberately deferred to v0.5.

### v0.4 synthesis

The curved model now realizes simultaneously

\[
\boxed{
\text{state count}
\oplus
\text{nonzero local curvature density}
\oplus
\text{global geodesic/holonomy corrections}
\oplus
\text{Hodge/determinant moduli geometry}.
}
\]

Source and sanity checker:

- `hyperbolic-model.md`
- `hyperbolic-loop.py`

---

## Milestone v0.5 — Quillen / analytic-torsion refinement — ACTIVE

The next task is to separate three metric levels on determinant-of-cohomology lines:

1. ordinary \(L^2\) determinant metric;
2. Quillen metric;
3. analytic-torsion / Selberg-zeta correction.

### Gate J — same line, two metrics

For a compact hyperbolic family, write both the \(L^2\) determinant norm and Quillen norm on the same \(\lambda_k\).

**Pass condition:** an explicit identity of the form

\[
\|\cdot\|_Q
=
\|\cdot\|_{L^2}\times
(\text{analytic torsion})^{\pm1/2}
\]

with conventions fixed and primary references attached.

### Gate K — curvature decomposition

Compute

\[
F_Q-F_{L^2}
\]

and identify exactly which term is supplied by analytic torsion.

**Pass condition:** no mixing of Quillen curvature with the elementary \(L^2\) determinant curvature used in v0.2--v0.3.

### Gate L — global spectral/geodesic expression

Relate the torsion factor to the Selberg zeta / closed-geodesic spectrum for compact hyperbolic curves.

**Pass condition:** a formula or theorem with clear literature provenance, plus at least one reproducible numerical or symbolic sanity check.

### Gate M — compare with FCIG sectors

Determine whether the geodesic sector visible in the Bergman density and the geodesic spectrum entering analytic torsion are linked functorially or merely coexist.

**Pass condition:** state a precise theorem, conjecture, or no-go statement; do not infer equivalence from similar-looking sums.

---

## Gravity Closure gate — NOT ACTIVE

No claim that FCIG derives gravity should be made until the preceding geometric and determinant tests pass.

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
