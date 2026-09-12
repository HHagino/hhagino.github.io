# FCIG Research Roadmap

**Current target:** v0.27 — full charged multiplet / quartic holonomy response  
**Updated:** 2026-09-10

The roadmap is ordered so that each mechanism is tested before any gravitational interpretation. Failed extrapolations remain explicit no-go results.

---

## Parallel mathematical track — Fisher–Bergman–Quillen Information Closure — ACTIVE

Sources:

- `fisher-bergman-quillen.md`
- `fisher-bergman-quillen.html`
- `fisher-bergman-quillen.bib`
- `kodaira-spencer-information.md`
- `kodaira-spencer-information.html`
- `kodaira-spencer-information.bib`
- `kodaira-spencer-information-citation-audit.md`
- `grassmannian-quantum-information.md`
- `chern-fisher-closure.md`
- `born-slater-information.md`
- `hermitian-born-fisher.md`
- `bls-position-transport.md`
- `bls-position-transport.bib`
- `bls-position-transport-citation-audit.md`

This track does **not** replace the v0.27 charged/Jacobi program. It isolates the mathematical relation among Fisher response, Bergman determinantal processes, direct-image curvature, Kodaira--Spencer deformation, Weil--Petersson geometry and Quillen determinant geometry.

### Gate FI-A — event/probability typing — PASS WITH CORRECTION

The event sigma-algebra can be regarded as a Boolean ring and hence by Stone duality through its spectrum. The null events form an ideal, so almost-everywhere identification is the quotient by the null ideal.

Because every Boolean ring is reduced,

\[
\boxed{\text{null ideal}\neq\text{nilradical}.}
\]

The project term “measured Stone scheme” means the Stone spectrum plus an additional probability valuation; sigma-additivity is not claimed to follow from ordinary scheme structure alone.

### Gate FI-B — exact fixed-complex score — DERIVED HERE

For the Bergman DPP associated with \(H^0(X,L^k)\), varying the Hermitian/Kähler potential by \(\psi\) gives

\[
\boxed{
D_\psi\log q_{k,\phi}
=
\sum_a(\Delta_\phi-k)\psi(x_a).
}
\]

The normalized score is the centered linear statistic of

\[
A_{k,\phi}\psi=(\Delta_\phi-k)\psi.
\]

### Gate FI-C — exact Fisher–Bergman energy — DERIVED HERE

Using the standard covariance identity for projection DPPs,

\[
\boxed{
\begin{aligned}
\mathcal I_{k,\phi}(\psi,\eta)
&=\frac12\iint
\bigl(A_k\psi(x)-A_k\psi(y)\bigr)
\bigl(A_k\eta(x)-A_k\eta(y)\bigr)
\\
&\qquad\qquad\times |K_k(x,y)|^2dV_xdV_y.
\end{aligned}
}
\]

This is the exact fixed-complex Fisher–Bergman side.

### Gate FI-D — moving-Kähler Hessian defect — DERIVED HERE

The naive exponential-family identity \(\mathcal I_k=\operatorname{Hess}\log Z_k\) fails because \(\Delta_\phi\) moves with \(\phi\). The exact correction is

\[
\boxed{
\mathcal I_k
=
\operatorname{Hess}\log Z_k
+
\mathfrak D_k^{\rm met},
}
\]

with

\[
\boxed{
\mathfrak D_k^{\rm met}(\psi,\eta)
=
\int_X\rho_k
\langle i\partial\bar\partial\psi,
i\partial\bar\partial\eta\rangle dV.
}
\]

### Gate FI-E — Quillen bookkeeping — PASS AS A TYPED IDENTITY

Using the Quillen convention already fixed in `quillen-refinement.md`,

\[
h_Q=e^{\mathcal T_k}h_{L^2},
\qquad
h_{L^2}(\Sigma,\Sigma)=Z_k,
\]

so on the real Kähler-potential space

\[
\boxed{
\mathcal I_k
=
\operatorname{Hess}\log h_Q
-
\operatorname{Hess}\mathcal T_k
+
\mathfrak D_k^{\rm met}.
}
\]

This is a functional-Hessian identity, not a convention-free Chern-form equality.

### Gate FI-F — intrinsic moving-complex-structure / Kodaira--Spencer channel — PASS

For a compact hyperbolic curve family set

\[
E_q=\pi_*K_{\mathcal X/B}^{q},
\qquad
m=q-1.
\]

Tracing the Kodaira--Spencer resolvent summand in Berndtsson's curvature formula defines the canonical positive Hermitian tensor

