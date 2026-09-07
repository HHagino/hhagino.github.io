# FCIG Explicit Model II: Weil Transport, Metaplectic Holonomy, and the Flat Anomaly Line

**Status:** worked completion of the elliptic FCIG model  
**Date:** 2026-09-08

> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are calculations carried out in these FCIG notes; statements marked **FCIG interpretation/conjecture** are not attributed to the cited literature. Full entries are collected at the end of this note and in [`references.bib`](references.bib).

> This note completes the modular part of the elliptic FCIG toy model.  
> The main point is that the local determinant curvature found in Explicit Model I can be cancelled exactly by a Hodge-line counterterm, after which a genuinely global modular multiplier remains.
>
> In this model the slogan
>
> \[
> \boxed{\text{anomaly}=\text{local curvature}+\text{global holonomy}}
> \]
>
> becomes an explicit calculation.

---

## 1. Setup and conventions

**Established background.** Classical theta functions transform under modular \(S\) and \(T\) moves with characteristic permutations and square-root automorphy factors; see [DLMF20; Mum83]. The exact finite matrices used later are derived in this note's convention.

Let

\[
E_\tau=\mathbf C/(\mathbf Z+\tau\mathbf Z),
\qquad
\tau\in\mathbb H,
\]

and let \(L\to E_\tau\) denote the degree-one theta line used in Explicit Model I.

For \(k\ge1\), define

\[
\theta_{k,j}(z,\tau)
=
\sum_{n\in\mathbf Z}
\exp\!\left[
\pi i k\tau\left(n+\frac jk\right)^2
+
2\pi i k\left(n+\frac jk\right)z
\right],
\]

with

\[
j\in\mathbf Z/k\mathbf Z.
\]

Equivalently, setting \(m=kn+j\),

\[
\boxed{
\theta_{k,j}(z,\tau)
=
\sum_{m\equiv j\; (\mathrm{mod}\;k)}
\exp\!\left(
\frac{\pi i\tau}{k}m^2+2\pi i mz
\right).
}
\]

These form a basis of

\[
\mathcal H_{k,\tau}=H^0(E_\tau,L_\tau^k),
\qquad
\dim\mathcal H_{k,\tau}=k.
\]

The classical modular transformations of theta functions follow from Poisson summation; the ordinary Jacobi cases are tabulated, for example, in NIST DLMF §20.7(viii).

References:

- https://dlmf.nist.gov/20.7
- https://math.berkeley.edu/~fengt/245C_2016.pdf
- https://math.berkeley.edu/~swshin/AV-Weil.pdf

---

# 2. The \(S\)-transformation

**Derived here (our convention), with standard background.** The finite Fourier matrix below is obtained directly from Poisson summation for the chosen level-\(k\) theta basis. [Fri85] is cited for the general Weil/metaplectic framework, not for our exact signs and normalizations.

Let

\[
S:\quad
\tau\mapsto-\frac1\tau,
\qquad
z\mapsto\frac z\tau.
\]

Poisson summation gives

\[
\boxed{
\theta_{k,j}\!\left(\frac z\tau,-\frac1\tau\right)
=
\sqrt{-i\tau}\,
\exp\!\left(\frac{\pi i k z^2}{\tau}\right)
\frac1{\sqrt{k}}
\sum_{\ell=0}^{k-1}
\exp\!\left(-\frac{2\pi i j\ell}{k}\right)
\theta_{k,\ell}(z,\tau).
}
\]

Define the normalized finite Fourier matrix

\[
\boxed{
(U_S)_{j\ell}
=
\frac1{\sqrt{k}}
\exp\!\left(-\frac{2\pi i j\ell}{k}\right).
}
\]

Then the transformation has three logically separate factors:

\[
\boxed{
\text{half-form factor}
\times
\text{prequantum Gaussian}
\times
\text{finite Fourier transform}.
}
\]

Explicitly,

\[
\sqrt{-i\tau}
\quad\times\quad
\exp\!\left(\frac{\pi i k z^2}{\tau}\right)
\quad\times\quad
U_S.
\]

The middle factor identifies the transformed theta line with the original one; the nontrivial finite action on the state labels is \(U_S\).

---

