# FCIG — Fibered Cohomological Information Geometry

Public research workspace for **Fibered Cohomological Information Geometry (FCIG)**.

The repository distinguishes **Established**, **Derived here**, **FCIG interpretation**, **Conjecture**, and **Open problem** claims. `main` is intended to remain readable and independently checkable.

- `RESEARCH_POLICY.md` — research/citation policy
- `ROADMAP.md` — active gates and completed milestones
- `references.bib` — general bibliography
- milestone `.bib` files — source sets for individual models
- `citation-map.md` / `cited-synthesis.md` — citation provenance and audited synthesis
- `normalization-topology-literature-audit.md` — normalization-lift theorem, reconstruction no-go, and prior-art matrix

Additional normalization-selector note: determinant-normalization-selector.md — operator-relative lift, functoriality, monoidality, and residual no-gos.

## Status

Completed numbered milestones: **v0.2–v0.26**. The charged/Jacobi program continues toward **v0.27**, while a parallel hyperbolic information-closure track now runs through Kodaira--Spencer/Born--Fisher closure, finite-\(q\) offsets, Chern-holonomy orbital cancellation, Casimir transmutation, cyclic Fourier profiles, Sun--Selberg unfolding, and the Orbital--Character Closure problem.

The controlled numbered chain is

\[
\boxed{
\text{theta / ppav}
\to\text{curved curves}
\to\text{Quillen / differential cohomology}
\to\text{Deligne--RR}
\to\text{response no-gos}
\to\text{operator / heat-kernel bridge}
\to\text{intrinsic elliptic spectrum}
\to\text{adiabatic KK response}
\to\text{spin/multiplet thresholds}
\to\text{anomaly / GS lattice audits}
\to\text{charged Jacobi spectrum}.
}
\]

No derivation of Einstein dynamics or horizon thermodynamics from FCIG alone is claimed.

## Normalization topology audit

The same global probability model admits lifts by arbitrary Hermitian holomorphic line bundles. Thus positive-measure normalization is globally trivial, a chosen holomorphic lift may be topologically nontrivial, and its topology is not determined by \(p\). The next publishable target is an **intrinsic selector**, not the elementary gluing identity. See [`normalization-topology-literature-audit.md`](normalization-topology-literature-audit.md).

The first selector is now constructed relative to an operator-enhanced model \((p,D)\): the Fredholm/elliptic family selects its determinant line, Quillen metric, and Bismut--Freed connection, while \(q_i=\|\sigma_i\|_Q^2p\) supplies compatible normalization weights. This is canonical relative to \(D\), not from \(p\) alone. See determinant-normalization-selector.md.

## Models I–XVIII — determinant, cohomological and response foundation

These models establish theta-state counting, Bergman local/global sectors, determinant/Quillen geometry, differential characters, transgression, pushforward no-gos, the metrized Deligne--Riemann--Roch identity

\[
\boxed{\widehat\kappa_1=12\widehat\lambda_Q},
\]

structure-group type constraints, anomaly descent, functional-response ambiguity and the conditional heat-kernel/realization-map bridge.

## Model XIX — intrinsic spectral--Hodge identity

For the area-one elliptic torus,

\[
\lambda_{m,n}(\tau)=\frac{4\pi^2}{Y}|m\tau-n|^2,
\qquad
\det{}'\Delta_\tau=Y|\eta(\tau)|^4,
\]

and

