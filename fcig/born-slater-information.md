# FCIG: Born–Slater Information Geometry

**Status:** established geometry + exact deductions + reconstruction program  
**Date:** 2026-09-10  
**Scope:** Born measurement maps, projective/Fubini–Study geometry, classical and quantum Fisher information, Slater/Grassmannian geometry, and determinantal probability laws.  
**Depends on:** [`fisher-bergman-quillen.md`](fisher-bergman-quillen.md), [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md), [`chern-fisher-closure.md`](chern-fisher-closure.md).

> **Claim policy.** **Established** means a cited theorem or standard construction. **Derived here** means a deduction written below from those inputs; it is not a novelty claim. **FCIG interpretation** means a proposed conceptual reading. **Reconstruction problem** is an open program. Nothing in this note claims that information geometry or thermodynamics alone has already derived quantum mechanics or the Born rule.
>
> Dedicated bibliography: [`born-slater-information.bib`](born-slater-information.bib). Citation audit: [`born-slater-information-citation-audit.md`](born-slater-information-citation-audit.md).

---

## 0. Result in one page

The mathematically controlled chain is

\[
\boxed{
\mathbb P(\mathcal H)
\xrightarrow{\;\mathcal B_M\;}
\mathcal P(\Omega_M),
\qquad
[\psi]\mapsto p_\psi^M,
}
\tag{0.1}
\]

where \(\mathcal B_M\) is the probability map determined by a measurement \(M\). For a rank-one position measurement,

\[
\boxed{
p_\psi(x)=|\langle x|\psi\rangle|^2.}
\tag{0.2}
\]

The domain carries the Fubini–Study metric \(g_{FS}\); the image probability model carries the classical Fisher metric \(I_M\). Wootters relates Hilbert-space angle to statistical distinguishability for pure states [Woo81], and Braunstein–Caves characterize the quantum metric through the maximal Fisher information obtainable from measurements [BC94]. In the usual pure-state normalization,

\[
\boxed{I_Q=4g_{FS},\qquad I_M\le I_Q.}
\tag{0.3}
\]

Thus the Born measurement map is information-contracting in the operational sense:

\[
\boxed{
\mathcal B_M^* I_{\rm Fisher}\preceq 4g_{FS}.
}
\tag{0.4}
\]

For a fixed real direction, writing a normalized amplitude as

\[
\psi=\sqrt p\,e^{i\theta},
\]

and denoting by \(a\) the centered phase score, the exact pure-state decomposition is

\[
\boxed{
4g_{FS}=I_M+4\operatorname{Var}_p(a).
}
\tag{0.5}
\]

Hence the information lost by the chosen probability measurement is exactly a nonnegative phase-information defect in this representation.

For fermions, let \(E\subset\mathcal H\) be an \(N\)-plane with orthonormal basis \(u_1,\ldots,u_N\). The Plücker map sends

\[
E\longmapsto
[\Psi_E],
\qquad
\Psi_E=u_1\wedge\cdots\wedge u_N,
\tag{0.6}
\]

so single Slater states form a Grassmannian submanifold of projective many-body Hilbert space [AS20]. In a position basis,

\[
\Psi_E(x_1,\ldots,x_N)
=\frac1{\sqrt{N!}}\det[u_i(x_j)].
\tag{0.7}
\]

Applying the Born map gives

\[
\boxed{
P_E(x_1,\ldots,x_N)
=\frac1{N!}\left|\det[u_i(x_j)]\right|^2
=\frac1{N!}\det[K_E(x_i,x_j)],
}
\tag{0.8}
\]

where

\[
K_E(x,y)=\sum_{i=1}^N u_i(x)\overline{u_i(y)}.
\]

Therefore the fermionic Slater ray produces exactly a projection determinantal point process.

The central diagram is

\[
\boxed{
\operatorname{Gr}(N,\mathcal H)
\xrightarrow{\rm Pl\ddot ucker}
\mathbb P(\wedge^N\mathcal H)
\xrightarrow{\rm Born}
\operatorname{DPP}(K_E).
}
\tag{0.9}
\]

