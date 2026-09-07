# FCIG — Fibered Cohomological Information Geometry

Research-program notes on local potentials, differential cohomology, derived direct images, determinant-line anomalies, Bergman kernels, modular holonomy, and the gravity closure problem.

## Repository policy

This directory is operated as a public research workspace, not just a blog archive.

- Research policy: `fcig/RESEARCH_POLICY.md`
- Active roadmap: `fcig/ROADMAP.md`
- Canonical bibliography: `fcig/references.bib`
- Citation provenance map: `fcig/citation-map.md`
- Citation-audited synthesis: `fcig/cited-synthesis.md`

`main` is intended to remain readable and checkable. Topic work is developed on branches and merged by pull request. Standard mathematics, FCIG-specific derivations, interpretations, conjectures, and open problems are kept explicitly separate.

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

For even level \(k\), the theta basis carries finite Weil matrices with a metaplectic eighth-root phase. Combining the determinant-state line with the Hodge line gives

\[
\boxed{
\mathscr A_k
=
\det\mathcal H_k\otimes\lambda_H^{k/2},
\qquad
F_{\mathscr A_k}=0.
}
\]

Thus the local curvature contribution can be cancelled while a flat Weil/metaplectic modular multiplier remains. For odd \(k\), the same statement requires the appropriate theta-characteristic/metaplectic refinement.

### Explicit Model III — higher-dimensional abelian varieties

- Web page: `fcig/abelian-model.html`
- Source note: `fcig/abelian-model.md`
- Numerical verifier: `fcig/abelian-gram.py`

For a principally polarized abelian variety

\[
A_\Omega
=
\mathbf C^g/(\mathbf Z^g+\Omega\mathbf Z^g),
\qquad
\Omega\in\mathfrak H_g,
\]

the level-\(k\) theta state space has rank \(N_k=k^g\), and the exact Gram computation gives

\[
\boxed{
F_{\det\mathcal H_k}
=
-\frac{k^g}{2}F_{\lambda_H}
=
-\frac{N_k}{2}F_{\lambda_H}.
}
\]

### Explicit Model IIIb — multidimensional Bergman lattice formula

- Web page: `fcig/abelian-bergman.html`
- Source note: `fcig/abelian-bergman.md`
- Numerical verifier: `fcig/abelian-bergman.py`

With

\[
Q_\Omega(p,\ell)
=(\ell-\Omega p)^*(\operatorname{Im}\Omega)^{-1}(\ell-\Omega p),
\]

the exact Poisson-resummed density is

\[
\boxed{
B_{g,k}(x,t;\Omega)
=
k^g\sum_{p,\ell\in\mathbf Z^g}
 e^{-\pi kQ_\Omega(p,\ell)/2}
 e^{2\pi ik(p^Tx+\ell^Tt)+\pi ikp^T\ell}.
}
\]

For fixed \(\Omega\), if \(\mu(\Omega)\) is the shortest nonzero value of \(Q_\Omega\), then

\[
\boxed{
B_{g,k}
=
k^g\left[1+O_\Omega\left(e^{-\pi k\mu(\Omega)/2}\right)\right].
}
\]

This completes the multidimensional Bergman/Poisson gate. The remaining v0.3 gate is the higher-dimensional finite Weil/metaplectic descent.

## Core formula

\[
\operatorname{ch}(R\pi_*\mathscr L^k)
=
\pi_*\left(e^{k c_1(\mathscr L)}\operatorname{Td}(T_\pi)\right).
\]

The project interprets degree zero as the state-capacity sector and degree two as the determinant/anomaly sector, while local Bergman-kernel asymptotics encode curvature information and modular Weil transport encodes a global flat sector.

## Current research order

\[
\boxed{
\text{elliptic curves}
\to
\text{higher-dimensional abelian varieties}
\to
\text{genus }g\ge2\text{ curves}
\to
\text{Quillen refinement}
\to
\text{Lorentzian closure}.
}
\]

The current milestone is **v0.3: higher-dimensional abelian generalization**. Gate E (multidimensional Bergman lattice formula) is complete; Gate D (finite Weil/metaplectic descent) remains open. See `ROADMAP.md` and Issues #6–#8.

## Status

This is a speculative mathematical-physics research program. Established mathematics, proposed interpretations, explicit calculations, and open gravitational claims are explicitly separated. The current results are not presented as a derivation of spacetime gravity.