# 3. The \(T\)-transformation and the parity obstruction

Consider

\[
T:\quad \tau\mapsto\tau+1.
\]

Directly from the series,

\[
\theta_{k,j}(z,\tau+1)
=
\sum_n
\exp\!\left[
\pi i k\tau\left(n+\frac jk\right)^2
+2\pi i k\left(n+\frac jk\right)z
\right]
\exp\!\left[
\pi i k\left(n+\frac jk\right)^2
\right].
\]

Since

\[
\exp\!\left[
\pi i k\left(n+\frac jk\right)^2
\right]
=
\exp\!\left(\frac{\pi i j^2}{k}\right)(-1)^{kn},
\]

there are two cases.

## 3.1 Even \(k\)

If \(k\) is even,

\[
(-1)^{kn}=1,
\]

so

\[
\boxed{
\theta_{k,j}(z,\tau+1)
=
\exp\!\left(\frac{\pi i j^2}{k}\right)
\theta_{k,j}(z,\tau).
}
\]

Thus

\[
\boxed{
(U_T)_{j\ell}
=
\delta_{j\ell}
\exp\!\left(\frac{\pi i j^2}{k}\right).
}
\]

For even \(k\), the chosen theta structure is therefore preserved by both \(S\) and \(T\).

## 3.2 Odd \(k\)

**Established background.** The modular \(T\)-move permutes theta-characteristic sectors in the classical theory [DLMF20; Mum83]. The exact level-\(k\) swap formulas and \(T^2\) closure below are **derived here**.

For odd \(k\),

\[
(-1)^{kn}=(-1)^n,
\]

so \(T\) does **not** preserve the chosen theta basis.

Introduce a companion sector

\[
\theta_{k,j}^{-}(z,\tau)
=
\sum_{n\in\mathbf Z}
(-1)^n
\exp\!\left[
\pi i k\tau\left(n+\frac jk\right)^2
+
2\pi i k\left(n+\frac jk\right)z
\right],
\]

and write the original sector as \(\theta_{k,j}^{+}\).

Then for odd \(k\),

\[
\boxed{
\theta_{k,j}^{+}(z,\tau+1)
=
\exp\!\left(\frac{\pi i j^2}{k}\right)
\theta_{k,j}^{-}(z,\tau),
}
\]

\[
\boxed{
\theta_{k,j}^{-}(z,\tau+1)
=
\exp\!\left(\frac{\pi i j^2}{k}\right)
\theta_{k,j}^{+}(z,\tau).
}
\]

Thus \(T\) exchanges two theta-characteristic sectors.

However

\[
T^2:\tau\mapsto\tau+2
\]

preserves the original sector:

\[
\boxed{
\theta_{k,j}(z,\tau+2)
=
\exp\!\left(\frac{2\pi i j^2}{k}\right)
\theta_{k,j}(z,\tau).
}
\]

This is the precise parity obstruction hidden by a naive formula for \(U_T\).

### Interpretation

For odd \(k\), a full modular action cannot be assigned to one fixed theta characteristic without extra structure. One must either

- pass to a subgroup preserving the characteristic,
- enlarge the state object to include the relevant theta-characteristic sectors,
- or formulate the theory on an appropriate level/metaplectic cover.

This is already a concrete global obstruction.

---

# 4. Finite Weil matrices at even level

**Derived here (our convention).** The relations among \(U_S\), \(U_T\), charge conjugation, and the Gauss phase are verified from the explicit finite matrices below. [Fri85] supports the general Weil-representation and eighth-root-of-unity phenomenon.

From now through §8 assume \(k\) is even.

Let

\[
C e_j=e_{-j}
\]

be charge conjugation on \(\mathbf C^k\).

The finite Fourier matrix obeys

\[
\boxed{U_S^2=C.}
\]

The normalized quadratic Gauss sum

\[
\gamma_k
=
\frac1{\sqrt{k}}
\sum_{j=0}^{k-1}
\exp\!\left(\frac{\pi i j^2}{k}\right)
\]

satisfies, for even \(k\),

\[
\boxed{\gamma_k=e^{\pi i/4}.}
\]

Consequently,

\[
\boxed{
(U_SU_T)^3
=
e^{\pi i/4}C.
}
\]

