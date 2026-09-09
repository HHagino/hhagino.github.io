# FCIG Research Roadmap

**Current target:** v0.18 — induced realization-map dynamics from determinants  
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

Sources:

- `realization-sigma.md`
- `realization-sigma.py`
- `realization-sigma.bib`

### Gate BI — target metric provenance — PASS

Use the actual elliptic FCIG target

\[
\mathbb H=\{u+iY\mid Y>0\},
\qquad
 ds^2=\frac{du^2+dY^2}{Y^2}.
\]

This Poincare/Hodge geometry already belongs to Models I--II; no new target metric is invented.

### Gate BJ — harmonic-map dynamics — PASS

Promote \(\Phi=(u,Y):M\to\mathbb H\) with

\[
S_\Phi=\frac{Z_\Phi}{2}\int_M\sqrt g\,
\frac{(\partial u)^2+(\partial Y)^2}{Y^2}.
\]

The field equations are

\[
\boxed{
\Box u-\frac2Y\partial u\cdot\partial Y=0,
\qquad
\Box Y+\frac{(\partial u)^2-(\partial Y)^2}{Y}=0.
}
\]

They are the standard harmonic-map/tension equations for the upper-half-plane metric.

### Gate BK — stress tensor — PASS

\[
\boxed{
T^{(\Phi)}_{\mu\nu}
=\frac{Z_\Phi}{Y^2}
\left[
\partial_\mu u\partial_\nu u+
\partial_\mu Y\partial_\nu Y-
\frac12g_{\mu\nu}((\partial u)^2+(\partial Y)^2)
\right].
}
\]

This is an ordinary matter/realization-field stress tensor, not anomaly-line curvature and not frame curvature.

### Gate BL — pulled-back Hodge-line coupling — PASS

Using the existing elliptic normalization,

\[
\mathfrak f_H=\frac{i}{2\pi}F_{\lambda_H}
=\frac1{4\pi}\frac{du\wedge dY}{Y^2},
\]

so

\[
\boxed{
(\Phi^*\mathfrak f_H)_{\mu\nu}
=\frac{1}{4\pi Y^2}
(\partial_\mu u\partial_\nu Y-
\partial_\nu u\partial_\mu Y).
}
\]

The corresponding unitary curvature enters the Model-XVI \(b_4\) bundle-curvature term.

### Gate BM — constitutive-input audit — PASS WITH NO-GO

The pulled-back curvature is bilinear in first derivatives of \(\Phi\); its square is quartic. The sigma kinetic action is quadratic. Therefore

\[
\boxed{
\Omega^2\text{ heat-kernel term}
\not\Rightarrow
Z_\Phi\text{ or the two-derivative sigma kinetic term}.
}
\]

The normalization \(Z_\Phi\) remains external unless a further microscopic/determinant calculation generates it.

### Gate BN — modular quotient/global audit — PASS WITH STACK/ORBIFOLD REQUIREMENT

The Poincare metric and area form descend under the modular group, so the local sigma density is well-defined on the modular quotient. Hodge/theta lines can nevertheless retain modular/metaplectic holonomy; global nontrivial sectors require orbifold/stack patching rather than a single global \(\tau\) coordinate.

### Gate BO — explicit witness/falsification — PASS

1. **Vertical geodesic:** \(u=u_0,\ Y=e^\varphi\) gives \(\Box\varphi=0\) and nontrivial sigma stress but \(\Phi^*F_H=0\).
2. **Hyperbolic identity map:** on a hyperbolic two-dimensional factor, the identity map is harmonic and has nonzero pulled-back area/Hodge curvature.

Hence realization-map dynamics and line-curvature coupling are independent structures. Any proposal equating the sigma stress tensor with Hodge curvature is explicitly falsified.

### v0.17 conclusion

\[
\boxed{
\text{FCIG target metric}\to S_\Phi\to T^{(\Phi)}_{\mu\nu},
\qquad
\text{FCIG Hodge connection}\to\Phi^*F_H\to W_{1\text{-loop}}
}
\]

is now a fully typed coupled construction.

References: Eells--Sampson (1964); Mumford (1983); Birkenhake--Lange (2004); Vassilevich (2003).

---

## v0.18 — induced realization-map dynamics from determinants — ACTIVE

The next target is to determine whether \(Z_\Phi\) itself can be induced rather than postulated.

Take an explicit slowly varying operator family

\[
P(\Phi)
\]

and study

\[
W[\Phi]=\frac12\log\det P(\Phi).
\]

### Gate BP — explicit parameter-dependent operator

Choose a concrete mass/endormorphism/connection dependence on \(\Phi\), with all dimensions and symmetries fixed.

### Gate BQ — derivative expansion

Compute the two-derivative term

\[
W[\Phi]\supset\frac12\int_M\sqrt g\,
G^{\rm ind}_{AB}(\Phi)
\partial_\mu\Phi^A\partial^\mu\Phi^B.
\]

### Gate BR — induced metric comparison

Compare \(G^{\rm ind}_{AB}\) with the pre-existing Poincare/Hodge/Fisher metric. Equality, proportionality, and inequivalence are all allowed outcomes; no identification is assumed.

### Gate BS — positivity / signature audit

Determine when the induced kinetic metric is positive in the Euclidean effective theory and how analytic continuation affects the statement.

### Gate BT — renormalization audit

Separate divergent wave-function renormalization from finite threshold/nonlocal contributions and identify which normalization is physical.

### Gate BU — explicit falsification

The proposed derivation fails if the induced metric depends arbitrarily on an unmotivated operator parametrization, has the wrong symmetry, or cannot reproduce the target metric even in the simplest elliptic model.

**Pass condition:** derive an actual two-derivative coefficient from a specified determinant and compare it quantitatively with the existing FCIG target metric.

---

## Gravity Closure gate — NOT ACTIVE

Even an induced sigma model is an additional dynamical sector. A Lorentzian gravitational/horizon closure remains a separate later gate.