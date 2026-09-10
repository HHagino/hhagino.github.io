# FCIG: Hermitian Born–Fisher Completion

**Status:** exact fixed/connection-parallel identity + hyperbolic model corollary + no-go correction  
**Date:** 2026-09-10  
**Scope:** projectively holomorphic pure-state families, Born position measurements, classical Fisher information, phase information, complex structure, and the Weil–Petersson limit.  
**Depends on:** [`born-slater-information.md`](born-slater-information.md), [`chern-fisher-closure.md`](chern-fisher-closure.md), [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md).

> **Claim policy.** **Established** means a cited theorem or formula. **Derived here** means a deduction written below from the stated hypotheses; it is not a novelty claim. **No-go** records an obstruction. **Open** marks the remaining moving-fiber transport problem.
>
> Dedicated bibliography: [`hermitian-born-fisher.bib`](hermitian-born-fisher.bib). Citation audit: [`hermitian-born-fisher-citation-audit.md`](hermitian-born-fisher-citation-audit.md).

---

## 0. Result in one page

The previous FCIG notes decomposed the Fubini–Study metric of a normalized amplitude

\[
\widehat\Psi=\sqrt p\,e^{i\theta}
\]

as

\[
\boxed{
 g_{FS}(X,Y)
 =\frac14 I_{\rm pos}(X,Y)
 +\operatorname{Cov}(a_X,a_Y),
}
\tag{0.1}
\]

where

\[
s_X:=D_X\log p,
\qquad
a_X:=D_X\theta-\mathbb E_p[D_X\theta]
\]

are the classical probability score and centered phase score. This amplitude/phase decomposition is established in the geometric quantum-information literature; in essentially this form see Facchi et al. [FKMMSV10]. Khesin–Misiołek–Modin place the same amplitude/density geometry in the Kähler geometry of the Madelung transform [KMM19].

The new observation here is that if the state family is **projectively holomorphic** and the measurement realization is fixed, or parallel for the chosen Hermitian connection, then the complex structure \(J\) rotates amplitude score into phase score.

Let

\[
\sigma_X
:=
\frac{D_X^\perp\widehat\Psi}{\widehat\Psi}
=\frac12s_X+i a_X.
\tag{0.2}
\]

Projective holomorphicity means

\[
\boxed{
D_{JX}^\perp\widehat\Psi
=iD_X^\perp\widehat\Psi.
}
\tag{0.3}
\]

Hence

\[
\boxed{
\sigma_{JX}=i\sigma_X,
\qquad
s_{JX}=-2a_X,
\qquad
a_{JX}=\frac12s_X.
}
\tag{0.4}
\]

Therefore the two classical Fisher measurements along the \(J\)-paired tangent directions reconstruct the full projective metric:

\[
\boxed{
I_{\rm pos}(X,Y)
+I_{\rm pos}(JX,JY)
=4g_{FS}(X,Y).
}
\tag{0.5}
\]

Equivalently define the **Hermitianized Born–Fisher metric**

\[
\boxed{
I_{\rm HBF}(X,Y)
:=\frac14\left[
I_{\rm pos}(X,Y)+I_{\rm pos}(JX,JY)
\right].
}
\tag{0.6}
\]

Then, under the hypotheses above,

\[
\boxed{I_{\rm HBF}=g_{FS}}
\tag{0.7}
\]

**exactly**.

For the hyperbolic family of holomorphic \(q\)-differentials, the companion FCIG calculation gives in the Chern/minimal-solution model

\[
 g_{{\rm Gr},q}^{\rm C}
 =\frac{q-1}{4\pi}G_{\rm WP}+O(1).
\tag{0.8}
\]

Thus, provided the position measurement frame is parallel for the same covariant realization,

\[
\boxed{
I_{{\rm pos},q}^{\rm C}(X,Y)
+I_{{\rm pos},q}^{\rm C}(JX,JY)
=
\frac{q-1}{\pi}G_{\rm WP}(X,Y)+O(1),
}
\tag{0.9}
\]

