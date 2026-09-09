# FCIG Model XVII — Realization-map / sigma-model dynamics audit

**Status:** Established harmonic-map geometry + derived FCIG realization/coupling audit.  
**Milestone:** v0.17.  
**Scope:** dynamics for the realization map \(\Phi\), elliptic upper-half-plane target, stress tensor, pullback Hodge curvature, modular quotient, and constitutive-input boundaries.  
**Not claimed:** that the sigma-model normalization is derived from FCIG, that \(\Phi\) is spacetime gravity, or that an Einstein equation follows.

---

## 1. Problem left by Model XVI

Model XVI constructed the conditional bridge

\[
(\mathscr L_{\rm FCIG},\nabla^{\rm FCIG})
+\Phi:M\to\mathcal B_{\rm FCIG}
\longrightarrow
P_\Phi
\longrightarrow
W_{1\text{-loop}}^{\rm ren}[g,\Phi].
\]

The new unexplained object was the realization map \(\Phi\).

The present model asks whether \(\Phi\) can be treated as a genuine spacetime field using target geometry which FCIG already possesses, rather than inventing a new target metric for convenience.

For the first exact test, choose the elliptic/modular model developed in Models I--II.

---

## 2. Concrete FCIG target: the elliptic upper half-plane

Write

\[
\tau=u+iY,
\qquad
Y>0,
\]

so the universal cover of elliptic-curve moduli is the upper half-plane

\[
\mathbb H=\{u+iY\mid Y>0\}.
\]

Use the standard Poincare metric

\[
\boxed{
 ds_{\mathbb H}^2
 =\frac{du^2+dY^2}{Y^2}.
}
\]

This metric is not introduced ad hoc for Model XVII: the same hyperbolic/Hodge geometry already appeared in the FCIG elliptic determinant-curvature calculation. The modular group acts by isometries. Standard harmonic-map geometry is due to Eells--Sampson [ES64]; the elliptic/theta/modular background is standard in Mumford and Birkenhake--Lange [Mum83, BL04].

Let the physical Euclidean background be a Riemannian four-manifold \((M,g)\) and promote

\[
\boxed{
\Phi:M\to\mathbb H,
\qquad
\Phi(x)=\tau(x)=u(x)+iY(x),
}
\]

to a field.

---

## 3. Sigma-model action

The canonical two-derivative harmonic-map energy associated with the target metric is

\[
\boxed{
S_\Phi
=\frac{Z_\Phi}{2}
\int_M\sqrt g\,
\frac{
\partial_\mu u\,\partial^\mu u
+\partial_\mu Y\,\partial^\mu Y
}{Y^2}.
}
\]

Here \(Z_\Phi\) is an overall coupling/normalization.

### Citation boundary

The energy functional and its tension-field Euler--Lagrange equation are standard harmonic-map geometry [ES64]. The choice of the particular target \(\mathbb H\) is inherited from the FCIG elliptic model. The assertion that \(Z_\Phi\) is **not yet fixed** by previous FCIG results is Derived here.

In four spacetime dimensions, if \(u,Y\) are dimensionless, \(Z_\Phi\) has mass dimension two. Nothing in Models I--XVI fixes its physical value.

---

## 4. Target Christoffel symbols and harmonic-map equations

For

\[
G_{uu}=G_{YY}=Y^{-2},
\qquad
G_{uY}=0,
\]

the nonzero Christoffel symbols are

\[
\boxed{
\Gamma^u{}_{uY}=\Gamma^u{}_{Yu}=-\frac1Y,
\qquad
\Gamma^Y{}_{uu}=\frac1Y,
\qquad
\Gamma^Y{}_{YY}=-\frac1Y.
}
\]

The standard harmonic-map equation

\[
\tau^A(\Phi)
=\Box_g\Phi^A
+\Gamma^A{}_{BC}(\Phi)
\partial_\mu\Phi^B\partial^\mu\Phi^C
=0
\]

therefore becomes

\[
\boxed{
\Box_g u
-\frac{2}{Y}\,
\partial_\mu u\,\partial^\mu Y
=0,
}
\]

and

\[
\boxed{
\Box_g Y
+\frac1Y
\left(
\partial_\mu u\,\partial^\mu u
-\partial_\mu Y\,\partial^\mu Y
\right)
=0.
}
\]

