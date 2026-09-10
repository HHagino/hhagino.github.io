# FCIG: Relative Invariantization

**Status:** exact diagonal-relative invariance + scalar-invariantization obstruction  
**Date:** 2026-09-10  
**Depends on:** [`cyclic-relative-trace.md`](cyclic-relative-trace.md), [`relative-character-weyl-closure.md`](relative-character-weyl-closure.md), [`coherent-state-discrete-series-closure.md`](coherent-state-discrete-series-closure.md), [`discrete-series-invariant-inversion.md`](discrete-series-invariant-inversion.md).

> **Claim firewall.** The FCIG deformation symbol `W` is not an Arthur truncation weight. The functional constructed below is a deformation-dependent relative orbital distribution, invariant under simultaneous conjugation of the hyperbolic element and transport of the symbol. It is not, for general `W`, a conjugation-invariant scalar distribution on `G`.

---

## 0. Setup

Let

\[
G=\operatorname{PSL}(2,\mathbb R),\qquad X=G/K,
\]

and let `gamma in G` be regular hyperbolic. Its centralizer is a split Cartan

\[
G_\gamma=A_\gamma\simeq\mathbb R.
\]

For the holomorphic discrete series `pi_q`, let

\[
m_{q,x}(g):=\langle e_x,\pi_q(g)e_x\rangle_{\rm transported}
\]

be the canonically transported coherent-state matrix coefficient. For the standard representative `a_L` and transverse Fermi coordinate `u`,

\[
m_{q,x_u}(a_L)=\kappa_{q,L}(u)
=\left(\cosh\frac L2-i\sinh\frac L2\,u\right)^{-2q}.
\]

Write

\[
d_q=C_q=\frac{2q-1}{4\pi}
\]

for the FCIG formal-degree/Bergman-density normalization.

---

# Part I. The relative orbital functional

## 1. Centralizer averaging

Let `W` be a smooth symbol on the cyclic quotient or, locally, a smooth symbol on `X` for which the integrals below converge. Define its normalized centralizer average by

\[
(\mathcal P_\gamma W)(A_\gamma x)
:=
\frac{1}{\operatorname{vol}(\Gamma_\gamma\backslash A_\gamma)}
\int_{\Gamma_\gamma\backslash A_\gamma}
W(ax)\,da,
\]

when a primitive lattice `Gamma_gamma=<delta>` is present. If no lattice is present, `mathcal P_gamma W` denotes an explicitly chosen `A_gamma`-invariant reduction whenever such a reduction exists.

For a primitive closed geodesic of length `ell`,

\[
\operatorname{vol}(\langle\delta\rangle\backslash A_\delta)=\ell
\]

under the Fermi-coordinate Haar convention used in the preceding notes.

---

## 2. Definition

Define the **FCIG relative hyperbolic orbital functional**

\[
\boxed{
\mathscr R_{q}(\gamma;W)
:=
 d_q
\Re\int_{A_\gamma\backslash X}
(\mathcal P_\gamma W)(\dot x)\,
 m_{q,x}(\gamma)\,d\dot x.
}
\tag{2.1}
\]

This is a scalar attached to the **pair** `(gamma,W)`.

For the standard representative `gamma=a_L`, Fermi disintegration gives

\[
A\backslash X\simeq\mathbb R_u,
\]

and therefore

\[
\boxed{
\mathscr R_q(a_L;W)
=
 d_q\Re\int_{\mathbb R}
\bar W(u)\kappa_{q,L}(u)\,du
=
 d_q\,\mathcal J_{q,L}[W].
}
\tag{2.2}
\]

For a primitive element `delta` of length `ell`, `L=m ell`, the cyclic trace is therefore

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=
\ell\,\mathscr R_q(\delta^m;W).
}
\tag{2.3}
\]

Thus the primitive centralizer length and the relative orbital functional factor exactly.

---

# Part II. Diagonal `G`-invariance

## 3. Transport action on symbols

For `h in G`, define

\[
(h\cdot W)(x):=W(h^{-1}x).
\tag{3.1}
\]

The centralizer transforms as

\[
A_{h\gamma h^{-1}}=hA_\gamma h^{-1}.
\tag{3.2}
\]

