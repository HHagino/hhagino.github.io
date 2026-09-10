# FCIG: Discrete-Series Invariant Inversion

**Status:** exact Fourier-block computation + invariant-inversion firewall  
**Date:** 2026-09-10  
**Depends on:** [`coherent-state-discrete-series-closure.md`](coherent-state-discrete-series-closure.md), [`k-type-group-lift.md`](k-type-group-lift.md), [`relative-character-weyl-closure.md`](relative-character-weyl-closure.md), [`character-trace-firewall.md`](character-trace-firewall.md).

> **Claim firewall.** A coherent-state matrix coefficient belongs to a discrete-series block, but a deformation-weighted superposition of conjugates is generally noncentral. Its group Fourier transform can be computed exactly in the target discrete-series representation, while Harish--Chandra *invariant* inversion applies only after an invariantization/centralization step. We therefore separate the noncommutative Fourier block from the invariant orbital transform.

---

## 0. Setup

Let `G=PSL(2,R)` (or `SU(1,1)` in the disk model), let `K` be maximal compact, and let

\[
\pi_q=D^+_{2q-1}
\]

be the holomorphic discrete series in the FCIG normalization. Fix a normalized lowest-`K`-type vector `e_0`, and for `x=g_xK` write

\[
e_x=\pi_q(g_x)e_0,
\qquad
P_x:=|e_x\rangle\langle e_x|.
\]

The coherent-state coefficient is

\[
m_{q,x}(g):=\langle e_x,\pi_q(g)e_x\rangle.
\]

The exact disk calculation already gives, for the hyperbolic element `a_L`,

\[
\boxed{
m_{q,x_u}(a_L)_{\rm transported}
=\kappa_{q,L}(u)
=\left(\cosh\frac L2-iu\sinh\frac L2\right)^{-2q}.
}
\tag{0.1}
\]

---

# Part I. The noncommutative Fourier transform of one coherent coefficient

## 1. Schur orthogonality

Normalize Haar measure so that the formal degree of `pi_q` is

\[
d_q=C_q=\frac{2q-1}{4\pi},
\]

consistent with the FCIG hyperbolic-area convention and `vol(K)=1`.

For a discrete-series representation, Schur orthogonality gives

\[
\int_G
\langle u,\pi_q(g)v\rangle
\overline{\langle u',\pi_q(g)v'\rangle}\,dg
=
\frac1{d_q}
\langle u,u'\rangle
\langle v',v\rangle.
\tag{1.1}
\]

Use the group Fourier convention

\[
\widehat f(\sigma)
:=\int_G f(g)\,\sigma(g^{-1})\,dg.
\tag{1.2}
\]

Then for

\[
f_x(g)=m_{q,x}(g)=\langle e_x,\pi_q(g)e_x\rangle,
\]

matrix-element testing against arbitrary `u,v` gives

\[
\begin{aligned}
\langle u,\widehat f_x(\pi_q)v\rangle
&=\int_G
\langle e_x,\pi_q(g)e_x\rangle
\langle u,\pi_q(g^{-1})v\rangle\,dg\\
&=\int_G
\langle e_x,\pi_q(g)e_x\rangle
\overline{\langle v,\pi_q(g)u\rangle}\,dg\\
&=d_q^{-1}
\langle e_x,v\rangle
\langle u,e_x\rangle.
\end{aligned}
\]

Hence

\[
\boxed{
\widehat{m_{q,x}}(\pi_q)
=d_q^{-1}P_x.
}
\tag{1.3}
\]

By discrete-series orthogonality, its Plancherel support is the `pi_q` block (with the usual contragredient/convention caveat if the Fourier convention is reversed).

This is the exact DS Fourier statement that was missing from the previous note.

---

# Part II. Weighted coherent superposition = Toeplitz Fourier block

## 2. Define the group kernel

For `W` compactly supported (or sufficiently integrable) on `G/K`, define

\[
F_{q,W}(g)
:=d_q\int_{G/K}W(x)m_{q,x}(g)\,dA(x).
\tag{2.1}
\]

Interchanging the integrals in the weak sense and using (1.3),