These equations are Derived here from the standard tension-field formula in the stated target coordinates.

---

## 5. Spacetime stress tensor of the realization map

Metric variation gives the ordinary sigma-model stress tensor

\[
\boxed{
T^{(\Phi)}_{\mu\nu}
=\frac{Z_\Phi}{Y^2}
\left[
\partial_\mu u\partial_\nu u
+\partial_\mu Y\partial_\nu Y
-\frac12g_{\mu\nu}
\left((\partial u)^2+(\partial Y)^2\right)
\right].
}
\]

This is a genuine spacetime first response of the supplied sigma-model action.

It must not be confused with

- the FCIG determinant-line curvature on target/moduli space;
- the pulled-back line curvature used in Model XVI;
- the spacetime Riemann tensor.

Thus Model XVII does not undo the type distinctions established in Models XI and XIV.

---

## 6. Hodge curvature as a target two-form

In the elliptic model, the Hodge line has curvature proportional to the hyperbolic area form. It is useful to work with the normalized real Chern form

\[
\mathfrak f_H
:=\frac{i}{2\pi}F_{\lambda_H}.
\]

With the Model-I convention,

\[
\boxed{
\mathfrak f_H
=\frac{1}{4\pi}\,\omega_{\rm hyp},
\qquad
\omega_{\rm hyp}
=\frac{du\wedge dY}{Y^2}.
}
\]

Equivalently, the unitary curvature is recovered from

\[
F_{\lambda_H}=-2\pi i\,\mathfrak f_H.
\]

The exact factor is convention dependent; the relation above fixes the convention used in the existing FCIG elliptic note.

---

## 7. Pullback curvature controlled by \(\Phi\)

Pull the normalized Hodge curvature to spacetime:

\[
\boxed{
\Phi^*\mathfrak f_H
=\frac{1}{4\pi Y^2}\,du\wedge dY.
}
\]

In components,

\[
\boxed{
(\Phi^*\mathfrak f_H)_{\mu\nu}
=\frac{1}{4\pi Y^2}
\left(
\partial_\mu u\,\partial_\nu Y
-\partial_\nu u\,\partial_\mu Y
\right).
}
\]

Thus the physical bundle curvature of Model XVI is no longer an arbitrary spacetime two-form once \(\Phi\) is dynamical: it is a composite of the realization field.

For the anti-Hermitian line curvature \(\Omega=\Phi^*F_{\lambda_H}\), the standard heat coefficient contains

\[
\boxed{
 b_4\supset\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}.
}
\]

The sign of the corresponding real \(\mathfrak f_H^2\) expression follows from the anti-Hermitian curvature convention; Model XVII keeps this conversion separate rather than silently changing conventions.

---

## 8. A crucial degree result: heat-kernel curvature does not generate the sigma kinetic term

The pullback curvature is bilinear in first derivatives of \(\Phi\):

\[
\Phi^*\mathfrak f_H
\sim
\frac{du\wedge dY}{Y^2}.
\]

Therefore

\[
\boxed{
(\Phi^*\mathfrak f_H)_{\mu\nu}
(\Phi^*\mathfrak f_H)^{\mu\nu}
}
\]

is **quartic in first derivatives** of \(u,Y\).

By contrast, the harmonic-map kinetic action is quadratic in first derivatives:

\[
S_\Phi\sim
Z_\Phi\int G_{AB}(\Phi)\partial\Phi^A\partial\Phi^B.
\]

Hence the Model-XVI \(b_4\) curvature term does not determine the coefficient \(Z_\Phi\):

\[
\boxed{
\Omega^2\text{ heat-kernel term}
\not\Rightarrow
\text{two-derivative sigma-model normalization}.
}
\]

This is the central constitutive-input no-go of Model XVII.

A two-derivative term could arise only from additional operator dependence or another microscopic/effective-action mechanism which must be exhibited explicitly.

---

## 9. Combined effective system

A controlled effective model may nevertheless be written as

\[
\boxed{
S_{\rm eff}[g,\Phi]
=S_{\rm grav}^{\rm ren}[g]
+S_\Phi[g,\Phi]
+W_{1\text{-loop}}^{\rm ren}[g,\Phi]
+\cdots.
}
\]