\[
\boxed{
\mathfrak K_q(\xi,\bar\eta)
=
m\sum_a
\left\langle
(m+\Delta')^{-1}i_{\mu_\xi}u_a,
 i_{\mu_\eta}u_a
\right\rangle.
}
\]

Specializing the Wan--Zhang high-power expansion to complex dimension one gives, without fitting a coefficient,

\[
\boxed{
\mathfrak K_q
=
\frac{q-1}{4\pi}G_{\rm WP}+O(1),
\qquad
\frac{4\pi}{q-1}\mathfrak K_q\to G_{\rm WP}.
}
\]

The factor is the product

\[
\boxed{
\frac12\times\frac{q-1}{2\pi}
=
\frac{q-1}{4\pi},
}
\]

where \(1/2\) is the leading Kodaira--Spencer resolvent coefficient and \((q-1)/(2\pi)\) is the leading curve Bergman density.

**Status:** derived in `kodaira-spencer-information.md` from established Berndtsson/Wan--Zhang formulas; no literature-novelty claim.

### Gate FI-G — moving-fiber classical Fisher transport — PASS AS A NO-GO

A moving-fiber classical Fisher tensor is not canonical before one fixes how neighboring configuration spaces are identified. If two transports differ infinitesimally by a vector field \(V_\xi\), then with the pullback convention

\[
\boxed{
S_\xi^{\tau'}
=
S_\xi^\tau
+
\operatorname{div}_{P}V_\xi.
}
\]

Consequently the Fisher covariance changes by the corresponding cross terms and probability-divergence norm. Therefore

\[
\boxed{
\text{arbitrary moving-fiber classical Fisher}
\neq
\text{canonical moduli tensor}.
}
\]

This replaces the earlier over-strong version of the Information Closure Conjecture.

### Gate FI-H — canonical statistical transport closure — PASS WITH BLS/KE TYPING

The transport ambiguity is resolved by distinguishing the ambient position measurement from its Bergman compression. For the ambient BLS Hilbert field

\[
\mathscr L_t=L^2(X_t,K_{X_t}\otimes E_t),
\]

Varolin's twisted-Lie BLS--Chern connection gives, for multiplication by a smooth observable \(\varphi\),

\[
\boxed{
\nabla_X^{\operatorname{End}\mathscr L}M_\varphi
=M_{V_X^\theta\varphi}.
}
\]

Thus horizontally advected position observables, and equivalently the ambient position PVM under the finite horizontal flow, are parallel.

For the Bergman projection \(P\), however, the compressed Toeplitz observable obeys the exact defect formula

\[
\boxed{
\nabla_X^{\operatorname{End}\mathscr H}(PM_\varphi P)
=
\mathbb B_X^*QM_\varphi P
+PM_\varphi Q\mathbb B_X
}
\]

when \(V_X^\theta\varphi=0\). Therefore the compressed POVM is generally not parallel; its defect is controlled by the same second fundamental form \(\mathbb B\) that produces the Grassmannian information metric.

The Bergman DPP itself is the Born law of a Slater state measured by the **ambient many-body position PVM**, so the first, parallel object is the relevant one. Choosing Schumacher's Kähler--Einstein horizontal lift and the corresponding BLS/Chern realization gives the exact Hermitian Born--Fisher identity

\[
\boxed{
I_q^{KE}(X,Y)+I_q^{KE}(JX,JY)
=4g_{\rm Pl,q}^{KE}(X,Y).
}
\]

With the audited Grassmannian asymptotic,

\[
\boxed{
\frac{\pi}{q-1}
\left(I_q^{KE}+J^*I_q^{KE}\right)
\to G_{\rm WP}.
}
\]

Equivalently,

\[
I_{\rm HBF,q}^{KE}
:=\frac14(I_q^{KE}+J^*I_q^{KE})
\]

satisfies

\[
\boxed{
I_{\rm HBF,q}^{KE}
=\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\]

Comparing with the intrinsic KS resolvent channel,

\[
\boxed{
I_{\rm HBF,q}^{KE}-\mathfrak K_q=O(1),
\qquad
\frac{4\pi}{q-1}
\left(I_{\rm HBF,q}^{KE}-\mathfrak K_q\right)\to0.
}
\]

**Source / proof location:** `bls-position-transport.md`. The ambient BLS machinery is established literature; the multiplication covariance, compression-defect identity and assembled DPP/WP closure are marked **Derived here**, not literature-novelty claims.

### Gate FI-I — Quillen/WP normalization crosswalk — OPEN TECHNICAL AUDIT

Wan--Zhang's Hermitian pairing convention and the Zograf--Takhtajan \(\omega_{\rm WP}\) first-Chern-form convention must be crosswalked explicitly before numerical coefficients are compared. No factor of \(2\), \(i\), or \(2\pi\) is to be inferred by notation matching alone.

**Next information-closure target:** compute the full finite-\(q\) expansion of

\[
I_{\rm HBF,q}^{KE}-\mathfrak K_q
=\mathfrak B_q-\mathfrak K_q,
\]

currently controlled only as \(O(1)\), and quantify the anisotropic split between the individual real Fisher channels \(X\) and \(JX\).

**Scope rule:** the entire Information Closure track remains Euclidean/Kähler. It does not activate the Lorentzian Gravity Closure gate.

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

---

## Normalization Topology audit — PASS / NO-GO / OPEN

Source: `normalization-topology-literature-audit.md`.

- **NT-A PASS:** positive finite measures modulo \(\mathbb R_{>0}\) have a global probability slice.
- **NT-B PASS:** equally transforming weights and partition functions descend and define the standard Chern curvature of a chosen lift.
- **NT-C NO-GO:** the descended probability does not determine the lift; the same \(p\) admits arbitrary Hermitian holomorphic line-bundle decorations.
- **NT-D CONDITIONAL:** \(\partial\bar\partial\log Z\) agrees with Fisher only under affine-exponential or equivalent hypotheses.
- **NT-E OPEN:** construct an intrinsic, functorial selector from determinant/direct-image, projective-amplitude, or probabilistic-morphism data.

No novelty claim is made for the elementary gluing theorem. Novelty assessment is deferred to the selector/classification problem.