and therefore

\[
\boxed{
\frac{\pi}{q-1}
\left[
I_{{\rm pos},q}^{\rm C}(X,Y)
+I_{{\rm pos},q}^{\rm C}(JX,JY)
\right]
\longrightarrow
G_{\rm WP}(X,Y).
}
\tag{0.10}
\]

This replaces the previous over-strong target that the phase variance should satisfy \(\operatorname{Var}(a_q)=o(q)\) in every real direction. In fact projective holomorphicity implies

\[
\boxed{
\operatorname{Var}(a_X)
+\operatorname{Var}(a_{JX})
=g_{FS}(X,X).
}
\tag{0.11}
\]

So when \(g_{FS,q}=O(q)\), both phase variances cannot simultaneously be \(o(q)\). The correct classical closure is therefore naturally **Hermitian / \(J\)-paired**, not single-real-direction saturation.

---

# Part I. Established amplitude–phase geometry

## 1. Pure state, one measurement

Let \((B,J)\) be a complex parameter manifold and let a normalized pure-state family be represented in a fixed measurement realization by

\[
\widehat\Psi_b(y)
=\sqrt{p_b(y)}e^{i\theta_b(y)}.
\]

For a real tangent vector \(X\in T_bB\), define

\[
s_X=D_X\log p_b,
\tag{1.1}
\]

and

\[
a_X=D_X\theta_b-\mathbb E_p[D_X\theta_b].
\tag{1.2}
\]

After removing the projective ray component,

\[
\boxed{
\frac{D_X^\perp\widehat\Psi}{\widehat\Psi}
=\frac12s_X+i a_X.
}
\tag{1.3}
\]

Taking the real part of the projective Hermitian tensor gives

\[
\boxed{
 g_{FS}(X,Y)
 =\frac14\mathbb E_p[s_Xs_Y]
 +\mathbb E_p[a_Xa_Y].
}
\tag{1.4}
\]

This is the Fisher-plus-phase covariance decomposition written by Facchi et al. [FKMMSV10]. In their notation the classical Fisher term appears with coefficient \(1/4\), while the remaining real term is the covariance of the phase differential. They also identify the imaginary part with geometric-phase data.

Thus a fixed Born measurement generally satisfies

\[
\frac14I_{\rm pos}\preceq g_{FS}.
\tag{1.5}
\]

Braunstein–Caves [BC94] give the corresponding operational statement: the classical Fisher information of a chosen measurement is bounded by the quantum Fisher information, which for pure states is \(4g_{FS}\) in the convention used here.

---

## 2. Madelung/Kähler interpretation

The map

\[
\widehat\Psi=\sqrt p\,e^{i\theta}
\longleftrightarrow
(p,\theta)
\]

should not be treated as an FCIG invention. Khesin–Misiołek–Modin prove that the Madelung transform is a Kähler map between an appropriate wave-function/projective geometry and a cotangent-density geometry carrying the Fisher–Rao metric [KMM19].

**Established prior-art boundary.** The general statement

\[
\text{amplitude + phase geometry}
\leftrightarrow
\text{Fisher–Rao / Fubini–Study Kähler geometry}
\]

is already part of the literature.

The FCIG-specific question is narrower: how this structure interacts with

\[
H^0(X,K^q),
\quad
\text{Slater/Plücker geometry},
\quad
\text{Bergman DPPs},
\quad
\text{Kodaira--Spencer deformation},
\quad
G_{\rm WP}.
\]

---

# Part II. Complex structure exchanges amplitude and phase

## 3. Projective holomorphicity hypothesis

Let \((\mathscr H,h,\nabla)\to B\) be a Hermitian Hilbert bundle and let \([\widehat\Psi_b]\) be a projective state family. Assume that, in the chosen covariant realization,

\[
\boxed{
D_{JX}^\perp\widehat\Psi
=iD_X^\perp\widehat\Psi
}
\tag{3.1}
\]

for every real tangent vector \(X\). This is the infinitesimal Cauchy–Riemann condition for the projective map.

