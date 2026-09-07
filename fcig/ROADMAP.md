# FCIG Research Roadmap

**Current target:** v0.3 — higher-dimensional abelian generalization  
**Updated:** 2026-09-08

The roadmap is ordered so that every new layer is tested before it is used in a gravitational interpretation.

## Milestone v0.3 — Principally polarized abelian varieties

Let

\[
\Omega=X+iY\in\mathfrak H_g,
\qquad
A_\Omega=\mathbf C^g/(\mathbf Z^g+\Omega\mathbf Z^g).
\]

The immediate goal is to determine whether the exact elliptic mechanism survives in dimension \(g>1\).

### Gate A — state space

Construct the level-\(k\) theta basis indexed by

\[
\mathbf j\in(\mathbf Z/k\mathbf Z)^g
\]

and recover

\[
\dim H^0(A_\Omega,L^k)=k^g
\]

for a principal polarization.

**Pass condition:** conventions are fixed and the basis/automorphy laws are explicit.

### Gate B — exact Gram determinant

Prove, for the metric and normalized volume used in Explicit Model III,

\[
\boxed{
\langle s_{\mathbf j}^{(k)},s_{\mathbf m}^{(k)}\rangle
=
\delta_{\mathbf j\mathbf m}
\det(2kY)^{-1/2}.
}
\]

**Pass condition:** analytic Gaussian derivation plus a non-diagonal \(g=2\) numerical check.

### Gate C — Hodge/determinant curvature

Let

\[
\mathcal H_k=\pi_*L^k,
\qquad
N_k=\operatorname{rank}\mathcal H_k=k^g,
\]

and let \(\lambda_H\) be the determinant of the Hodge bundle. Test the exact identity

\[
\boxed{
F_{\det\mathcal H_k}
=
-\frac{N_k}{2}F_{\lambda_H}
=
-\frac{k^g}{2}F_{\lambda_H}.
}
\]

**Pass condition:** derived from the Gram determinant under explicit metric conventions; no appeal to Bismut–Freed for the coefficient.

### Gate D — flat corrected line and metaplectic descent

For even \(N_k\), form

\[
\mathscr A_{g,k}
=
\det\mathcal H_k\otimes\lambda_H^{N_k/2}.
\]

For odd \(N_k\), formulate the same object on an appropriate metaplectic/square-root cover.

**Pass condition:** local curvature cancels and the remaining global multiplier is identified through the finite Weil representation of the relevant theta structure.

### Gate E — multidimensional Bergman lattice sector

Derive a multivariate Poisson-resummed formula for \(B_{g,k}\) and isolate the shortest-vector scale of the normalized period lattice.

Expected structure to test:

\[
B_{g,k}
=
k^g
\left[1+O_\Omega(e^{-c(\Omega)k})\right]
\]

on compact subsets of Siegel space away from degeneration.

**Pass condition:** exact lattice formula, explicit \(c(\Omega)\), and numerical verification.

---

## Milestone v0.4 — Curved genus-\(g\ge2\) curves

Move from flat abelian fibers to compact hyperbolic Riemann surfaces.

The purpose is to force local curvature and global topology to coexist:

\[
\boxed{
\text{polynomial Bergman }1/k\text{ sector}
+
\text{global/geodesic nonperturbative sector}.
}
\]

Questions:

- Does the elliptic local/global split survive when scalar curvature is nonzero?
- Which global corrections are controlled by closed geodesics, injectivity radius, or degeneration toward the Deligne–Mumford boundary?
- How does the determinant/Hodge sector interact with the period map into \(\mathcal A_g\)?

**Pass condition:** at least one explicit curved family where both the local curvature coefficient and a global correction are independently visible.

---

## Milestone v0.5 — Quillen refinement

Replace elementary determinant metrics by Quillen metrics and include analytic torsion.

Targets:

- compare the elementary \(L^2\) determinant identities with Quillen curvature;
- identify which locally cancellable terms change under zeta regularization;
- determine which flat/global holonomy survives the refinement;
- relate the result to families index theory without reversing the logical direction of the theorem.

**Pass condition:** one complete model with ordinary \(L^2\), Quillen, and holonomy data displayed side by side.

---

## Gravity Closure gate

No claim that FCIG derives gravity should be made until the previous milestones pass.

The closure target remains:

\[
\boxed{
\text{local state-density/index data}
+
\text{global holonomy data}
+
\text{causal thermodynamics}
\Longrightarrow ?
\text{Lorentzian field equation}.
}
\]

A successful closure must specify:

1. what geometric object is physical spacetime;
2. how Kähler/moduli data are mapped to Lorentzian variables;
3. how tensor types match;
4. what entropy functional is varied;
5. what limiting regime reproduces known gravitational dynamics;
6. what observation or mathematical counterexample would falsify the proposal.