\[
\begin{aligned}
\widehat F_{q,W}(\pi_q)
&=d_q\int_{G/K}W(x)
\widehat{m_{q,x}}(\pi_q)\,dA(x)\\
&=\int_{G/K}W(x)P_x\,dA(x).
\end{aligned}
\]

But the coherent-state Toeplitz resolution is

\[
T_W^{(q)}
=d_q\int_{G/K}W(x)P_x\,dA(x).
\tag{2.2}
\]

Therefore

\[
\boxed{
\widehat F_{q,W}(\pi_q)
=d_q^{-1}T_W^{(q)}.
}
\tag{2.3}
\]

Equivalently, if one absorbs the formal degree into the definition

\[
\mathcal F_{q,W}:=d_qF_{q,W},
\]

then

\[
\boxed{
\widehat{\mathcal F}_{q,W}(\pi_q)=T_W^{(q)}.
}
\tag{2.4}
\]

Thus the FCIG Toeplitz operator is literally the `D^+_{2q-1}` noncommutative Fourier coefficient of an explicit coherent-state group kernel.

This is a stronger and more precise statement than the earlier schematic arrow

\[
\text{Toeplitz symbol}\to\text{discrete-series block}.
\]

---

# Part III. Why this does not yet equal invariant inversion

## 3. Noncentrality

For general deformation data `W`,

\[
F_{q,W}(hgh^{-1})
\neq F_{q,W}(g).
\]

Indeed covariance gives

\[
m_{q,x}(hgh^{-1})=m_{q,h^{-1}x}(g),
\]

so

\[
F_{q,W}(hgh^{-1})
=F_{q,h\cdot W}(g),
\tag{3.1}
\]

with the natural transported symbol. Therefore `F_{q,W}` is equivariant in the pair `(g,W)`, not a class function of `g` for fixed noninvariant `W`.

Consequently one must not insert it directly into a scalar Harish--Chandra character inversion formula and pretend that its hyperbolic restriction is an invariant orbital transform.

This is the precise obstruction behind the old DS-B wording.

---

# Part IV. Centralization and the character

## 4. Compact conjugation average

A legitimate first invariantization is the `K`-conjugation average

\[
F_{q,W}^{K}(g)
:=\int_K F_{q,W}(kgk^{-1})\,dk.
\tag{4.1}
\]

On the Fourier side,

\[
\widehat{F_{q,W}^{K}}(\pi_q)
=
\int_K
\pi_q(k)\widehat F_{q,W}(\pi_q)\pi_q(k)^{-1}\,dk.
\tag{4.2}
\]

This projects the Toeplitz Fourier block onto its `K`-type diagonal. It is still not full conjugation invariance under `G`, but it already makes explicit which information survives a compact angular average.

Full invariantization is distributional: pairing against conjugation-invariant test functions collapses an operator-valued Fourier block to character data. For a suitable test function `f`, the spectral scalar is

\[
\Theta_{\pi_q}(f)=\operatorname{Tr}\pi_q(f),
\tag{4.3}
\]

whereas pointwise `Theta_{\pi_q}(a_L)` is the regular-set representative of the Harish--Chandra character distribution. These remain distinct from `m_{q,x}(a_L)`.

Arthur's 1976 theorem gives a rigorous standard-theory bridge in the opposite direction: discrete-series characters can be represented in terms of orbital integrals. This confirms that character/orbital conversion belongs to invariant harmonic analysis, not to a naive pointwise trace of `pi_q(a_L)`.

---

# Part V. Hyperbolic orbital restriction of the explicit Fourier kernel

## 5. FCIG classwise value

At a hyperbolic element `a_L`, (0.1) and (2.1) give

\[
\boxed{
F_{q,W}(a_L)
=d_q\int_{G/K}
W(x)\,m_{q,x}(a_L)\,dA(x).
}
\tag{5.1}

For periodic FCIG data the full integral is replaced by the primitive centralizer reduction. With `L=m\ell`,

\[
\boxed{
F^{\rm cyc}_{q,W}(a_L)
:=d_q\Re\int_{\langle\delta\rangle\backslash G/K}
W(x)m_{q,x}(a_L)dA(x)
=d_q\ell\,\mathcal J_{q,L}[W].
}
\tag{5.2}
\]

Thus the same explicit coherent kernel has two exact readings:

\[
\boxed{
\begin{array}{rcl}
\text{noncommutative Fourier side}&:&
\widehat F_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)},\\[1mm]
\text{cyclic hyperbolic side}&:&
F^{\rm cyc}_{q,W}(a_L)=d_q\ell\mathcal J_{q,L}[W].
\end{array}
}
\tag{5.3}
\]