Compare this with the modular-group relation

\[
S^2=(ST)^3=-I.
\]

The finite matrices therefore give a **projective** modular action rather than an ordinary representation of \(SL_2(\mathbf Z)\).

The obstruction is the eighth root of unity

\[
\boxed{e^{\pi i/4}.}
\]

This is the simplest explicit form of the metaplectic multiplier in the model.

A standard Weil normalization absorbs the Gauss phase into the lifted \(S\)-operator. Define

\[
\boxed{
\widetilde U_S=e^{-\pi i/4}U_S.
}
\]

Then

\[
\widetilde U_S^2
=
(\widetilde U_SU_T)^3
=
-iC.
\]

The point is not that the obstruction disappears: it is moved into the action of the central element of the metaplectic double cover.

This agrees with the general structure of Weil representations, in which odd-signature theta representations naturally live on \(Mp_2(\mathbf Z)\) rather than directly on \(SL_2(\mathbf Z)\).

---

# 5. The state bundle is projectively flat, not canonically trivial

The theta heat equation reads

\[
4\pi i\,\partial_\tau\vartheta
=
\partial_z^2\vartheta.
\]

For the level-\(k\) states,

\[
\boxed{
\left(
\partial_\tau
-
\frac{1}{4\pi i k}\partial_z^2
\right)
\theta_{k,j}=0.
}
\]

Thus motion in moduli is intertwined with a second-order operator along the fiber.

The modular matrices \(U_S,U_T\) are therefore not arbitrary basis changes: they are monodromy data of the theta/heat transport, up to the scalar metaplectic factor.

This is the finite-dimensional realization of the general statement that theta functions transform by Weil representations.

---

# 6. Recall the determinant curvature from Explicit Model I

With normalized flat area

\[
\omega_\tau
=
\frac{i}{2\operatorname{Im}\tau}
\,dz\wedge d\bar z,
\]

and the natural Hermitian metric on \(L^k\), the theta basis has diagonal \(L^2\) Gram matrix

\[
\boxed{
\langle\theta_{k,j},\theta_{k,\ell}\rangle
=
\delta_{j\ell}
\frac1{\sqrt{2kY}},
\qquad
Y=\operatorname{Im}\tau.
}
\]

Let

\[
\Sigma_k
=
\theta_{k,0}\wedge\cdots\wedge\theta_{k,k-1}
\]

be the determinant frame.

Then

\[
\boxed{
\|\Sigma_k\|^2
=(2kY)^{-k/2}.
}
\]

The Chern curvature of the determinant state line is therefore

\[
F_{\det\mathcal H_k}
=
-\partial\bar\partial
\log\|\Sigma_k\|^2
=
\frac{k}{2}\partial\bar\partial\log Y.
\]

---

# 7. Hodge curvature and exact cancellation

**Derived here.** The corrected line \(\mathscr A_k=\det\mathcal H_k\otimes\lambda_H^{k/2}\) and its vanishing Chern curvature follow from Explicit Model I. The general principle that flat connection data may retain nontrivial holonomy is standard [Bry93; ADH21]; the phrase “flat anomaly line” is **FCIG terminology**.

Let

\[
\lambda_H
=
\pi_*\Omega^1_{\mathcal E/\mathbb H}
\]

be the Hodge line, with frame \(dz\).

Up to an irrelevant positive constant,

\[
\|dz\|^2=Y.
\]

Hence

\[
F_{\lambda_H}
=
-\partial\bar\partial\log Y.
\]

Therefore

\[
\boxed{
F_{\det\mathcal H_k}
=
-\frac{k}{2}F_{\lambda_H}.
}
\]

This is the key exact identity of the elliptic model.

For even \(k\), define the **flat anomaly line candidate**

\[
\boxed{
\mathscr A_k
=
\det\mathcal H_k
\otimes
\lambda_H^{k/2}.
}
\]

Then

\[
\boxed{
F_{\mathscr A_k}=0.
}
\]

The cancellation is also visible directly at the metric level:

\[
\|\Sigma_k\|^2\,\|dz\|^k
=
(2kY)^{-k/2}Y^{k/2}
=
(2k)^{-k/2},
\]

