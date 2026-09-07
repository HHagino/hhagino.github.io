# Fibered Cohomological Information Geometry — Citation-Audited Synthesis

**Status:** literature-audited research synthesis  
**Date:** 2026-09-08

This document consolidates the mathematical core of the FCIG notes while distinguishing three kinds of statements:

- **[Established]** standard mathematics supported by the cited literature;
- **[Derived here]** calculations carried out explicitly in the FCIG notes;
- **[FCIG interpretation / conjecture]** terminology or physical interpretation proposed here and **not** attributed to the cited references.

The purpose of this separation is to avoid a common failure mode in speculative mathematical physics: attaching a correct reference to a nearby but stronger claim that the reference does not actually prove.

---

## 1. Basic fibered setup

Let

\[
\pi:\mathcal X\to B
\]

be a proper smooth family of compact complex manifolds, and let

\[
\mathscr L\to\mathcal X
\]

be a relatively positive holomorphic line bundle with Hermitian metric \(h\). For \(b\in B\), write

\[
X_b=\pi^{-1}(b),\qquad L_b=\mathscr L|_{X_b}.
\]

The FCIG dictionary is

\[
B=\text{parameter/inference/moduli space},
\qquad
(X_b,L_b)=\text{geometric state space}.
\]

**Status:** the geometry is standard; the information-theoretic interpretation is an **FCIG interpretation**.

---

## 2. Local Hermitian weights and curvature

Choose a local holomorphic frame \(e_i\) of \(\mathscr L\) and write

\[
\|e_i\|_h^2=e^{-\phi_i}.
\]

On an overlap, if

\[
e_i=g_{ij}e_j,
\]

then

\[
\phi_i-\phi_j=-\log|g_{ij}|^2.
\]

The Chern curvature is locally

\[
\Theta_h=\partial\bar\partial\phi_i
\]

up to the conventional factors of \(i\) and \(2\pi\), and the resulting curvature form is globally defined.

**Status:** **[Established]** standard Hermitian holomorphic line-bundle geometry. See Brylinski for line bundles with connection and differential-geometric refinements [Bry93], and standard complex-geometry texts.

The slogan

\[
\boxed{\text{potential is gauge-dependent; curvature is gauge-invariant}}
\]

is therefore a faithful summary of this standard structure.

The phrase “local information potential” is an **FCIG interpretation**.

---

## 3. Differential cohomology: curvature does not exhaust global data

A \(U(1)\)-bundle with connection is encoded by local transition data, connection forms, and curvature:

\[
(g_{ij},A_i,F).
\]

Degree-two differential cohomology is a natural home for this data; in particular it retains both curvature and global holonomy information [Bry93, ADH21].

Thus one may have

\[
F=0
\]

but still

\[
\operatorname{Hol}_\gamma(\nabla)\neq1.
\]

**Status:** **[Established]** differential-cohomological structure [Bry93, ADH21].

Accordingly, the FCIG anomaly dictionary is

\[
\boxed{
\text{local anomaly sector}\sim F,
\qquad
\text{global anomaly sector}\sim\operatorname{Hol}.
}
\]

**Status:** the mathematical distinction between curvature and flat holonomy is established; calling the two sectors “local anomaly” and “global anomaly” is an **FCIG interpretation**, motivated by standard anomaly language.

---

## 4. Quantization spaces and direct images

For \(k\ge1\), define

\[
\mathcal H_{k,b}=H^0(X_b,L_b^k).
\]

In holomorphic/Kähler geometric quantization, spaces of polarized holomorphic sections of a positive prequantum line bundle are standard quantum state spaces [SW76].

Across a family, the robust object is the derived direct image

\[
R\pi_*\mathscr L^k,
\]

rather than automatically an ordinary vector bundle. Under base-change and vanishing hypotheses one recovers

\[
\pi_*\mathscr L^k
\]

with fibers \(H^0(X_b,L_b^k)\).

**Status:** **[Established]** geometric quantization/direct-image geometry [SW76; Stacks-GRR].

The determinant of cohomology is

\[
\lambda_k=\det R\pi_*\mathscr L^k.
\]

Quillen introduced the determinant-line metric in the Cauchy–Riemann setting [Qui85]. Bismut and Freed constructed natural metrics/connections for determinant bundles of elliptic families and computed the associated curvature; their second paper treats the Dirac/eta/holonomy side [BF86a, BF86b].

