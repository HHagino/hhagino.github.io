# Fibered Cohomological Information Geometry

## 局所ポテンシャル、直像、状態密度、アノマリー曲率から重力への閉包問題

**Status:** Research note / speculative synthesis  
**Date:** 2026-09-08

> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are calculations carried out in these FCIG notes; statements marked **FCIG interpretation/conjecture** are not attributed to the cited literature. Full entries are collected at the end of this note and in [`references.bib`](references.bib).

> **中心命題（研究プログラム）**  
> 重力を単純に「エントロピーの勾配」と同一視するのではなく、**局所情報ポテンシャルの貼り合わせ、量子化線束の直像、determinant line の anomaly data、Bergman kernel の局所状態密度**を、一つの index-theoretic structure の異なる射影として読む。Lorentzian 重力への最後の写像は独立した **Gravity Closure Problem** として切り出す。

---

## Abstract

We propose a mathematical research program called **Fibered Cohomological Information Geometry (FCIG)**. Its basic object is a polarized Hermitian family

\[
\pi:(\mathcal X,\mathscr L,h)\longrightarrow B,
\]

where \(B\) is interpreted as a parameter, inference, or moduli space, while \((X_b,L_b)\) is a geometric state space over \(b\in B\).

The proposal separates four layers which should not be conflated:

1. local information/free-energy potentials are treated as local weights of Hermitian line bundles;
2. global obstruction and anomaly data are encoded by differential cohomology and determinant lines;
3. global state capacity is measured by
   \[
   S_k^{\mathrm{cap}}=\log\dim H^0(X,L^k);
   \]
4. local state density is measured by the Bergman kernel \(B_k(x)\), whose asymptotic coefficients contain curvature invariants.

The organizing equation is relative Grothendieck–Riemann–Roch:

\[
\operatorname{ch}(R\pi_*\mathscr L^k)
=
\pi_*\!\left(e^{k c_1(\mathscr L)}\operatorname{Td}(T_\pi)\right).
\]

The degree-zero component controls the virtual rank and, under positivity/vanishing hypotheses, the asymptotic state count. The degree-two component controls the first Chern class of the determinant of cohomology. This motivates the interpretation

\[
\boxed{\text{capacity entropy and anomaly are two degree projections of one index class}.}
\]

This sentence is **not** a theorem of physics; it is a proposed interpretation built on established geometry. The genuinely open step is to construct a Lorentzian dynamical closure from local state-density and anomaly data.

---

## 1. Three epistemic levels

A viable formulation must distinguish theorem from interpretation.

### Established mathematics

- Hermitian local weights and Chern curvature;
- degree-2 differential cohomology / Deligne cohomology and \(U(1)\)-bundles with connection;
- derived direct images \(R\pi_*\mathscr L^k\);
- determinant of cohomology \(\det R\pi_*\mathscr L^k\);
- relative Grothendieck–Riemann–Roch;
- holomorphic geometric quantization under standard positivity/polarization hypotheses;
- families index theory and determinant-line curvature/holonomy;
- Bergman-kernel asymptotics.

### FCIG definitions / interpretations

- \(\log h^0(X,L^k)\) is called **capacity entropy**;
- the logarithmic norm of a local determinant-line section is interpreted as a local free-energy-like potential;
- degree zero and degree two of the same index class are read respectively as state-capacity and anomaly sectors.

### Conjectural physics

The passage

\[
(\text{state density},\text{anomaly})
\stackrel{?}{\longrightarrow}
\text{Lorentzian gravitational dynamics}
\]

is **not derived here**. It is the main closure problem.

---

## 2. The basic fibered object

Let

\[
\pi:\mathcal X\longrightarrow B
\]

be a proper smooth family of compact complex manifolds of complex dimension \(d\). Let

\[
\mathscr L\longrightarrow\mathcal X
\]

be a relatively positive holomorphic line bundle with Hermitian metric \(h\). For \(b\in B\), write

\[
X_b=\pi^{-1}(b),\qquad L_b=\mathscr L|_{X_b}.
\]

The intended dictionary is

\[
\boxed{B=\text{parameter / inference / moduli space}},
\qquad
\boxed{(X_b,L_b)=\text{geometric state space over }b}.
\]

No global scalar information potential \(\Phi:B\to\mathbf R\) is assumed.

---

## 3. Local potentials are gauge data