which is constant on \(\mathbb H\).

Thus the local curvature can be cancelled completely without trivializing the global modular transport.

This is the central FCIG result of this note:

\[
\boxed{
\text{zero local curvature does not imply zero global anomaly.}
}
\]

---

# 8. Residual modular holonomy of the flat line

Because \(\mathscr A_k\) is Chern-flat on \(\mathbb H\), all remaining information in a modular quotient is global monodromy/multiplier data.

With the conventions above, the finite state-space part is carried by \(U_S,U_T\).

For the ordered basis \(j=0,\ldots,k-1\),

\[
\boxed{
\det U_T
=
\exp\!\left[
\frac{\pi i}{6}(k-1)(2k-1)
\right],
}
\]

and

\[
\boxed{
\det U_S
=
\exp\!\left[
-\frac{\pi i}{4}(k-1)(3k-2)
\right].
}
\]

Under \(S\), the state transformation contributes the scalar factor

\[
(\sqrt{-i\tau})^k=(-i\tau)^{k/2},
\]

while the Hodge factor \(\lambda_H^{k/2}\) contributes \(\tau^{-k/2}\) in the chosen frame convention.

Thus the \(\tau\)-dependence cancels and the residual \(S\)-multiplier is a constant phase,

\[
\boxed{
\chi_k(S)
=
(-i)^{k/2}\det U_S,
}
\]

while

\[
\boxed{
\chi_k(T)=\det U_T.
}
\]

The exact phase depends on the convention for the metaplectic lift and for the trivialization of the Hodge line; the invariant statement is that **after curvature cancellation the residual transition is unitary and locally constant**.

Hence the determinant line sees the abelianized part of the Weil/metaplectic monodromy:

\[
\boxed{
\rho_k:\operatorname{Mp}_2(\mathbf Z)	o U(k)
\quad\leadsto\quad
\det\rho_k:\operatorname{Mp}_2(\mathbf Z)	o U(1).
}
\]

The full state bundle remembers \(\rho_k\); the determinant anomaly line remembers only \(\det\rho_k\).

---

# 9. Odd level and the Hodge square root

The even-level formula

\[
\mathscr A_k
=
\det\mathcal H_k\otimes\lambda_H^{k/2}
\]

suggests what happens at odd level.

If \(k\) is odd, then \(k/2\) is half-integral, so cancelling the same local curvature requires a square root

\[
\lambda_H^{1/2}.
\]

Such a square root is not naturally an ordinary line over the coarse modular quotient; it belongs naturally to the metaplectic setting.

At the same time, §3 showed independently that \(T\) exchanges theta-characteristic sectors at odd level.

Thus two independent calculations point to the same conclusion:

\[
\boxed{
\text{odd-level modular completion naturally requires extra metaplectic/theta-structure data.}
}
\]

This is stronger than merely observing a mysterious phase in an \(S,T\) relation.

It appears simultaneously in

1. theta-characteristic transport;
2. the half-integral Hodge counterterm;
3. the Weil representation.

---

# 10. Relation to the Bergman nonperturbative sector

Explicit Model I gave the exact Poisson-resummed Bergman density

\[
B_k(x,t;\tau)
=
k
\sum_{p,\ell\in\mathbf Z}
\exp\!\left[
-\frac{\pi k}{2Y}|\ell-p\tau|^2
\right]
\exp\!\left[
2\pi i k(px+\ell t)+\pi i kp\ell
\right].
\]

For fixed \(\tau\), define

\[
\mu(\tau)
=
\min_{(p,\ell)\neq(0,0)}
\frac{|\ell-p\tau|^2}{Y}.
\]

Then

\[
\boxed{
B_k(z;\tau)
=
k\left[1+O_\tau\left(e^{-\pi k\mu(\tau)/2}\right)\right].
}
\]

Since the flat elliptic fiber has

\[
\operatorname{Riem}
=
\operatorname{Ric}
=
\operatorname{Scal}
=0,
\]

all power-law local curvature corrections vanish.

What remains is exponentially small global lattice data.

We therefore obtain two complementary global sectors:

