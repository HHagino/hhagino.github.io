# FCIG: Relative Character and Weyl-Denominator Closure

**Status:** exact centralizer disintegration + exact Weyl-discriminant factorization; relative-character identification partial  
**Date:** 2026-09-10  
**Depends on:** [`cyclic-relative-trace.md`](cyclic-relative-trace.md), [`centralizer-spectral-window.md`](centralizer-spectral-window.md), [`character-trace-firewall.md`](character-trace-firewall.md), [`discrete-series-selberg-crosswalk.md`](discrete-series-selberg-crosswalk.md).

> **Claim firewall.** The centralizer disintegration and the `PSL(2,R)` Weyl-discriminant computation below are exact. The resulting FCIG functional has the **type** of a periodized split-Cartan orbital distribution after reduction by `K`, but this note does not claim that a standard named relative character theorem has already been proved for the noncentral Toeplitz symbol. Ordinary character values, ordinary traces, orbital integrals, and the cyclic relative trace remain distinct objects.

---

## 0. Result in one page

Let

\[
G=PSL(2,\mathbb R),\qquad K=PSO(2),\qquad \mathbb H\simeq G/K,
\]

and let the positive split Cartan be

\[
A=\{a_L:L\in\mathbb R\},\qquad
 a_L=\begin{bmatrix}e^{L/2}&0\\0&e^{-L/2}\end{bmatrix}.
\]

Fix a primitive hyperbolic element `delta` of length `ell`, conjugated to `a_ell`, and put `L=m ell`.

The cyclic quotient is

\[
Y_\delta=\langle\delta\rangle\backslash G/K.
\]

Because `A` translates the longitudinal Fermi coordinate and leaves the transverse coordinate fixed, the cyclic trace disintegrates exactly as

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=C_q\ell\int_{A\backslash G/K}
(\mathcal P_\delta W)(\dot x)\,
\Re\kappa_{q,L}(\dot x)\,d\dot x,
}
\tag{0.1}
\]

where

\[
\boxed{
(\mathcal P_\delta W)(\dot x)
:=\frac1\ell\int_{\langle\delta\rangle\backslash A}
W(ax)\,da
}
\tag{0.2}
\]

is the primitive centralizer-period average. In Fermi coordinates, `A\G/K` is parametrized by `u in R` and `d dot x=du`, so (0.1) is exactly the previously derived cylinder formula.

Thus FCIG is not initially a standard `A\G` orbital integral. It is a **centralizer-lattice period followed by a K-reduced split-Cartan orbital pairing**.

Now compute the Weyl discriminant. On the two root spaces of `g/a`,

\[
\operatorname{Ad}(a_L)=e^{\pm L}.
\]

Hence

\[
\boxed{
|D(a_L)|^{1/2}
:=\left|\det(1-\operatorname{Ad}(a_L))_{\mathfrak g/\mathfrak a}\right|^{1/2}
=2\sinh\frac{|L|}{2}.
}
\tag{0.3}
\]

For `L>0`, write

\[
\Delta(L):=2\sinh\frac L2.
\]

The holomorphic discrete-series character used in FCIG therefore factorizes exactly as

\[
\boxed{
\Theta_{2q-1}^{+}(a_{L/2})
=\frac{e^{-qL}}{1-e^{-L}}
=\frac{e^{-(q-\frac12)L}}{\Delta(L)}.
}
\tag{0.4}
\]

Equivalently,

\[
\boxed{
\Delta(L)\Theta_{2q-1}^{+}(a_{L/2})
=e^{-(q-\frac12)L}.
}
\tag{0.5}
\]

This is the exact correction to the old descendant-ladder heuristic: the denominator is the inverse square root of the hyperbolic Weyl discriminant, while the numerator is the Weyl-shifted exponential.

The same factor occurs on the geometric side of the scalar Selberg trace formula, whose hyperbolic term has the standard shape

\[
\frac{\ell(\gamma_0)}{2\sinh(\ell(\gamma)/2)}\,g(\ell(\gamma)).
\tag{0.6}
\]

Therefore the denominator match is structural:

\[
\boxed{
\text{Harish--Chandra discrete-series character}
\quad\text{and}\quad
\text{Selberg hyperbolic orbital term}
\quad\text{carry the same }\Delta(L)^{-1}.
}
\tag{0.7}
\]

---

# Part I. Exact centralizer disintegration

## 1. Fermi realization of the split Cartan

Conjugate the primitive deck transformation to

\[
z\mapsto e^\ell z
\]

on the upper half-plane. Write

\[
z=e^{t+i\theta},\qquad t\in\mathbb R,\quad 0<\theta<\pi.
\]

Then

\[
ds^2=\frac{dt^2+d\theta^2}{\sin^2\theta}.
\]

With

\[
u=\cot\theta=\sinh r,\]

this becomes

\[
 ds^2=\frac{du^2}{1+u^2}+(1+u^2)dt^2,
\qquad dA=dt\,du.
\tag{1.1}
\]

The split Cartan acts by