Then the \(\Phi\) equation is schematically

\[
\boxed{
Z_\Phi\,\tau^A(\Phi)
+\frac{1}{\sqrt g}
\frac{\delta W_{1\text{-loop}}^{\rm ren}}{\delta\Phi^A}
=0,
}
\]

with normalization depending on the coordinate/index convention.

The metric equation receives both

\[
T^{(\Phi)}_{\mu\nu}
\]

and the metric variation of the determinant effective action.

This is a legitimate coupled EFT once all couplings and renormalization conditions are stated. It is not derived from the anomaly class alone.

---

## 10. Explicit witness I: vertical geodesic sector

Take

\[
u(x)=u_0,
\qquad
Y(x)=e^{\varphi(x)}.
\]

Then the \(u\) equation is automatic and the \(Y\) equation reduces exactly to

\[
\boxed{\Box_g\varphi=0.}
\]

The sigma-model action becomes

\[
\boxed{
S_\Phi
=\frac{Z_\Phi}{2}
\int_M\sqrt g\,(\partial\varphi)^2.
}
\]

However,

\[
 du=0
\quad\Longrightarrow\quad
\boxed{\Phi^*\mathfrak f_H=0.}
\]

This gives an explicit nontrivial realization-map dynamics whose pulled-back Hodge curvature vanishes.

Therefore

\[
\boxed{
T^{(\Phi)}_{\mu\nu}\neq0
\quad\text{can coexist with}\quad
\Omega=0.
}
\]

This is another concrete proof that the sigma stress tensor is not determined by the determinant-line curvature.

---

## 11. Explicit witness II: nonzero Hodge-curvature sector

Let the four-dimensional background locally factor as

\[
M\supset\Sigma\times N,
\]

where \(\Sigma\) is a two-dimensional hyperbolic patch with coordinates \((u,Y)\) and metric

\[
(ds_\Sigma)^2=\frac{du^2+dY^2}{Y^2}.
\]

Take \(\Phi\) to be the identity map on \(\Sigma\) and constant along \(N\).

The identity is a harmonic map between identical Riemannian targets, and

\[
\boxed{
\Phi^*\omega_{\rm hyp}=\omega_\Sigma\neq0.
}
\]

Thus this sector activates the Hodge-curvature-squared contribution in Model XVI.

The vertical-geodesic and identity-map examples demonstrate that nontrivial \(\Phi\) dynamics and nonzero pulled-back FCIG curvature are logically independent conditions.

---

## 12. Modular quotient and global structure

The true elliptic moduli target is not simply \(\mathbb H\) but the modular orbifold/stack

\[
\mathcal M_{1,1}\simeq[\mathbb H/SL(2,\mathbf Z)]
\]

(up to the standard stack/orbifold qualifications). The Poincare metric and its area form are modular invariant, so the local sigma-model energy descends.

However, the Hodge/theta lines carry nontrivial automorphy and the earlier FCIG modular models showed projective/metaplectic holonomy. Therefore a global realization map into the quotient can carry monodromy around spacetime loops.

### Derived global conclusion

The local fields \((u,Y)\) should be viewed as local lifts of an orbifold-valued map when nontrivial modular monodromy is present. The sigma kinetic density may patch invariantly while the pulled-back FCIG line retains global holonomy data.

Thus Model XVII preserves the hierarchy

\[
\boxed{
\text{local target metric}
\oplus
\text{local pulled-back curvature}
\oplus
\text{global modular/line holonomy}.
}
\]

A complete global treatment should use the moduli stack/orbifold rather than a single global \(\tau\) coordinate.

---

## 13. Renormalization / EFT audit

In four dimensions the coefficient \(Z_\Phi\) is dimensionful for dimensionless target coordinates. The nonlinear target geometry produces an effective field theory rather than a parameter-free universal sigma model.

The v0.16 one-loop \(\Omega^2\) term is a separate higher-order interaction in \(\partial\Phi\), and its coefficient is itself subject to the renormalization audit already imposed there.

Therefore a predictive realization-map theory requires at minimum

