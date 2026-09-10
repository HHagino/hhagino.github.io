# FCIG: K-Type Group Lift of the Cyclic Bergman Orbital

**Status:** exact group-level kernel lift + RC-B partial pass; discrete-series transform closure remains open  
**Date:** 2026-09-10  
**Depends on:** [`cyclic-relative-trace.md`](cyclic-relative-trace.md), [`relative-character-weyl-closure.md`](relative-character-weyl-closure.md), [`disk-transported-bergman.md`](disk-transported-bergman.md), [`character-trace-firewall.md`](character-trace-firewall.md).

> **Claim firewall.** The lift constructed below is an explicit `K`-type-covariant kernel on `G=PSL(2,R)` whose hyperbolic cyclic diagonal reproduces the FCIG orbital. This is not yet a proof that its invariant group Fourier transform is a pure discrete-series character transform. Ordinary spherical/horospherical Abel transforms are insufficient for that purpose: they can miss the discrete-series sector. The remaining problem is therefore a `K`-type-sensitive discrete-series transform problem.

---

## 0. Result

Let

\[
G=PSL(2,\mathbb R),\qquad K=PSO(2),\qquad X=G/K\simeq\mathbb H.
\]

Let `L_q=K_X^q` be the `q`-canonical homogeneous line bundle. In a unitary local frame, let

\[
\mathcal C_q(x,y)
\]

be the scalar Bergman coherent kernel, normalized so that on the disk

\[
\mathcal C_q(z,w)
=C_q\left[
\frac{\sqrt{(1-|z|^2)(1-|w|^2)}}{1-z\bar w}
\right]^{2q},
\qquad C_q=\frac{2q-1}{4\pi}.
\]

For a real geometric symbol `W` on `X`, define the group-level transported Toeplitz kernel

\[
\boxed{
\mathscr F_{q,W}(g;x)
:=W(x)\,\mathcal T_q(g;x),
}
\tag{0.1}
\]

where `\mathcal T_q(g;x)` is the scalar obtained by composing the off-diagonal Bergman kernel from `x` to `gx` with the canonical unitary transport in `L_q` back from `gx` to `x`.

Equivalently, before choosing a frame,

\[
\boxed{
\mathcal T_q(g;x)
:=\operatorname{tr}_{(L_q)_x}
\bigl(U_{g,x}^{-1}\circ P_q(gx,x)\bigr).
}
\tag{0.2}
\]

Because the fiber is one-dimensional, this is a scalar and is independent of the chosen unitary frame.

For the hyperbolic element `a_L` and the normal coordinate `u` used in the disk/cylinder notes,

\[
\boxed{
\mathcal T_q(a_L;u)
=C_q\kappa_{q,L}(u),
}
\tag{0.3}
\]

with

\[
\kappa_{q,L}(u)
=\left(\cosh\frac L2-iu\sinh\frac L2\right)^{-2q}.
\]

Thus the FCIG cyclic relative trace is exactly the centralizer-reduced diagonal of the group-level kernel (0.1):

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=
\Re\int_{\langle\delta\rangle\backslash X}
\mathscr F_{q,W}(\delta^m;x)dA(x).
}
\tag{0.4}
\]

This supplies the missing **group variable** without replacing the line-bundle kernel by a spherical scalar function.

---

# Part I. Why the lift must retain a K-type

## 1. Homogeneous line-bundle realization

A section of `L_q` may be represented on `G` by a function with a fixed right-`K` covariance

\[
F(gk_\theta)=\chi_q(k_\theta)^{-1}F(g),
\tag{1.1}
\]

where `\chi_q` is the character determined by the `q`-canonical fiber convention. The exact integer appearing in the exponent depends on whether one writes the action in `PSL(2,R)`, `SL(2,R)`, or `SU(1,1)` coordinates; the geometric bundle definition is invariant and is therefore primary here.

Consequently the Bergman projection is not naturally encoded by a bi-`K`-invariant scalar kernel. It belongs to a fixed `K`-type block.

This matters because the ordinary spherical Abel transform probes the class-one principal-series sector. FCIG instead starts from the holomorphic discrete-series Bergman projector.

Hence the correct transform cannot discard the bundle `K`-type before harmonic analysis.

---

## 2. Covariance of the transported kernel

Let `k_1,k_2 in K`. Equivariance of the Bergman kernel and the unitary line-bundle action imply a covariance law of the form

