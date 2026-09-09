# FCIG Model XXIV — Multiplet threshold versus anomaly polynomial

**Status:** derived comparison in the same six-dimensional \(\mathcal N=(1,0)\) vector/hyper/tensor counting convention used in Model XXIII. The anomaly coefficients are **Established**; the coefficient-space comparison is **Derived here**.

## 1. Purpose and citation policy

Model XXIII fixed the parity-even finite elliptic two-derivative threshold

\[
G_{VHT}^{\rm fin}
=\frac{K(n_V,n_H,n_T)}{16\pi^3L^2}
Z_\tau(2)g_{\rm hyp},
\qquad
\boxed{K=2n_V-n_H+2n_T}.
\tag{XXIV.1}
\]

This note compares \(K\) with the independently established six-dimensional anomaly polynomial. No anomaly coefficient is identified with a kinetic coefficient.

For free \(\mathcal N=(1,0)\) multiplets, Appendix A of Ohmori--Shimizu--Tachikawa--Yonekura [OhmoriEtAl2014] gives the standard contributions. With background gauge fields switched off and one vector degree counted per gauge generator,

\[
\boxed{
I_8^{H}=\frac{7p_1(T)^2-4p_2(T)}{5760},
}
\tag{XXIV.2}
\]

\[
\boxed{
I_8^{V}
=-\frac{c_2(R)^2}{24}
-\frac{c_2(R)p_1(T)}{48}
-\frac{7p_1(T)^2-4p_2(T)}{5760},
}
\tag{XXIV.3}
\]

\[
\boxed{
I_8^{T}
=\frac{c_2(R)^2}{24}
+\frac{c_2(R)p_1(T)}{48}
+\frac{23p_1(T)^2-116p_2(T)}{5760}.
}
\tag{XXIV.4}
\]

These are **Established** formulas [OhmoriEtAl2014]. The same pure-gravitational coefficients are reproduced in later 6d anomaly reviews and compactification literature.

---

## 2. Anomaly coefficient map

For a field-content vector

\[
x=(n_V,n_H,n_T)^T,
\]

define integer-normalized anomaly functionals

\[
R(x):=-n_V+n_T,
\tag{XXIV.5}
\]

\[
P_1(x):=-7n_V+7n_H+23n_T,
\tag{XXIV.6}
\]

\[
P_2(x):=4n_V-4n_H-116n_T.
\tag{XXIV.7}
\]

Then

\[
I_8^{VHT}
=\frac{R}{24}c_2(R)^2
+\frac{R}{48}c_2(R)p_1(T)
+\frac{P_1}{5760}p_1(T)^2
+\frac{P_2}{5760}p_2(T).
\tag{XXIV.8}
\]

The two \(SU(2)_R\) coefficients are proportional, so the independent coefficient map is

\[
\mathcal A:\mathbb Q^3\to\mathbb Q^3,
\qquad
x\mapsto(R,P_1,P_2).
\]

Its matrix is

\[
M_\mathcal A=
\begin{pmatrix}
-1&0&1\\
-7&7&23\\
4&-4&-116
\end{pmatrix}.
\tag{XXIV.9}
\]

Direct evaluation gives

\[
\boxed{\det M_\mathcal A=720\neq0.}
\tag{XXIV.10}
\]

Thus the three independent one-loop anomaly coefficients form a basis of the dual multiplet-count space. In particular,

\[
\boxed{\ker\mathcal A=\{0\}.}
\tag{XXIV.11}
\]

This is a **Derived here** linear-algebra statement about the established coefficient table. It does **not** mean a physical 6d theory cannot cancel anomalies: Green--Schwarz terms, a gravity multiplet, gauge representations and additional sectors can and do modify the full cancellation problem.

---

## 3. Threshold is not any individual anomaly coefficient

The threshold functional is

\[
K=(2,-1,2)\cdot x.
\]

It is not proportional to \(R\), \(P_1\), or \(P_2\). Their kernels are therefore different.

### Explicit threshold-canceling witness

Take

\[
(n_V,n_H,n_T)=(1,2,0).
\]

Then

\[
\boxed{K=2-2=0,}
\]

but

\[
R=-1,\qquad P_1=7,\qquad P_2=-4.
\]

Therefore

\[
\boxed{K=0\not\Rightarrow I_8^{VHT}=0.}
\tag{XXIV.12}
\]

### Explicit pure-gravitational witness in the opposite direction

For

\[
(n_V,n_H,n_T)=(1,1,0),
\]

we have

\[
P_1=P_2=0,
\]

so the pure \(p_1^2,p_2\) part cancels between one vector and one hyper, while

\[
\boxed{K=1\neq0}
\]

and \(R=-1\). Thus

\[
\boxed{P_1=P_2=0\not\Rightarrow K=0.}
\tag{XXIV.13}
\]

This is the first exact no-go of this model: **kinetic-threshold cancellation and pure-gravitational anomaly cancellation are inequivalent conditions.**

---

## 4. Pure-gravitational anomaly map

The pure-gravitational map

\[
\mathcal G:x\mapsto(P_1,P_2)
\]

has rank two. Its kernel is

\[
\boxed{\ker\mathcal G
=\operatorname{span}_{\mathbb Q}\{(1,1,0)\}.}
\tag{XXIV.14}
\]

The threshold kernel is the plane

\[
\boxed{
\ker K=\{(n_V,n_H,n_T):n_H=2n_V+2n_T\}.
}
\tag{XXIV.15}
\]

A convenient basis is

\[
(1,2,0),\qquad(0,2,1).
\]