1. a physical normalization/renormalization condition for \(Z_\Phi\);
2. a rule fixing the relation between the physical operator and the pulled-back FCIG line;
3. control of higher-order target-space invariants/counterterms;
4. a global prescription for modular/orbifold sectors.

---

## 14. Gate audit

### Gate BI — target metric provenance: PASS

The Poincare metric is already part of the elliptic/Hodge FCIG target geometry; no new target metric is invented.

### Gate BJ — harmonic-map equation: PASS

The explicit \(u,Y\) equations follow from the standard Eells--Sampson energy/tension formalism.

### Gate BK — stress tensor: PASS

The realization-map stress tensor is explicit and remains distinct from anomaly-line curvature and spacetime frame curvature.

### Gate BL — pulled-back line coupling: PASS

The normalized Hodge curvature pulls back to

\[
\frac{1}{4\pi Y^2}du\wedge dY,
\]

and the corresponding line curvature enters the Model-XVI \(b_4\) coefficient.

### Gate BM — constitutive-input audit: PASS WITH NO-GO

The pulled-back curvature-squared heat-kernel term is quartic in \(\partial\Phi\) and therefore does not fix the two-derivative sigma-model coefficient \(Z_\Phi\). That normalization remains external unless a further microscopic derivation is supplied.

### Gate BN — modular quotient/global audit: PASS WITH STACK/ORBIFOLD REQUIREMENT

The local Poincare sigma model descends under modular transformations, while global Hodge/theta line data can retain modular/metaplectic holonomy. Global nontrivial sectors require orbifold/stack patching.

### Gate BO — explicit witness/falsification: PASS

The vertical-geodesic sector gives nontrivial sigma dynamics with zero pulled-back curvature; the identity-map hyperbolic sector gives nonzero pulled-back curvature. A proposal which equates sigma stress with Hodge curvature is therefore falsified by the first witness.

---

## 15. Main result of v0.17

The realization map can be made dynamical in a completely typed way:

\[
\boxed{
(M,g)
\xrightarrow{\Phi}
(\mathbb H,G_{\rm hyp},\lambda_H,\nabla^H),
}
\]

with

\[
S_\Phi
\quad\text{and}\quad
\Omega=\Phi^*F_H
\]

coexisting as **different target-geometric structures**.

The resulting chain is

\[
\boxed{
\text{FCIG target metric}
\to S_\Phi\to T^{(\Phi)}_{\mu\nu},
\qquad
\text{FCIG Hodge connection}
\to\Omega\to W_{1\text{-loop}}.
}
\]

This is stronger than an arbitrary realization map, but it remains conditional because the overall sigma-model normalization and the physical choice of target sector are not yet derived from microscopic FCIG data.

---

## 16. Next target

**v0.18 — induced realization-map dynamics from determinants.**

Instead of postulating \(Z_\Phi\), the next test should ask whether integrating out an explicit operator whose parameters vary with \(\Phi\) generates a two-derivative target-space kinetic term.

The standard mechanism to audit is a derivative expansion of

\[
W[\Phi]=\frac12\log\det P(\Phi),
\]

where \(E(\Phi)\), masses, or bundle connections depend on slowly varying \(\Phi\). The target is to compute the coefficient of

\[
\partial_\mu\Phi^A\partial^\mu\Phi^B
\]

and determine whether the induced metric is related to a pre-existing FCIG Fisher/Hodge metric or is a different spectral metric.

Only such a calculation could turn the sigma-model normalization from constitutive input into a derived quantity.

---

## References used in this model

- [ES64] J. Eells, Jr. and J. H. Sampson, *Harmonic Mappings of Riemannian Manifolds*, American Journal of Mathematics **86** (1964), 109--160, DOI 10.2307/2373037.
- [Mum83] D. Mumford, *Tata Lectures on Theta I*, Birkhauser (1983).
- [BL04] C. Birkenhake and H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer (2004).
- Vassilevich (2003) and Gilkey (1995), as cited in Model XVI, for the heat-kernel bundle-curvature insertion.

### Citation boundary

The harmonic-map energy/tension formalism and modular upper-half-plane geometry are established background. The specific FCIG realization-map model, the pullback-coupling hierarchy, the vertical-geodesic/identity witnesses, and the no-go separating \(\Omega^2\) from the two-derivative sigma normalization are **Derived here / conditional construction**.