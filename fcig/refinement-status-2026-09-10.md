# FCIG Semiclassical Refinement Status — 2026-09-10

This file is the authoritative status ledger for the post-SAC quantitative refinement.

## Closed

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

For every fixed \(D,E\) and \(N\),
\[
\boxed{\begin{aligned}
p_{D,E,N}(M_{m,n}^{(q)})
\le{}&C_{D,E,N}(1+q+m)^{\deg D}(1+q+n)^{\deg E}\\
&\times\left[1+\operatorname{arcosh}(1+m/q)+\operatorname{arcosh}(1+n/q)\right]^N.
\end{aligned}}
\]

Equivalently the spatial K-type loss is only logarithmic.

\[
\boxed{\textbf{DA-A1: PASS}}
\]
Canonical radial derivative scales:
\[
\text{ordinary saddle}:q^j,\qquad
\text{Airy}:q^{2j/3},\qquad
\text{Bessel}:q^j,\qquad
\text{Hermite}:q^{j/2}.
\]

\[
\boxed{\textbf{OSB-A1/A2/A3: PASS}}
\]
Exact Bergman/orbital kernel crosswalk, exact transverse Gamma window, and quantitative common hyperbolic-coordinate/semiclassical-scale compatibility.

## Remaining quantitative gate

\[
\boxed{\textbf{SR-B2 / DA-A2: OPEN}}
\]
One globally differentiated remainder/overlap theorem simultaneously uniform through ordinary saddle, Airy, Bessel, Hermite, and all transition overlaps.

The sectorwise stitch law near a simple outer Airy fold is already
\[
q\Phi_+(t)\approx\frac t2+N\log(1+t)+\log P_{D,E}(q,m,n)+\frac{2j}{3}\log q,
\]
with
\[
P_{D,E}=(1+q+m)^{\deg D}(1+q+n)^{\deg E}.
\]

## Remaining transform-theoretic gate

\[
\boxed{\textbf{OSB-B: OPEN}}
\]
Construct a typed relative/Harish--Chandra transform carrying the cyclic Bergman/Toeplitz relative functional into the discrete-series spectral block.  This must not identify the transverse Fourier variable, cyclic deformation mode, K-type label, and Harish--Chandra spectral parameter.

## Claim firewall

- SR-B1 is a quantitative global upper-bound theorem, not a claim of optimal numerical constants.
- The principal radial ODE turning points agree with SAC caustics; finite-q lower-order corrections are kept distinct.
- DA-A1 gives local differentiated scaling laws, not a single globally uniform differentiated remainder theorem.
- OSB-A is a typed compatibility theorem; OSB-B is the still-missing transform theorem.
- No novelty claim is made without a separate literature audit of the combined parameter-uniform formulation.