Choose a local holomorphic frame \(e_i\) for \(\mathscr L\) on \(U_i\), and write

\[
\|e_i\|_h^2=e^{-\phi_i}.
\]

If on \(U_i\cap U_j\)

\[
e_i=g_{ij}e_j,
\qquad g_{ij}\in\mathcal O^\times(U_i\cap U_j),
\]

then

\[
\phi_i-\phi_j=-\log|g_{ij}|^2.
\]

Thus \(\phi_i\) is not a global scalar. Nevertheless

\[
\omega_{\mathscr L}
=
\frac{i}{2\pi}\partial\bar\partial\phi_i
\]

is global (with the chosen standard normalization) and represents \(c_1(\mathscr L)\) in de Rham cohomology.

**Established.** This is standard Hermitian holomorphic line-bundle/Chern-connection geometry; see [Bry93]. The subsequent reading of these local weights as information potentials is an **FCIG interpretation**.

Hence

\[
\boxed{\text{potential is gauge-dependent; curvature is gauge-invariant}.}
\]

This replaces the naive requirement that information geometry must arise from one global convex potential.

---

## 4. Čech–de Rham data and differential cohomology

In a unitary trivialization write

\[
g_{ij}=e^{i\chi_{ij}}.
\]

Local connection forms satisfy

\[
A_j=A_i+d\chi_{ij},
\]

and on triple overlaps

\[
\chi_{ij}+\chi_{jk}+\chi_{ki}=2\pi n_{ijk},
\qquad n_{ijk}\in\mathbf Z.
\]

The curvature

\[
F=dA_i
\]

is global. The full data

\[
(\chi_{ij},A_i,F)
\]

should be regarded as differential-cohomological rather than merely de Rham data. Schematically,

**Established.** Differential/Deligne cohomology provides a model for line bundles with connection and retains curvature together with flat-holonomy data; see [Bry93; ADH21]. Calling the two sectors “local anomaly” and “global anomaly” is **FCIG terminology**.

\[
[(L,\nabla)]\in\widehat H^2(B;\mathbf Z).
\]

This matters because curvature alone does not detect all global information: a flat bundle may satisfy

\[
F=0
\]

while having nontrivial holonomy

\[
\operatorname{Hol}_\gamma(\nabla)\neq1.
\]

Hence a useful decomposition is

\[
\boxed{\text{local anomaly data}\sim F,\qquad\text{global anomaly data}\sim\operatorname{Hol}.}
\]

For a worldline \(\gamma:S^1\to B\), the observable is schematically

\[
\operatorname{Hol}_\gamma(\nabla)
=
\exp\!\left(i\oint_\gamma A\right).
\]

This is the precise core behind the phrase **worldline bundle anomaly**.

---

## 5. State spaces as direct images

For \(k\ge1\), define the fiberwise holomorphic state space

**Established background.** Holomorphic sections of a polarized/prequantum line bundle form the standard state space in holomorphic geometric quantization under the usual positivity and polarization hypotheses; see [SW76].

\[
\mathcal H_{k,b}=H^0(X_b,L_b^k).
\]

When higher cohomology vanishes and base-change hypotheses are satisfied, these spaces form a vector bundle

\[
\mathcal H_k=\pi_*\mathscr L^k.
\]

More generally the correct object is the derived direct image

\[
\boxed{\mathcal H_k^{\mathrm{der}}=R\pi_*\mathscr L^k.}
\]

Its determinant of cohomology is

\[
\boxed{\lambda_k=\det R\pi_*\mathscr L^k.}
\]

This already forces a separation:

\[
\mathscr L\text{ lives on }\mathcal X,
\qquad
\lambda_k\text{ lives on }B.
\]

The polarization line and the anomaly/determinant line are not the same geometric object.

---

## 6. Global capacity entropy

Set

\[
N_k(b)=\dim H^0(X_b,L_b^k).
\]

Define

\[
\boxed{S_k^{\mathrm{cap}}(b)=\log N_k(b).}
\]

This is not the entropy of an arbitrary state. For a density matrix \(\rho\) on an \(N_k\)-dimensional Hilbert space,

\[
S_{\mathrm{vN}}(\rho)=-\operatorname{Tr}(\rho\log\rho)\le\log N_k,
\]

with equality for the maximally mixed state. Therefore \(\log N_k\) is naturally a **capacity entropy**: the maximal entropy permitted by the finite-dimensional state space.

