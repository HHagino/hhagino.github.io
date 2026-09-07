# FCIG — Fibered Cohomological Information Geometry

Research-program notes on local potentials, differential cohomology, derived direct images, determinant-line anomalies, Bergman kernels, and the gravity closure problem.

## Read

### Citation-audited synthesis

- Source: `fcig/cited-synthesis.md`
- BibTeX: `fcig/references.bib`

This is the preferred entry point when checking literature provenance. It marks each important statement as **Established**, **Derived here**, or **FCIG interpretation / conjecture**, so a citation to a standard theorem is not accidentally presented as support for a stronger speculative claim.

### Main research-program note

- Web page: `fcig/index.html`
- Source note: `fcig/research-note.md`

### Explicit Model I — elliptic curves

- Web page: `fcig/elliptic-model.html`
- Source note: `fcig/elliptic-model.md`
- Numerical verifier: `fcig/elliptic-bergman.py`

This model computes a level-\(k\) theta basis, its exact \(L^2\) Gram matrix, a Poisson-resummed Bergman density, the Hodge curvature over \(\mathbb H\), and

\[
F_{\det\mathcal H_k}
=
-\frac{k}{2}F_{\lambda_H}.
\]

It separates local curvature asymptotics from exponentially small global lattice corrections.

### Explicit Model II — modular holonomy and metaplectic anomaly

- Web page: `fcig/modular-holonomy.html`
- Source note: `fcig/modular-holonomy.md`
- Numerical verifier: `fcig/weil-holonomy.py`

For even level \(k\), the theta basis carries the finite matrices

\[
(U_S)_{j\ell}=k^{-1/2}e^{-2\pi i j\ell/k},
\qquad
(U_T)_{j\ell}=\delta_{j\ell}e^{\pi i j^2/k},
\]

with

\[
U_S^2=C,
\qquad
(U_SU_T)^3=e^{\pi i/4}C.
\]

Combining the determinant-state line with the Hodge line gives

\[
\boxed{
\mathscr A_k
=
\det\mathcal H_k\otimes\lambda_H^{k/2},
\qquad
F_{\mathscr A_k}=0.
}
\]

Thus the local curvature anomaly can be cancelled while a flat Weil/metaplectic modular multiplier remains. For odd \(k\), the \(T\)-move exchanges theta-characteristic sectors and the same cancellation naturally requires a Hodge square root, making the metaplectic structure explicit.

## Core formula

\[
\operatorname{ch}(R\pi_*\mathscr L^k)
=
\pi_*\left(e^{k c_1(\mathscr L)}\operatorname{Td}(T_\pi)\right).
\]

The project interprets degree zero as the state-capacity sector and degree two as the determinant/anomaly sector, while local Bergman-kernel asymptotics encode curvature information and modular Weil transport encodes a global flat sector.

## Elliptic-model synthesis

The two explicit models now realize

\[
\boxed{
\text{FCIG data}
=
\text{local curvature}
\oplus
\text{flat modular holonomy}
\oplus
\text{nonperturbative lattice corrections}.
}
\]

This is an exact toy-model decomposition, not a derivation of spacetime gravity.

## Status

This is a speculative mathematical-physics research program. Established mathematics, proposed interpretations, explicit calculations, and open gravitational claims are explicitly separated.
