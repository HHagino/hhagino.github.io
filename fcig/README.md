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
\text{descent / inflow}
\to
\text{functional-response no-go}
\to
\text{semiclassical closure audit}
\to
\text{heat-kernel effective-action bridge}.
}
\]

Completed milestones: **v0.2–v0.16**. No derivation of Einstein dynamics from FCIG alone is claimed.

## Models I–X — geometric / determinant foundation

The elliptic, ppav and curved-curve laboratories establish exact theta/state counting, Bergman local/global sectors, determinant/Quillen geometry, differential characters, transgression, pushforward no-gos and the global metrized Deligne--Riemann--Roch closure

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q}
\]

in the canonical smooth curve-family model.

Main files include `elliptic-model.md`, `modular-holonomy.md`, `abelian-model.md`, `abelian-bergman.md`, `abelian-weil.md`, `hyperbolic-model.md`, `quillen-refinement.md`, `differential-holonomy.md`, `response-transgression.md`, `factorized-pushforward.md`, `kappa1-quillen.md`, and `global-deligne-rr.md`.

## Model XI — structure-group bridge audit

`structure-group-bridge.md`

\[
1\to SU(n)\to U(n)\xrightarrow{\det}U(1)\to1,
\qquad
F_{\det E}=\operatorname{Tr}F_E.
\]

The determinant connection retains trace/Ricci information but cannot reconstruct a generic nonabelian frame connection for \(n>1\).

## Models XII–XIII — mixed anomaly polynomial and descent

`mixed-characteristic.md`, `descent-inflow.md`.

With independent line and frame connections,

\[
\widehat c_1(L)\cup\widehat p_1(TM)\in\widehat H^6(M;\mathbf Z),
\]

and

\[
\boxed{
[\widehat A(TM)\operatorname{ch}(L)]_{(6)}
=\frac16c_1^3-\frac1{24}c_1p_1.
}
\]

Local descent gives a five-dimensional secondary/inflow form; global fermionic quantization is controlled by the Dirac index / Dai--Freed anomaly theory.

## Model XIV — functional-response no-go

`functional-response.md`, `functional-response.py`, `functional-response.bib`.

For any globally defined invariant functional \(S_{\rm inv}\),

\[
W'=W+S_{\rm inv}
\]

has the same anomaly while its first functional derivatives can differ. Hence

\[
\boxed{
\text{same anomaly class}\not\Rightarrow\text{same }W,J,T_{\mu\nu}.
}
\]

## Model XV — constitutive / semiclassical closure audit

`semiclassical-closure.md`, `semiclassical-closure.py`, `semiclassical-closure.bib`.

Supplying independent renormalized gravitational and matter/effective actions gives a legitimate conditional variational bridge,

\[
\mathcal E^{\rm grav}_{\mu\nu}=T_{\mu\nu}^{\rm ren},
\]

but the action principle, renormalized couplings and any Jacobson-style Lorentzian horizon data are extra inputs. Current \(\log h^0\) / Bergman quantities are not yet a canonical local Lorentzian horizon entropy.

## Model XVI — explicit operator / heat-kernel effective-action bridge

- Web: `heat-kernel-bridge.html`
- Source: `heat-kernel-bridge.md`
- Checker: `heat-kernel-bridge.py`
- Milestone bibliography: `heat-kernel-bridge.bib`

Supply a four-dimensional Euclidean background and an additional realization map

\[
\boxed{\Phi:M\to\mathcal B_{\rm FCIG}}.
\]

Pull back an FCIG Hermitian line with connection:

\[
L_M=\Phi^*\mathscr L_{\rm FCIG},
\qquad
\Omega=F_{\nabla^M}=\Phi^*F_{\rm FCIG}.
\]

For the Laplace-type operator

\[
P=-\left(g^{\mu\nu}\nabla_\mu\nabla_\nu+E\right),
\]

standard heat-kernel geometry gives

\[
\operatorname{Tr}(e^{-tP})
\sim
(4\pi t)^{-2}
\int_M\sqrt g\,\operatorname{tr}(b_0+t b_2+t^2 b_4+\cdots),
\]

with

\[
b_0=I,
\qquad
b_2=E+\frac16R,
\]

and

\[
\boxed{
b_4\supset\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}.
}
\]

Thus, after the explicit pullback realization,

\[
\boxed{
b_4^{\rm FCIG}\supset
\frac1{12}(\Phi^*F_{\rm FCIG})_{\mu\nu}(\Phi^*F_{\rm FCIG})^{\mu\nu}.}
\]

This is the first operator-level local spacetime effective-action invariant built from FCIG line curvature without identifying that curvature with Riemann curvature.

In four dimensions the one-loop proper-time expansion organizes UV local terms as

\[
b_0\to\text{volume/cosmological},\qquad
b_2\to\text{Einstein--Hilbert},\qquad
b_4\to\text{curvature-squared / bundle-curvature}.
\]

These divergent local coefficients renormalize couplings; they are not parameter-free FCIG predictions.

For the scalar specialization \(E=-\xi R\),

\[
b_2=\left(\frac16-\xi\right)R,
\]

and, after dropping integrated total derivatives on a closed manifold,

\[
\boxed{
 b_4=
\frac12\left(\xi-\frac16\right)^2R^2
+\frac1{180}(R_{\mu\nu\rho\sigma}^2-R_{\mu\nu}^2)
+\frac1{12}\Omega_{\mu\nu}^2.
}
\]

The model also preserves the earlier FCIG local/global split: a flat line with nontrivial holonomy has \(\Omega=0\), so local heat coefficients can miss information retained by the global spectrum/determinant.

References: Vassilevich (2003); Gilkey (1995); Birrell--Davies (1982); Wald (1993); Iyer--Wald (1994).

## Current controlled frontier

The previous missing arrow now has a conditional operator-level realization:

\[
\boxed{
(\mathscr L_{\rm FCIG},\nabla^{\rm FCIG})
+\Phi
\to
P_\Phi
\to
\text{heat kernel}
\to
W_{1\text{-loop}}^{\rm ren}[g,\Phi].
}
\]

The remaining new object is the realization map \(\Phi\). The active target is **v0.17 — realization-map / sigma-model dynamics audit**: determine whether the geometry already present on \(\mathcal B_{\rm FCIG}\) supplies a controlled spacetime action and equation of motion for \(\Phi\), or whether such a sigma-model term is merely another constitutive input.

The Lorentzian horizon/thermodynamic closure remains inactive pending a controlled physical realization.