This is the exact FCIG Fourier/orbital crosswalk at the **noninvariant coherent-kernel level**.

---

# Part VI. Weyl normalization

## 6. Separate the universal denominator

Set

\[
\Delta(L)=2\sinh\frac L2.
\]

The previous Weyl-closure note established

\[
\Theta_{2q-1}^{+}(a_{L/2})
=\Delta(L)^{-1}e^{-(q-\frac12)L}.
\tag{6.1}
\]

Define

\[
\widetilde{\mathcal J}_{q,L}[W]
:=\Delta(L)\mathcal J_{q,L}[W].
\]

Then

\[
\boxed{
F^{\rm cyc}_{q,W}(a_L)
=
\frac{d_q\ell}{\Delta(L)}
\widetilde{\mathcal J}_{q,L}[W].
}
\tag{6.2}
\]

This puts the cyclic coherent-state orbital and the discrete-series character into the same Weyl-normalized hyperbolic coordinate without identifying their numerators.

The remaining numerator comparison is a genuine invariant-transform question.

---

# Part VII. Gate result

## 7. DS-B

The previous DS-B asked for a group-level Fourier block and invariant inversion. These must be split.

### DS-B1 — explicit noncommutative Fourier block

From (2.3),

\[
\boxed{
\widehat F_{q,W}(D^+_{2q-1})
=d_q^{-1}T_W^{(q)}.
}
\]

Therefore

\[
\boxed{\textbf{DS-B1: PASS.}}
\]

### DS-B2 — invariantization / orbital-to-character inversion

For general deformation symbols the kernel is noncentral. A rigorous map from the cyclic weighted orbital functional to a scalar Harish--Chandra invariant distribution still requires an invariantization or relative trace formula.

Therefore

\[
\boxed{\textbf{DS-B2: OPEN / sharply typed.}}
\]

This is not a failure of the Fourier construction; it is the correct distinction between noncommutative Fourier inversion and invariant harmonic analysis.

---

# Part VIII. New frontier: relative invariantization

The shortest remaining target is no longer “find the Fourier block”; it is already explicit. The new gate is

\[
\boxed{
\textbf{RI-A — Relative Invariantization:}
\quad
\text{construct the canonical invariant/relative distribution associated to}
\quad
W\mapsto F_{q,W}^{\rm cyc}.
}
\]

The standard guideposts are:

1. Harish--Chandra invariant distributions and characters;
2. Arthur's realization of discrete-series characters through orbital integrals;
3. local/relative trace formulas when the inserted symbol is not central;
4. the FCIG centralizer quotient, which already supplies the primitive `A`-period and the factor `ell`.

The expected typed architecture is

\[
\boxed{
T_W^{(q)}
\xleftrightarrow{\ \text{noncommutative Fourier}\ }
F_{q,W}
\xrightarrow{\ \text{centralizer reduction}\ }
F_{q,W}^{\rm cyc}(a_L)
\xrightarrow{\ \text{relative invariantization}\ }
I_{q,W}(a_L)
\xleftrightarrow{\ \text{HC/Arthur}\ }
\text{invariant spectral distribution}.
}
\]

The first two arrows are now exact. The third is the remaining representation-theoretic closure problem.

## Sources

- James Arthur, *The Characters of Discrete Series as Orbital Integrals*, Inventiones Mathematicae **32** (1976), 205--261.
- James Arthur, *A Local Trace Formula*, Publications Mathématiques de l'IHÉS **73** (1991), 5--96.
- Harish--Chandra, discrete-series character and Plancherel theory for real reductive groups.
- Jingzhou Sun, *On the Bergman Kernel of complex hyperbolic manifolds*, arXiv:2511.16240v3 (2026).
- FCIG exact coherent-state derivation: [`coherent-state-discrete-series-closure.md`](coherent-state-discrete-series-closure.md).
