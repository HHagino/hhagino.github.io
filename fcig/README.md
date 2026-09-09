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
\text{Quillen / analytic torsion}
\to
\text{differential-cohomology / holonomy synthesis}
\to
\text{response / transgression test}
\to
\text{canonical coupling-class test}
\to
\text{Lorentzian closure?}
}
\]

Completed milestones: **v0.2 (elliptic)**, **v0.3 (flat ppav)**, **v0.4 (curved hyperbolic curves)**, **v0.5 (Quillen / analytic torsion)**, **v0.6 (differential cohomology / determinant holonomy)**, and **v0.7 (response / transgression)**. Gravity closure remains inactive.

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

For determinant/Hodge geometry,

\[
\boxed{
\lambda_k
\simeq
\lambda_1^{\otimes(6k^2-6k+1)}.
}
\]

This gives a no-go for a universal extrapolation of the flat ppav rank/2 law.

## Explicit Model V — Quillen / analytic-torsion refinement

- Web: `quillen-refinement.html`
- Source: `quillen-refinement.md`
- Sanity checker: `quillen-refinement.py`

On the same determinant line \(\lambda_k\), fix the holomorphic analytic-torsion convention

\[
\mathcal T_k
=
\sum_{q=0}^{1}(-1)^q q\log\det{}'\Delta_{0,q}^{(k)}.
\]

Then

\[
\boxed{
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
F_Q-F_{L^2}=-\partial\bar\partial\mathcal T_k.
}
\]

Combining this with the established Zograf–Takhtajan formula gives

\[
\boxed{
c_1(\lambda_k,h_{L^2})
=
\frac{6k^2-6k+1}{12\pi^2}\omega_{\mathrm{WP}}
+
\frac{i}{2\pi}\partial\bar\partial\mathcal T_k.
}
\]

Thus the elementary \(L^2\) determinant curvature and the Quillen/family-index curvature are related but not interchangeable.

The spectral determinant is globally encoded by Selberg-zeta / closed-geodesic data. The pointwise Bergman loop correction from Model IV is nevertheless **not** literally analytic torsion; shared geodesic input does not imply equality of the two functionals.

## Explicit Model VI — differential cohomology / determinant holonomy

- Web: `differential-holonomy.html`
- Source: `differential-holonomy.md`
- Sanity checker: `differential-holonomy.py`

A Hermitian line with unitary connection defines

\[
\boxed{
\widehat c_1(L,\nabla)
\in
\widehat H^2(B;\mathbf Z).
}
\]

Its standard outputs are

\[
\boxed{
I(\widehat c_1)=c_1(L),
\qquad
R(\widehat c_1)=\frac{F_\nabla}{2\pi i},
\qquad
\operatorname{Hol}_\nabla(\gamma)=e^{2\pi i h(\gamma)}.
}
\]

The curvature exact sequence

\[
0\to H^1(B;\mathbf R/\mathbf Z)
\to\widehat H^2(B;\mathbf Z)
\xrightarrow{R}\Omega^2_{\mathbf Z}(B)\to0
\]

makes the earlier local/global distinction precise. The flat ppav corrected line lies in the flat sector when it descends on the chosen theta/metaplectic cover, while the curved Quillen determinant line has nonzero local-index curvature and eta-invariant holonomy.

## Explicit Model VII — response / transgression bridge

- Web: `response-transgression.html`
- Source: `response-transgression.md`
- Degree checker: `response-transgression.py`

Loop-space transgression is the standard map

\[
\boxed{
\tau_{S^1}
=
\widehat\pi_!\operatorname{ev}^*:
\widehat H^2(B;\mathbf Z)
\to
\widehat H^1(LB;\mathbf Z).
}
\]

For a line with connection, the resulting degree-one differential character is exactly its holonomy function:

\[
\boxed{
\tau_{S^1}(\widehat{\mathcal A})(\gamma)
=
\operatorname{Hol}_{\widehat{\mathcal A}}(\gamma).
}
\]

This is a genuine response map, but it also exposes a degree obstruction. For a correspondence

\[
M\xleftarrow{p}Z\xrightarrow{q}B
\]

with real \(d\)-dimensional fibers,

\[
\boxed{
p_!q^*\widehat{\mathcal A}
\in
\widehat H^{2-d}(M;\mathbf Z),
}
\]

so a positive-dimensional pushforward does not by itself yield another degree-two line with connection.

A degree-preserving template requires an additional class

\[
\widehat u\in\widehat H^d(Z;\mathbf Z),
\]

leading to

\[
\boxed{
\widehat{\mathcal R}_{p,q,\widehat u}
=
p_!(q^*\widehat{\mathcal A}\cup\widehat u)
\in\widehat H^2(M;\mathbf Z).
}
\]

The operation is standard once \(p,q,\widehat u\) are supplied; FCIG has not yet derived a canonical physical choice of \(\widehat u\). The same note also makes explicit that any resulting degree-two class is still a \(U(1)\) connection, not automatically a tangent/frame connection.

## Current synthesis

The explicit models now support

\[
\boxed{
\text{state counting}
\oplus
\text{local curvature asymptotics}
\oplus
\text{global lattice/geodesic data}
\oplus
\text{determinant metric / analytic torsion}
\oplus
\text{differential-character curvature + holonomy}
\oplus
\text{functorial response with a degree/type audit}.
}
\]

The next controlled question is whether the **existing geometry of the family** supplies a canonical degree-restoring coupling class, rather than inventing one solely to force a desired response. No Lorentzian/gravitational closure is claimed at this stage.