The coherent states are covariant, so after the canonical line-bundle phase is accounted for,

\[
\boxed{
m_{q,hx}(h\gamma h^{-1})
=m_{q,x}(\gamma).
}
\tag{3.3}
\]

The quotient measure is `G`-invariant.

---

## 4. Relative invariance theorem

Changing variables `y=hx` in (2.1) gives

\[
\boxed{
\mathscr R_q(h\gamma h^{-1};h\cdot W)
=
\mathscr R_q(\gamma;W).
}
\tag{4.1}
\]

Hence `mathscr R_q` is invariant under the diagonal action

\[
h:(\gamma,W)\longmapsto
(h\gamma h^{-1},h\cdot W).
\]

Equivalently,

\[
\boxed{
\mathscr R_q
\text{ descends to a scalar functional on the diagonal quotient }
(G_{\rm hyp}^{\rm reg}\times\mathcal W)/G.
}
\tag{4.2}
\]

This is the correct exact meaning of **relative invariantization** for FCIG.

It preserves the deformation symbol instead of averaging it away.

---

# Part III. Why ordinary scalar conjugation invariance fails

## 5. Fixed-symbol transformation law

If `W` is held fixed while `gamma` is conjugated, then in general

\[
\boxed{
\mathscr R_q(h\gamma h^{-1};W)
=
\mathscr R_q(\gamma;h^{-1}\cdot W)
\neq
\mathscr R_q(\gamma;W).
}
\tag{5.1}
\]

Therefore `gamma mapsto mathscr R_q(gamma;W)` is not a class function for a generic deformation symbol.

It becomes conjugation invariant only if `W` is itself invariant under the relevant `G`-action, which is not the FCIG situation of interest.

---

## 6. The tempting conjugacy average is generally not canonical

One could formally try

\[
\mathscr I_q(\gamma;W)
\stackrel{?}{=}
\int_{G/A_\gamma}
\mathscr R_q(h\gamma h^{-1};W)\,d\dot h.
\tag{6.1}
\]

But for a periodic or noncompactly lifted FCIG symbol there is no automatic absolute convergence, and no preferred regularization has been proved.

Thus (6.1) is **not** adopted as a definition.

This prevents an illegitimate jump from relative covariance to an ordinary Harish--Chandra invariant distribution.

---

# Part IV. Relation to standard orbital integrals

## 7. Standard orbital integral versus FCIG relative orbital

For a scalar test function `f on G`, the standard regular semisimple orbital integral is

\[
O_\gamma(f)
=
\int_{G_\gamma\backslash G}
f(x^{-1}\gamma x)\,d\dot x.
\tag{7.1}
\]

This is a distribution in the **test function `f`** and is conjugacy-invariant in `gamma` after the usual transport of measures.

By contrast, FCIG uses

\[
\mathscr R_q(\gamma;W)
=
d_q\Re\int_{A_\gamma\backslash X}
(\mathcal P_\gamma W)(\dot x)
m_{q,x}(\gamma)\,d\dot x.
\tag{7.2}
\]

The two objects share centralizer geometry, but their test data are typed differently:

\[
\boxed{
\begin{array}{rcl}
O_\gamma(f)&:& f\in C_c^\infty(G),\\
\mathscr R_q(\gamma;W)&:& W\text{ is a deformation symbol on }G/K.
\end{array}
}
\tag{7.3}
\]

The missing map is therefore an explicit intertwining lift

\[
\boxed{
\mathcal L_q:\mathcal W\longrightarrow\mathcal S(G)
\quad\text{such that}\quad
O_\gamma(\mathcal L_qW)
=\mathscr R_q(\gamma;W)
}
\tag{7.4}
\]

in a suitable Harish--Chandra Schwartz/test-function space.

Equation (7.4), not a formal conjugacy average, is the sharp next target.

---

# Part V. Relation to Arthur weighted orbital integrals

## 8. Important non-identification

Arthur's weighted orbital integrals and the explicit `SL(2,R)` calculations of Herb belong to the standard trace-formula framework. Their weights arise from the trace-formula/truncation structure and have their own invariantization and Fourier-transform theory.