The left/middle spaces carry Grassmannian/Fubini–Study quantum geometry; the right side carries classical Fisher geometry. The preceding FCIG notes show that in the hyperbolic \(H^0(K^q)\) family the Chern-covariant Grassmannian metric has the asymptotic

\[
\boxed{
\frac{4\pi}{q-1}g_{{\rm Gr},q}^{\rm C}
\longrightarrow G_{\rm WP}.
}
\tag{0.10}
\]

Thus Slater geometry is not merely compatible with an information-geometric reading: in this model it gives a concrete bridge from fermionic quantization to moduli-space information geometry.

What is **not** proved is equally important. Equation (0.2) is assumed as the quantum probability rule. Gleason's theorem shows that, once one assumes the Hilbert-space event lattice and noncontextual additive probabilities in dimension at least three, probabilities are of the form \(\operatorname{tr}(\rho P)\), giving squared amplitudes for pure states [Gle57]. Busch gives an analogous effect/POVM formulation [Bus03]. These are reconstruction results **inside quantum event geometry**, not derivations of Hilbert-space quantum mechanics from thermodynamics.

Accordingly, FCIG should formulate three separate reconstruction problems:

\[
\boxed{
\begin{array}{rcl}
\text{R1} &:& \text{why complex projective state space?}\\
\text{R2} &:& \text{why the Born quadratic probability map?}\\
\text{R3} &:& \text{why exterior-power composition for fermions?}
\end{array}}
\tag{0.11}
\]

Only after these are derived from independent statistical/thermodynamic/index axioms would it be legitimate to claim an emergence of quantum mechanics.

---

# Part I. Born measurement as a map of information geometries

## 1. Projective pure-state geometry

A nonzero vector \(\psi\in\mathcal H\) defines the same pure physical state as \(c\psi\) for any nonzero complex scalar \(c\). Pure states therefore live in

\[
\mathbb P(\mathcal H).
\]

The Hermitian inner product induces the Fubini–Study Kähler metric on this projective space. This is standard geometric quantum mechanics [AS98].

For a normalized local section \(\psi(\theta)\), the real pure-state metric in parameter directions \(\partial_i\) is

\[
\boxed{
(g_{FS})_{ij}
=\operatorname{Re}
\left(
\langle\partial_i\psi,\partial_j\psi\rangle
-\langle\partial_i\psi,\psi\rangle
 \langle\psi,\partial_j\psi\rangle
\right).
}
\tag{1.1}
\]

With the conventional symmetric-logarithmic-derivative normalization for pure states,

\[
\boxed{(I_Q)_{ij}=4(g_{FS})_{ij}.}
\tag{1.2}
\]

[BC94].

---

## 2. The Born measurement map

Let \(M\) be a POVM on an outcome space \(\Omega_M\), written schematically as \(M(dx)\). A normalized pure state determines

\[
\boxed{
p_\psi^M(dx)=\langle\psi,M(dx)\psi\rangle.}
\tag{2.1}
\]

This defines

\[
\boxed{
\mathcal B_M:\mathbb P(\mathcal H)\to\mathcal P(\Omega_M).
}
\tag{2.2}
\]

For a rank-one sharp measurement \(M_x=|x\rangle\langle x|\),

\[
\boxed{p_\psi(x)=|\langle x|\psi\rangle|^2.}
\tag{2.3}
\]

**Established:** this is the usual Born probability rule; Born's 1926 scattering paper is the historical origin of the probabilistic amplitude-squared interpretation [Bor26].

**FCIG interpretation:** \(\mathcal B_M\) is a map from projective quantum-state geometry to a classical probability manifold.

This interpretation does not replace the physical measurement postulate. It makes its geometric effect explicit.

---

## 3. The measurement map contracts information

For a parameterized family \(\psi_\theta\), the output model \(p_\theta^M\) has classical Fisher information

\[
(I_M)_{ij}
=
\int
\partial_i\log p_\theta^M\,
\partial_j\log p_\theta^M\,
p_\theta^M.
\tag{3.1}
\]

Braunstein–Caves show that the quantum statistical metric is obtained by optimizing distinguishability over measurements; in particular every fixed measurement satisfies

\[
\boxed{I_M\preceq I_Q.}
\tag{3.2}
\]