\[
\boxed{
\begin{array}{ll}
\text{fiber-global data}
&\sim e^{-k\mu(\tau)},\\[1mm]
\text{moduli-global data}
&\sim \rho_k(S),\rho_k(T).
\end{array}
}
\]

These are invisible to a purely local curvature expansion.

---

# 11. Elliptic local/global splitting theorem

Within the explicit choices and conventions of the elliptic model, we can summarize the calculations as follows.

### Proposition — Elliptic FCIG splitting

For even level \(k\):

1. The state space \(\mathcal H_{k,\tau}=H^0(E_\tau,L_\tau^k)\) carries modular theta transport generated projectively by
   \[
   U_S{}_{j\ell}=k^{-1/2}e^{-2\pi ij\ell/k},
   \qquad
   U_T{}_{j\ell}=\delta_{j\ell}e^{\pi ij^2/k}.
   \]
2. The generators satisfy
   \[
   U_S^2=C,
   \qquad
   (U_SU_T)^3=e^{\pi i/4}C.
   \]
3. The determinant-state curvature obeys
   \[
   F_{\det\mathcal H_k}
   =
   -\frac{k}{2}F_{\lambda_H}.
   \]
4. Therefore
   \[
   \mathscr A_k
   =
   \det\mathcal H_k\otimes\lambda_H^{k/2}
   \]
   is Chern-flat over \(\mathbb H\).
5. After this local cancellation, modular transport leaves a unitary multiplier system / flat monodromy, governed by the Weil representation and its determinant.
6. The exact fiber Bergman density still carries exponentially small lattice information even though every local curvature coefficient vanishes.

Hence the model exhibits the simultaneous decomposition

\[
\boxed{
\text{FCIG anomaly data}
=
\underbrace{\text{local curvature}}_{\text{Chern / Hodge}}
\oplus
\underbrace{\text{flat modular holonomy}}_{\text{Weil / metaplectic}}
\oplus
\underbrace{\text{nonperturbative fiber lattice data}}_{e^{-k\mu}}.
}
\]

For odd \(k\), the same architecture survives only after including additional theta-characteristic/metaplectic data.

---

# 12. Why this is a genuine improvement over “entropy gradient = gravity”

The original heuristic tried to read geometry from

\[
\nabla S.
\]

The elliptic model now gives a sharper hierarchy.

### Local perturbative sector

The Bergman expansion recovers local curvature invariants in powers of \(1/k\).

### Global fiber sector

Poisson-resummed terms of order

\[
e^{-k\mu}
\]

remember lattice topology/geometry beyond all orders in the local expansion.

### Global moduli sector

Weil/metaplectic matrices encode transport around the modular quotient.

### Determinant anomaly sector

The determinant line abelianizes the modular transport, while its local curvature is tied exactly to the Hodge line.

Thus “information geometry” in this model is not a single scalar entropy. It is a hierarchy:

\[
\boxed{
\text{state count}
+
\text{state density}
+
\text{connection curvature}
+
\text{holonomy}
+
\text{nonperturbative lattice terms}.
}
\]

---

# 13. What is theorem, what is convention, what is FCIG interpretation?

## Standard mathematics used here

- modular transformation laws of theta functions;
- Poisson summation;
- finite Fourier transforms and quadratic Gauss sums;
- Weil representations and the metaplectic group;
- Hodge bundles over elliptic moduli;
- Chern connections of Hermitian holomorphic bundles.

The general Weil-representation structure and its metaplectic nature are standard; see, for example, the notes by Venkatesh/Feng/Ronchetti and Shin cited above.

## Exact calculations specific to this note

Given the chosen basis and metrics:

- the explicit \(S,T\) formulas;
- the parity split between even and odd \(k\);
- the matrix relation
  \[
  (U_SU_T)^3=e^{\pi i/4}C;
  \]
- the determinant formulas for \(U_S,U_T\);
- the curvature cancellation
  \[
  F_{\det\mathcal H_k}+\frac{k}{2}F_{\lambda_H}=0.
  \]

## FCIG interpretation

The interpretation

\[
\boxed{\text{local anomaly}=\text{curvature},\qquad
\text{global anomaly}=\text{residual flat holonomy}}
\]

is the conceptual dictionary proposed by FCIG.