An arbitrary FCIG deformation symbol `W` is **not** one of those weights by definition.

Therefore

\[
\boxed{
\text{FCIG deformation weight}
\neq
\text{Arthur weight}
}
\tag{8.1}
\]

unless a separate theorem constructs the identification.

What the standard theory does establish is that weighted and ordinary orbital distributions on real reductive groups admit nontrivial Fourier-transform/invariantization machinery, and in `SL(2,R)` the weighted orbital transforms can be computed explicitly. This makes that theory a model for the next gate, not a result that may simply be imported unchanged.

---

# Part VI. Weyl-normalized form

## 9. Relative Weyl normalization

Let

\[
\Delta(L)=2\sinh\frac L2.
\]

Define

\[
\widetilde{\mathscr R}_q(a_L;W)
:=
\Delta(L)\mathscr R_q(a_L;W).
\tag{9.1}
\]

Then

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=
\frac{\ell}{\Delta(L)}
\widetilde{\mathscr R}_q(a_L;W),
\qquad L=m\ell.
}
\tag{9.2}
\]

This has exactly the standard hyperbolic structural factor

\[
\boxed{
\text{primitive centralizer volume}
\times
\text{inverse Weyl discriminant}
\times
\text{Weyl-normalized numerator}.
}
\tag{9.3}
\]

No claim is made here that the numerator is already the Harish--Chandra transform of a scalar central test function.

---

# Part VII. Gate status

## 10. RI-A

The requested invariantization exists canonically at the level naturally selected by the deformation data:

\[
\boxed{
\mathscr R_q(h\gamma h^{-1};h\cdot W)
=
\mathscr R_q(\gamma;W).
}
\]

Therefore

\[
\boxed{\textbf{RI-A: PASS as a diagonal relative invariant distribution.}}
\]

The stronger scalar statement

\[
\gamma\mapsto\mathscr R_q(\gamma;W)
\quad\text{conjugation invariant for fixed }W
\]

is false in general.

---

## 11. RI-B — orbital-lift closure

The next falsifiable gate is:

> Construct an explicit `K`-type-sensitive lift `mathcal L_q W` on `G` such that its standard hyperbolic orbital integral equals the FCIG relative orbital functional.

Formally,

\[
\boxed{
O_{a_L}(\mathcal L_qW)
\stackrel{?}{=}
\mathscr R_q(a_L;W)
=d_q\mathcal J_{q,L}[W].
}
\tag{11.1}
\]

If such a lift belongs to a Harish--Chandra Schwartz class, standard invariant harmonic analysis can then be applied without changing the type of the object.

This is now the shortest legitimate route from the exact FCIG coherent-state kernel to a standard invariant orbital transform.

---

# Part VIII. Architecture after RI-A

The hyperbolic information channel is now

\[
\boxed{
\begin{aligned}
W
&\longrightarrow T_W^{(q)}\\
&\xleftrightarrow{\text{discrete-series Fourier block}}
F_{q,W}\\
&\longrightarrow
\mathscr R_q(\gamma;W)\\
&\xrightarrow{\text{diagonal quotient}}
[(\gamma,W)]_G\\
&\xrightarrow{\text{RI-B}}
O_\gamma(\mathcal L_qW)\\
&\xrightarrow{\text{HC/Arthur inversion}}
\text{invariant spectral data}.
\end{aligned}
}
\]

The diagonal-invariance arrow is now exact. The orbital-lift arrow remains open.

## Sources

- J. Arthur, *The characters of discrete series as orbital integrals*, Inventiones Mathematicae **32** (1976), 205--261.
- J. Arthur, *The invariant trace formula I. Local theory*, Journal of the American Mathematical Society **1** (1988), 323--383.
- J. Arthur, *A local trace formula*, Publications Mathématiques de l'IHÉS **73** (1991), 5--96.
- R. A. Herb, *Weighted orbital integrals on SL(2,R)*, Mémoires de la Société Mathématique de France, N.S. **15** (1984), 201--217.
- R. A. Herb, *An inversion formula for weighted orbital integrals*, Compositio Mathematica **47** (1982), 333--355.