\[
a_s:(t,u)\mapsto(t+s,u).
\tag{1.2}
\]

Therefore

\[
A\backslash G/K\simeq\mathbb R_u.
\tag{1.3}
\]

The lattice `\langle delta\rangle` acts by `t -> t+ell`, hence

\[
\langle\delta\rangle\backslash A\simeq\mathbb R/\ell\mathbb Z.
\tag{1.4}
\]

---

## 2. Disintegration theorem

The transported Bergman diagonal for `delta^m` is

\[
\mathcal K_q(\delta^m;t,u;t,u)
=C_q\kappa_{q,L}(u),
\qquad L=m\ell,
\tag{2.1}
\]

so it is invariant under the full `A`-translation in `t`.

For every integrable cyclic symbol `W`, Fubini gives

\[
\begin{aligned}
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
&=C_q\Re\int_0^\ell dt\int_{\mathbb R}du\,
W(t,u)\kappa_{q,L}(u)\\
&=C_q\ell\Re\int_{\mathbb R}du\,
\left[\frac1\ell\int_0^\ell W(t,u)dt\right]\kappa_{q,L}(u).
\end{aligned}
\tag{2.2}
\]

This proves (0.1)-(0.2).

The correct quotient architecture is therefore

\[
\boxed{
\langle\delta\rangle\backslash G/K
\xrightarrow{\text{period along }\langle\delta\rangle\backslash A}
A\backslash G/K.
}
\tag{2.3}
\]

It is not legitimate to erase the first step and call the original cyclic quotient `A\G`.

---

# Part II. Relation to standard orbital geometry

## 3. Standard hyperbolic orbital integral

For a regular hyperbolic `a_L`, its connected centralizer in `G` is `A`. A standard group orbital integral of a test function `f` has the form

\[
O_{a_L}(f)
=\int_{A\backslash G}f(x^{-1}a_Lx)d\dot x.
\tag{3.1}
\]

The FCIG functional differs in two ways:

1. it starts from a geometric symbol on `G/K`, not a central test function on `G`;
2. the primitive lattice period in `\langle\delta\rangle\backslash A` is retained and produces the factor `ell`.

After the period average, however, its remaining transverse integration is the `K`-reduced version of the same split-Cartan conjugacy geometry. Thus the safe typing is

\[
\boxed{
\text{FCIG cyclic trace}
=\text{primitive }A\text{-period}
\times
\text{K-reduced hyperbolic orbital pairing}.
}
\tag{3.2}
\]

This is the correct entry point for relative harmonic analysis.

---

# Part III. Weyl discriminant from first principles

## 4. Root-space calculation

Take the standard `sl_2` basis

\[
H=\begin{bmatrix}1&0\\0&-1\end{bmatrix},\quad
E=\begin{bmatrix}0&1\\0&0\end{bmatrix},\quad
F=\begin{bmatrix}0&0\\1&0\end{bmatrix}.
\]

For

\[
a_L=\exp\left(\frac L2H\right),
\]

one has

\[
\operatorname{Ad}(a_L)E=e^LE,
\qquad
\operatorname{Ad}(a_L)F=e^{-L}F.
\tag{4.1}
\]

Since `g/a` is spanned by `E,F`,

\[
\begin{aligned}
D(a_L)
&=(1-e^L)(1-e^{-L})\\
&=2-e^L-e^{-L}\\
&=-4\sinh^2\frac L2.
\end{aligned}
\tag{4.2}
\]

Therefore

\[
\boxed{|D(a_L)|^{1/2}=2\sinh\frac{|L|}{2}.}
\tag{4.3}
\]

No representation-theoretic assumption enters this calculation.

---

# Part IV. Character denominator closure

## 5. Exact factorization

The FCIG discrete-series crosswalk uses

\[
\Theta_{2q-1}^{+}(a_{L/2})
=\frac{e^{-qL}}{1-e^{-L}},\qquad L>0.
\tag{5.1}
\]

But

\[
1-e^{-L}=2e^{-L/2}\sinh\frac L2,
\]

so

\[
\Theta_{2q-1}^{+}(a_{L/2})
=\frac{e^{-(q-1/2)L}}{2\sinh(L/2)}.
\tag{5.2}
\]

Using (4.3),

\[
\boxed{
\Theta_{2q-1}^{+}(a_{L/2})
=|D(a_L)|^{-1/2}e^{-(q-1/2)L}.
}
\tag{5.3}
\]

Hence the geometric-series identity

\[
\frac1{1-e^{-L}}=\sum_{k\ge0}e^{-kL}
\]

is algebraically true but conceptually secondary. The primary invariant factorization is

\[
\boxed{
\text{character}
=\text{Weyl-discriminant}^{-1/2}
\times\text{Weyl-shifted exponential}.
}
\tag{5.4}
\]

This closes the denominator question raised by the character-trace firewall.

---

# Part V. Selberg comparison

## 6. The same denominator on the geometric side

For the scalar Selberg trace formula on a compact hyperbolic surface, the contribution of a closed geodesic `gamma=gamma_0^m` has the standard form

