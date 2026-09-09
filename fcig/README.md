# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository separates **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research and citation policy
- `ROADMAP.md` — milestone gates
- `references.bib` — canonical bibliography
- `citation-map.md` — citation provenance map
- `cited-synthesis.md` — citation-audited synthesis

## Completed sequence

\[
\boxed{
\text{theta / ppav}
\to
\text{curved curves}
\to
\text{Quillen / differential cohomology}
\to
\text{transgression / pushforward}
\to
\text{Deligne--RR closure}
\to
\text{structure-group audit}
\to
\text{mixed anomaly polynomial}
\to
\text{descent / inflow}.
}
\]

Completed milestones: **v0.2–v0.13**. No Lorentzian/gravitational closure is claimed.

## Models I–III — flat theta / abelian laboratories

The elliptic and ppav models establish exact theta-state counting, exact Gram determinants, Poisson-resummed Bergman lattice sectors, and finite Weil/metaplectic holonomy. In the ppav conventions,

\[
F_{\det\mathcal H_k}=-\frac{k^g}{2}F_{\lambda_H}.
\]

Main files: `elliptic-model.md`, `modular-holonomy.md`, `abelian-model.md`, `abelian-bergman.md`, `abelian-weil.md` and their Python checkers.

## Model IV — compact hyperbolic curves

`hyperbolic-model.md` / `hyperbolic-loop.py`

The curved model separates a nonzero local Bergman-curvature sector from an independent global geodesic/holonomy sector. The Mumford determinant relation is a no-go for a universal extrapolation of the flat-ppav rank/2 coefficient.

## Model V — Quillen / analytic torsion

`quillen-refinement.md` / `quillen-refinement.py`

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

## Model VI — differential cohomology / determinant holonomy

`differential-holonomy.md` / `differential-holonomy.py`

A unitary line with connection defines

\[
\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbf Z),
\]

carrying topology, curvature and loop holonomy in one object.

## Model VII — response / transgression

`response-transgression.md` / `response-transgression.py`

\[
\tau_{S^1}:\widehat H^2(B;\mathbf Z)\to\widehat H^1(LB;\mathbf Z)
\]

is a genuine response map whose value is the determinant holonomy function.

## Model VIII — factorized-pushforward no-go

`factorized-pushforward.md` / `factorized-pushforward.py`

\[
\boxed{
p_!\bigl(p^*\widehat{\mathcal A}\cup\widehat u\bigr)
=n\widehat{\mathcal A},
\qquad n\in\mathbf Z,
}
\]

so factorized degree restoration cannot create an independent degree-two response direction.

## Models IX–X — \(\widehat\kappa_1\), Quillen, and global Deligne--RR

`kappa1-quillen.md` / `global-deligne-rr.md`

For \(\omega=K_{X/B}\),

\[
\widehat\kappa_1:=\pi_!\bigl(\widehat c_1(\omega)^2\bigr),
\]

and the metrized Deligne-pairing realization closes the comparison globally:

\[
\boxed{
\widehat\kappa_1=12\widehat\lambda_Q.
}
\]

Thus topology, local curvature and loop holonomy satisfy the same connection-level identity in the canonical smooth curve-family determinant sector.

## Model XI — determinant trace / Spin\(^c\) / reconstruction no-go

`structure-group-bridge.md` / `structure-group-bridge.py`

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

For fixed determinant connection, unitary lifts form an affine space over

\[
\Omega^1(M;\mathfrak{su}(E)).
\]

Hence determinant data fixes only the trace sector for \(n>1\). Kähler geometry identifies this trace with Ricci curvature; Ricci-flat K3 geometry is an explicit witness that determinant curvature can vanish while nonabelian tangent curvature remains. Spin\(^c\) gives a positive extension bridge only when the frame connection is supplied independently.

## Model XII — mixed characteristic classes / degree-six anomaly bridge

- `mixed-characteristic.html`
- `mixed-characteristic.md`
- `mixed-characteristic.py`
- `mixed-characteristic.bib`

Treat the line and frame connections as independent fields on the same base. The first canonical mixed differential characteristic class is

\[
\boxed{
\widehat c_1(L)\cup\widehat p_1(TM)
\in\widehat H^6(M;\mathbf Z).
}
\]

For a line-twisted Dirac index,

\[
\boxed{
\left[\widehat A(TM)\operatorname{ch}(L)\right]_{(6)}
=
\frac16c_1^3-rac1{24}c_1p_1.
}
\]

This is a genuine mixed gauge/frame invariant, but its degree is six, so it is not itself a local four-form action density in four dimensions.

## Model XIII — five-dimensional descent / global anomaly inflow

- Web: `descent-inflow.html`
- Source: `descent-inflow.md`
- Checker: `descent-inflow.py`
- Milestone bibliography: `descent-inflow.bib`

On a patch with normalized local potential \(a\), \(da=c\), define

\[
\boxed{
I_5^{(0)}
=a\wedge\left(\frac16c^2-\frac1{24}p_1\right).
}
\]

Then

\[
\boxed{
dI_5^{(0)}
=
I_6
=
\frac16c^3-\frac1{24}cp_1.
}
\]

Under \(a\mapsto a+d\alpha\),

\[
\boxed{
\delta_\alpha I_5^{(0)}
=
d\left[
\alpha\left(\frac16c^2-\frac1{24}p_1\right)
\right],
}
\]

so the five-dimensional variation becomes a four-dimensional boundary anomaly term.

The global audit is crucial. The integral product

\[
\widehat c_1\cup\widehat p_1
\]

is an ordinary differential character, but the full fermionic index polynomial contains rational coefficients. Its global quantization is therefore justified by the spin Dirac index / Dai--Freed anomaly theory, not by simply declaring the fractional polynomial to be an arbitrary integral \(\widehat H^6\) class.

This gives the controlled chain

\[
\boxed{
\text{index polynomial}
\to
\text{5D secondary/inflow datum}
\to
\text{4D symmetry anomaly}.
}
\]

It does **not** identify anomaly response with stress-energy response or horizon thermodynamics.

References: Zumino--Wu--Zee; Bardeen--Zumino; Alvarez-Gaumé--Ginsparg; Cheeger--Simons; Bär--Becker; Dai--Freed; Freed.

## Current controlled frontier

The characteristic-class and anomaly-descent bridges are now explicit. The next bottleneck is **dynamical response**, not topology.

The active target is **v0.14: background-field functional response audit**. It will distinguish:

1. curvature/holonomy of the anomaly line over a space of backgrounds;
2. gauge-current variation of an effective action;
3. metric/frame variation producing stress-energy;
4. trace/diffeomorphism anomalies;
5. any additional constitutive or thermodynamic law required for gravitational dynamics.

No Lorentzian metric, causal structure, horizon entropy law, or Einstein equation has yet been derived.