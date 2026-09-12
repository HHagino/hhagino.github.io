# FCIG: Normalization Lifts, Line-Bundle Curvature, and a Literature Audit

**Status:** theorem/no-go note + prior-art audit  
**Date:** 2026-09-12  
**Scope:** positive finite measures, normalization, holomorphic line-bundle lifts, log-partition potentials, Fisher geometry, anomaly lines, and the precise residue available to FCIG.  
**Depends on:** [`research-note.md`](research-note.md), [`chern-fisher-closure.md`](chern-fisher-closure.md), [`quillen-refinement.md`](quillen-refinement.md).

> **Claim policy.** **Established** labels published background. **Derived here** labels proofs written in this note but does not assert priority. **No-go** records an obstruction. **FCIG interpretation** is project terminology. **Open novelty question** means that no equivalent formulation was located in the sources checked here, not that priority has been established.

---

## 1. Executive finding

The attractive chain

\[
\text{unnormalized local weights}\to\text{probability normalization}
\to\text{line bundle}\to\text{Chern/Fisher curvature}
\]

contains three distinct statements.

1. A finite positive measure modulo positive scalar multiplication has a unique probability representative. Total-mass normalization globally trivializes this quotient.
2. Local positive weights transforming by squared moduli of holomorphic transition functions define a Hermitian holomorphic line-bundle lift. Their ratios may descend to a global probability model, while their logarithms give the standard Chern-curvature formula.
3. The topology of that lift is **not determined by the descended probability model**. Given a global probability model and an arbitrary Hermitian holomorphic line bundle, one can construct such a lift. The line-bundle class is additional data, not an invariant recoverable from probability alone.

Hence the defensible slogan is

\[
\boxed{\text{normalization forgets the topology of a chosen lift; it does not create or determine it.}}
\]

General measure models and Fisher tensors [AJLS17], exponential statistical bundles [CMP21; Pis22; Pis25], Kählerification [Mol13], positive-measure Fisher/Hellinger geometry [IS17; vO22], and partition functions on determinant/anomaly lines [Fre86; BF86a; BF86b; Qui85; Mon14] are established. No novelty claim is available for those ingredients or their elementary composition.

The possible FCIG residue is relative and categorical: define the **groupoid of normalization lifts over a fixed probability model**, then impose an intrinsic construction—determinant of cohomology, a family of operators, geometric quantization, projective amplitudes, or a functorial pushforward—that selects a lift. Without such a selector, its Chern class is arbitrary decoration.

---

## 2. Established background

### 2.1 Measure models before normalization

Ay, Jost, Lê, and Schwachhöfer define parametrized measure models as differentiable maps into finite measures and statistical models as the probability-measure subcase. They obtain Fisher and Amari--Chentsov tensors from roots of measures without requiring common null sets [AJLS17]. Thus

\[
M\to\mathcal M_+(\Omega)\quad\text{versus}\quad M\to\mathcal P(\Omega)
\]

is established territory.

Pistone and collaborators use “statistical bundle” for pairs consisting of a probability density and a centered random variable/Fisher score [CMP21; Pis22; Pis25]. This is a tangent/cotangent construction over a probability manifold, not a holomorphic normalization line. The same word therefore denotes a different bundle type.

### 2.2 Positive cones and the probability slice

The square-root representation maps positive densities into an \(L^2\) cone; total mass one gives a sphere-like probability submanifold. Fisher--Rao/Hellinger geometry on probability measures and positive cones is classical and appears in modern geometric treatments [IS17; vO22]. The mass coordinate is radial; fixing it gives a global slice rather than a topological obstruction.

### 2.3 Log partitions and Kählerification

For an exponential family

\[
p_\theta(x)=\exp\{\theta^aT_a(x)-\psi(\theta)\}r(x),\qquad
\psi=\log\int e^{\theta^aT_a(x)}r(x)d\nu,
\]

one has

\[
\partial_a\psi=\mathbb E_\theta[T_a],\qquad
\partial_a\partial_b\psi=\operatorname{Cov}_\theta(T_a,T_b)=g^F_{ab}.
\]