Define

\[
\sigma_X
:=
\frac{D_X^\perp\widehat\Psi}{\widehat\Psi}.
\tag{3.2}
\]

From (1.3),

\[
\sigma_X=\frac12s_X+i a_X.
\tag{3.3}
\]

### Proposition 3.1 — Cauchy–Riemann score identities

Under (3.1),

\[
\boxed{
 s_{JX}=-2a_X,
 \qquad
 a_{JX}=\frac12s_X.
}
\tag{3.4}
\]

### Proof

Equation (3.1) gives

\[
\sigma_{JX}=i\sigma_X.
\]

Substitute (3.3):

\[
\frac12s_{JX}+ia_{JX}
=i\left(\frac12s_X+ia_X\right)
=-a_X+i\frac12s_X.
\]

Equating real and imaginary parts gives (3.4). \(\square\)

**Derived here.** This is elementary once projective holomorphicity and the amplitude/phase decomposition are imposed. No literature-novelty claim is made.

**Interpretation.** The complex structure on parameter space exchanges the two pieces that a single Born probability representation separates:

\[
\boxed{
\text{amplitude score}
\xleftrightarrow{\ J\ }
\text{phase score}.
}
\tag{3.5}
\]

---

# Part III. Exact Hermitian completion of classical Fisher

## 4. Theorem 4.1 — J-paired Fisher completion

For real tangent vectors \(X,Y\),

\[
\boxed{
 I_{\rm pos}(X,Y)
 +I_{\rm pos}(JX,JY)
 =4g_{FS}(X,Y).
}
\tag{4.1}
\]

### Proof

By Proposition 3.1,

\[
I_{\rm pos}(JX,JY)
=\mathbb E_p[s_{JX}s_{JY}]
=4\mathbb E_p[a_Xa_Y].
\]

Using (1.4),

\[
\begin{aligned}
I_{\rm pos}(X,Y)+I_{\rm pos}(JX,JY)
&=I_{\rm pos}(X,Y)+4\operatorname{Cov}(a_X,a_Y)
\\
&=4g_{FS}(X,Y).
\end{aligned}
\]

\(\square\)

Define

\[
\boxed{
I_{\rm HBF}(X,Y)
:=\frac14
\left[
I_{\rm pos}(X,Y)+I_{\rm pos}(JX,JY)
\right].
}
\tag{4.2}
\]

Then

\[
\boxed{I_{\rm HBF}=g_{FS}.}
\tag{4.3}
\]

We call (4.2) **Hermitian Born–Fisher completion** in this project. The name is not standard terminology.

### What is exact here?

Theorem 4.1 is exact under three explicit conditions:

1. the pure-state family is projectively holomorphic;
2. the probability representation uses a fixed measurement frame, or a frame parallel under the same chosen Hermitian connection;
3. the score is differentiated with respect to that representation.

Dropping condition 2 returns the moving-sample-space transport ambiguity established in [`kodaira-spencer-information.md`](kodaira-spencer-information.md).

---

## 5. Phase/Fisher duality

Proposition 3.1 also gives

\[
\boxed{
I_{\rm pos}(JX,JY)
=4\operatorname{Cov}(a_X,a_Y),
}
\tag{5.1}
\]

and

\[
\boxed{
4\operatorname{Cov}(a_{JX},a_{JY})
=I_{\rm pos}(X,Y).
}
\tag{5.2}
\]

So the phase information invisible to the position probabilities in one real direction is the probability Fisher information of the complex-rotated direction.

This changes the interpretation of the “phase defect.” It is not simply missing information with no geometric address. Under projective holomorphicity it is the **quadrature partner** of the classical score.

---

# Part IV. No-go for uniform single-direction saturation

## 6. Proposition 6.1 — phase-variance sum rule

On a diagonal direction,

\[
\boxed{
\operatorname{Var}(a_X)
+
\operatorname{Var}(a_{JX})
=g_{FS}(X,X).
}
\tag{6.1}
\]