\[
\boxed{-\partial\bar\partial\log\det{}'\Delta_\tau=F_{\lambda_H}.}
\]

This is the first no-fit spectral regeneration of the pre-existing elliptic Hodge curvature.

## Models XX–XXIII — adiabatic and multiplet thresholds

After the adiabatic KK and spin-connection audits, the restricted parity-even 6d \(\mathcal N=(1,0)\) table is

\[
\boxed{
\begin{array}{c|ccc}
\text{multiplet}&C_{\rm local}&A_{\mathcal G_4}&B_{Z_2}\\ \hline
\text{vector}&0&0&\frac18\\
\text{hyper}&6&0&-\frac1{16}\\
\text{tensor}&0&0&\frac18
\end{array}}
\]

so

\[
\boxed{
G_{VHT}^{\rm fin}
=\frac{K}{16\pi^3L^2}Z_\tau(2)g_{\rm hyp},
\qquad
K:=2n_V-n_H+2n_T.
}
\]

Self-dual zero modes, theta characteristics and global anomaly phases remain separate from this parity-even determinant magnitude.

## Models XXIV–XXV — anomaly / Green--Schwarz audits

The free-multiplet anomaly map reconstructs \((n_V,n_H,n_T)\) but its natural cancellation kernels differ from the threshold kernel. After the irreducible gravitational anomaly condition,

\[
\boxed{K=V+31T-273.}
\]

Green--Schwarz lattice refinements \(a,b_i\), lattice embeddings and global gauge-group data can change quantum admissibility without changing this gauge-blind threshold. Explicit F-theory witnesses occur with both signs of \(K\).

Sources: `threshold-anomaly.*`, `green-schwarz-lattice.*`.

## Model XXVI — charged elliptic / Jacobi spectral determinant

- Web: `charged-jacobi.html`
- Source: `charged-jacobi.md`
- Checker: `charged-jacobi.py`
- Milestone bibliography: `charged-jacobi.bib`

Introduce flat gauge holonomies by

\[
z=\alpha\tau+\beta.
\]

For integral charge \(q\), the exact shifted spectrum is

\[
\boxed{
\lambda^{(q)}_{m,n}(\tau,z)
=\frac{4\pi^2}{Y}|m\tau-n+qz|^2.
}
\]

The second Kronecker limit formula gives

\[
\boxed{
D_q(\tau,z)
=\det\Delta_{q,z}
=e^{-2\pi q^2(\operatorname{Im}z)^2/Y}
\left|\frac{\theta_1(qz|\tau)}{\eta(\tau)}\right|^2.
}
\]

This is invariant under modular transformations and the allowed elliptic large-gauge shifts. Its zero-mode limit reproduces Model XIX:

\[
\boxed{
\lim_{z\to0}\frac{D_q(\tau,z)}{\lambda^{(q)}_{0,0}}
=Y|\eta(\tau)|^4.
}
\]

Away from the zero divisor,

\[
\boxed{
-\partial\bar\partial\log D_q
=
\frac{\pi q^2}{Y}
\left(dz-\frac{\operatorname{Im}z}{Y}d\tau\right)
\wedge
\left(d\bar z-\frac{\operatorname{Im}z}{Y}d\bar\tau\right).
}
\]

Thus the holomorphic factor has Jacobi index \(q^2/2\), and for many charges the quadratic spectral response is controlled by

\[
\boxed{\mathcal Q_2=\sum_a\nu_a q_a^2.}
\]

This is the first direct microscopic overlap with the six-dimensional abelian anomaly relation

\[
a\cdot\widetilde b=-\frac16\sum_qx_qq^2,
\]

while the quartic moment

\[
\widetilde b\cdot\widetilde b=\frac13\sum_qx_qq^4
\]

is not determined by the quadratic Jacobi curvature.

The common \(\sum q^2\) is a shared microscopic invariant, not an equality between anomaly and spectral observables.

## Parallel frontier — hyperbolic information / Orbital--Character Closure

For a primitive class \(c\), the cyclic-cover calculation diagonalizes the deformation in coefficients \(|b_{n,c}|^2\). The Selberg length Hessian and the weighted Bergman/Fisher orbital are distinct spectral filters of those same data. The Casimir-transmutation identity converts the surface resolvent into a differential operator in conjugacy length, while the holomorphic discrete-series character gives the exact Selberg descendant factor

\[
\boxed{
\Theta_{2q-1}^{+}(a_{L/2})
=\frac{e^{-qL}}{1-e^{-L}}.
}
\]

The current representation-theory target is **not** to equate the weighted orbital with the ordinary character. It is to construct, or rule out, a canonical deformation insertion \(\mathcal A_{c,\mu}\) such that classwise

\[
\boxed{
\mathfrak T_{q,c}[\mu]
=\operatorname{Tr}_{D_{2q-1}^{+}}
\bigl(\mathcal A_{c,\mu}\,\pi_q(a_{\ell_c/2})\bigr)
}
\]

reproduces the cyclic-mode Bergman/Fisher transform with all centralizer, orientation and winding normalizations. This is the **Orbital--Character Closure (OCC)** problem; see `orbital-character-closure.md`.

The firewall is

\[
\boxed{
\text{kernel match}
\not\Rightarrow
\text{classwise coefficient match}
\not\Rightarrow
\text{global determinant identity}.
}
\]

## Current numbered frontier

The active numbered target remains **v0.27 — full charged multiplet / quartic holonomy response**.

The next task is to compute charged vector/hyper/tensor multiplet determinants on the same \((\tau,z)\) background and separate

\[
\sum q^2
\quad\text{from}\quad
\sum q^4
\]

as genuine second- versus fourth-order holonomy response. Only after that can the full Green--Schwarz pairings \(a\cdot b_i\) and \(b_i\cdot b_j\) be compared through one microscopic spectral model.

The rule remains

\[
\boxed{
\text{common invariant or asymptotic scale}
\neq
\text{physical identification of observables}.
}
\]

Lorentzian/horizon closure remains inactive.