---

## 5. Capacity entropy

Define

\[
N_k(b)=\dim H^0(X_b,L_b^k),
\]

and

\[
S_k^{\mathrm{cap}}(b)=\log N_k(b).
\]

For a density matrix on an \(N_k\)-dimensional Hilbert space,

\[
S_{\mathrm{vN}}(\rho)\le\log N_k,
\]

with equality for the maximally mixed state.

Therefore \(\log N_k\) is naturally the maximal entropy compatible with the finite-dimensional state-space dimension.

**Status:** the entropy bound is standard quantum information; the term **capacity entropy** is an **FCIG definition**. No cited algebraic-geometry source is being claimed to interpret \(h^0\) thermodynamically.

---

## 6. Relative Grothendieck–Riemann–Roch

For a proper smooth morphism and a finite locally free sheaf, relative GRR gives

\[
\boxed{
\operatorname{ch}(R\pi_*\mathscr L^k)
=
\pi_*\left(
\operatorname{Td}(T_\pi)e^{k c_1(\mathscr L)}
\right).
}
\]

More explicitly, the left side is

\[
\sum_i(-1)^i\operatorname{ch}(R^i\pi_*\mathscr L^k).
\]

**Status:** **[Established]** exactly the relative GRR structure recorded in the Stacks Project, Tag 02UO [Stacks-GRR].

### Degree zero

Under positivity and higher-cohomology vanishing, the leading asymptotics are

\[
h^0(X_b,L_b^k)
=
\frac{k^d}{d!}
\int_{X_b}c_1(L_b)^d
+O(k^{d-1}).
\]

Hence

\[
S_k^{\mathrm{cap}}
=
d\log k
+
\log\left(
\frac1{d!}\int_{X_b}c_1(L_b)^d
\right)
+O(k^{-1}).
\]

**Status:** **[Established]** Hilbert-polynomial/Riemann–Roch asymptotics; see GRR [Stacks-GRR].

### Degree two

For the determinant line,

\[
c_1(\lambda_k)
=
\operatorname{ch}_1(R\pi_*\mathscr L^k),
\]

so

\[
\boxed{
c_1(\lambda_k)
=
\left[
\pi_*\left(e^{k c_1(\mathscr L)}\operatorname{Td}(T_\pi)\right)
\right]_{(2)}.
}
\]

**Status:** **[Established]** consequence of GRR and the determinant-of-cohomology formalism [Stacks-GRR].

The slogan

\[
\boxed{\text{capacity entropy and anomaly are two degree projections of one index class}}
\]

is an **FCIG interpretation**. GRR itself does not use the words “entropy” or “anomaly” in this sense.

---

## 7. Determinant-line curvature and anomaly geometry

For elliptic families, Bismut–Freed construct a natural connection on the determinant line and compute its curvature [BF86a]. The holonomy/eta-invariant side is developed in the sequel [BF86b]. Quillen's earlier paper provides the determinant metric in the Cauchy–Riemann setting [Qui85].

Schematically, for a family of Dirac-type operators one encounters a curvature formula of the form

\[
F_{\det D}
\sim
\left[
\pi_*(\widehat A(R^{T_\pi})\operatorname{ch}(F^E))
\right]_{(2)},
\]

with normalization and precise hypotheses fixed by the chosen index-theorem convention.

**Status:** **[Established]** families-index/determinant-line principle [BF86a, BF86b].

The reverse implication

\[
F_{\det D}\stackrel{?}{\longrightarrow}R^{LC}
\]

is **not** provided by Bismut–Freed or the index theorem. It is part of the **FCIG Gravity Closure Problem**.

---

## 8. Bergman kernel asymptotics

Let \(L\to X\) be positive over a compact Kähler manifold and let \(B_k(x)\) denote the diagonal Bergman density of \(H^0(X,L^k)\).

The Tian–Yau–Zelditch expansion gives a full asymptotic series; Zelditch established the diagonal Szegő/Bergman asymptotics in this context [Zel98], and Lu computed lower-order coefficients explicitly [Lu00]. Ma–Marinescu provide a systematic heat-kernel/local-index treatment [MM07].

With convention-dependent constants,

\[
B_k(x)
\sim
k^d+c_{\mathrm{BK}}\operatorname{Scal}_\omega(x)k^{d-1}+a_2(x)k^{d-2}+\cdots.
\]

