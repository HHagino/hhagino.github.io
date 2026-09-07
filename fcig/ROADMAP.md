# FCIG Research Roadmap

**Current target:** v0.4 — curved genus-\(g\ge2\) test  
**Updated:** 2026-09-08

The roadmap is ordered so that every new layer is tested before it is used in a gravitational interpretation.

## Milestone v0.3 — Principally polarized abelian varieties — COMPLETE

Let

\[
\Omega=X+iY\in\mathfrak H_g,
\qquad
A_\Omega=\mathbf C^g/(\mathbf Z^g+\Omega\mathbf Z^g).
\]

The v0.3 goal was to determine whether the exact elliptic local/global mechanism survives in dimension \(g>1\). The answer is affirmative for the flat principally polarized abelian laboratory, with the parity/metaplectic qualification stated below.

### Gate A — state space — PASS

The level-\(k\) theta basis is indexed by

\[
\mathbf j\in(\mathbf Z/k\mathbf Z)^g
\]

and

\[
\boxed{
\dim H^0(A_\Omega,L^k)=k^g.
}
\]

Standard theta/polarization background is cited in `abelian-model.md` to Mumford and Birkenhake–Lange.

### Gate B — exact Gram determinant — PASS

For the metric and normalized volume of Explicit Model III,

\[
\boxed{
\langle s_{\mathbf j}^{(k)},s_{\mathbf m}^{(k)}\rangle
=
\delta_{\mathbf j\mathbf m}
\det(2kY)^{-1/2}.
}
\]

The analytic Gaussian derivation is in `abelian-model.md`; `abelian-gram.py` supplies a non-diagonal genus-two numerical check.

### Gate C — Hodge/determinant curvature — PASS

With

\[
\mathcal H_k=\pi_*L^k,
\qquad
N_k=k^g,
\]

and \(\lambda_H\) the determinant Hodge line,

\[
\boxed{
F_{\det\mathcal H_k}
=
-\frac{N_k}{2}F_{\lambda_H}
=
-\frac{k^g}{2}F_{\lambda_H}.
}
\]

This coefficient is derived from the exact Gram determinant in the FCIG normalization and is not attributed to the determinant-line literature.

### Gate D — flat corrected line and metaplectic descent — PASS

For even \(k\), the elementary finite Weil matrices in `abelian-weil.md` are

\[
\boxed{
\begin{aligned}
U_k(T_B)_{\mathbf j\mathbf m}
&=\delta_{\mathbf j\mathbf m}e^{\pi i\mathbf j^TB\mathbf j/k},\\
U_k(S)_{\mathbf j\boldsymbol\ell}
&=k^{-g/2}e^{-2\pi i\mathbf j^T\boldsymbol\ell/k},\\
U_k(R_A)_{\mathbf j\mathbf m}
&=\delta_{\mathbf m,A^T\mathbf j}.
\end{aligned}
}
\]

They satisfy

\[
\boxed{
U_k(S)^2=C,
\qquad
(U_k(S)U_k(T_{I_g}))^3=e^{\pi i g/4}C.
}
\]

For

\[
\mathscr A_{g,k}
=
\det\mathcal H_k\otimes\lambda_H^{N_k/2},
\]

local curvature cancels. The remaining descent is a finite/metaplectic multiplier. It is not merely formal: at \(g=2,k=2\),

\[
B_\times=
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

gives

\[
\boxed{
\chi_{2,2}(T_{B_\times})=-1.
}
\]

Thus a flat corrected determinant line can have nontrivial global holonomy.

For odd \(k\), the fixed zero-characteristic basis is not stable under every symplectic shear; the correct object lives on an enlarged characteristic bundle, theta subgroup, or metaplectic/theta cover. This is standard theta-transformation structure, not an FCIG-specific anomaly. Sources are cited in `abelian-weil.md` to Igusa, DLMF Chapter 21, and Lion–Vergne.

The reproducible verifier is `abelian-weil.py`.

### Gate E — multidimensional Bergman lattice sector — PASS

Explicit Model IIIb derives

\[
\boxed{
B_{g,k}(x,t;\Omega)
=
k^g\sum_{p,\ell\in\mathbf Z^g}
 e^{-\pi kQ_\Omega(p,\ell)/2}
 e^{2\pi ik(p^Tx+\ell^Tt)+\pi ikp^T\ell},
}
\]

where

\[
Q_\Omega(p,\ell)
=(\ell-\Omega p)^*Y^{-1}(\ell-\Omega p).
\]

If

\[
\mu(\Omega)
=
\min_{(p,\ell)\ne0}Q_\Omega(p,\ell),
\]

then for fixed \(\Omega\), uniformly in the fiber coordinate,

\[
\boxed{
B_{g,k}
=
k^g\left[1+O_\Omega\left(e^{-\pi k\mu(\Omega)/2}\right)\right].
}
\]

The exact derivation and literature boundary are in `abelian-bergman.md`; the non-diagonal genus-two numerical check is `abelian-bergman.py`.

### v0.3 summary

The flat abelian laboratory now separates

\[
\boxed{
\text{state capacity}
\oplus
\text{local Hodge/determinant curvature}
\oplus
\text{nonperturbative lattice sector}
\oplus
\text{finite/metaplectic global holonomy}.
}
\]

This closes v0.3. It does **not** imply a gravitational field equation.

---

## Milestone v0.4 — Curved genus-\(g\ge2\) curves — ACTIVE

Move from flat abelian fibers to compact hyperbolic Riemann surfaces.

The purpose is to force local curvature and global topology to coexist:

\[
\boxed{
\text{polynomial Bergman }1/k\text{ sector}
+
\text{global/geodesic nonperturbative sector}.
}
\]

### Gate F — choose an explicit curved family

Work with a compact family of genus-\(g\ge2\) Riemann surfaces carrying a positive line bundle whose Bergman kernel can be controlled analytically.

**Pass condition:** the family, metric, polarization, and normalization are explicit enough that the first nonzero local Bergman coefficient is computable without ambiguity.

### Gate G — local curvature sector

Use established Bergman asymptotics to obtain a nonzero local coefficient proportional, under fixed conventions, to scalar curvature and its higher invariants.

**Pass condition:** identify the normalization-dependent coefficient and cite an appropriate source such as Zelditch/Lu/Ma–Marinescu rather than importing the flat-abelian result.

### Gate H — independent global sector

Identify a correction not captured by the local \(1/k\) expansion, controlled by genuinely global data such as injectivity radius, closed geodesics, period data, or degeneration.

**Pass condition:** exhibit at least one global term or bound whose dependence cannot be reduced to the local scalar-curvature coefficient.

### Gate I — determinant/Hodge comparison through the period map

Compare the determinant/Hodge sector on the curve family with the ppav/Jacobian data induced by the period map.

**Pass condition:** state exactly which v0.3 identities survive pullback, which deform, and which fail. Failure is an acceptable no-go result.

### v0.4 questions

- Does the elliptic/abelian local-global split survive when scalar curvature is nonzero?
- Which global corrections are controlled by closed geodesics, injectivity radius, or degeneration toward the Deligne–Mumford boundary?
- How does the determinant/Hodge sector interact with the period map into \(\mathcal A_g\)?
- Does the rank/2 determinant-response scaling survive, deform, or fail outside flat abelian geometry?

**Milestone pass condition:** at least one explicit curved family where both the local curvature coefficient and an independent global correction are visible, with determinant/Hodge data compared under fixed conventions.

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
