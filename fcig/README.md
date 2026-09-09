# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository separates **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research and citation policy
- `ROADMAP.md` — milestone gates
- `references.bib` — general bibliography
- milestone `.bib` files — source sets for individual models
- `citation-map.md` — citation provenance map
- `cited-synthesis.md` — citation-audited synthesis

## Completed sequence

\[
\boxed{
\text{theta / ppav}
\to\text{curved curves}
\to\text{Quillen / differential cohomology}
\to\text{Deligne--RR closure}
\to\text{anomaly / response audits}
\to\text{semiclassical closure}
\to\text{heat-kernel bridge}
\to\text{realization-map dynamics}
\to\text{induced determinant metric}
\to\text{intrinsic elliptic spectral curvature}
\to\text{adiabatic KK response}
\to\text{field-content supertrace audit}.
}
\]

Completed milestones: **v0.2–v0.21**. No derivation of Einstein dynamics from FCIG alone is claimed.

## Models I–X — geometric / determinant foundation

The elliptic, ppav and curved-curve laboratories establish exact theta/state counting, Bergman local/global sectors, determinant/Quillen geometry, differential characters, transgression, pushforward no-gos and the global metrized Deligne--Riemann--Roch closure

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

in the canonical smooth curve-family model.

## Model XI — structure-group bridge audit

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

The determinant connection retains trace/Ricci information but cannot reconstruct a generic nonabelian frame connection for \(n>1\).

## Models XII–XV — anomaly, response and conditional closure

With independent line and frame connections,

\[
\widehat c_1(L)\cup\widehat p_1(TM)\in\widehat H^6(M;\mathbf Z),
\qquad
[\widehat A(TM)\operatorname{ch}(L)]_{(6)}=\frac16c_1^3-\frac1{24}c_1p_1.
\]

Descent/inflow is explicit, but anomaly data alone do not determine the effective action or first response:

\[
\boxed{\text{same anomaly class}\not\Rightarrow\text{same }W,J,T_{\mu\nu}.}
\]

A gravitational equation only appears after supplying an independent renormalized variational principle.

## Models XVI–XVII — operator bridge and realization dynamics

For a supplied realization map \(\Phi:M\to\mathcal B_{\rm FCIG}\), pulled-back FCIG line curvature enters a physical Laplace-type operator through

\[
\boxed{b_4\supset\frac1{12}(\Phi^*F_{\rm FCIG})_{\mu\nu}(\Phi^*F_{\rm FCIG})^{\mu\nu}}.
\]

On the elliptic target

\[
\mathbb H=\{\tau=u+iY\mid Y>0\},
\qquad ds^2_{\mathbb H}=\frac{du^2+dY^2}{Y^2},
\]

\(\Phi=(u,Y)\) can be promoted to a harmonic-map field. Its two-derivative normalization is not fixed by the four-derivative curvature-square term.

## Model XVIII — induced determinant metric no-gos

For diagonal heavy scalars,

\[
\boxed{G^{\rm ind}_{AB}=\frac1{192\pi^2}\sum_i\frac{\partial_AV_i\partial_BV_i}{V_i}}
=\frac1{48\pi^2}s^*\delta_{\mathbb R^N},
\qquad s_i=\sqrt{V_i}.
\]

One species has rank at most one; two species are degenerate or locally flat; unconstrained higher-dimensional mass maps turn target-metric matching into inverse design.

Sources: `induced-metric.md`, `induced-metric.py`, `induced-metric.bib`.

## Model XIX — intrinsic spectral--Hodge identity

For the area-one elliptic torus,

\[
\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4.
\]

Therefore

\[
\boxed{
-\partial\bar\partial\log\det{}'\Delta_\tau
=\frac1{4Y^2}d\tau\wedge d\bar\tau
=F_{\lambda_H}.
}
\]

The actual full torus spectrum regenerates the Hodge curvature with the same coefficient and no adjustable spectral map.

Sources: `intrinsic-spectral.md`, `intrinsic-spectral.py`, `intrinsic-spectral.bib`.

## Model XX — adiabatic elliptic / Kaluza--Klein response

For the fixed-volume local torus family,

\[
M_{m,n}^2=\frac{4\pi^2}{L^2Y}|m\tau-n|^2,
\qquad
R_6=R_4-\frac1{2Y^2}\partial_\mu\tau\partial^\mu\bar\tau.
\]

The Poincare-shaped local kinetic coefficient is UV/counterterm sensitive. After Epstein analytic subtraction the finite one-real-scalar threshold is

\[
\boxed{
G^{\rm fin}_{(2)}
=-\frac1{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2],
\qquad
\operatorname{tr}_{g_{\rm hyp}}G^{\rm fin}_{(2)}=0.
}
\]

Thus Model XIX and Model XX are distinct spectral projections: finite \((1,1)\) Chern curvature versus finite trace-free spacetime response.

Sources: `adiabatic-elliptic.md`, `adiabatic-elliptic.py`, `adiabatic-elliptic.bib`.

## Model XXI — field-content / supertrace audit

- Web: `field-content-supertrace.html`
- Source: `field-content-supertrace.md`
- Checker: `field-content-supertrace.py`
- Milestone bibliography: `field-content-supertrace.bib`

Using the standard Laplace-type coefficient \(b_2=E+R/6\), the six-dimensional local \(R_6\) response, normalized to one real minimal scalar, is

\[
\boxed{
\text{real scalar : complex Dirac : Maxwell+ghost}=1:4:-2.
}
\]

Hence

\[
\boxed{
C_{\rm loc}=N_{\rm real\ scalar}+4N_{\rm Dirac}-2N_{\rm Maxwell}
}
\]

for the free untwisted fields in the fixed conventions. This is **not** a naive signed physical-polarization count: Lichnerowicz/Weitzenbock curvature endomorphisms and ghosts matter.

A 6d \(\mathcal N=(1,0)\) vector multiplet gives a concrete local cancellation:

\[
\boxed{c_{\rm Maxwell+gh}+c_{\rm SMW\ gaugino}=-2+2=0.}
\]

This is a parity-even local statement and does not imply cancellation of anomalies or finite thresholds.

For genuinely scalar-type trivial bundles, signed multiplicity remains exact:

\[
\boxed{
G^{\rm fin}_{\nu}
=-\frac{\nu}{16\pi^3L^2}
\operatorname{Re}[\mathcal G_4(\tau)(d\tau)^2].
}
\]

But true spinors and vectors have nontrivial bundle connections and curvature endomorphisms. Their winding heat kernels depend on Lorentz-representation data such as \(\operatorname{tr}(\Sigma\Sigma)\), so

\[
\boxed{
G^{\rm fin}_{\rm spin>0}
\neq(\text{signed component count})\,G^{\rm fin}_{\rm scalar}
\quad\text{in general}.
}
\]

This is the central v0.21 obstruction.

References: Vassilevich (2003); Lawson--Michelsohn (1989); von Gersdorff (2008); Ferrara--Riccioni--Sagnotti (1998); Ohmori--Shimizu--Tachikawa--Yonekura (2014).

## Current controlled frontier

The field-content audit shows that the remaining finite problem is representation-theoretic, not a species count. The active target is **v0.22 — spin-connection automorphic threshold**.

The next calculation must evaluate the Dirac and Maxwell+ghost winding/periodic heat-kernel coefficients on the Model-XX elliptic family, including spin parallel transport and curvature endomorphisms. The goal is to determine the actual coefficients/tensor structures that replace the scalar weight-four threshold and then test a physically specified multiplet without fitting field multiplicities.

No Lorentzian/horizon closure is claimed.