---

## 7. GRR as the organizing equation

Let

\[
\ell=c_1(\mathscr L).
\]

Relative Grothendieck–Riemann–Roch gives

**Established.** The relative GRR identity for the alternating derived direct image is standard; see [Stacks-GRR]. Reading degree zero as a capacity sector and degree two as an anomaly sector is an **FCIG interpretation**.

\[
\boxed{
\operatorname{ch}(R\pi_*\mathscr L^k)
=
\pi_*\left(e^{k\ell}\operatorname{Td}(T_\pi)\right).
}
\]

More precisely the left-hand side is the Chern character of the alternating derived direct image

\[
\sum_i(-1)^i[R^i\pi_*\mathscr L^k].
\]

### Degree zero: state counting

For sufficiently positive \(k\), under higher-cohomology vanishing,

\[
N_k
=
\frac{k^d}{d!}\int_{X_b}c_1(L_b)^d+O(k^{d-1}).
\]

Therefore

\[
S_k^{\mathrm{cap}}
=
d\log k
+
\log\!\left(\frac1{d!}\int_{X_b}c_1(L_b)^d\right)
+O(k^{-1}).
\]

Thus

\[
\boxed{\text{leading state capacity}\longleftrightarrow\text{polarized volume}.}
\]

### Degree two: determinant-line class

Since

\[
c_1(\lambda_k)=\operatorname{ch}_1(R\pi_*\mathscr L^k),
\]

we obtain

\[
\boxed{
c_1(\lambda_k)
=
\left[\pi_*\left(e^{k\ell}\operatorname{Td}(T_\pi)\right)\right]_{(2)}.
}
\]

The same index density therefore produces a degree-zero state-counting sector and a degree-two determinant/anomaly sector.

Hence the FCIG slogan:

\[
\boxed{\textbf{capacity entropy and anomaly are two shadows of one index class.}}
\]

The cohomological relation is classical; the entropy/anomaly dictionary is the proposed interpretation.

---

## 8. Determinant-line geometry as local free energy

Equip \(\lambda_k\) with a Hermitian metric, for instance of Quillen type when an appropriate determinant-line construction is available.

**Established background.** Determinant lines and Quillen metrics originate in [Qui85]; natural determinant-bundle connections and their curvature/holonomy for elliptic families are developed in [BF86a; BF86b]. Calling the logarithmic norm below a free-energy potential is an **FCIG interpretation**. For a local nonzero section \(\sigma_i\), define

\[
\mathcal F_i=-\log\|\sigma_i\|^2.
\]

On overlaps, if \(\sigma_i=g_{ij}\sigma_j\), then

\[
\mathcal F_i-\mathcal F_j=-\log|g_{ij}|^2.
\]

Thus \(\mathcal F_i\) is a local potential, while

\[
\Omega_k=
\frac{i}{2\pi}\partial\bar\partial\mathcal F_i
\]

is global. This suggests the interpretation

\[
\boxed{\text{local free-energy potential}\longleftrightarrow\text{metric on determinant line}\longleftrightarrow\text{anomaly curvature}.}
\]

Calling \(\mathcal F_i\) “free energy” is the proposed physical dictionary; the line-bundle geometry itself is standard.

---

## 9. Why a global entropy gradient cannot be gravity

Suppose one tries

\[
\text{gravity}\propto\nabla_BS_k^{\mathrm{cap}}.
\]

In a smooth family for which \(h^0(X_b,L_b^k)\) is locally constant,

\[
\nabla_BS_k^{\mathrm{cap}}=0.
\]

Yet the fibers may have nonzero intrinsic curvature. Therefore

\[
\boxed{R\neq0\quad\centernot\Rightarrow\quad\nabla\log h^0\neq0.}
\]

A universal law

\[
\text{gravity}=\nabla\log\dim H^0
\]

is therefore untenable. The global count must be refined to a **local density of states**.

---

## 10. Bergman kernel as local state density

Let \(\{s_\alpha\}_{\alpha=1}^{N_k}\) be an orthonormal basis of \(H^0(X,L^k)\). Define

\[
\boxed{B_k(x)=\sum_{\alpha=1}^{N_k}|s_\alpha(x)|_{h^k}^2.}
\]

Up to the normalization convention for the volume form,

\[
\int_XB_k\,\frac{\omega^d}{d!}=N_k.
\]

Thus \(B_k\) refines the global state count into a pointwise density.