The invariant statement is that the first subleading local coefficient is proportional to scalar curvature; the numerical value of \(c_{\mathrm{BK}}\) depends on curvature/\(2\pi\) normalizations [Zel98, Lu00, MM07].

**Status:** **[Established]** [Zel98, Lu00, MM07].

Define

\[
s_k(x)=\log B_k(x)-d\log k.
\]

Then formally

\[
s_k(x)
=
\frac{c_{\mathrm{BK}}}{k}\operatorname{Scal}(x)+O(k^{-2}).
\]

**Status:** **[Derived from the established expansion]**; the terminology “local state-density entropy” is an **FCIG definition**.

The sharpened FCIG slogan is therefore

\[
\boxed{\text{curvature occurs in subleading local state-counting asymptotics}.}
\]

This is a synthesis of established Bergman asymptotics with the FCIG state-counting interpretation; it is not a theorem that “gravity equals entropy”.

---

## 9. Abelian varieties and the single-bundle no-go

For a polarized abelian variety \((A,L)\), the cohomology of ample line bundles, theta groups, polarization types, and the associated section spaces are standard material in the theory of complex abelian varieties [BL04].

If the polarization type is

\[
(d_1,\ldots,d_g),
\qquad D=\prod_i d_i,
\]

then for an ample \(L\),

\[
h^0(A,L^k)=Dk^g.
\]

Moreover

\[
K_A\simeq\mathcal O_A.
\]

Hence an ample quantization line cannot generally be identified with the anticanonical line on a positive-dimensional abelian variety.

**Status:** **[Established ingredients]** from abelian-variety theory [BL04]; the formulation as an FCIG “single-bundle no-go proposition” is **[Derived here]**.

This supports the three-layer architecture

\[
\boxed{(L_Q,\lambda_{\mathrm{an}},TM)}
\]

rather than a universal identification of quantization, anomaly, and tangent/spacetime geometry.

**Status:** **FCIG structural conclusion**.

---

# Part II — Explicit elliptic model

## 10. Elliptic curve and theta line

Let

\[
E_\tau=\mathbf C/(\mathbf Z+\tau\mathbf Z),
\qquad \tau\in\mathbb H.
\]

Classical theta functions, their quasi-periodicity, characteristics, and modular transformations are standard [Mum83; DLMF20]. The classical one-variable theory is particularly well covered in Mumford's *Tata Lectures on Theta I* [Mum83].

For a degree-one theta line \(L\), the level-\(k\) section space has dimension

\[
\dim H^0(E_\tau,L^k)=k.
\]

This is the genus-one case of standard line-bundle theory on abelian varieties [BL04].

A convenient basis is

\[
\theta_{k,j}(z,\tau)
=
\sum_{n\in\mathbf Z}
\exp\left[
\pi i k\tau(n+j/k)^2
+2\pi i k(n+j/k)z
\right],
\]

\[
j=0,\ldots,k-1.
\]

**Status:** **[Established]** theta-function/abelian-variety technology [Mum83, BL04].

---

## 11. Exact Gram matrix

Using the flat normalized Kähler form and the standard Hermitian metric on the theta line, the FCIG note computes directly

\[
\boxed{
\langle\theta_{k,j},\theta_{k,m}\rangle
=
\delta_{jm}\frac1{\sqrt{2k\operatorname{Im}\tau}}.
}
\]

Therefore

\[
\widehat\theta_{k,j}
=(2k\operatorname{Im}\tau)^{1/4}\theta_{k,j}
\]

is orthonormal.

**Status:** **[Derived here]** by explicit Fourier/Gaussian integration. The literature on theta functions supplies the basis and transformation laws, but no external reference is being claimed for this exact normalization convention.

---

## 12. Exact Poisson-resummed Bergman density

Writing

\[
z=x+\tau t,
\]

the FCIG calculation gives

\[
\boxed{
B_k(x,t;\tau)
=
k\sum_{p,\ell\in\mathbf Z}
\exp\left(-\frac{\pi k}{2Y}|\ell-p\tau|^2\right)
\exp\left(2\pi i k(px+\ell t)+\pi i k p\ell\right),
}
\]

where \(Y=\operatorname{Im}\tau\).

**Status:** **[Derived here]** by Poisson summation from the explicit theta basis. This is not attributed to Zelditch or Lu; those references concern the general local asymptotic expansion, not this exact lattice formula.