\[
\mathcal T_q(k_1gk_2;k_1x)
=\chi_q(k_1,k_2)\,\mathcal T_q(g;x),
\tag{2.1}
\]

with the phase fixed by the homogeneous line-bundle convention. After composing source and target fibers as in (0.2), all frame-dependent phases cancel.

The important invariant statement is therefore not that `\mathcal T_q` is spherical, but that it is the scalar contraction of a `K`-type-covariant bundle kernel.

This is exactly the information lost by a premature projection to `C_c(G//K)`.

---

# Part II. Centralizer disintegration

## 3. From the cyclic quotient to the split Cartan quotient

Let `delta` be primitive with length `ell`, and identify its connected centralizer with the split Cartan `A`. The cyclic quotient is

\[
\langle\delta\rangle\backslash X
=\langle\delta\rangle\backslash G/K.
\]

Disintegrating first along the compact longitudinal quotient

\[
\langle\delta\rangle\backslash A\simeq\mathbb R/\ell\mathbb Z
\]

gives the centralizer period

\[
(\mathcal P_\delta W)(\dot x)
:=\frac1\ell\int_{\langle\delta\rangle\backslash A}W(ax)da.
\tag{3.1}
\]

Then

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=C_q\ell\,
\Re\int_{A\backslash X}
(\mathcal P_\delta W)(\dot x)
\kappa_{q,m\ell}(\dot x)d\dot x.
}
\tag{3.2}
\]

In Fermi coordinates `A\backslash X` is represented by the transverse coordinate `u`, and (3.2) becomes exactly

\[
C_q\ell\,
\Re\int_{\mathbb R}\overline W(u)\kappa_{q,m\ell}(u)du.
\]

Thus the group lift and the previous cylinder formula agree identically.

---

# Part III. Weyl normalization

## 4. Hyperbolic discriminant

For

\[
a_L=\operatorname{diag}(e^{L/2},e^{-L/2}),
\]

the adjoint eigenvalues on `\mathfrak g/\mathfrak a` are `e^L` and `e^{-L}`. Hence

\[
\boxed{
\Delta(L):=|D(a_L)|^{1/2}=2\sinh\frac L2.
}
\tag{4.1}
\]

Define the Weyl-normalized FCIG numerator

\[
\boxed{
\widetilde{\mathcal J}_{q,L}[W]
:=\Delta(L)\mathcal J_{q,L}[W].
}
\tag{4.2}
\]

Then

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=
\frac{C_q\ell}{\Delta(L)}
\widetilde{\mathcal J}_{q,L}[W],
\qquad L=m\ell.
}
\tag{4.3}
\]

This has exactly the geometric shape required for comparison with hyperbolic orbital/character formulas: primitive centralizer volume times inverse Weyl discriminant times a numerator.

For the holomorphic discrete series in the repo convention,

\[
\Theta_{2q-1}^{+}(a_{L/2})
=\frac{e^{-qL}}{1-e^{-L}}
=\frac{e^{-(q-1/2)L}}{\Delta(L)}.
\tag{4.4}
\]

Therefore the denominator has already closed. The remaining transform problem concerns the numerator.

---

# Part IV. The correct transform target

## 5. Why the ordinary Abel transform is not enough

For bi-`K`-invariant functions, the spherical Abel transform converts the spherical transform into an ordinary Fourier transform on `A`. That is the correct tool for the class-one principal series.

But the FCIG kernel is generated by the Bergman projector onto a holomorphic discrete-series block. A transform that first replaces the kernel by its spherical `K`-fixed part can annihilate precisely the sector we need.

Thus the correct RC-B target is a **fixed-K-type group Fourier transform**, not the spherical Abel transform.

Concretely, if `\pi` is an irreducible unitary representation, the group Fourier transform of a suitable group kernel is operator-valued:

\[
\widehat F(\pi)=\int_G F(g)\pi(g)dg.
\tag{5.1}
\]

For a kernel with prescribed left/right `K` covariance, only the corresponding `K`-type matrix block survives. The FCIG problem is to construct the scalar or operator-valued test kernel associated to (0.1) so that its `D_{2q-1}^{+}` block reproduces the Weyl-normalized numerator (4.2).

This is the legitimate place for the holomorphic discrete series to enter.

---

## 6. Proposed typed transform