For a positive line bundle, the Tian–Catlin–Zelditch–Lu expansion has the schematic form

**Established.** The diagonal Bergman/Szegő asymptotic expansion and its curvature coefficients are standard; see [Zel98; Lu00; MM07]. The coefficient is deliberately kept as \(c_{\mathrm{BK}}\) because it depends on curvature and \(2\pi\) normalization conventions.

\[
B_k(x)
\sim
k^d
+
c_{\mathrm{BK}}\operatorname{Scal}_\omega(x)k^{d-1}
+
a_2(x)k^{d-2}
+\cdots,
\]

where the numerical coefficient \(c_{\mathrm{BK}}\) depends on the normalization convention for \(\omega\), curvature and scalar curvature. The invariant structural statement is

\[
a_1(x)\propto\operatorname{Scal}_\omega(x).
\]

Define

\[
\boxed{s_k(x)=\log B_k(x)-d\log k.}
\]

Then

\[
s_k(x)
=
\frac{c_{\mathrm{BK}}}{k}\operatorname{Scal}_\omega(x)+O(k^{-2}).
\]

Hence

\[
\boxed{\textbf{curvature appears in the subleading asymptotics of local state counting.}}
\]

Moreover

\[
\nabla s_k
=
\frac{c_{\mathrm{BK}}}{k}\nabla\operatorname{Scal}+O(k^{-2}),
\]

so entropy gradients are sensitive first to **curvature gradients**, not directly to curvature itself.

---

## 11. Three test geometries

### 11.1 Projective line

Take

\[
X=\mathbf P^1,\qquad L=\mathcal O(n),\quad n>0.
\]

Then

\[
h^0(\mathbf P^1,\mathcal O(nk))=nk+1,
\]

so

\[
S_k^{\mathrm{cap}}=\log(nk+1).
\]

Also

\[
K_{\mathbf P^1}^{-1}\simeq\mathcal O(2).
\]

For the Fubini–Study metric, scalar curvature and Bergman density are constant by homogeneity. Hence

\[
\nabla s_k=0
\]

while

\[
\operatorname{Scal}>0.
\]

Therefore curved homogeneous geometry does not require an entropy gradient.

### 11.2 Elliptic curve

Let \(E\) be an elliptic curve and let \(\deg L=d>0\). Since \(K_E\simeq\mathcal O_E\), Riemann–Roch gives for \(k>0\)

\[
h^0(E,L^k)=kd.
\]

Therefore

\[
S_k^{\mathrm{cap}}=\log k+\log d.
\]

But

\[
c_1(TE)=0,
\]

and a translation-invariant Kähler metric is flat. Thus a positive quantization line can have growing state capacity even when tangent geometry is Ricci-flat:

\[
\boxed{\text{quantization curvature}\neq\text{Ricci curvature}.}
\]

### 11.3 Abelian variety

**Established background.** Standard line-bundle, polarization, and theta-group theory on abelian varieties is developed in [BL04; Mum83]. The “single-bundle no-go” below is a short consequence **derived here**, not a named result from those sources.

Let \(A\) be a \(g\)-dimensional abelian variety and \(L\) an ample line bundle of polarization type \((d_1,\ldots,d_g)\). Put

\[
D=\prod_{i=1}^g d_i.
\]

Riemann–Roch gives

\[
h^0(A,L^k)=Dk^g.
\]

Hence

\[
S_k^{\mathrm{cap}}=g\log k+\log D.
\]

But

\[
K_A\simeq\mathcal O_A,
\qquad c_1(K_A^{-1})=0,
\]

whereas an ample \(L\) satisfies \(c_1(L)^g>0\).

### Single-bundle no-go proposition

On a positive-dimensional abelian variety, an ample quantization line cannot be identified with the anticanonical line:

\[
\boxed{L_Q\not\simeq K_A^{-1}.}
\]

Therefore a theory in which one single line bundle is simultaneously “quantization”, “entropy” and “gravity” is too rigid.

---

## 12. The minimal three-layer architecture

The test geometries force at least three layers:

### Quantization layer

\[
L_Q\to X
\]

controls \(H^0(X,L_Q^k)\) and state counting.

### Anomaly layer

\[
\lambda_{\mathrm{an}}=\det R\pi_*E\to B
\]

controls determinant-line curvature and holonomy over parameter/moduli space.

### Gravitational layer

