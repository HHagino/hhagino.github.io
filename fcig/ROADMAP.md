# FCIG Research Roadmap

**Current target:** v0.19 — intrinsic elliptic spectral metric  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are retained as explicit no-go results.

---

## v0.3–v0.16 — geometry through explicit operator realization — COMPLETE

Earlier milestones establish the determinant/differential-cohomology foundation, local/global anomaly hierarchy, pushforward and reconstruction no-gos, mixed anomaly descent, functional-response ambiguity, conditional semiclassical closure, and the explicit operator bridge

\[
(\mathscr L_{\rm FCIG},\nabla^{\rm FCIG})+\Phi
\to P_\Phi
\to\operatorname{Tr}e^{-tP_\Phi}
\to W_{1\text{-loop}}^{\rm ren}[g,\Phi].
\]

At heat-kernel order \(b_4\), pulled-back FCIG line curvature enters as an ordinary bundle-curvature invariant, without being identified with Riemann curvature.

---

## v0.17 — realization-map / sigma-model dynamics audit — COMPLETE WITH CONSTITUTIVE NO-GO

Use the actual elliptic FCIG target

\[
\mathbb H=\{u+iY\mid Y>0\},
\qquad ds^2=\frac{du^2+dY^2}{Y^2}.
\]

The harmonic-map action and stress tensor are standard and explicit. The pulled-back Hodge curvature enters the Model-XVI four-derivative \(\Omega^2\) sector, but it does not determine the two-derivative sigma normalization \(Z_\Phi\).

Sources: `realization-sigma.md`, `realization-sigma.py`, `realization-sigma.bib`.

---

## v0.18 — induced realization-map metric from determinants — COMPLETE WITH SPECTRAL-INPUT NO-GO

Sources:

- `induced-metric.md`
- `induced-metric.py`
- `induced-metric.bib`

### Gate BP — two-point derivative calculation — PASS IN FIXED 1PI BUBBLE CONVENTION

For one heavy real scalar

\[
P(\Phi)=-\partial^2+V(\Phi),\qquad V>0,
\]

the one-loop quadratic bubble obeys

\[
I(p)=I(0)-\frac{p^2}{96\pi^2V}+O(p^4),
\]

so the induced two-derivative response is

\[
\boxed{G^{\rm ind}_{AB}=\frac1{192\pi^2}\frac{V_{,A}V_{,B}}{V}.}
\]

The definition is operational: it is the constant-background 1PI two-point \(p^2\) coefficient. It is not asserted to be the unique global off-shell derivative-expanded functional; Chan, Henning--Lu--Murayama, and Canevarolo--Prokopec are used to document the derivative-expansion context and caveat.

### Gate BQ — multi-species induced metric — PASS

For independent diagonal species,

\[
\boxed{
G^{\rm ind}_{AB}=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}.
}
\]

With \(s_i=\sqrt{V_i}\),

\[
\boxed{
G^{\rm ind}=\frac1{48\pi^2}\sum_i ds_i^2
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N}.
}
\]

Thus the determinant metric is the Euclidean pullback of the mass map.

### Gate BR — rank / curvature audit — PASS WITH EXACT NO-GOS

1. **One species:** \(\operatorname{rank}G^{\rm ind}\le1\).
2. **Two species:** if nondegenerate, \((s_1,s_2)\) are local coordinates and
   \[
   G^{\rm ind}=\frac1{48\pi^2}(ds_1^2+ds_2^2),
   \]
   so \(K=0\). Therefore two species can never reproduce the Poincare metric \(K=-1\) on an open set.
3. **Three species:** exact matching is an isometric immersion into \(\mathbb R^3\). Local negative-curvature fitting is possible, but Hilbert's theorem forbids a complete regular immersion of the full hyperbolic plane into \(\mathbb R^3\).

### Gate BS — method / reparametrization audit — PASS WITH QUALIFICATION

All rank and curvature statements refer to the explicitly defined 1PI bubble metric above. Off-shell gradient-expanded effective actions have additional prescription issues; Model XVIII does not erase that distinction.