Because the flat elliptic curve has

\[
\operatorname{Scal}=0,
\]

all local curvature coefficients that would be built from the curvature tensor and its derivatives vanish, while the exact lattice expression still contains exponentially small terms.

For fixed \(\tau\), with normalized lattice systole

\[
\mu(\tau)=
\min_{(p,\ell)\ne(0,0)}
\frac{|\ell-p\tau|^2}{Y},
\]

one obtains

\[
B_k=k\left[1+O_\tau(e^{-\pi k\mu(\tau)/2})\right].
\]

**Status:** the vanishing of local curvature invariants is elementary for a flat metric; the exponential formula and estimate are **[Derived here]**.

This motivates the FCIG split

\[
\boxed{
\text{local perturbative geometry}
\oplus
\text{global exponentially small lattice sector}.
}
\]

**Status:** **FCIG interpretation** of the exact calculation.

---

## 13. Theta heat equation

Jacobi theta functions satisfy the classical heat equation

\[
4\pi i\,\partial_\tau\vartheta
=
\partial_z^2\vartheta.
\]

**Status:** **[Established]** classical identity; see the standard theta literature [Mum83] and modern reviews of the heat equation for theta functions [ThetaHeat].

For the level-\(k\) basis used here, rescaling yields the corresponding level-dependent heat operator.

**Status:** **[Derived here from the classical heat equation]**.

The interpretation of \(\tau\)-variation as an “information-state heat evolution” is an **FCIG interpretation**.

---

## 14. Hodge line on elliptic moduli

For the universal elliptic curve, the Hodge line is

\[
\lambda_H=\pi_*\Omega^1_{\mathcal E/B}.
\]

Modular forms of weight \(m\) are naturally interpreted as sections of powers of the Hodge bundle; this is standard in the moduli interpretation of modular forms [Katz73].

On the upper half-plane, take the frame \(dz\) with Petersson-type metric

\[
\|dz\|^2=Y=\operatorname{Im}\tau.
\]

Then direct differentiation gives

\[
F_{\lambda_H}
=-\partial\bar\partial\log Y,
\]

which is proportional to the hyperbolic \((1,1)\)-form.

**Status:** the Hodge-line/modular-form framework is **[Established]** [Katz73]; the displayed curvature formula in this normalization is **[Derived here]** by direct differentiation.

---

## 15. Determinant curvature identity in the elliptic model

From the exact Gram matrix,

\[
\|\theta_{k,0}\wedge\cdots\wedge\theta_{k,k-1}\|^2
=(2kY)^{-k/2}.
\]

Therefore the local Chern curvature of \(\det\mathcal H_k\) satisfies

\[
\boxed{
F_{\det\mathcal H_k}
=-\frac{k}{2}F_{\lambda_H}
}
\]

under the conventions of the FCIG note.

**Status:** **[Derived here]** from the explicit Gram determinant. Bismut–Freed [BF86a] supports the general determinant-line curvature framework, but is **not** being cited as the source of this specific genus-one coefficient.

This distinction is essential for citation accuracy.

---

# Part III — Modular transport and global anomaly

## 16. Classical modular transformation of theta functions

Jacobi theta functions transform nontrivially under

\[
T:\tau\mapsto\tau+1,
\qquad
S:\tau\mapsto-1/\tau,
\]

including square-root automorphy factors and permutations of theta characteristics [DLMF20; Mum83].

**Status:** **[Established]** classical theta-function theory [DLMF20, Mum83].

For finite theta spaces, these transformations are organized by Weil/metaplectic representation theory; Friedberg gives a classical treatment connecting theta transformation formulas and the Weil representation, including the eighth-root-of-unity factor [Fri85].

---

## 17. Finite Weil matrices in the chosen basis

For even \(k\), the FCIG convention yields

\[
(U_S)_{j\ell}
=
\frac1{\sqrt{k}}
 e^{-2\pi i j\ell/k},
\]

and

\[
(U_T)_{j\ell}
=
\delta_{j\ell}e^{\pi i j^2/k}.
\]

The finite Fourier/Gauss-sum calculation gives

\[
U_S^2=C,
\]

and

\[
\boxed{(U_SU_T)^3=e^{\pi i/4}C}
\]

in the conventions adopted in the note.