The two kernels are different, and their intersection is trivial:

\[
\boxed{\ker K\cap\ker\mathcal G=\{0\}.}
\tag{XXIV.16}
\]

So no nonzero free vector/hyper/tensor content can simultaneously cancel the Model-XXIII threshold and the complete pure-gravitational one-loop polynomial.

---

## 5. The irreducible gravitational condition

The \(p_2(T)\) numerator can be written

\[
P_2=-4\bigl(n_H-n_V+29n_T\bigr).
\tag{XXIV.17}
\]

Hence for a matter sector by itself,

\[
P_2=0
\quad\Longleftrightarrow\quad
n_H-n_V+29n_T=0.
\tag{XXIV.18}
\]

When a six-dimensional \(\mathcal N=(1,0)\) gravity multiplet is included, the standard irreducible gravitational-anomaly condition becomes

\[
\boxed{n_H-n_V+29n_T=273,}
\tag{XXIV.19}
\]

under the usual supergravity hypotheses [AndrianopoliFerraraLledo2004]. This is an **Established** necessary condition; additional gauge, factorization and global consistency conditions remain.

Substituting (XXIV.19) into the threshold functional gives

\[
K=n_V+31n_T-273.
\tag{XXIV.20}
\]

Therefore the standard irreducible gravitational-anomaly condition does not fix the sign or vanishing of the finite threshold.

For example,

\[
(n_V,n_H,n_T)=(0,244,1)
\]

satisfies

\[
244+29=273,
\]

but

\[
\boxed{K=-242.}
\tag{XXIV.21}
\]

This is only an arithmetic witness to inequivalent constraints; it is not asserted to define a complete consistent supergravity model.

Conversely, imposing both (XXIV.19) and \(K=0\) gives

\[
\boxed{n_V+31n_T=273,\qquad n_H=2n_V+2n_T.}
\tag{XXIV.22}
\]

For example \((n_V,n_H,n_T)=(25,66,8)\) satisfies these two linear conditions. Again, this is not by itself a complete anomaly-free model.

---

## 6. A subtle positive result: full anomaly coefficients algebraically determine K

Because \(M_\mathcal A\) is invertible, any linear functional on the three-dimensional multiplet-count space can be expressed as a linear combination of \(R,P_1,P_2\). Solving for \(K\) gives

\[
\boxed{
K=-R-\frac{8}{45}P_1-\frac{11}{180}P_2.
}
\tag{XXIV.23}
\]

This identity is **Derived here** and is exact in the fixed free-multiplet convention.

It must be interpreted carefully. It does **not** identify the finite kinetic threshold with an anomaly polynomial. It only states that, once three independent anomaly coefficients have already reconstructed the three multiplet counts, every other linear field-content observable can be reconstructed algebraically as well.

Thus the correct conclusion is

\[
\boxed{
\text{coefficient-space reconstructibility}
\neq
\text{physical equality of observables}.
}
\tag{XXIV.24}
\]

---

## 7. Kernel geometry

The important hyperplanes are:

\[
\ker K:\quad 2n_V-n_H+2n_T=0,
\]

\[
\ker R:\quad n_T=n_V,
\]

\[
\ker P_2:\quad n_H-n_V+29n_T=0.
\]

Their pairwise intersections are one-dimensional. For example,

\[
\boxed{
\ker K\cap\ker P_2
=\operatorname{span}\{(-31,-60,1)\}
}
\tag{XXIV.25}
\]

as a rational vector space. There is no nonzero vector common to \(K,R,P_1,P_2\) because \(\mathcal A\) is invertible.

For physical nonnegative multiplet counts, positivity/integrality imposes further restrictions; the linear-algebra statements above are made over \(\mathbb Q\) unless otherwise stated.

---

## 8. What v0.24 establishes

Within the fixed Model-XXIII kinetic convention and the standard free-multiplet anomaly convention:

1. \(K\) is not proportional to any individual gravitational or R-symmetry anomaly coefficient.
2. \(K=0\) does not imply anomaly cancellation.
3. Pure-gravitational one-loop cancellation does not imply \(K=0\).
4. The standard supergravity irreducible gravitational condition does not determine \(K\).
5. The full three-component one-loop anomaly coefficient vector is invertible as a map from \((n_V,n_H,n_T)\), so it can algebraically reconstruct \(K\), but this is not a dynamical or geometric identification.

The threshold and anomaly polynomial therefore remain **distinct observables with different natural operations**, even though both are linear in the same microscopic field counts.

---

## 9. Scope and next gate

This model compares free-multiplet coefficients only. It does not include Green--Schwarz factorization data, gauge-representation anomaly coefficients, global self-dual anomalies, interacting SCFT contributions, or a gravity/horizon equation.

A natural next gate is to add the **Green--Schwarz/anomaly-lattice data** as a genuinely new structure and ask whether any independently motivated factorization condition constrains the finite automorphic threshold beyond mere field counting.

## References

- [OhmoriEtAl2014] K. Ohmori, H. Shimizu, Y. Tachikawa, K. Yonekura, *Anomaly Polynomial of General 6d SCFTs*, PTEP 2014 (2014) 103B07, arXiv:1408.5572. Appendix A is the coefficient source used here.
- [AndrianopoliFerraraLledo2004] L. Andrianopoli, S. Ferrara, M. A. Lledó, *No-scale D=5 supergravity from Scherk--Schwarz reduction of D=6 theories*, JHEP 06 (2004) 018, hep-th/0406018. Used only for the standard \(n_H-n_V+29n_T=273\) supergravity condition.
