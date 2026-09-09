# FCIG Research Roadmap

**Current target:** v0.20 — adiabatic elliptic family / Kaluza--Klein response  
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

Thus one species has rank at most one, two species are degenerate or locally flat, and sufficiently free higher-dimensional mass maps turn local metric matching into inverse design. FCIG prediction requires an intrinsic operator/spectrum fixed independently of the desired target metric.

Sources: `induced-metric.md`, `induced-metric.py`, `induced-metric.bib`.

---

## v0.19 — intrinsic elliptic spectral metric — COMPLETE WITH EXACT SPECTRAL--HODGE IDENTITY

Sources:

- `intrinsic-spectral.md`
- `intrinsic-spectral.py`
- `intrinsic-spectral.bib`

### Gate BW — exact spectral normalization — PASS

For

\[
E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z),
\qquad
 ds_\tau^2=\frac{|dz|^2}{Y},
\qquad \tau=u+iY,
\]

the metric has unit area. With \(z=x+\tau t\),

\[
\boxed{
\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad (m,n)\in\mathbb Z^2.
}
\]

Only \((0,0)\) is a zero mode.

### Gate BX — spectral zeta / Kronecker audit — PASS

The nonzero spectral zeta function is

\[
\zeta_{\Delta_\tau}(s)
=(4\pi^2)^{-s}
\sum_{(m,n)\ne(0,0)}\frac{Y^s}{|m\tau-n|^{2s}}.
\]

The Kronecker limit formula yields

\[
\boxed{
\det{}'\Delta_\tau=Y|\eta(\tau)|^4.
}
\]

The normalization is fixed by the area-one metric and zeta regularization; no adjustable mass functions occur.

### Gate BY — intrinsic moduli curvature — PASS WITH EXACT IDENTITY

Since \(\eta\) is holomorphic and nonvanishing on \(\mathbb H\),

\[
\partial\bar\partial\log|\eta|^4=0.
\]

Therefore

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=-\partial\bar\partial\log Y
=\frac1{4Y^2}d\tau\wedge d\bar\tau.
}
\]

Model I fixed

\[
F_{\lambda_H}=-\partial\bar\partial\log Y
=\frac1{4Y^2}d\tau\wedge d\bar\tau,
\]

hence

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=F_{\lambda_H}.
}
\]

This is the exact intrinsic spectral--Hodge identity of Model XIX.

### Gate BZ — modular/global audit — PASS

The spectrum is modular invariant as a multiset by the lattice relabeling

\[
(m,n)\mapsto(am-cn,\;dn-bm)
\]

for \(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in SL(2,\mathbb Z)\).

The Dedekind eta transformation law and

\[
Y\mapsto\frac{Y}{|c\tau+d|^2}
\]

imply

\[
\boxed{Y'|\eta(\tau')|^4=Y|\eta(\tau)|^4.}
\]

The zeta determinant therefore descends as a modular invariant scalar.

### Gate CA — Quillen/Hodge consistency — PASS WITH OBJECT DISTINCTION

The spectral determinant curvature matches the Hodge-line curvature in the genus-one convention already fixed by Models I--II. This is a spectral consistency closure inside the Ray--Singer/Quillen determinant framework; it does not identify every determinant line or every scalar Laplacian determinant appearing elsewhere in FCIG.

### Gate CB — Hessian versus spacetime kinetic term — PASS WITH TYPE NO-GO

The derived object is a \((1,1)\) curvature/Hessian on the moduli space of **constant** elliptic structures. It does not by itself imply

\[
\int_M\sqrt g\,\frac{\partial_\mu\tau\partial^\mu\bar\tau}{Y^2}.
\]

A spacetime kinetic coefficient requires a genuine family \(\tau=\tau(x)\), a total-space/fibered physical operator and an adiabatic derivative expansion. The full real Hessian of \(\log|\eta|^4\) also contains harmonic trace-free information, so the canonical equality is the Chern/mixed-complex one above.

### Gate CC — no-fit prediction test — PASS

The area-one metric, lattice, operator, spectrum, zeta prescription and modular transformation law are all fixed before comparison with the Hodge curvature. The equality is therefore not obtained by inverse-designing spectral masses.

### v0.19 conclusion

\[
\boxed{
\text{actual elliptic lattice spectrum}
\to\det{}'\Delta_\tau
\to-\partial\bar\partial\log\det{}'\Delta_\tau
=F_{\lambda_H}.
}
\]

This is the first FCIG model where a pre-existing target curvature is regenerated exactly from the intrinsic full spectrum with no adjustable spectral map.

References: Ray--Singer (1973); Quillen (1985); Osgood--Phillips--Sarnak (1988); Faulhuber (2020/2021); NIST DLMF Chapter 23.

---

## v0.20 — adiabatic elliptic family / Kaluza--Klein response — ACTIVE

The remaining problem is to turn the constant-modulus spectral identity into a genuine spacetime/base response for \(\tau=\tau(x)\).

### Gate CD — total-space family geometry

Specify a base \(M\), an elliptic fiber with area-one metric depending on \(\tau(x)\), and a total-space metric/operator. The construction must state whether horizontal distributions, Kaluza--Klein gauge fields and fiber-volume modes are frozen or dynamical.

### Gate CE — mode-basis connection and mixing

The instantaneous Fourier/eigenmode basis varies with \(x\). Derive the induced Berry/adiabatic connection and off-diagonal mode mixing rather than replacing the tower by independent scalar masses \(\lambda_{m,n}(\tau(x))\) by fiat.

### Gate CF — modular-covariant tower regularization

Regularize the infinite KK/spectral tower by a prescription compatible with the modular lattice symmetry. Track local counterterms separately from finite threshold/nonlocal terms.

### Gate CG — genuine two-derivative spacetime response

Compute the coefficient of

\[
\int_M\sqrt g\,
G^{\rm ad}_{\tau\bar\tau}(\tau)
\partial_\mu\tau\partial^\mu\bar\tau
\]

from the total family operator. Determine whether \(G^{\rm ad}\) is a fixed multiple of the Poincare metric.

### Gate CH — compare three geometries

Keep distinct and compare:

1. Model XVII's postulated harmonic-map target metric;
2. Model XIX's intrinsic moduli Chern curvature;
3. Model XX's derived spacetime adiabatic kinetic metric.

Equality of any two is a theorem to prove, not a convention.

### Gate CI — cusp / degeneration test

Study \(Y\to\infty\), where the elliptic torus degenerates and light KK modes appear. A trustworthy adiabatic expansion must state its domain of validity and failure scale.

### Gate CJ — no-gravity-overclaim gate

Even if a Poincare kinetic metric is induced exactly, it is a moduli/matter sector. It does not by itself derive an Einstein equation or local horizon entropy law.

**Pass condition:** a modularly controlled total-space calculation that produces a spacetime two-derivative modulus response and cleanly relates or distinguishes it from the exact Model-XIX spectral-Hodge curvature.

---

## Gravity Closure gate — NOT ACTIVE

Lorentzian gravitational/horizon closure remains separate until an independently justified causal/dynamical bridge is supplied.