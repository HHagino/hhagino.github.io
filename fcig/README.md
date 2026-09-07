# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository separates **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. See:

- `RESEARCH_POLICY.md` — research and citation policy
- `ROADMAP.md` — active milestone gates
- `references.bib` — canonical bibliography
- `citation-map.md` — citation provenance map
- `cited-synthesis.md` — citation-audited synthesis

`main` is intended to remain readable and independently checkable. Exploratory work is developed on topic branches and merged through pull requests.

## Research sequence

\[
\boxed{
\text{elliptic curves}
\to
\text{higher-dimensional abelian varieties}
\to
\text{compact hyperbolic curves}
\to
\text{Quillen / analytic-torsion refinement}
\to
\text{Lorentzian closure}.
}
\]

The current completed milestones are **v0.2 (elliptic)**, **v0.3 (flat ppav)**, and **v0.4 (curved hyperbolic curves)**. The active target is **v0.5: systematic \(L^2\) vs Quillen / analytic-torsion comparison**.

## Main research-program note

- Web page: `index.html`
- Source: `research-note.md`

## Explicit Model I — elliptic curves

- Web: `elliptic-model.html`
- Source: `elliptic-model.md`
- Verifier: `elliptic-bergman.py`

For the level-\(k\) theta space on an elliptic curve,

\[
F_{\det\mathcal H_k}
=-\frac{k}{2}F_{\lambda_H}.
\]

The exact Bergman density separates a constant local sector from exponentially small lattice corrections.

## Explicit Model II — modular holonomy / metaplectic anomaly

- Web: `modular-holonomy.html`
- Source: `modular-holonomy.md`
- Verifier: `weil-holonomy.py`

The finite theta transport exhibits a projective/metaplectic phase. After local curvature cancellation, a flat global multiplier can remain.

## Explicit Model III — principally polarized abelian varieties

- Web: `abelian-model.html`
- Source: `abelian-model.md`
- Verifier: `abelian-gram.py`

For

\[
A_\Omega=\mathbf C^g/(\mathbf Z^g+\Omega\mathbf Z^g),
\qquad
N_k=k^g,
\]

the exact Gram determinant gives

\[
\boxed{
F_{\det\mathcal H_k}
=-\frac{k^g}{2}F_{\lambda_H}
=-\frac{N_k}{2}F_{\lambda_H}.
}
\]

### Model IIIb — exact multidimensional Bergman lattice sector

- Web: `abelian-bergman.html`
- Source: `abelian-bergman.md`
- Verifier: `abelian-bergman.py`

With

\[
Q_\Omega(p,\ell)
=(\ell-\Omega p)^*(\operatorname{Im}\Omega)^{-1}(\ell-\Omega p),
\]

one obtains

\[
B_{g,k}
=
k^g\sum_{p,\ell\in\mathbf Z^g}
 e^{-\pi kQ_\Omega(p,\ell)/2}
 e^{2\pi ik(p^Tx+\ell^Tt)+\pi ikp^T\ell},
\]

and, for fixed \(\Omega\),

\[
B_{g,k}
=
k^g\left[1+O_\Omega\left(e^{-\pi k\mu(\Omega)/2}\right)\right].
\]

### Model IIIc — higher-dimensional Weil / metaplectic descent

- Web: `abelian-weil.html`
- Source: `abelian-weil.md`
- Verifier: `abelian-weil.py`

For even \(k\), the elementary finite Weil matrices satisfy

\[
U_k(S)^2=C,
\qquad
(U_k(S)U_k(T_{I_g}))^3=e^{\pi ig/4}C.
\]

The corrected determinant line can be locally flat yet globally nontrivial; for example, the genus-two level-two shear in the note has multiplier \(-1\).

## Explicit Model IV — compact hyperbolic curves

- Web: `hyperbolic-model.html`
- Source: `hyperbolic-model.md`
- Sanity checker: `hyperbolic-loop.py`

Let \(X\) be a compact hyperbolic Riemann surface of genus \(g\ge2\), and consider \(H^0(X,K_X^k)\). The established exact hyperbolic Bergman formula [Sun26] gives

\[
\boxed{
\rho_k(p)
=
\frac{2k-1}{4\pi}
\left[
1+
\sum_{\gamma\in\mathfrak G_p}
\cosh^{-2k}\!\left(\frac{\ell(\gamma)}2\right)
\cos(2\pi k\alpha_\gamma)
\right].
}
\]

This realizes, in one curved model,

\[
\boxed{
\text{nonzero local curvature sector}
\oplus
\text{global geodesic/holonomy sector}.
}
\]

The local factor integrates exactly to

\[
\dim H^0(X,K_X^k)=(2k-1)(g-1),
\]

so the global loop correction redistributes state density while integrating to zero.

For determinant/Hodge geometry, the established Mumford isomorphism gives

\[
\boxed{
\lambda_k
\simeq
\lambda_1^{\otimes(6k^2-6k+1)}.
}
\]

This is a useful no-go result for a naive universal extrapolation of the flat ppav law: the curved canonical-family determinant coefficient is quadratic in \(k\), while the state rank is linear in \(k\) at fixed genus.

The Quillen benchmark is

\[
\boxed{
c_1(\lambda_k,\|\cdot\|_Q)
=
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}}.
}
\]

Systematic separation of ordinary \(L^2\) determinant geometry from analytic torsion is deferred to v0.5.

## Current synthesis

The explicit models now support a hierarchy

\[
\boxed{
\text{state counting}
\oplus
\text{local curvature asymptotics}
\oplus
\text{global lattice/geodesic data}
\oplus
\text{connection/holonomy}
\oplus
\text{determinant/index geometry}.
}
\]

This is a mathematical-physics research program, not a derivation of spacetime gravity. The Lorentzian closure problem remains open and is deliberately downstream of the geometric tests.