### Gate BT — modular symmetry — PASS WITH TWO-SPECIES NO-GO

Klein's complete invariant obeys \(J(\gamma\tau)=J(\tau)\). The positive modular-invariant masses

\[
V_1=M^2e^{2a\Re J(\tau)},\qquad
V_2=M^2e^{2a\Im J(\tau)}
\]

produce a rank-two metric at regular points, but by the two-species theorem it is locally flat rather than hyperbolic. At elliptic branch points the explicit metric loses rank.

### Gate BU — constitutive-input no-go — PASS

If the mass functions are chosen freely, the problem becomes an inverse-design problem. Since

\[
G^{\rm ind}\propto s^*\delta,
\]

choosing the spectrum is equivalent to choosing Euclidean embedding coordinates for the desired target geometry. A local hyperbolic match can be engineered with sufficiently unconstrained spectral functions and therefore is not, by itself, an FCIG prediction.

### Gate BV — explicit witness — PASS

\[
V_1=e^{2au},\qquad V_2=e^{2aY}
\]

restores rank two but gives

\[
G^{\rm ind}=\frac{a^2}{48\pi^2}
\left(e^{2au}du^2+e^{2aY}dY^2\right),
\]

which is Euclidean after the coordinate changes \(U=e^{au}\), \(W=e^{aY}\).

### v0.18 conclusion

\[
\boxed{
\text{determinant}\to G^{\rm ind}\text{ is real, but }
\text{FCIG prediction requires FCIG to fix the microscopic operator spectrum.}
}
\]

References: Chan (1986); Henning--Lu--Murayama (2018); Canevarolo--Prokopec (2024); NIST DLMF Chapter 23; do Carmo (1976); Hilbert (1901).

---

## v0.19 — intrinsic elliptic spectral metric — ACTIVE

Arbitrary mass functions are no longer allowed. Use the **actual modular-covariant spectrum** of the elliptic FCIG laboratory.

### Initial spectral object

For an area-normalized flat torus \(E_\tau\), use the scalar Laplacian spectrum schematically

\[
\lambda_{m,n}(\tau)\propto\frac{|m\tau-n|^2}{Y},
\qquad (m,n)\neq(0,0),
\]

whose multiset is modular invariant.

### Gate BW — exact spectral normalization

Fix the area-one metric/Laplacian convention and derive the exact eigenvalue normalization rather than using proportionality.

### Gate BX — zeta determinant / Kronecker audit

Use the spectral zeta function and Kronecker limit formula to recover the known flat-torus determinant, including the \(Y|\eta(\tau)|^4\) dependence in the fixed convention.

### Gate BY — moduli Hessian / curvature response

Compute the \(\partial_\tau\partial_{\bar\tau}\) response of the zeta determinant/Quillen quantity. Determine precisely whether the non-holomorphic \(\log Y\) term gives the Poincare/Hodge metric and what coefficient is fixed.

### Gate BZ — spacetime adiabatic versus moduli Hessian

Do **not** identify a moduli-space Hessian with a spacetime sigma kinetic term automatically. Derive, or explicitly fail to derive, the adiabatic \((\partial\tau)^2\) term for a slowly varying family \(\tau(x)\).

### Gate CA — theta / Quillen consistency

Compare the result with Models I, II, V, and X: theta-state Gram determinants, Hodge curvature, Quillen metric, and the existing determinant/Hodge identities must use compatible normalizations.

### Gate CB — no-fit prediction test

No adjustable \(V_i(\tau)\) are allowed. The spectrum, regularization, and modular transformation law must be fixed before the target metric is compared.

**Pass condition:** an intrinsic spectral calculation either yields a fixed Poincare/Hodge response from the actual elliptic spectrum or gives a clean no-go separating spectral determinant curvature from spacetime realization dynamics.

---

## Gravity Closure gate — NOT ACTIVE

Even a successful intrinsic spectral metric remains a matter/moduli response sector. Lorentzian gravitational/horizon closure is separate.