Molitor shows that the tangent bundle of an exponential family has a natural Kähler structure and develops Kählerification, including the relation of the positive probability simplex to an open part of complex projective space [Mol13]. Neither the Hessian identity nor Kählerification is an FCIG novelty.

### 2.4 Partition functions and anomaly lines

In determinant/anomaly geometry a partition function may be a section of a determinant or anomaly line rather than a scalar. Its norm, connection, curvature, and holonomy encode local and global anomaly data [Fre86; BF86a; BF86b; Qui85; Mon14]. This is close to “normalization data carry geometry,” but more intrinsic: a family of operators or a field theory selects the line.

---

## 3. The real normalization bundle is trivial

Let \(\mathcal M_+^{\mathrm{fin}}(\Omega)\) be the nonzero finite positive measures and let \(\mathbb R_{>0}\) act by scalar multiplication.

### Proposition 3.1 — normalization triviality

\[
N(\mu)=\frac{\mu}{\mu(\Omega)}
\]

induces

\[
\mathcal M_+^{\mathrm{fin}}(\Omega)/\mathbb R_{>0}\cong\mathcal P(\Omega)
\]

and

\[
\boxed{\mathcal M_+^{\mathrm{fin}}(\Omega)
\cong\mathcal P(\Omega)\times\mathbb R_{>0},\quad
\mu\mapsto(N(\mu),\mu(\Omega)).}
\]

#### Proof

The inverse maps \((p,m)\) to \(mp\). Both composites are identities. The result holds topologically or smoothly whenever evaluation, scaling, and positive division have the corresponding regularity. \(\square\)

### No-go 3.2 — mass normalization has no characteristic curvature

The slice \(\mu(\Omega)=1\) is global. If locally \(g_{ij}=Z_j/Z_i\), then \(g_{ij}=Z_i^{-1}Z_j\) is a Čech coboundary. Likewise

\[
A_i=d\log Z_i\quad\Rightarrow\quad F_i=dA_i=0.
\]

Therefore ordinary positive rescaling and total-mass gauge fixing cannot generate a nonzero characteristic class. This is an elementary structural audit, not a novelty theorem.

---

## 4. Holomorphic normalization lifts

Let \(B\) be complex with cover \(\{U_i\}\). Suppose positive local weights \(q_i:\Omega\times U_i\to\mathbb R_{>0}\) and \(g_{ij}\in\mathcal O^\times(U_{ij})\) satisfy a cocycle law and, after fixing a transition convention,

\[
q_j=|g_{ij}|^2q_i. \tag{4.1}
\]

Assume \(0<Z_i(b):=\int q_i(x,b)d\nu(x)<\infty\).

### Theorem 4.1 — descent and Chern curvature

The densities \(p_i=q_i/Z_i\) agree on overlaps. Moreover

\[
Z_j=|g_{ij}|^2Z_i,\qquad K_j-K_i=\log|g_{ij}|^2,
\quad K_i=\log Z_i,
\]

so

\[
\boxed{\omega=i\partial\bar\partial K_i}
\]

is a global real \((1,1)\)-form and, up to the fixed sign and \(2\pi\) convention, the Chern curvature form.

#### Proof

The transition factor is independent of \(x\), so integration gives the law for \(Z_i\); it cancels in \(q_i/Z_i\). Since \(g_{ij}\) is holomorphic and nonzero,

\[
\partial\bar\partial\log|g_{ij}|^2=0,
\]

and the local curvature forms agree. \(\square\)

**Status:** **Derived here from established line-bundle geometry.** It is a packaging lemma, not presently a defensible standalone novelty claim.

### Convention firewall

If \(e_i=t_{ij}e_j\), local metric coefficients satisfy \(h_i=|t_{ij}|^2h_j\). Equation (4.1) may instead use \(g_{ij}=t_{ij}^{-1}\), depending on whether \(q_i\) is treated as a frame or metric coefficient. A final paper must derive rather than guess the sign in

\[
[\omega/2\pi]=\pm c_1(L).
\]

---

## 5. Reconstruction no-go

### Proposition 5.1 — arbitrary-lift theorem

Let \(p(x|b)\) be any global positive probability density. Let \(L\to B\) be any holomorphic line bundle with smooth Hermitian metric coefficients \(h_i>0\). Define