\[
(TM,g,\nabla^{LC})
\]

or its Lorentz frame bundle controls spacetime curvature

\[
R^{ab}=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb}.
\]

Thus the mature architecture is

\[
\boxed{(L_Q,\lambda_{\mathrm{an}},TM)}
\]

with nontrivial maps between them, not their naive identification.

---

## 13. Families index theory already gives one direction

For a family of Dirac-type operators \(D_b\), the determinant line over parameter space carries a natural connection whose curvature is governed by the local families index density. Schematically,

\[
F_{\det D}
\sim
\left[
\pi_*\left(\widehat A(R^{T_\pi})\operatorname{ch}(F^E)\right)
\right]_{(2)}.
\]

This establishes a mathematically controlled direction

**Established background.** Families index theory controls determinant-line curvature and holonomy from geometric/gauge curvature data; see [BF86a; BF86b]. Those references do **not** assert an inverse map from determinant anomaly to spacetime curvature.

\[
\boxed{\text{geometric/gauge curvature}\longrightarrow\text{determinant-line curvature}.}
\]

FCIG asks whether sufficiently rich anomaly and state-density data can support a reverse **dynamical** closure. No such inverse follows automatically from index theory.

---

## 14. Gravity Closure Problem

A \(U(1)\) anomaly curvature and a Lorentzian Riemann curvature do not live in the same representation:

\[
F_{\mathrm{an}}\in\Omega^2(B;i\mathbf R),
\]

whereas

\[
R^{LC}\in\Omega^2(M;\mathfrak{so}(1,3)).
\]

Therefore

\[
F_{\mathrm{an}}=R^{LC}
\]

is generally type-incorrect.

A legitimate theory needs extra geometric data and a response map, schematically

\[
\mathfrak R:
(\widehat{\mathfrak a},B_k,g,J,\mathcal C)
\longmapsto
R^{LC},
\]

where \(\mathcal C\) contains causal/Lorentzian structure.

A more physical alternative is inspired by Jacobson's local horizon thermodynamics.

**Established reference point.** Jacobson derives the Einstein equation as an equation of state from the Clausius relation on local Rindler horizons together with an entropy-area assumption [Jac95]. The FCIG entropy functional sought here is **not** supplied by that paper. Instead of identifying entropy gradients with forces, seek an FCIG entropy functional satisfying a local Clausius relation

\[
\boxed{\delta Q=T_U\,\delta S_{\mathrm{FCIG}}}
\]

for all suitable local causal horizons.

The sharpened question becomes

\[
\boxed{\text{Can index/Bergman/determinant data produce the correct local horizon entropy functional?}}
\]

That is the Gravity Closure Problem in a falsifiable form.

---

## 15. Algebraic thermodynamics from the Hilbert series

The Kodaira dimension should not itself be called an energy. A better object is the graded state space

\[
\mathcal H=\bigoplus_{k\ge0}H^0(X,L^k)
\]

with Hilbert series

\[
\boxed{Z(q)=\sum_{k\ge0}h^0(X,L^k)q^k.}
\]

Algebraic geometry determines the degeneracies. To obtain thermodynamics one must add a Hamiltonian interpretation such as

\[
q=e^{-\beta\varepsilon}.
\]

Then

\[
F=-\beta^{-1}\log Z,
\qquad
E=-\partial_\beta\log Z,
\qquad
S=\beta(E-F).
\]

The assignment \(E_k=\varepsilon k\) is an extra dynamical postulate, not a theorem of algebraic geometry.

### Exact model series

For \(X=\mathbf P^1\), \(L=\mathcal O(n)\),

\[
Z(q)=\sum_{k\ge0}(nk+1)q^k
=
\frac{1+(n-1)q}{(1-q)^2}.
\]

For an elliptic curve with \(\deg L=d\),

\[
Z(q)=1+\frac{dq}{(1-q)^2}.
\]

For a \(g\)-dimensional abelian variety with \(h^0(A,L^k)=Dk^g\),

\[
Z(q)=1+D\operatorname{Li}_{-g}(q).
\]

---

## 16. Moduli, theta functions and level structures

The abelian-variety case naturally promotes the theory from a single fiber to moduli. For a polarized abelian variety \((A,L)\), theta-group representations organize \(H^0(A,L)\), while suitable level structures provide distinguished theta coordinates/bases.

At the moduli level one has line bundles such as the Hodge line