Let `p_q` denote the projection onto the relevant one-dimensional lowest `K`-type line inside the holomorphic discrete series. For a sufficiently regular group-level lift `F_{q,W}`, define the `q`-type Fourier coefficient

\[
\boxed{
\mathscr H_q[F_{q,W}]
:=p_q\left(\int_G F_{q,W}(g)\pi_q(g)dg\right)p_q.
}
\tag{6.1}
\]

Because the projected line is one-dimensional, this block is scalar after a choice of unit vector.

The **RC-B conjecture** is not that (6.1) equals the pointwise cyclic trace. Rather, it is that there exists a canonical smoothing/test-kernel completion of the geometric lift (0.1) for which the hyperbolic orbital transform and the `D_{2q-1}^{+}` Fourier block are related by the standard invariant inversion machinery, with

\[
\widetilde{\mathcal J}_{q,L}[W]
\]

as the hyperbolic numerator.

This distinction preserves the character/trace firewall.

---

# Part V. A stronger obstruction and a sharper route

## 7. Discrete series is invisible to naive horospherical inversion

The ordinary horospherical/Radon route on a real semisimple group is tailored to the maximally continuous series. For `SL(2,R)`, the discrete-series component is a genuine separate summand of harmonic analysis.

Therefore an attempted proof

\[
\text{FCIG cylinder}
\to\text{spherical Abel transform}
\to\text{ordinary Fourier transform on }A
\to D^+_{2q-1}
\]

is structurally wrong.

The correct route is

\[
\boxed{
\text{bundle Bergman kernel}
\to
\text{fixed }K\text{-type group kernel}
\to
\text{discrete-series Fourier block}
\to
\text{relative/orbital inversion}.
}
\tag{7.1}
\]

This is not merely a technical refinement; it changes which harmonic-analysis transform is allowed.

---

# Part VI. Gate status

## 8. RC-B

The missing group variable has now been supplied by the intrinsic transported Bergman kernel (0.2), and its restriction to every hyperbolic element reproduces the exact Sun kernel. The cyclic quotient and Weyl normalization are compatible with this lift.

Therefore:

\[
\boxed{\textbf{RC-B: PARTIAL PASS.}}
\]

What is still missing is a theorem identifying an appropriate regularized/smoothing completion of `\mathscr F_{q,W}` with a standard test object in the `SL(2,R)` Schwartz algebra and computing its discrete-series Fourier block.

---

## 9. New gate: DS-A

The next gate is now precise.

\[
\boxed{
\textbf{DS-A — Discrete-Series K-Type Transform Closure}
}
\]

Construct a test kernel `F_{q,W}` with the same hyperbolic transported diagonal as (0.1), lying in a function/distribution space on which Harish--Chandra Fourier inversion is valid, and prove that

1. its relevant `K`-type block is supported on / detects `D^+_{2q-1}`;
2. its hyperbolic orbital transform is `C_q ell J_{q,L}[W]` after centralizer periodization;
3. Weyl normalization gives `\widetilde{\mathcal J}_{q,L}[W]`;
4. the discrete-series character denominator is supplied solely by `\Delta(L)^{-1}`.

This is now a falsifiable representation-theoretic theorem rather than a character analogy.

---

# References / transform firewall

- Harish-Chandra, *Discrete Series for Semisimple Lie Groups II: Explicit Determination of the Characters*, Acta Math. 116 (1966), 1--111.
- James Arthur, *The characters of discrete series as orbital integrals*, Invent. Math. 32 (1976), 205--261.
- James Arthur, Rebecca A. Herb, Paul J. Sally Jr., *The Fourier transform of weighted orbital integrals on SL(2,R)*, in *The Selberg Trace Formula and Related Topics*, Contemp. Math. 53 (1986).
- R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS 76 (1988), no. 393.
- S. Helgason, *Orbital integrals, symmetric Fourier analysis, and eigenspace representations*, in *Representation Theory and Automorphic Forms*, Proc. Sympos. Pure Math. 61 (1997).
- R. Camporesi's homogeneous-vector-bundle Fourier-transform framework is the appropriate neighboring technology for retaining nontrivial `K`-types.

The role of these references is structural: they justify keeping orbital integrals, distribution characters, fixed `K`-types, and group Fourier transforms as distinct typed operations. No claim of a pre-existing FCIG identity is made.
