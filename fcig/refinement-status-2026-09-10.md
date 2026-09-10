# FCIG Semiclassical Refinement Status — 2026-09-10

This file is the authoritative status ledger for the post-SAC quantitative and transform-theoretic refinement.

## Closed quantitative gates

\[
\boxed{\textbf{SR-A1: PASS}}
\]
Sharp derivative polynomial degrees at zero spatial weight:
\[
|L_D R_E M_{m,n}^{(q)}(g)|
\le C_{D,E}(1+q+m)^{\deg D}(1+q+n)^{\deg E}\Xi(g).
\]

\[
\boxed{\textbf{SR-A2: PASS}}
\]
Exact inverse-synthesis formal-degree cost:
\[
h_{|e_n\rangle\langle e_m|,q}=d_qM_{m,n}^{(q)},\qquad d_q=(2q-1)/(4\pi).
\]

\[
\boxed{\textbf{SR-B1a: PASS}}
\]
Lowest-K logarithmic spatial cost.

\[
\boxed{\textbf{TF-A1/TF-A2: PASS}}
\]
The inner forbidden chamber is not a separate Schwartz-tail obstruction; both forbidden rates are retained in the sharp SAC atlas.

\[
\boxed{\textbf{SR-B1b: PASS}}
\]
The unrestricted two-high-K outer tail is controlled by the exact radial ODE and a parameter-uniform one-dimensional Agmon comparison.

Therefore
\[
\boxed{\textbf{SR-B1: PASS — unrestricted logarithmic spatial Schwartz cost.}}
\]

For every fixed `D,E,N`,
\[
\boxed{\begin{aligned}
p_{D,E,N}(M_{m,n}^{(q)})
\le{}&C_{D,E,N}(1+q+m)^{\deg D}(1+q+n)^{\deg E}\\
&\times\left[1+\operatorname{arcosh}(1+m/q)+\operatorname{arcosh}(1+n/q)\right]^N.
\end{aligned}}
\]

\[
\boxed{\textbf{DA-A1: PASS}}
\]
Canonical local radial derivative scales:
\[
\text{ordinary saddle}:q^j,\qquad
\text{Airy}:q^{2j/3},\qquad
\text{Bessel}:q^j,\qquad
\text{Hermite}:q^{j/2}.
\]

\[
\boxed{\textbf{DA-B1: PASS}}
\]
For every fixed derivative order `J` and spatial order `N`, the local canonical charts patch to the unrestricted Agmon exterior. In particular, for `j<=J`,
\[
\sup_{t\ge0}(1+t)^N\Xi(a_t)^{-1}|\partial_t^jM_{m,n}^{(q)}(t)|
\le C_{J,N}(1+q+m+n)^j(1+t_+)^N,
\]
where
\[
t_+=\operatorname{arcosh}(1+m/q)+\operatorname{arcosh}(1+n/q).
\]

Hence
\[
\boxed{\textbf{SR-B2a: PASS — finite-order differentiated SAC--Schwartz stitching.}}
\]

The old `SR-B2 / DA-A2` wording is superseded. The only stronger quantitative refinement left is an all-orders single-formula theorem on the fully resolved degeneration space.

## Closed orbital/Fourier bridge gates

\[
\boxed{\textbf{OSB-A1/A2/A3: PASS}}
\]
Exact Bergman/orbital kernel crosswalk, exact transverse Gamma window, and quantitative common hyperbolic-coordinate/semiclassical-scale compatibility.

The intervening representation-theoretic chain is also closed in its natural typed domains:
\[
\text{DS-B1 PASS},\quad
\text{RI-A PASS},\quad
\text{RI-B PASS modulo orbital kernel},\quad
\text{OKI-A2 PASS in the smoothing sector},\quad
\text{SC-A PASS}.
\]

Consequently
\[
\boxed{\textbf{OSB-B1: PASS — typed orbital/Fourier interpolation in the smoothing sector.}}
\]

For admissible `W`, choose an orbital lift `f_0` with
\[
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
\]
If
\[
A_W=d_q^{-1}T_W^{(q)}-\widehat f_0(\pi_q)\in\mathscr S(\mathcal H_q),
\]
then discrete-series cuspidal synthesis gives `h_{A_W}` with
\[
O_{a_L}(h_{A_W})=0,\qquad \widehat h_{A_W}(\pi_q)=A_W.
\]
Thus
\[
f_{q,W}=f_0+h_{A_W}
\]
satisfies simultaneously
\[
\boxed{
O_{a_L}(f_{q,W})=d_q\mathcal J_{q,L}[W],
\qquad
\widehat f_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)}.
}
\]

This is the precise typed transform closure: one common Harish--Chandra-Schwartz test object realizes the hyperbolic FCIG orbital data and the holomorphic discrete-series Toeplitz Fourier block.

## Remaining stronger refinements

### DA-B2 — resolved all-orders atlas

\[
\boxed{\textbf{DA-B2: OPEN}}
\]
Construct one explicit polyhomogeneous/all-orders canonical expansion with a single remainder architecture uniform through ordinary saddles, separated Airy folds, the Bessel identity merger, the Hermite lowest-K merger, and every overlap face.

This is stronger than what is required for finite-order Schwartz closure.

### OSB-B2 — canonical/automorphic refinement

\[
\boxed{\textbf{OSB-B2: OPEN}}
\]
The local smoothing-sector interpolation theorem does not choose a unique representative modulo components invisible to both selected transforms. A stronger theorem could select a canonical/minimal representative and identify the compact automorphic multiplicity block with the universal-cover discrete-series operator model.

## Current frontier

The project has therefore moved past the former two principal open gates. The next genuinely stronger targets are:

\[
\boxed{
\text{resolved all-orders semiclassical geometry}
\quad\text{and}\quad
\text{automorphic/canonical transform refinement}.
}
\]

Neither is needed to retain the already closed exact kernel, cyclic trace, smoothing Fourier block, unrestricted logarithmic Schwartz bound, or finite-order differentiated atlas.

## Claim firewall

- `DA-B1` is finite-order: derivative order is fixed before constants are chosen.
- `SR-B2a` is a rigorous finite-order patching statement, not a single global canonical asymptotic formula.
- `OSB-B1` is an interpolation/existence theorem in the smoothing sector, not a pointwise identification of orbital and spectral variables.
- The transverse Fourier variable, cyclic deformation mode, K-type label, and Harish--Chandra spectral parameter remain distinct.
- The common Weyl denominator does not imply equality of FCIG and character numerators.
- Compact automorphic Toeplitz blocks remain distinct from the universal-cover discrete-series operator until multiplicity compatibility is specified.
- No literature-novelty claim is made without a separate audit of the combined formulation.