**Status:** the general phenomenon—Weil representation, metaplectic cover, and an eighth-root phase—is **[Established]** [Fri85]. The exact matrices and sign/phase convention above are **[Derived here]** and verified numerically in `weil-holonomy.py`.

This convention warning matters: different normalizations of the Fourier transform and theta characteristics move phases among \(S\), \(T\), and the metaplectic lift.

---

## 18. Odd-level parity issue

For odd \(k\), the chosen single theta-characteristic sector is not closed under \(T\); the transformation exchanges characteristic sectors, while \(T^2\) closes.

This behavior is consistent with classical theta-characteristic transformation theory [DLMF20, Mum83].

**Status:** the characteristic permutation is **[Established in classical theta theory]**; the exact level-\(k\) formulas in the FCIG basis are **[Derived here]** and numerically checked.

Therefore the modular completion at odd level naturally requires extra theta/metaplectic structure.

**Status:** **FCIG structural conclusion**, consistent with the standard metaplectic viewpoint [Fri85].

---

## 19. Flat anomaly line

For even \(k\), define locally

\[
\boxed{
\mathscr A_k
=
\det\mathcal H_k\otimes\lambda_H^{k/2}.
}
\]

Using the explicit curvature identity,

\[
F_{\mathscr A_k}
=
F_{\det\mathcal H_k}
+
\frac{k}{2}F_{\lambda_H}
=0.
\]

**Status:** **[Derived here]**.

Yet modular transport can retain a nontrivial Weil/metaplectic multiplier. Thus local Chern curvature can be cancelled while nontrivial global monodromy remains.

**Status:** the general possibility “flat connection with nontrivial holonomy” is **[Established]** differential geometry/differential cohomology [Bry93, ADH21]; the realization by \(\mathscr A_k\) in this exact theta model is **[Derived here]**.

This gives the most precise FCIG toy-model statement to date:

\[
\boxed{\text{anomaly}=\text{local curvature sector}+\text{global holonomy sector}.}
\]

**Status:** **FCIG interpretation** of a mathematically explicit decomposition.

---

## 20. What the cited literature does *not* prove

None of [Stacks-GRR], [Qui85], [BF86a], [BF86b], [Zel98], [Lu00], [MM07], [Mum83], [Fri85], or [Jac95] proves the full FCIG program.

In particular, these references do **not** prove:

1. that Bayesian inference is literally a line-bundle gauge theory;
2. that capacity entropy \(\log h^0\) is a thermodynamic entropy without an ensemble/Hamiltonian;
3. that determinant-line anomaly curvature determines spacetime curvature;
4. that Bergman curvature coefficients by themselves produce Lorentzian dynamics;
5. that the flat metaplectic anomaly line is a gravitational anomaly of a physical quantum field theory;
6. that Einstein's equation follows from the FCIG state-counting data.

Those are either interpretations or open closure problems.

This non-attribution statement is part of the citation policy of the project.

---

## 21. Jacobson and the gravity closure target

Jacobson's 1995 paper derives the Einstein equation as an equation of state by demanding a Clausius relation

\[
\delta Q=T\delta S
\]

for all local Rindler causal horizons, together with entropy proportional to horizon area [Jac95].

**Status:** **[Established]** statement of Jacobson's result [Jac95].

The FCIG question is therefore formulated more narrowly:

\[
\boxed{
\text{Can Bergman/index/determinant data define a local horizon entropy functional with the required variation?}
}
\]

**Status:** **FCIG conjectural research question**. Jacobson does not supply such a functional from algebraic-geometric state counting.

---

# 22. Provenance table