[BC94]. Wootters' earlier statistical-distance construction already identifies the Hilbert-space angle with the optimal statistical distinguishability of pure preparations [Woo81].

Combining with (1.2),

\[
\boxed{
\mathcal B_M^*I_{\rm Fisher}
\preceq 4g_{FS}.
}
\tag{3.3}
\]

**FCIG interpretation:** Born measurement is an information channel from a richer projective state geometry to a classical statistical geometry.

The word “shadow” can be used heuristically, but the precise statement is the metric inequality (3.3), not an isometry for every measurement.

---

## 4. Exact amplitude/phase decomposition

Fix one real parameter direction and a normalized state. In a measurement representation write, away from the nodal set,

\[
\psi(x)=\sqrt{p(x)}e^{i\theta(x)}.
\]

Let

\[
s(x)=\partial\log p(x)
\]

be the classical score and

\[
a(x)=\partial\theta(x)-\mathbb E_p[\partial\theta]
\]

be the centered phase score.

Projecting the state derivative orthogonally to the ray gives

\[
D^\perp\psi
=\psi\left(\frac12s+ia\right).
\tag{4.1}
\]

Therefore

\[
\boxed{
 g_{FS}
 =\frac14\mathbb E_p[s^2]
 +\mathbb E_p[a^2].
}
\tag{4.2}
\]

Equivalently,

\[
\boxed{
I_Q=I_M+4\operatorname{Var}_p(a).
}
\tag{4.3}
\]

**Derived here / companion-note identity.** This is the position-representation form already used in [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md).

Hence equality in the quantum Fisher bound for this measurement occurs precisely when the projective phase-score variance vanishes in the direction considered.

This yields a useful information-theoretic reading of the Born map:

\[
\boxed{
\text{probability retains amplitude distinguishability;}
\quad
\text{phase variance measures the information inaccessible to that measurement.}
}
\tag{4.4}
\]

---

# Part II. Why this does not yet derive the Born rule

## 5. Gleason's theorem: what it proves

Let \(\mathcal H\) be a separable Hilbert space of dimension at least three. Gleason studies countably additive probability measures on its closed subspaces / orthogonal projectors and proves that such measures are represented by positive trace-class operators:

\[
\boxed{
\mu(P)=\operatorname{tr}(\rho P).
}
\tag{5.1}
\]

[Gle57]. For a pure state \(\rho=|\psi\rangle\langle\psi|\) and a rank-one projector \(P_\phi=|\phi\rangle\langle\phi|\),

\[
\boxed{
\mu(P_\phi)
=|\langle\phi|\psi\rangle|^2.
}
\tag{5.2}
\]

Thus the quadratic probability rule is strongly constrained once the Hilbert event structure and the relevant noncontextual additivity assumptions are accepted.

Busch obtains an effect/POVM version in which states are again represented by density operators [Bus03].

### The boundary

Gleason does **not** prove

\[
\text{thermodynamics}\Longrightarrow\mathbb C\text{-Hilbert space}.
\]

Nor does it show that Fisher geometry alone selects complex amplitudes, unitary dynamics, tensor products, or fermionic exterior powers.

Therefore FCIG should state:

\[
\boxed{
\text{Gleason constrains the Born map after quantum event geometry is given;}
\\
\text{it does not derive quantum event geometry from statistical mechanics.}
}
\tag{5.3}
\]

---

## 6. A precise Born reconstruction problem

Suppose an independent FCIG construction produces a projective state space \(\mathbb P(\mathcal H)\) together with an event structure represented by orthogonal projectors. Then a realistic reconstruction target is:

> **Born Reconstruction Problem.** Identify physically/statistically natural assumptions on event probabilities—normalization, orthogonal additivity, noncontextuality or an effect analogue—under which the only admissible probability assignment is
>
> \[
> P\mapsto\operatorname{tr}(\rho P).
> \]

At this stage the mathematical backbone would be Gleason/Busch rather than a new FCIG theorem.

The genuinely FCIG part would have to explain why the assumptions themselves emerge from the thermodynamic/cohomological construction.

---

# Part III. Slater determinants as the fermionic information bridge

## 7. Fermionic composition and the Grassmannian