\[
q_i(x,b)=h_i(b)p(x|b),\qquad Z_i(b)=h_i(b).
\]

Then \(q_i/Z_i=p\), while the normalization lift has the Chern class of \(L\).

#### Proof

Since \(\int p\,d\nu=1\), \(\int h_ip\,d\nu=h_i\). The transition law of \(q_i\) is that of \(h_i\), and normalization cancels it. Since \(L\) was arbitrary, so is its permitted holomorphic Chern class. \(\square\)

### Corollary 5.2 — non-identifiability

No function of the descended probability model alone recovers \(c_1(L)\) for all normalization lifts: the same \(p\) admits the trivial lift and, where available, lifts with nonzero first Chern class.

Thus **hidden normalization topology** is safe only when “hidden” means “forgotten by a specified forgetful map,” not “intrinsically encoded in probability.” One should define

\[
\mathsf{NormLift}(B,\Omega)\longrightarrow\mathsf{Prob}(B,\Omega),
\qquad (L,h,\{q_i\})\mapsto p.
\]

The topology lies in the fiber of this map.

\[
\boxed{\text{the quotient remembers probability; the choice of numerator remembers geometry.}}
\]

---

## 6. Exact scope of Fisher identification

Writing \(\ell=\log q\) locally and differentiating under the integral gives

\[
\partial_a\partial_{\bar b}\log Z
=\operatorname{Cov}_p(\partial_a\ell,\partial_{\bar b}\ell)
+\mathbb E_p[\partial_a\partial_{\bar b}\ell]. \tag{6.1}
\]

A log-partition Hessian is therefore not automatically Fisher information. For

\[
\ell=\log r+z^aT_a+\bar z^b\overline{T_b},
\]

the second term vanishes and

\[
\partial_a\partial_{\bar b}\log Z
=\operatorname{Cov}_p(T_a,\overline{T_b}),
\]

the Hermitian Fisher tensor of this exponential family.

For Proposition 5.1, however,

\[
\log q_i=\log p+\log h_i,\qquad \log Z_i=\log h_i.
\]

Changing \((L,h)\) varies the Chern curvature while leaving \(p\) and its Fisher metric fixed. Hence

\[
\boxed{i\partial\bar\partial\log Z_i\neq g^F(p)\quad\text{in general}.}
\]

Equality requires a selector tying \(q\) intrinsically to the statistical model.

---

## 7. Prior-art matrix

| Statement | Closest literature | Audit result |
| --- | --- | --- |
| Finite measures before probability normalization | Parametrized measure models [AJLS17] | Established |
| Probability density plus score as a bundle | Pistone statistical bundle [CMP21; Pis22; Pis25] | Established, different bundle type |
| Fisher geometry on positive/probability measures | [IS17; vO22] | Established |
| \(\log Z\) Hessian equals Fisher for exponential families | Standard information geometry; [Mol13] | Established under hypotheses |
| Kähler geometry from exponential families | [Mol13] | Established |
| Local Hermitian weights yield Chern curvature | Standard complex geometry | Established |
| Partition function as section/norm of a line | [Fre86; BF86a; BF86b; Qui85; Mon14] | Established in intrinsic operator/QFT settings |
| Equal transformation of \(q_i,Z_i\) makes \(q_i/Z_i\) descend | Theorem 4.1 | Elementary packaging; no novelty claim |
| Same \(p\) supports arbitrary line-bundle lifts | Proposition 5.1 | Elementary no-go; essential correction |
| Functorial groupoid/classification of intrinsically selected normalization lifts | No exact match located | Open novelty question; broader database audit required |

---

## 8. Potentially original residue

A viable theorem must make the lift canonical or constrained.

1. **Determinant-selected lift.** Start from \(L=\det R\pi_*E\); the Quillen/Bismut--Freed structures select its geometry.
2. **Projective statistical state.** Use projective amplitudes or a projective Hilbert bundle, where quadratic probabilities can descend despite a genuine obstruction to global amplitudes. This meets `chern-fisher-closure.md` naturally.
3. **Functorial lift.** Require naturality under probabilistic mappings and sufficient statistics [AJLS17; Le20]. A classification of such lifts may eliminate arbitrary decorations.
4. **Differential refinement.** Select \(\widehat c_1(L,\nabla)\in\widehat H^2(B;\mathbb Z)\), retaining both curvature and flat holonomy.

