# FCIG Research Roadmap

**Current target:** v0.21 — field-content / supertrace completion audit  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are retained as explicit no-go results.

---

## v0.3–v0.17 — geometry through realization-map dynamics — COMPLETE

Earlier milestones establish the determinant/differential-cohomology foundation, local/global anomaly hierarchy, pushforward and reconstruction no-gos, mixed anomaly descent, functional-response ambiguity, conditional semiclassical closure, the explicit heat-kernel operator bridge, and harmonic-map realization dynamics on the elliptic target.

---

## v0.18 — induced realization-map metric from determinants — COMPLETE WITH SPECTRAL-INPUT NO-GO

For diagonal heavy species,

\[
G^{\rm ind}_{AB}=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N},
\qquad s_i=\sqrt{V_i}.
\]

Thus one species has rank at most one, two species are degenerate or locally flat, and unconstrained higher-dimensional mass maps turn metric matching into inverse design. FCIG prediction requires an intrinsic operator/spectrum.

Sources: `induced-metric.md`, `induced-metric.py`, `induced-metric.bib`.

---

## v0.19 — intrinsic elliptic spectral metric — COMPLETE WITH EXACT SPECTRAL--HODGE IDENTITY

For the area-one torus,

\[
\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4.
\]

Hence

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=F_{\lambda_H}
=\frac1{4Y^2}d\tau\wedge d\bar\tau.
}
\]

This is a finite moduli-space Chern-curvature identity, not yet a spacetime kinetic term.

Sources: `intrinsic-spectral.md`, `intrinsic-spectral.py`, `intrinsic-spectral.bib`.

---

## v0.20 — adiabatic elliptic family / Kaluza--Klein response — COMPLETE IN THE RESTRICTED SCALAR MODEL

Sources:

- `adiabatic-elliptic.md`
- `adiabatic-elliptic.py`
- `adiabatic-elliptic.bib`

### Gate CD — total-space geometry — PASS

For

\[
 ds_6^2=g_{\mu\nu}dx^\mu dx^\nu+L^2G_{ab}(\tau(x))dy^ady^b,
\qquad
\det G=1,
\]

with

\[
G(\tau)=\frac1Y
\begin{pmatrix}
1&u\\
u&u^2+Y^2
\end{pmatrix},
\]

one finds

\[
\boxed{
R_6=R_4-\frac1{2Y^2}\partial_\mu\tau\partial^\mu\bar\tau.
}
\]

The Poincare tensor shape is intrinsic to the fixed-volume torus geometry.

### Gate CE — mode decomposition — PASS WITH CORRECTION

In the locally trivial block-diagonal scalar model, the coordinate Fourier basis is \(\tau\)-independent. Hence there is no local Berry/off-diagonal mode mixing and

\[
\boxed{
M_{m,n}^2(\tau)=\frac{4\pi^2}{L^2Y}|m\tau-n|^2.
}
\]

Global modular monodromy and nontrivial torus bundles remain separate extensions.

### Gate CF — local one-loop response — PASS WITH RENORMALIZATION NO-GO

The six-dimensional heat kernel gives

\[
W_{\rm div}^{(\tau)}
=\frac{\Lambda^4L^2}{48(4\pi)^3}
\int\sqrt{g_4}\,
\frac{\partial_\mu\tau\partial^\mu\bar\tau}{Y^2}
\]

in the fixed sharp proper-time convention. This Poincare-shaped normalization is a local Einstein--Hilbert/shape-modulus counterterm and is not parameter-free.

### Gate CG — Epstein finite-part tower — PASS

Let

\[
Q_{m,n}=\frac{|m\tau-n|^2}{Y},
\qquad
Z_\tau(s)=\sum{}'Q_{m,n}^{-s}.
\]

For the hyperbolic metric \(g_{\rm hyp}\), every lattice form satisfies

\[
\boxed{
\nabla^2Q=Qg_{\rm hyp},
\qquad
|dQ|_{g_{\rm hyp}}^2=Q^2.
}
\]

The determinant-one Epstein functional equation gives

\[
Z_\tau(-1)=0,
\qquad
Z_\tau'(-1)=-\frac1{\pi^3}Z_\tau(2).
\]

Therefore the analytically subtracted tower tensor is

\[
\boxed{
\mathcal T^{\rm fin}_{AB}
=\frac1{\pi^3}
\left(\nabla_A\nabla_BZ_\tau(2)-Z_\tau(2)g^{\rm hyp}_{AB}\right).
}
\]

### Gate CH — finite modular threshold — PASS WITH TRACE-FREE THEOREM

Since

\[
\Delta_{\rm hyp}Z_\tau(2)=2Z_\tau(2),
\]