Let \(E\subset\mathcal H\) be an \(N\)-dimensional subspace. Any orthonormal basis \(u_1,\ldots,u_N\) determines

\[
\Psi_E=u_1\wedge\cdots\wedge u_N
\in\wedge^N\mathcal H.
\tag{7.1}
\]

A unitary change of basis in \(E\) multiplies \(\Psi_E\) by \(\det U\), a phase. Hence the projective state depends only on \(E\):

\[
\boxed{
\operatorname{Gr}(N,\mathcal H)
\xrightarrow{\rm Pl\ddot ucker}
\mathbb P(\wedge^N\mathcal H).
}
\tag{7.2}
\]

Single Slater determinants form precisely such a Grassmannian submanifold of projective many-body Hilbert space [AS20].

This makes antisymmetric many-body composition geometrically visible:

\[
\boxed{
\text{occupied one-particle subspace}
\longleftrightarrow
\text{Grassmannian point}
\longleftrightarrow
\text{Slater ray}.
}
\tag{7.3}
\]

---

## 8. Theorem 8.1 — Born image of a Slater state is a projection DPP

Assume \(\mathcal H\subset L^2(X,\nu)\), and let \(u_1,\dots,u_N\) be orthonormal. Define

\[
\Psi_E(x_1,\dots,x_N)
=\frac1{\sqrt{N!}}
\det[u_i(x_j)].
\tag{8.1}
\]

Let

\[
K_E(x,y)=\sum_{i=1}^Nu_i(x)\overline{u_i(y)}.
\tag{8.2}
\]

Then

\[
\boxed{
|\Psi_E(x_1,\dots,x_N)|^2
=\frac1{N!}\det[K_E(x_i,x_j)]_{i,j=1}^N.
}
\tag{8.3}
\]

### Proof

Let \(U\) be the \(N\times N\) matrix

\[
U_{ij}=u_i(x_j).
\]

Then the kernel matrix is

\[
[K_E(x_i,x_j)]=U^*U
\]

up to the harmless transpose convention determined by row/column indexing. Hence

\[
\det[K_E(x_i,x_j)]
=\det(U^*U)
=|\det U|^2.
\]

Substitution into (8.1) gives (8.3). \(\square\)

**Derived here from elementary linear algebra / established DPP structure.** Projection DPPs and the complex-geometric Bergman instances are standard; see [HKPV09; Ber08].

Thus

\[
\boxed{
\text{Slater antisymmetry}
+\text{Born squared norm}
\Longrightarrow
\text{determinantal probability law}.
}
\tag{8.4}
\]

This implication is exact.

---

## 9. Why the determinant is simultaneously quantum and statistical

Equation (8.3) shows that the same determinant appears in two roles:

\[
\det[u_i(x_j)]
\quad\text{is a fermionic amplitude},
\]

while

\[
\det[K_E(x_i,x_j)]
\quad\text{is a joint probability density up to normalization}.
\]

The bridge is not “determinants are thermodynamic, therefore quantum mechanics follows.” It is the exact algebraic identity

\[
\boxed{
|\det U|^2=\det(U^*U).
}
\tag{9.1}
\]

For Bergman quantization, \(E=H^0(X,L^k)\), this projection DPP is precisely the type studied by Berman; its correlation kernel is the Bergman kernel and it has a free-fermion interpretation [Ber08].

**FCIG interpretation:** the Slater determinant is a common mother object for

\[
\boxed{
\text{fermionic projective geometry}
\quad\text{and}\quad
\text{determinantal probability geometry}.
}
\tag{9.2}
\]

---

# Part IV. Information geometry of the Slater–Born diagram

## 10. Quantum side

Let \(E_b\) be a smooth family of occupied \(N\)-planes in a Hermitian Hilbert bundle with specified unitary connection. If \(\mathbb B_\xi\) is the second fundamental form, then the Plücker/Fubini–Study metric is

\[
\boxed{
 g_{\rm Gr}^{\nabla}(\xi,\bar\eta)
 =\operatorname{Tr}_E(\mathbb B_\eta^*\mathbb B_\xi).
}
\tag{10.1}
\]

This is the Grassmannian quantum-information tensor developed in the companion note.