No claim is made that this elliptic modular anomaly is already spacetime gravity.

---

# 14. The completed elliptic FCIG diagram

The two explicit notes can now be summarized in one diagram:

\[
\boxed{
\begin{array}{ccccc}
L^k
&\longrightarrow&
H^0(E_\tau,L^k)
&\longrightarrow&
\det\mathcal H_k
\\[1mm]
&&\downarrow&&\downarrow
\\[-1mm]
&&B_k(z;\tau)
&&F_{\det\mathcal H_k}
\\[1mm]
&&\downarrow&&\downarrow
\\[-1mm]
&&k+O(e^{-k\mu})
&&-\frac{k}{2}F_{\lambda_H}
\\[3mm]
&&\searrow&&\swarrow
\\[-1mm]
&&&
\mathscr A_k
=
\det\mathcal H_k\otimes\lambda_H^{k/2}
&
\\[2mm]
&&&\downarrow&
\\[-1mm]
&&&F_{\mathscr A_k}=0&
\\[2mm]
&&&\downarrow&
\\[-1mm]
&&&\text{Weil/metaplectic holonomy}.&
\end{array}
}
\]

The model therefore realizes, explicitly,

\[
\boxed{
\text{local potential}
\to
\text{curvature}
\to
\text{counterterm cancellation}
\to
\text{flat but globally nontrivial modular data}.
}
\]

This is the cleanest mathematical realization so far of the original FCIG local/global-anomaly idea.

---

# 15. What remains open

The **elliptic modular model is now closed at the toy-model level**, but the full gravitational program is not.

The next genuinely new steps are:

1. Replace elliptic curves by higher-genus curves or higher-dimensional polarized abelian varieties, where the Weil representation is higher rank and moduli curvature is richer.
2. Determine which parts of the flat anomaly line survive after Quillen refinement and analytic torsion are included.
3. Study degeneration toward the cusp jointly with \(k\to\infty\), using the natural double-scaling parameter \(k/\operatorname{Im}\tau\).
4. Formulate a Lorentzian analogue of the local/global split.
5. Test whether a horizon entropy functional can be built from the local Bergman/index sector plus flat global anomaly data.

The point is that the next step is no longer “make the analogy more beautiful.”

It is to decide whether the exact elliptic mechanism has a functorial higher-dimensional continuation.

---

## References

1. NIST Digital Library of Mathematical Functions, §20.7(viii), modular transformations of theta functions: https://dlmf.nist.gov/20.7
2. A. Venkatesh, notes by T. Feng and N. Ronchetti, lectures including the finite Weil representation: https://math.berkeley.edu/~fengt/245C_2016.pdf
3. S. W. Shin, *Abelian Varieties and Weil Representations*: https://math.berkeley.edu/~swshin/AV-Weil.pdf
4. D. S. Freed, *Determinant Line Bundles Revisited*, arXiv:dg-ga/9505002: https://arxiv.org/abs/dg-ga/9505002
5. D. Quillen, *Determinants of Cauchy–Riemann operators over a Riemann surface*, Functional Analysis and Its Applications 19 (1985).

---

## Research-status statement

This note completes the **explicit elliptic modular toy model** of FCIG, not the proposed theory of gravity.

The modular formulas, Gauss-sum relations, determinant metrics and curvature cancellation are concrete mathematical statements within the stated conventions. The identification of their local/global split with an “information anomaly” is the FCIG interpretation. Any passage from this structure to Lorentzian gravitational dynamics remains conjectural.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[DLMF20]** NIST Digital Library of Mathematical Functions, Chapter 20, especially §20.7(viii), transformations of the lattice parameter.
- **[Mum83]** D. Mumford, *Tata Lectures on Theta I*, Progress in Mathematics 28, Birkhäuser (1983).
- **[Fri85]** S. Friedberg, “Theta Function Transformation Formulas and the Weil Representation,” *Journal of Number Theory* **20**(2) (1985), 121–127.
- **[Bry93]** J.-L. Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser (1993).
- **[ADH21]** A. Amabel, A. Debray & P. J. Haine, *Differential Cohomology: Categories, Characteristic Classes, and Connections* (2021), arXiv:2109.12250.