\[
\boxed{
\operatorname{tr}_{g_{\rm hyp}}\mathcal T^{\rm fin}=0.
}
\]

Thus the finite nonlocal two-derivative threshold is not another constant multiple of the Poincare metric. The Poincare trace sector is the local renormalization sector.

### Gate CI — holomorphic weight-four form — PASS

Define

\[
\mathcal G_4(\tau)=\sum{}'(m\tau-n)^{-4}.
\]

Then

\[
\boxed{
\mathcal T^{\rm fin}
=-\frac3{\pi^3}\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2],
}
\]

and the physical one-real-scalar finite threshold is

\[
\boxed{
G^{\rm fin}_{(2)}
=-\frac1{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2].
}
\]

Because \(\mathcal G_4\) has modular weight four and \((d\tau)^2\) weight minus four, the tensor is modular invariant.

### Gate CJ — positivity / type audit — PASS WITH NO-GO

A nonzero trace-free symmetric tensor in two real dimensions is indefinite. Therefore the finite threshold alone is not a positive sigma metric. The renormalized kinetic tensor is

\[
\boxed{
G^{\rm ren}=Z_Rg_{\rm hyp}+G^{\rm fin}_{(2)}+\cdots,
}
\]

where \(Z_R\) is an independently renormalized local coupling.

### Gate CK — Model XIX versus XX — PASS WITH STRICT DISTINCTION

\[
\boxed{
\begin{array}{ll}
\text{Model XIX:}&-\partial\bar\partial\log\det{}'\Delta=F_{\lambda_H}\quad\text{finite }(1,1)\text{ moduli curvature},\\
\text{Model XX:}&G^{\rm fin}_{(2)}\propto\operatorname{Re}[\mathcal G_4(d\tau)^2]\quad\text{finite trace-free spacetime threshold}.
\end{array}}
\]

They are different tensor projections of the same elliptic spectral family, not objects to be identified.

### Gate CL — cusp / EFT validity — PASS

As \(Y\to\infty\), \(M_{0,n}^2\to0\), so integrating out the whole nonzero tower fails uniformly. The cusp is an explicit EFT validity boundary.

### v0.20 conclusion

\[
\boxed{
\text{local: }Z_Rg_{\rm hyp}
\quad\oplus\quad
\text{finite: }-\frac1{16\pi^3L^2}\operatorname{Re}[\mathcal G_4(d\tau)^2].
}
\]

References: Maharana--Schwarz (1993); Vassilevich (2003); von Gersdorff (2008); Terras (1980, 2013); Apostol (1990).

---

## v0.21 — field-content / supertrace completion audit — ACTIVE

The scalar result is now exact enough to ask the next physical question: what happens for a **fixed microscopic multiplet** rather than one real scalar?

### Gate CM — determinant/statistics normalization

Fix the one-loop signs and multiplicities for real/complex scalars, Dirac/Weyl fermions, vectors and ghosts. Do not infer fermionic or vector answers by multiplying the scalar result unless the squared operators and connection/endormorphism terms justify it.

### Gate CN — intrinsic torus operators by spin

Write the actual torus/Kaluza--Klein spectra and Laplace-type operators for each field representation in the same fixed-volume elliptic background. Track spin connection, bundle curvature and gauge-fixing/ghost operators explicitly.

### Gate CO — local supertrace sector

Compute the combined heat-kernel two-derivative trace sector. Determine when the Poincare-shaped local divergence cancels or renormalizes a residual coupling.

### Gate CP — finite weight-four threshold

Compute the coefficient multiplying

\[
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2]
\]

for the specified field content. Determine whether statistics/spin cancel the scalar threshold, rescale it, or introduce additional automorphic tensors.

### Gate CQ — positivity and EFT interpretation

Determine whether the complete renormalized target-space kinetic tensor can be positive and whether positivity constrains the local coefficient \(Z_R\). A trace-free threshold cannot supply positivity by itself.

### Gate CR — anomaly / determinant-line consistency

Compare the same field content with its determinant/anomaly line and index polynomial. Kinetic threshold, anomaly and Quillen curvature remain distinct observables even when generated by the same microscopic fields.

### Gate CS — no multiplet fitting

The field content must be specified independently by a geometric or physical model. Choosing boson/fermion multiplicities merely to cancel or reproduce a desired tensor is not an FCIG prediction.

**Pass condition:** an explicit field-content supertrace calculation that fixes the local and finite two-derivative elliptic response and states all remaining renormalized inputs.

---

## Gravity Closure gate — NOT ACTIVE

Lorentzian gravitational/horizon closure remains separate until an independently justified causal/dynamical bridge is supplied.
