# FCIG Research Roadmap

**Current target:** v0.22 — spin-connection automorphic threshold  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations are retained as explicit no-go results.

---

## v0.3–v0.17 — geometry through realization-map dynamics — COMPLETE

Earlier milestones establish the determinant/differential-cohomology foundation, local/global anomaly hierarchy, pushforward and reconstruction no-gos, mixed anomaly descent, functional-response ambiguity, conditional semiclassical closure, the explicit heat-kernel operator bridge, and harmonic-map realization dynamics on the elliptic target.

---

## v0.18 — induced realization-map metric — COMPLETE WITH SPECTRAL-INPUT NO-GO

For diagonal heavy scalars,

\[
G^{\rm ind}_{AB}
=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N}.
\]

Arbitrary masses turn target-metric matching into inverse design; prediction requires an intrinsic operator/spectrum.

---

## v0.19 — intrinsic elliptic spectral metric — COMPLETE

For the area-one torus,

\[
\lambda_{m,n}=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4,
\]

and

\[
\boxed{-\partial\bar\partial\log\det{}'\Delta_\tau=F_{\lambda_H}.}
\]

This is a finite moduli-space Chern-curvature identity.

---

## v0.20 — adiabatic elliptic / KK response — COMPLETE IN THE RESTRICTED REAL-SCALAR MODEL

For the fixed-volume elliptic family,

\[
R_6=R_4-\frac1{2Y^2}\partial_\mu\tau\partial^\mu\bar\tau,
\qquad
M_{m,n}^2=\frac{4\pi^2}{L^2Y}|m\tau-n|^2.
\]

The local Poincare-shaped two-derivative normalization is UV/counterterm sensitive. Epstein analytic continuation gives the finite one-real-scalar response

\[
\boxed{
G^{\rm fin}_{(2)}
=-\frac1{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2],
\qquad
\operatorname{tr}_{g_{\rm hyp}}G^{\rm fin}_{(2)}=0.
}
\]

The finite threshold is modular, trace-free and not a positive sigma metric by itself.

---

## v0.21 — field-content / supertrace audit — COMPLETE WITH SPIN-CONNECTION OBSTRUCTION

Sources:

- `field-content-supertrace.md`
- `field-content-supertrace.py`
- `field-content-supertrace.bib`

### Gate CM — determinant/statistics normalization — PASS

Use

\[
W_0=\frac12\log\det\Delta_0,
\qquad
W_{1/2}^{\rm even}=-\frac12\log\det\slashed D^2,
\qquad
W_1=\frac12\log\det\Delta_1-\log\det\Delta_0.
\]

Fermion phases/chiral anomalies remain separate.

### Gate CN — local Laplace-type operators — PASS

With

\[
P=-(\nabla^2+E),
\qquad b_2=E+\frac16R,
\]

- real scalar: \(E=0\);
- Dirac: \(\slashed D^2=-\nabla^2+R/4\), hence \(E=-R/4\);
- one-form: \(\Delta_1=-\nabla^2+\mathrm{Ric}\), hence \(E=-\mathrm{Ric}\), plus the complex scalar FP ghost.

### Gate CO — exact local supertrace — PASS WITH DEGREE-COUNT NO-GO

In six dimensions, normalized to one real minimal scalar,

\[
\boxed{
\text{real scalar : complex Dirac : Maxwell+ghost}=1:4:-2.
}
\]

Therefore

\[
\boxed{C_{\rm loc}=N_{\rm real\ scalar}+4N_{\rm Dirac}-2N_{\rm Maxwell}.}
\]

The result is not the naive signed count of physical polarizations; curvature endomorphisms and ghosts matter.

### Gate CP — physical local multiplet witness — PASS

A 6d \(\mathcal N=(1,0)\) vector multiplet contains Maxwell plus one symplectic-Majorana-Weyl gaugino. Its parity-even local coefficient is

\[
\boxed{-2+2=0.}
\]

Thus the local \(R_6\)/Poincare-trace one-loop coefficient cancels in this specified multiplet. This does not imply anomaly or finite-threshold cancellation.

### Gate CQ — scalar-type finite multiplicity — PASS

For a trivial spectator bundle with quadratic operator exactly \(-\Delta_6\otimes I_r\), determinant powers scale the Model-XX finite result exactly. With scalar-equivalent multiplicity \(\nu\),

\[
\boxed{
G^{\rm fin}_{\nu}
=-\frac{\nu}{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2].
}
\]

### Gate CR — true spin-field finite audit — PASS WITH STRUCTURAL NO-GO

A genuine spinor/vector operator contains nontrivial bundle connection and curvature endomorphism:

\[
\slashed D^2=-(\nabla_{\rm spin})^2+\frac14R,
\qquad
\Delta_1=-\nabla_{T^*}^2+\mathrm{Ric}.
\]

The periodic/winding heat kernel therefore depends on spin parallel transport and Lorentz-representation invariants such as \(\operatorname{tr}(\Sigma\Sigma)\). Hence

\[
\boxed{
G^{\rm fin}_{\rm spin>0}
\neq(\text{signed component count})G^{\rm fin}_{\rm scalar}
\quad\text{in general}.
}
\]

### Gate CS — original full-supertrace pass condition — FAILS AS STATED / REFACTORED

The original idea of fixing the full finite multiplet threshold by a species supertrace is false. The remaining calculation is representation-theoretic and is promoted to v0.22 rather than guessed.

### v0.21 conclusion

\[
\boxed{
\text{local field-content response is fixed,}
\qquad
\text{finite spin response requires spin-connection data.}
}
\]

References: Vassilevich (2003); Lawson--Michelsohn (1989); von Gersdorff (2008); Ferrara--Riccioni--Sagnotti (1998); Ohmori--Shimizu--Tachikawa--Yonekura (2014).

---

## v0.22 — spin-connection automorphic threshold — ACTIVE

The next milestone computes the representation-dependent finite threshold for genuine spin fields on the same elliptic family.

### Gate CT — internal spin connection

Choose an explicit orthonormal frame for

\[
G(\tau)=\frac1Y
\begin{pmatrix}1&u\\u&u^2+Y^2\end{pmatrix}
\]

and derive all base/fiber spin-connection components generated by \(\partial_\mu\tau\). Keep local SO(2) frame-gauge dependence separate from invariant traces.

### Gate CU — periodic spinor heat kernel

For the Dirac Laplace-type operator, compute the winding Wilson line / parallel transport and the curvature endomorphism contribution to quadratic order in \(\partial\tau\). Reduce all representation traces to fixed Spin(6) generator invariants.

### Gate CV — Maxwell plus ghost heat kernel

Repeat for the one-form Hodge Laplacian and combine the gauge field with its FP ghost before extracting any finite coefficient.

### Gate CW — automorphic decomposition

After Epstein analytic subtraction, decompose the finite tensor into allowed modular structures, including possible Poincare-trace terms proportional to nonholomorphic Eisenstein functions and trace-free weight-four terms.

### Gate CX — vector-multiplet test

Combine Maxwell+ghost with a symplectic-Majorana-Weyl gaugino and determine whether the local cancellation extends, fails, or partially survives in the finite automorphic sector.

### Gate CY — gauge/frame independence

Verify that the final tensor is independent of gauge-fixing and local internal-frame choices, up to allowed local counterterms.

### Gate CZ — no gravity overclaim

Even a fully fixed multiplet threshold remains a moduli/matter effective response and is not an Einstein equation or horizon law.

**Pass condition:** explicit Dirac and Maxwell+ghost finite coefficients/tensors with a checked physical vector-multiplet combination.

---

## Gravity Closure gate — NOT ACTIVE

Lorentzian gravitational/horizon closure remains separate until an independently justified causal/dynamical bridge is supplied.