\[
\lambda_H=\det\pi_*\Omega^1_{\mathcal A/B},
\]

whose powers support modular forms. This creates two levels of state spaces:

\[
\boxed{\text{fiber: }H^0(A,L^k)}
\]

and

\[
\boxed{\text{moduli: }H^0(\overline{\mathcal A}_{g,N},\lambda_H^m(\cdots)).}
\]

Correspondingly, when finite-dimensionality and compactification data make the expression meaningful, one may compare

\[
S_{\mathrm{fiber}}=\log h^0(A,L^k)
\]

with a modular capacity

\[
S_{\mathrm{mod}}
=
\log\dim H^0(\overline{\mathcal A}_{g,N},\lambda_H^m(\cdots)).
\]

This is a plausible place for the originally envisioned relation among level structure, modular geometry, energy and entropy to become mathematically testable.

---

## 17. Five axioms and one conjectural closure

### Axiom I — Fibered geometry

\[
\pi:(\mathcal X,\mathscr L,h)\to B
\]

is a polarized Hermitian family.

### Axiom II — Locality

Information/free-energy potentials are local weights. Global observables are encoded by characteristic class, curvature and holonomy.

### Axiom III — Quantization

\[
\mathcal H_k^{\mathrm{der}}=R\pi_*\mathscr L^k.
\]

### Axiom IV — Entropy hierarchy

Global capacity:

\[
S_k^{\mathrm{cap}}=\log\operatorname{rank}\mathcal H_k.
\]

Local density:

\[
s_k(x)=\log B_k(x)-d\log k.
\]

### Axiom V — Anomaly

\[
\lambda_k=\det R\pi_*\mathscr L^k
\]

with its connection defines the anomaly object.

### Conjectural closure — gravity

There exists a physically meaningful local functional built from Bergman, determinant and index data whose causal-horizon variation satisfies a local thermodynamic relation sufficient to close the equations into Lorentzian gravitational dynamics.

---

## 18. Falsifiable questions

A research program becomes useful only when it can fail.

1. **Inverse Bergman geometry.** To what extent does the full asymptotic sequence \(\{B_k(x)\}_{k\to\infty}\) determine the metric and curvature tensor?
2. **Index compatibility.** Can one define a local entropy density whose integral reproduces the global state count while whose variation couples naturally to determinant-line curvature?
3. **Lorentzianization.** What replaces holomorphic positivity and Bergman asymptotics on a Lorentzian or causal background?
4. **Anomaly inversion.** Under what hypotheses can determinant-line data constrain the geometry from which the index density arose?
5. **Horizon closure.** Can an FCIG entropy density satisfy \(\delta Q=T\delta S\) for every suitable local causal horizon?
6. **Modular information geometry.** Can natural metrics/curvatures on moduli of polarized varieties be related to a statistically meaningful Fisher-type structure without imposing global dual flatness by hand?

---

## 19. What would count as genuine progress?

The next milestone is **not** “derive Einstein's equation”. A serious sequence is

\[
\boxed{
\begin{array}{l}
\text{(i) prove exact compatibility statements for families;}\\
\text{(ii) compute Bergman and determinant data in explicit models;}\\
\text{(iii) formulate a local entropy functional;}\\
\text{(iv) test it on homogeneous, Ricci-flat and curved examples;}\\
\text{(v) only then attempt Lorentzian closure.}
\end{array}}
\]

The first laboratories should be

\[
\mathbf P^1,\qquad E_\tau,\qquad A_\tau,\qquad\mathbf P^n,\qquad\Sigma_g\;(g\ge2).
\]

The genus \(0,1,\ge2\) trichotomy is especially useful because positive, zero and negative canonical-curvature behavior can be compared against state-counting growth.

---

## 20. Final formulation

The current core is

\[
\boxed{
\begin{aligned}
\pi:(\mathcal X,\mathscr L,h)&\to B,\\
\mathcal H_k^{\mathrm{der}}&=R\pi_*\mathscr L^k,\\
\lambda_k&=\det R\pi_*\mathscr L^k,\\
S_k^{\mathrm{cap}}&=\log\operatorname{rank}\mathcal H_k,\\
B_k(x)&=\sum_\alpha|s_\alpha(x)|^2,\\
\widehat{\mathfrak a}_k&=[(\lambda_k,\nabla_k)]\in\widehat H^2(B;\mathbf Z),\\
\operatorname{ch}(R\pi_*\mathscr L^k)
&=
\pi_*\left(e^{k c_1(\mathscr L)}\operatorname{Td}(T_\pi)\right).
\end{aligned}}
\]

