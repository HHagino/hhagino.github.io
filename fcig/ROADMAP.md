# FCIG Research Roadmap

**Current target:** v0.27 — full charged multiplet / quartic holonomy response  
**Updated:** 2026-09-09

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations remain explicit no-go results.

---

## v0.3–v0.17 — geometric, determinant and response foundation — COMPLETE

Established milestones include theta/ppav state counting, curved-curve Bergman and Quillen sectors, differential cohomology, determinant holonomy, global metrized Deligne--Riemann--Roch, structure-group and pushforward no-gos, anomaly descent, functional-response ambiguity, conditional semiclassical closure, heat-kernel operators and elliptic realization-map dynamics.

No Einstein equation is derived from these data alone.

---

## v0.18–v0.20 — induced and intrinsic elliptic geometry — COMPLETE

Arbitrary heavy masses do not predict the FCIG metric without an intrinsic operator. The actual area-one elliptic Laplacian gives

\[
\boxed{-\partial\bar\partial\log\det{}'\Delta_\tau=F_{\lambda_H}},
\]

and the adiabatic calculation separates UV-sensitive local terms from a finite automorphic threshold.

---

## v0.21–v0.23 — field-content and multiplet thresholds — COMPLETE

For the restricted parity-even elliptic family,

\[
\boxed{
G_{VHT}^{\rm fin}
=\frac{K}{16\pi^3L^2}Z_\tau(2)g_{\rm hyp},
\qquad
K=2n_V-n_H+2n_T.
}
\]

Vector and tensor multiplets give positive \(B_{Z_2}=1/8\); a hypermultiplet gives \(-1/16\). Self-dual zero modes and global phases remain separate.

---

## v0.24 — threshold / anomaly-polynomial comparison — COMPLETE

The free-multiplet anomaly coefficient map is invertible and therefore reconstructs the field counts, but threshold and anomaly cancellation have different kernels. Reconstructibility is not identification of observables.

Sources: `threshold-anomaly.*`.

---

## v0.25 — Green--Schwarz / anomaly-lattice audit — COMPLETE WITH NO-GO

After

\[
H-V+29T=273,
\]

the gauge-blind threshold obeys

\[
\boxed{K=V+31T-273.}
\]

At fixed \((V,T)\), Green--Schwarz lattice refinements \(a,b_i\), lattice embeddings and global gauge-group data do not change \(K\), even though they can change the global consistency of the theory. F-theory witnesses occur with both signs of \(K\).

Sources: `green-schwarz-lattice.*`.

---

## v0.26 — charged elliptic / Jacobi spectral determinant — COMPLETE

Sources:

- `charged-jacobi.md`
- `charged-jacobi.py`
- `charged-jacobi.bib`
- `charged-jacobi.html`

### Gate DV — exact charged spectrum — PASS

With

\[
z=\alpha\tau+\beta
\]

and the stated quasi-periodic boundary convention, an integral charge \(q\) has

\[
\boxed{
\lambda^{(q)}_{m,n}
=\frac{4\pi^2}{Y}|m\tau-n+qz|^2.
}
\]

The zero-mode divisor is

\[
qz\in\mathbb Z\tau+\mathbb Z.
\]

### Gate DW — Kronecker / zeta determinant — PASS

The second Kronecker limit formula gives

\[
\boxed{
D_q(\tau,z)
=e^{-2\pi q^2(\operatorname{Im}z)^2/Y}
\left|\frac{\theta_1(qz|\tau)}{\eta(\tau)}\right|^2.
}
\]

The zero-mode normalization matches Model XIX exactly:

\[
\boxed{
\lim_{z\to0}\frac{D_q}{\lambda^{(q)}_{0,0}}
=Y|\eta(\tau)|^4
=\det{}'\Delta_\tau.
}
\]

### Gate DX — Jacobi covariance — PASS

The holomorphic factor \(\theta_1(qz|\tau)/\eta(\tau)\) has weight zero and Jacobi index

\[
\boxed{m_q=\frac{q^2}{2}}.
\]

The Gaussian completion cancels its absolute-value automorphy factor, so \(D_q\) is invariant under the modular action and the allowed elliptic large-gauge translations.

The checker verifies the \(S\), \(T\) and elliptic generators numerically in the chosen normalization.

### Gate DY — exact Jacobi curvature — PASS

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

At fixed \(\tau\),

\[
\boxed{-\partial_z\partial_{\bar z}\log D_q=\frac{\pi q^2}{Y}.}
\]

Thus the charged spectral geometry reads the quadratic charge moment exactly.

### Gate DZ — many charges / representation index — PASS

For determinant weights \(\nu_a\) and charges \(q_a\),

\[
\boxed{\mathcal Q_2=\sum_a\nu_aq_a^2}
\]

controls both the total Jacobi index and the fiberwise spectral curvature. For a nonabelian Cartan holonomy, \(q^2\) is replaced by the quadratic weight tensor \(\sum_{\rho\in R}\rho\otimes\rho\).

### Gate EA — Green--Schwarz common microscopic invariant — PASS WITH INTERPRETATION BOUNDARY

For a 6d \(U(1)\) factor, the established anomaly equations include

\[
\boxed{
a\cdot\widetilde b=-\frac16\sum_qx_qq^2,
\qquad
\widetilde b\cdot\widetilde b=\frac13\sum_qx_qq^4.
}
\]

Therefore the same microscopic quadratic charge moment \(\sum x_qq^2\) occurs in the Jacobi spectral index/curvature and in \(a\cdot\widetilde b\). This is a genuine common microscopic invariant, but not an equality between anomaly and spectral observables.

The quartic moment \(\sum x_qq^4\) is not determined by the quadratic Jacobi metric.

### Gate EB — global gauge data — PASS AS A TYPED CHANNEL

Allowed elliptic translations are determined by the cocharacter lattice: a holonomy shift is a gauge identification only when every allowed weight evaluates integrally. Thus the charged determinant can see global gauge-group information that the gauge-blind Model XXV threshold could not.

### Gate EC — scope — PASS

The model is a flat-holonomy, parity-even determinant calculation. Full charged multiplet spin structure, nonabelian Weyl quotients, chiral phases, background gauge curvature and quartic response remain separate.

---

## v0.27 — full charged multiplet / quartic holonomy response — ACTIVE

### Gate ED — charged multiplet completion

Repeat the Jacobi calculation for complete charged vector/hyper/tensor multiplets, including spin connections and determinant signs rather than scalar multiplicity alone.

### Gate EE — quadratic index matrix

For abelian and Cartan holonomies, compute the complete multiplet coefficient multiplying

\[
\sum_{\rho}\rho\otimes\rho.
\]

Compare it with the microscopic representation invariant entering \(a\cdot b_i\) only after conventions are fixed.

### Gate EF — quartic holonomy response

Compute fourth derivatives / four-point holonomy response and determine whether the independent invariant

\[
\sum_qx_qq^4
\]

appears with the expected representation-theoretic structure.

### Gate EG — Green--Schwarz pairings

Only after ED–EF compare the spectral quadratic/quartic invariants with

\[
a\cdot b_i,
\qquad
b_i\cdot b_j.
\]

Do not infer anomaly cancellation from a finite determinant.

### Gate EH — global form

Track the cocharacter lattice and Weyl quotient explicitly so global gauge-group data affect the holonomy domain rather than being added by analogy.

**Pass condition:** a full charged-multiplet spectral model in which quadratic and quartic charge invariants are independently derived and compared with Green--Schwarz gauge pairings through the same microscopic representation data.

---

## Gravity Closure gate — NOT ACTIVE

Lorentzian gravitational/horizon closure remains separate until an independently justified causal/dynamical bridge is supplied.