The pass condition is

\[
\boxed{\text{the model's intrinsic data select the lift, and the selection commutes with natural morphisms.}}
\]

---

## 9. Research gates

- **NT-A — PASS:** positive finite measures modulo \(\mathbb R_{>0}\) have the global probability slice.
- **NT-B — PASS:** a chosen holomorphic normalization lift gives descent and standard Chern curvature.
- **NT-C — NO-GO:** probability alone does not determine the lift or its topology.
- **NT-D — CONDITIONAL PASS:** Fisher equals the log-partition Hessian only under explicit affine-exponential or equivalent conditions.
- **NT-E — OPEN:** construct an intrinsic determinant, projective-amplitude, functorial, or differential-cohomological selector.
- **NT-F — OPEN:** search MathSciNet, zbMATH, Web of Science/Scopus and reference chains before any priority statement. This web-accessible audit positions the claim but is not exhaustive priority certification.

---

## 10. Relation to FCIG

The audit supports the existing three-layer architecture \((L_Q,\lambda_{\rm an},TM)\): it rules out manufacturing \(\lambda_{\rm an}\) from scalar normalization alone, favors determinant/Quillen or projective-state data as an intrinsic source, and leaves Lorentzian Gravity Closure inactive.

\[
\boxed{
\begin{array}{c}
\text{intrinsic operator / derived family / projective state}\\
\Downarrow\\
\text{canonical line or projective bundle with connection}\\
\Downarrow\\
\text{local weights and normalized observables}\\
\Downarrow\\
\text{Fisher/Chern comparison under typed hypotheses}.
\end{array}}
\]

The arrow cannot be reversed from the bottom row without extra information.

---

## 11. Sources

1. Ay, Jost, Lê, Schwachhöfer, “Parametrized Measure Models,” *Bernoulli* 24 (2018), [arXiv:1510.07305](https://arxiv.org/abs/1510.07305).
2. Molitor, “Exponential Families, Kähler Geometry and Quantum Mechanics,” *J. Geom. Phys.* 70 (2013), 54--80, [arXiv:1203.2056](https://arxiv.org/abs/1203.2056).
3. Chirco, Malagò, Pistone, “Lagrangian and Hamiltonian Mechanics for Probabilities on the Statistical Manifold,” [arXiv:2009.09431](https://arxiv.org/abs/2009.09431).
4. Pistone, “Information Geometry of Bayes Computations,” [arXiv:2502.02160](https://arxiv.org/abs/2502.02160).
5. Itoh, Satoh, “Geometric Mean of Probability Measures and Geodesics of Fisher Information Metric,” [arXiv:1708.07211](https://arxiv.org/abs/1708.07211).
6. van Oostrum, “Bures--Wasserstein Geometry for Positive-Definite Hermitian Matrices and Their Trace-One Subset,” [arXiv:2001.08056](https://arxiv.org/abs/2001.08056).
7. Freed, “Determinants, Torsion, and Strings,” *Commun. Math. Phys.* 107 (1986), [Project Euclid](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-107/issue-3/Determinants-torsion-and-strings/cmp/1104116145.full).
8. Bismut, Freed, “The Analysis of Elliptic Families. I--II,” *Commun. Math. Phys.* 106--107 (1986).
9. Quillen, “Determinants of Cauchy--Riemann Operators over a Riemann Surface,” *Funct. Anal. Appl.* 19 (1985).
10. Monnier, “The Anomaly Line Bundle of the Self-Dual Field Theory,” *Commun. Math. Phys.* 325 (2014), [arXiv:1109.2904](https://arxiv.org/abs/1109.2904).
11. Lê, “Diffeological Statistical Models, the Fisher Metric and Probabilistic Mappings,” [arXiv:1912.02090](https://arxiv.org/abs/1912.02090).

Machine-readable entries are in [`normalization-topology.bib`](normalization-topology.bib).