| FCIG claim/object | Status | Best supporting source(s) |
|---|---|---|
| Relative GRR formula | Established | [Stacks-GRR] |
| Holomorphic quantization by sections | Established | [SW76] |
| Determinant line / Quillen metric | Established | [Qui85] |
| Determinant connection curvature | Established | [BF86a] |
| Determinant holonomy / eta side | Established | [BF86b] |
| Differential cohomology stores curvature + holonomy | Established | [Bry93], [ADH21] |
| Bergman full asymptotic expansion | Established | [Zel98], [MM07] |
| Lower curvature coefficients | Established | [Lu00], [MM07] |
| Theta quasi-periodicity / S,T transformations | Established | [Mum83], [DLMF20] |
| Weil representation / eighth-root phase | Established | [Fri85] |
| Abelian-variety line bundles/theta groups | Established | [BL04] |
| Modular forms as Hodge-bundle sections | Established | [Katz73] |
| Theta heat equation | Established | [Mum83], [ThetaHeat] |
| Exact elliptic Gram matrix | Derived here | FCIG Explicit Model I |
| Exact Poisson-resummed Bergman lattice formula | Derived here | FCIG Explicit Model I |
| \(F_{\det\mathcal H_k}=-(k/2)F_{\lambda_H}\) in our normalization | Derived here | FCIG Explicit Model I |
| Finite matrices \(U_S,U_T\) in our convention | Derived here | FCIG Explicit Model II, checked against [Fri85]/classical theta theory |
| Flat anomaly line \(\mathscr A_k\) | Derived here | FCIG Explicit Model II |
| “capacity entropy” terminology | FCIG definition | not attributed |
| “entropy/anomaly are two shadows of one index class” | FCIG interpretation | built on [Stacks-GRR] |
| Gravity Closure Problem | FCIG conjecture | motivated partly by [Jac95] |

---

# References

Full BibTeX records are in [`references.bib`](references.bib).

- **[ADH21]** A. Amabel, A. Debray, P. J. Haine, *Differential Cohomology: Categories, Characteristic Classes, and Connections*, arXiv:2109.12250.
- **[BF86a]** J.-M. Bismut, D. S. Freed, “The analysis of elliptic families. I. Metrics and connections on determinant bundles,” *Commun. Math. Phys.* **106** (1986), 159–176. DOI: 10.1007/BF01210930.
- **[BF86b]** J.-M. Bismut, D. S. Freed, “The analysis of elliptic families. II. Dirac operators, eta invariants, and the holonomy theorem,” *Commun. Math. Phys.* **107** (1986), 103–163.
- **[BL04]** C. Birkenhake, H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer, 2004. DOI: 10.1007/978-3-662-06307-1.
- **[Bry93]** J.-L. Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser, 1993.
- **[DLMF20]** NIST Digital Library of Mathematical Functions, Chapter 20, especially §20.7(viii), “Transformations of Lattice Parameter.”
- **[Fri85]** S. Friedberg, “Theta function transformation formulas and the Weil representation,” *J. Number Theory* **20** (1985), 121–127. DOI: 10.1016/0022-314X(85)90032-0.
- **[Jac95]** T. Jacobson, “Thermodynamics of Spacetime: The Einstein Equation of State,” *Phys. Rev. Lett.* **75** (1995), 1260–1263. DOI: 10.1103/PhysRevLett.75.1260.
- **[Katz73]** N. M. Katz, “p-adic properties of modular schemes and modular forms,” in *Modular Functions of One Variable III*, LNM 350, Springer (1973), 69–190. DOI: 10.1007/978-3-540-37802-0_3.
- **[Lu00]** Z. Lu, “On the lower order terms of the asymptotic expansion of Tian–Yau–Zelditch,” *Amer. J. Math.* **122** (2000), 235–273. DOI: 10.1353/ajm.2000.0013.
- **[MM07]** X. Ma, G. Marinescu, *Holomorphic Morse Inequalities and Bergman Kernels*, Birkhäuser, 2007. DOI: 10.1007/978-3-7643-8115-8.
- **[Mum83]** D. Mumford, *Tata Lectures on Theta I*, Birkhäuser, 1983; reprint/modern edition available from Birkhäuser.
- **[Qui85]** D. Quillen, “Determinants of Cauchy–Riemann operators over a Riemann surface,” *Funct. Anal. Appl.* **19** (1985), 31–34. DOI: 10.1007/BF01086022.
- **[Stacks-GRR]** The Stacks Project, Tag 02UO, “Grothendieck–Riemann–Roch.”
- **[SW76]** D. J. Simms, N. M. J. Woodhouse, *Lectures on Geometric Quantization*, Lecture Notes in Physics 53, Springer, 1976. DOI: 10.1007/3-540-07860-6.
- **[ThetaHeat]** Classical Jacobi theta heat equation; a modern explicit statement is given in the literature on heat equations for theta/sigma functions, e.g. *Glasgow Mathematical Journal* article “Theory of heat equations for sigma functions,” equation (0.6).
- **[Zel98]** S. Zelditch, “Szegő kernels and a theorem of Tian,” *International Mathematics Research Notices* 1998(6), 317–331. DOI: 10.1155/S107379289800021X.