The conceptual synthesis is

\[
\boxed{
\text{local potentials}
\to
\text{differential cohomology}
\to
\text{direct image}
\to
\begin{cases}
\text{global state capacity},\\
\text{determinant anomaly},\\
\text{local Bergman density}.
\end{cases}}
\]

with curvature appearing in local asymptotics and anomaly geometry appearing in the determinant line.

The most defensible form of the original intuition is therefore

\[
\boxed{\textbf{Geometry is encoded not by entropy alone, but by the asymptotic and cohomological structure of state counting.}}
\]

The remaining question is mathematical rather than rhetorical:

\[
\boxed{\textbf{What additional causal and variational structure turns that encoding into gravity?}}
\]

---

## References / starting points

- The Stacks Project, **Grothendieck–Riemann–Roch**, Tag 02UO: https://stacks.math.columbia.edu/tag/02UO
- D. Quillen, *Determinants of Cauchy–Riemann operators over a Riemann surface*, Functional Analysis and Its Applications 19 (1985).
- D. S. Freed, *Determinant Line Bundles Revisited*, arXiv:dg-ga/9505002: https://arxiv.org/abs/dg-ga/9505002
- J.-L. Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser.
- X. Ma and G. Marinescu, *Holomorphic Morse Inequalities and Bergman Kernels*, Birkhäuser.
- N. M. J. Woodhouse, *Geometric Quantization*.
- T. Jacobson, *Thermodynamics of Spacetime: The Einstein Equation of State*, Phys. Rev. Lett. 75 (1995), 1260–1263: https://doi.org/10.1103/PhysRevLett.75.1260

---

## Research-status statement

This note deliberately separates:

- standard results in algebraic, complex and differential geometry;
- newly introduced terminology such as **capacity entropy**;
- proposed interpretations of determinant-line geometry;
- speculative gravitational closure.

It should therefore be presented as a **research-program note**, not as a completed derivation of quantum gravity.

---

## References cited in this note

Canonical BibTeX entries: [`references.bib`](references.bib).

- **[Bry93]** J.-L. Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser (1993).
- **[ADH21]** A. Amabel, A. Debray & P. J. Haine, *Differential Cohomology: Categories, Characteristic Classes, and Connections* (2021), arXiv:2109.12250.
- **[SW76]** D. J. Simms & N. M. J. Woodhouse, *Lectures on Geometric Quantization*, Lecture Notes in Physics 53, Springer (1976).
- **[Stacks-GRR]** The Stacks Project, Tag 02UO, “Grothendieck–Riemann–Roch.”
- **[Qui85]** D. Quillen, “Determinants of Cauchy–Riemann Operators over a Riemann Surface,” *Functional Analysis and Its Applications* **19**(1) (1985), 31–34.
- **[BF86a]** J.-M. Bismut & D. S. Freed, “The Analysis of Elliptic Families. I. Metrics and Connections on Determinant Bundles,” *Communications in Mathematical Physics* **106** (1986), 159–176.
- **[BF86b]** J.-M. Bismut & D. S. Freed, “The Analysis of Elliptic Families. II. Dirac Operators, Eta Invariants, and the Holonomy Theorem,” *Communications in Mathematical Physics* **107** (1986), 103–163.
- **[Zel98]** S. Zelditch, “Szegő Kernels and a Theorem of Tian,” *International Mathematics Research Notices* **1998**(6), 317–331.
- **[Lu00]** Z. Lu, “On the Lower Order Terms of the Asymptotic Expansion of Tian–Yau–Zelditch,” *American Journal of Mathematics* **122**(2) (2000), 235–273.
- **[MM07]** X. Ma & G. Marinescu, *Holomorphic Morse Inequalities and Bergman Kernels*, Progress in Mathematics 254, Birkhäuser (2007).
- **[BL04]** C. Birkenhake & H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer (2004).
- **[Mum83]** D. Mumford, *Tata Lectures on Theta I*, Progress in Mathematics 28, Birkhäuser (1983).
- **[Jac95]** T. Jacobson, “Thermodynamics of Spacetime: The Einstein Equation of State,” *Physical Review Letters* **75**(7) (1995), 1260–1263.