### Proof

By Proposition 3.1,

\[
\operatorname{Var}(a_{JX})
=\frac14I_{\rm pos}(X,X).
\]

Insert this into (1.4). \(\square\)

Therefore

\[
\boxed{
\max\{\operatorname{Var}(a_X),\operatorname{Var}(a_{JX})\}
\ge\frac12g_{FS}(X,X).
}
\tag{6.2}
\]

### No-go 6.2

Suppose a sequence of projectively holomorphic state families has

\[
g_{FS,q}(X,X)\sim c_X q,
\qquad c_X>0.
\]

Then it is impossible that both

\[
\operatorname{Var}(a_{q,X})=o(q)
\]

and

\[
\operatorname{Var}(a_{q,JX})=o(q)
\]

hold simultaneously.

**Consequence for the previous FCIG target.** The sufficient condition

\[
\operatorname{Var}(a_q)=o(q)
\]

may still hold along a specially chosen real direction or Lagrangian slice, but it cannot be the correct uniform closure condition on an entire complex tangent plane when the projective family is holomorphic.

Thus the natural target is not

\[
I_{\rm pos}\sim 4g_{FS}
\]

in each individual real direction, but rather the exact Hermitian completion (4.1).

---

# Part V. Hyperbolic Slater/Bergman family

## 7. Input from the 50–50 Kodaira–Spencer calculation

For the compact hyperbolic curve family and

\[
E_q=\pi_*K_{\mathcal X/B}^q,
\]

the companion note [`grassmannian-quantum-information.md`](grassmannian-quantum-information.md) derives, inside the stated Chern/minimal-solution connection model,

\[
\boxed{
 g_{{\rm Gr},q}^{\rm C}
 =\frac{q-1}{4\pi}G_{\rm WP}+O(1).
}
\tag{7.1}
\]

This is the normal-motion half of the 50–50 Kodaira–Spencer decomposition.

The normalized Slater ray is the Plücker line of the moving holomorphic subspace. Its projective metric is therefore \(g_{{\rm Gr},q}^{\rm C}\).

---

## 8. Corollary 8.1 — J-paired Bergman-DPP Fisher/WP limit

Assume in addition that the Bergman position measurement is represented in a frame parallel for the same connection, so that Theorem 4.1 applies to the moving Slater ray. Then

\[
\boxed{
\begin{aligned}
&I_{{\rm pos},q}^{\rm C}(X,Y)
+I_{{\rm pos},q}^{\rm C}(JX,JY)
\\
&\qquad=4g_{{\rm Gr},q}^{\rm C}(X,Y)
=\frac{q-1}{\pi}G_{\rm WP}(X,Y)+O(1).
\end{aligned}
}
\tag{8.1}
\]

Hence

\[
\boxed{
\frac{\pi}{q-1}
\left[
I_{{\rm pos},q}^{\rm C}(X,Y)
+I_{{\rm pos},q}^{\rm C}(JX,JY)
\right]
\longrightarrow
G_{\rm WP}(X,Y).
}
\tag{8.2}
\]

**Status:** **conditional corollary.** The Hilbert/Slater side and the 50–50 asymptotic are already derived in the companion notes. The remaining condition is that the concrete moving-fiber position measurement be parallel for the same Chern/minimal-solution realization. That global transport compatibility has not yet been proved.

This is nevertheless stronger than the previous phase-defect formulation because it identifies the correct invariant completion before that last transport theorem is available.

---

## 9. Hyperbolic no-go coefficient

From (7.1) and (6.2), for every nonzero tangent direction,

\[
\boxed{
\max\{\operatorname{Var}(a_{q,X}),
\operatorname{Var}(a_{q,JX})\}
\ge
\frac{q-1}{8\pi}G_{\rm WP}(X,X)+O(1).
}
\tag{9.1}
\]

Thus a uniform \(o(q)\) phase defect is impossible in a projectively holomorphic realization with the WP leading metric.

The earlier “maybe the phase defect is negligible everywhere” hope is therefore replaced by a more structured statement:

\[
\boxed{
\text{the missing phase information in }X
=\text{the Born/Fisher information of }JX.
}
\tag{9.2}
\]

---

# Part VI. Relation to Born–Slater information geometry

## 10. Corrected diagram

The previous Born–Slater diagram becomes

\[
\boxed{
\begin{array}{ccccc}
\operatorname{Gr}(N,\mathcal H)
&\longrightarrow&
\mathbb P(\wedge^N\mathcal H)
&\xrightarrow{\rm Born}&
\mathcal P(X^N)
\\
&&\downarrow g_{FS}&&\downarrow I_{\rm pos}
\\
&&\multicolumn{3}{c}{
 g_{FS}
 =\frac14\bigl(I_{\rm pos}+J^*I_{\rm pos}\bigr)
}
\end{array}}
\tag{10.1}
\]

where

\[
(J^*I_{\rm pos})(X,Y):=I_{\rm pos}(JX,JY).
\]

So one fixed classical probability metric need not equal the projective metric, but its \(J\)-Hermitian completion does under the stated holomorphic/parallel hypotheses.

**FCIG interpretation:**

\[
\boxed{
\textbf{Born probability is one real quadrature of projective information;}
\\
\textbf{the complex structure supplies its phase-conjugate quadrature.}
}
\tag{10.2}
\]

This is an interpretation of the exact score identities, not a derivation of the Born rule.

---

# Part VII. Relation to reconstruction of quantum mechanics

## 11. What this does for the Born problem

The result does **not** prove

\[
\text{thermodynamics}\Longrightarrow p=|\psi|^2.
\]

Instead it supplies a new consistency criterion for any proposed reconstruction.

If a thermodynamic/index principle is eventually claimed to derive a complex projective state space and a probability map, then that map should reproduce the compatible Kähler information tensor. In the present setting, the Born map passes this test through

\[
\boxed{
 g_{FS}
 =\frac14(I+J^*I).
}
\tag{11.1}
\]

Thus the FCIG reconstruction gates can be sharpened:

- **R1:** derive the complex projective state space and its Kähler structure;
- **R2:** derive a probability rule whose Hermitianized classical information agrees with the projective metric, and then determine whether this singles out the Born quadratic map under suitable event/composition axioms;
- **R3:** derive the exterior-power composition law for identical fermions, so that the Born image becomes the determinantal process already analyzed here.

Gleason-type theorems remain the established benchmark for R2 once Hilbert-space event geometry is already assumed; the present theorem supplies an additional differential-geometric compatibility condition, not a replacement for Gleason.

---

# Part VIII. Remaining theorem

## 12. The one genuinely moving-fiber problem left

The unresolved step is now geometric rather than probabilistic:

\[
\boxed{
\text{Does the Kähler--Einstein/Chern horizontal transport make the Bergman position POVM parallel}
\\
\text{with the minimal-solution connection used in the direct-image calculation?}
}
\tag{12.1}
\]

If yes, Corollary 8.1 becomes an intrinsic theorem for the actual moving-fiber Bergman DPP.

If no, the failure defines an explicit measurement-connection defect. Either outcome is useful.

This is the correct successor to the discarded uniform \(\operatorname{Var}(a_q)=o(q)\) target.

---

# 13. Reference map

- **Fisher + phase covariance decomposition of projective quantum geometry:** [FKMMSV10].
- **Madelung transform as Kähler/Fisher–Rao geometry:** [KMM19].
- **Quantum Fisher as measurement-optimized statistical distinguishability:** [BC94].
- **Attainability of the quantum Fisher bound for fixed measurements:** [TFD17].
- **Bergman statistical embedding context:** [CY23].
- **Hyperbolic direct-image / KS asymptotics:** see the dedicated references and audits in `kodaira-spencer-information.md` and `grassmannian-quantum-information.md`.

No reference is used to claim that the J-paired formula (4.1), its FCIG terminology, or its hyperbolic corollary is literature-new.