\[
\boxed{
\frac{\ell(\gamma_0)}{2\sinh(\ell(\gamma)/2)}
\,g(\ell(\gamma)).
}
\tag{6.1}
\]

Thus

\[
\frac1{2\sinh(L/2)}=|D(a_L)|^{-1/2}
\tag{6.2}
\]

is simultaneously the hyperbolic Weyl factor in the character formula and the universal Jacobian factor multiplying the Selberg length transform.

What differs between theories is the numerator / transformed test object:

\[
\boxed{
\begin{array}{rcl}
\text{discrete-series character} &:& e^{-(q-1/2)L},\\[1mm]
\text{scalar Selberg orbital} &:& g(L),\\[1mm]
\text{FCIG Toeplitz orbital} &:& \Delta(L)\,\mathcal J_{q,L}[W]\ \text{after Weyl normalization}.
\end{array}
}
\tag{6.3}
\]

Therefore FCIG should not try to manufacture the denominator from its deformation modes. The denominator belongs to the conjugacy-class measure / Weyl normalization; the deformation information belongs in the numerator.

This is the decisive separation.

---

# Part VI. Weyl-normalized FCIG response

## 7. Definition

Define the Weyl-normalized class response

\[
\boxed{
\widetilde{\mathcal J}_{q,L}[W]
:=\Delta(L)\mathcal J_{q,L}[W],
\qquad
\Delta(L)=2\sinh\frac L2.
}
\tag{7.1}
\]

Then the oriented cyclic trace becomes

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=\frac{C_q\ell}{\Delta(L)}
\widetilde{\mathcal J}_{q,L}[W].
}
\tag{7.2}
\]

This puts FCIG in exactly the same **denominator-normalized shape** as the Selberg hyperbolic term and the discrete-series character:

\[
\boxed{
\frac{\ell}{\Delta(L)}\times
\text{Weyl-normalized numerator}.
}
\tag{7.3}
\]

For the character the numerator is `exp[-(q-1/2)L]`; for FCIG it is the deformation-dependent function `C_q widetilde J_{q,L}[W]`.

This does **not** assert equality of the numerators. It identifies the exact invariant denominator common to the three constructions.

---

# Part VII. Gate status

## 8. RC-A — relative-distribution identification

**PARTIAL PASS.** The cyclic functional has now been canonically disintegrated into

\[
\boxed{
\text{primitive centralizer period}
\times
\text{K-reduced split-Cartan orbital pairing}.
}
\]

What remains is to package the noncentral Toeplitz symbol into a standard distribution on `G` (or a relative distribution on the appropriate homogeneous space) without losing the bundle `K`-type.

## 9. RC-B — invariant transform

**OPEN.** Construct the group-level test kernel corresponding to the Weyl-normalized numerator

\[
\widetilde{\mathcal J}_{q,L}[W]
\]

and compute its invariant Fourier/Harish--Chandra transform.

## 10. RC-C — Weyl denominator

**PASS.** The denominator is no longer conjectural:

\[
\boxed{
\frac1{1-e^{-L}}
=\frac{e^{L/2}}{\Delta(L)},
\qquad
\Delta(L)=|D(a_L)|^{1/2}=2\sinh\frac L2.
}
\]

The factor arises from the hyperbolic Weyl discriminant, not from an alleged trace-class descendant ladder.

---

# Part VIII. New frontier

The corrected nonperturbative chain is now

\[
\boxed{
\begin{aligned}
|\mu|^2
&\xrightarrow{(1+\square_0)^{-1}} f_\mu\\
&\xrightarrow{P_qM_{f_\mu}P_q}T_{f_\mu}^{(q)}\\
&\xrightarrow{\langle\delta\rangle\backslash A\text{ period}}
\text{cyclic relative trace}\\
&\xrightarrow{\times\Delta(L)}
\text{Weyl-normalized FCIG numerator}\\
&\xrightarrow{\text{group-level lift}}
\text{Harish--Chandra/Selberg spectral transform}.
\end{aligned}
}
\]

The remaining hard problem is therefore very specific:

\[
\boxed{
\textbf{Group-Level Lift Problem:}
\quad
\text{construct a }K\text{-type-sensitive kernel/distribution on }G
\text{ whose hyperbolic orbital transform equals }
\widetilde{\mathcal J}_{q,L}[W].
}
\]

Once that is done, the Weyl denominator no longer needs to be discovered: it is already fixed by the group geometry.

---

## References

- Harish-Chandra, *Discrete Series for Semisimple Lie Groups II: Explicit Determination of the Characters*, Acta Mathematica **116** (1966), 1--111.
- Dennis A. Hejhal, *The Selberg Trace Formula for PSL(2,R), Vol. I*, Lecture Notes in Mathematics 548, Springer, 1976.
- Standard scalar Selberg hyperbolic term: `ell(gamma_0)/(2 sinh(ell(gamma)/2))` times the length-side test transform.
- See also the existing FCIG bibliography and the source audit in `character-trace-firewall.md`.