---

## 11. Classical side

The Born image of the Slater ray is the DPP (8.3). The corresponding position Fisher metric satisfies, for real directions and the same covariant realization,

\[
\boxed{
\frac14 I_{\rm DPP}
=
 g_{\rm Gr}^{\nabla}
-
\operatorname{Cov}(a,a).
}
\tag{11.1}
\]

The defect is positive semidefinite.

Thus the diagram carries a metric inequality:

\[
\boxed{
\frac14I_{\rm DPP}
\preceq
 g_{\rm Gr}^{\nabla}.
}
\tag{11.2}
\]

Equality means that the chosen position measurement loses no projective phase information in those parameter directions.

This is the precise information-geometric version of the slogan

\[
\boxed{
\text{Born probability is a classical statistical image of a projective quantum state.}
}
\tag{11.3}
\]

“Image” is preferable to “equivalent”: the map may strictly contract the metric.

---

## 12. Hyperbolic FCIG specialization

For

\[
E_q=H^0(X,K_X^q)
\]

in a compact hyperbolic Teichmüller family, the preceding FCIG calculation gives, in the chosen Chern/minimal-solution connection model,

\[
\boxed{
 g_{{\rm Gr},q}^{\rm C}
 =\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\tag{12.1}
\]

Therefore

\[
\boxed{
\frac{4\pi}{q-1}g_{{\rm Gr},q}^{\rm C}
\to G_{\rm WP}.
}
\tag{12.2}
\]

On the Born/DPP side,

\[
\boxed{
\frac14 I_{{\rm DPP},q}^{\rm C}
=
\frac{q-1}{4\pi}G_{\rm WP}
-
\operatorname{Cov}(a_q,a_q)
+O(1).
}
\tag{12.3}
\]

Hence the remaining classical problem is exactly the phase-defect estimate

\[
\boxed{\operatorname{Cov}(a_q,a_q)=o(q)?}
\tag{12.4}
\]

If yes,

\[
\boxed{
\frac{\pi}{q-1}I_{{\rm DPP},q}^{\rm C}
\to G_{\rm WP}.
}
\tag{12.5}
\]

This is a concrete falsifiable statement, not an analogy.

---

# Part V. Thermodynamic language: what is legitimate

## 13. Determinant normalization and free-energy structure

For nonorthonormal one-particle states with Gram matrix \(G\), the Slater norm is controlled by

\[
\boxed{\|u_1\wedge\cdots\wedge u_N\|^2=\det G.}
\tag{13.1}
\]

In the Bergman DPP setting the many-body normalization/partition function is similarly

\[
\boxed{Z=\det G.}
\tag{13.2}
\]

Thus

\[
\boxed{\mathcal F:=-\log Z=-\log\det G}
\tag{13.3}
\]

has the formal and, in statistical-mechanical models, literal role of a free energy. Berman's fermionic DPP constructions and the FCIG Quillen notes make this determinant structure precise in geometric quantization contexts [Ber08].

This justifies saying:

\[
\boxed{
\text{Slater/Bergman quantization possesses a genuine determinant thermodynamic structure.}
}
\tag{13.4}
\]

It does **not** justify saying:

\[
\boxed{
\text{thermodynamics alone has derived complex amplitudes, Born probabilities, or fermionic statistics.}
}
\tag{13.5}
\]

Those are separate reconstruction obligations.

---

## 14. Three reconstruction gates

### Gate R1 — projective complex state space

Find axioms on the FCIG state/entropy structure that force states to be rays in a complex Hilbert space, rather than merely points of an arbitrary statistical manifold.

**Status:** open.

### Gate R2 — Born quadraticity

Once projective Hilbert space and an orthogonal event structure are available, derive the admissible probability law from independent FCIG axioms. Gleason/Busch show what happens under standard noncontextual-additivity/effect assumptions [Gle57; Bus03].

The FCIG problem is to justify those assumptions from its own thermodynamic/cohomological structure.

**Status:** open, with strong existing reconstruction theorems available after the Hilbert/event input is granted.

### Gate R3 — exterior-power fermionic composition

Explain why the composition law for identical fermionic degrees of freedom should be

\[
\wedge^N\mathcal H
\]

rather than simply postulating antisymmetry.

The determinant/Quillen/graded-state structure may provide useful clues, but no derivation is claimed here.

**Status:** open.

Only if R1–R3 are independently closed should FCIG use language such as “quantum mechanics emerges from thermodynamic/information geometry.”

---

# Part VI. A theorem-level diagram and a conjectural extension

## 15. Established/derived diagram

The controlled finite-dimensional/many-body chain is

\[
\boxed{
\begin{array}{ccccc}
\operatorname{Gr}(N,\mathcal H)
&\xrightarrow{\rm Pl\ddot ucker}&
\mathbb P(\wedge^N\mathcal H)
&\xrightarrow{\rm Born}&
\operatorname{DPP}(K_E)
\\[2mm]
\downarrow && \downarrow && \downarrow
\\[-1mm]
 g_{\rm Gr}
&& g_{FS},\ I_Q=4g_{FS}
&& I_{\rm DPP}\le I_Q.
\end{array}}
\tag{15.1}
\]

The top row is exact. The metric comparison on the bottom row is exact once the same connection/measurement realization is fixed.

For the hyperbolic \(H^0(K^q)\) model,

\[
\boxed{
\frac{4\pi}{q-1}g_{{\rm Gr},q}^{\rm C}
\to G_{\rm WP}.
}
\tag{15.2}
\]

This is the current strongest FCIG information-geometric statement involving Slater states.

---

## 16. Born–Slater Information Closure Conjecture

A conservative next conjecture is not that Born's rule follows from thermodynamics. It is:

> **Conjecture.** For the hyperbolic Bergman/Slater family with the geometrically distinguished Chern/KE transport, the phase-information defect satisfies
>
> \[
> \operatorname{Cov}(a_q,a_q)=o(q)
> \]
>
> on compact subsets of Teichmüller space.

If true, the position Born measurement becomes asymptotically information-complete at the leading Kodaira–Spencer scale:

\[
\boxed{
\frac{\pi}{q-1}I_{{\rm DPP},q}^{\rm C}
\to G_{\rm WP}.
}
\tag{16.1}
\]

If false with an \(O(q)\) defect, the limit identifies a new phase-loss tensor rather than destroying the program.

---

# 17. What can safely be said now

The following sentences are justified:

> **Born map:** A quantum measurement sends projective Hilbert geometry to a classical statistical model, and the classical Fisher information obtained from a fixed measurement is bounded by the quantum/Fubini–Study information.

> **Slater map:** A Slater determinant is simultaneously a Plücker representative of an occupied Grassmannian plane and, after the Born map, the square root of a determinantal probability density.

> **FCIG hyperbolic model:** The Chern-covariant Grassmannian information metric of the high-power holomorphic fermionic state space converges, after normalization, to Weil–Petersson geometry.

The following sentence is **not yet justified**:

> “Thermodynamics derives quantum mechanics and the Born rule.”

The correct research program is instead

\[
\boxed{
\text{thermodynamic/index structure}
\stackrel{?}{\Longrightarrow}
\begin{cases}
\text{projective complex state space},\\
\text{Born probability law},\\
\text{exterior-power fermionic composition}.
\end{cases}
}
\tag{17.1}
\]

with each arrow treated as an independent theorem obligation.

---

# 18. Reference map

- **Original probabilistic interpretation:** [Bor26].
- **Projective/Kähler formulation of pure quantum states:** [AS98].
- **Statistical distance and Hilbert angle:** [Woo81].
- **Quantum Fisher as optimal measurement distinguishability:** [BC94].
- **Classical/quantum Fisher in geometric quantum mechanics:** [FKMMSV10].
- **Born-type probability reconstruction on Hilbert projectors:** [Gle57].
- **Effect/POVM Gleason-type theorem:** [Bus03].
- **Single Slater determinants as a Grassmannian in projective Hilbert space:** [AS20].
- **Projection DPP background:** [HKPV09].
- **Bergman DPP / free-fermion complex geometry:** [Ber08].

The FCIG synthesis connecting these ingredients is a research organization, not a claim that the cited authors stated the complete diagram (15.1).