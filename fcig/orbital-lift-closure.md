# FCIG: Orbital-Lift Closure

**Status:** RI-B constructive reduction + exact orbital right-inverse on the hyperbolic Cartan; full K-type/Toeplitz compatibility remains open  
**Date:** 2026-09-10  
**Depends on:** `relative-invariantization.md`, `discrete-series-invariant-inversion.md`, `coherent-state-discrete-series-closure.md`, `relative-character-weyl-closure.md`.

> **Claim firewall.** This note does not identify the FCIG symbol with an Arthur weight, and it does not claim that a scalar class function can retain the full noncentral Toeplitz operator. The exact result below is an orbital-lift theorem for the scalar hyperbolic response. Compatibility with the fixed K-type Fourier block is a stronger problem.

---

## 0. Problem

For `G=PSL(2,R)` and a regular hyperbolic element `a_L`, define the ordinary orbital integral

\[
O_{a_L}(f):=\int_{A\backslash G} f(x^{-1}a_Lx)\,d\dot x,
\]

with `A=G_{a_L}` and a fixed quotient-measure convention.

The FCIG relative response from the previous note is

\[
\mathscr R_q(a_L;W)=d_q\,\mathcal J_{q,L}[W].
\]

The RI-B question is whether one can construct a test function `\mathcal L_qW` whose ordinary hyperbolic orbital integral equals this response.

---

## 1. Weyl-normalized target

Let

\[
\Delta(L)=2\sinh(L/2),\qquad L>0.
\]

Set

\[
R_{q,W}(L):=d_q\mathcal J_{q,L}[W],
\qquad
H_{q,W}(L):=\Delta(L)R_{q,W}(L).
\]

The earlier Weyl-denominator calculation showed that `\Delta(L)^{-1}` is exactly the invariant hyperbolic denominator appearing in both the Harish--Chandra character formula and the scalar Selberg hyperbolic term. Hence `H_{q,W}` is the natural Weyl-normalized numerator.

For compactly supported/Schwartz deformation data we assume the resulting `H_{q,W}` belongs to the corresponding admissible even test class on the split Cartan. Periodic global FCIG data require the already-defined primitive-centralizer reduction before this step.

---

## 2. Orbital transform and its right inverse

Harish--Chandra's rank-one orbital analysis for `SL(2,R)` identifies the Weyl-normalized hyperbolic orbital transform

\[
\mathcal O:f\longmapsto \left[L\mapsto \Delta(L)O_{a_L}(f)\right]
\]

with a rank-one Abel/orbital transform. On the appropriate compactly supported smooth or Schwartz test spaces this transform has a continuous right inverse after the usual Weyl/parity conditions are imposed.

Denote one such right inverse by

\[
\mathcal O^{-1}_{\rm hyp}.
\]

Define the **scalar FCIG orbital lift** by

\[
\boxed{
\mathcal L_q^{\rm orb}W
:=\mathcal O^{-1}_{\rm hyp}[H_{q,W}].
}
\tag{2.1}
\]

Then, by construction and the inversion theorem,

\[
\Delta(L)O_{a_L}(\mathcal L_q^{\rm orb}W)
=H_{q,W}(L)
=\Delta(L)d_q\mathcal J_{q,L}[W].
\]

For `L>0`, division by `\Delta(L)` gives

\[
\boxed{
O_{a_L}(\mathcal L_q^{\rm orb}W)
=d_q\mathcal J_{q,L}[W]
=\mathscr R_q(a_L;W).
}
\tag{2.2}
\]

Thus the scalar relative FCIG response has an ordinary-orbital-integral representative.

---

## 3. What is exact and what is noncanonical

Equation (2.2) is exact once the Haar/quotient measures and the standard orbital-transform normalization are fixed. The lift itself need not be unique: any function in the kernel of the hyperbolic orbital transform may be added without changing (2.2).

Therefore the canonical object is not an individual group test function but the quotient class

\[
\boxed{
[\mathcal L_q^{\rm orb}W]
\in
\mathcal S(G)/\ker\mathcal O_{\rm hyp}.
}
\tag{3.1}
\]

This is the correct invariant statement.

In particular, RI-B should not demand a unique pointwise formula on `G`; the orbital data determine only an orbital-equivalence class unless additional K-type/Fourier constraints are imposed.

---

## 4. Why this does not yet solve the Toeplitz problem

Earlier we proved for the coherent-state group kernel `F_{q,W}` that

\[
\widehat F_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)}.
\]

The scalar orbital lift above satisfies

\[
O_{a_L}(\mathcal L_q^{\rm orb}W)=\mathscr R_q(a_L;W),
\]

but the orbital inversion theorem alone does **not** imply

\[
\widehat{\mathcal L_q^{\rm orb}W}(\pi_q)
=d_q^{-1}T_W^{(q)}.
\]

Indeed a scalar orbital transform forgets data lying in its kernel, whereas the noncentral Toeplitz operator retains the full symbol-dependent fixed-K-type information.

Hence there are two different closures:

\[
\boxed{
\begin{array}{lll}
\text{orbital closure:}
& W\mapsto [\mathcal L_q^{\rm orb}W]
& \text{determines }\mathscr R_q(a_L;W),\\[1mm]
\text{Fourier/Toeplitz closure:}
& W\mapsto F_{q,W}
& \text{determines }T_W^{(q)}.
\end{array}
}
\tag{4.1}
\]

The remaining theorem must find a representative satisfying both constraints simultaneously, or prove the precise obstruction.

---

## 5. The simultaneous interpolation problem

The next target is therefore:

> Given `W`, find `f_{q,W}` in a K-finite Harish--Chandra Schwartz/test space such that
> \[
> \boxed{
> O_{a_L}(f_{q,W})=d_q\mathcal J_{q,L}[W]
> }
> \tag{5.1}
> \]
> for every regular hyperbolic `L`, and
> \[
> \boxed{
> \widehat f_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)}.
> }
> \tag{5.2}
> \]

Call this **K-Type Orbital Interpolation (KOI)**.

The existence of K-finite test functions and discrete-series pseudo-coefficients shows that K-type constraints can be imposed nontrivially in `C_c^\infty(G)`, while Harish--Chandra's explicit `SL(2,R)` formulas relate character distributions to the hyperbolic and elliptic orbital transforms. But those facts alone do not prove simultaneous solvability of (5.1)--(5.2) for arbitrary FCIG symbols.

---

## 6. Relation to the standard SL(2,R) formulas

For `f\in C_c^\infty(G)`, Harish--Chandra's rank-one formulas express discrete-series characters in terms of orbital transforms associated with the split and compact Cartans. Schematically,

\[
\Theta_k(f)
=
\text{hyperbolic-orbital transform of }f
+
\text{elliptic-orbital transform of }f.
\]

This immediately supplies a second firewall: **hyperbolic orbital data alone do not determine the discrete-series Fourier block**. Elliptic/compact-Cartan information also enters character inversion.

That is exactly why (2.2) closes RI-B only at the scalar hyperbolic-orbital level, while KOI remains a genuine additional constraint.

---

## 7. Gate status

The original RI-B target was

\[
O_{a_L}(\mathcal L_qW)=\mathscr R_q(a_L;W).
\]

For admissible compactly supported/Schwartz FCIG response profiles, rank-one orbital inversion supplies precisely such a lift modulo the kernel of the hyperbolic orbital transform. Therefore

\[
\boxed{\textbf{RI-B: PASS modulo orbital-transform kernel.}}
\]

The stronger statement preserving the Toeplitz/discrete-series Fourier block is not yet proved:

\[
\boxed{\textbf{KOI-A: OPEN — simultaneous hyperbolic-orbital and }D^+_{2q-1}\textbf{ Fourier interpolation.}}
\]

This is a sharper frontier than the previous generic call for `invariantization`.

---

## 8. Updated FCIG chain

\[
\boxed{
\begin{aligned}
W
&\xrightarrow{\text{coherent lift}}F_{q,W}
\xrightarrow{\mathcal F_G}
d_q^{-1}T_W^{(q)},\\
W
&\xrightarrow{\text{cyclic reduction}}
R_{q,W}(L)=d_q\mathcal J_{q,L}[W]\\
&\xrightarrow{\times\Delta(L)}H_{q,W}(L)
\xrightarrow{\mathcal O_{\rm hyp}^{-1}}
[\mathcal L_q^{\rm orb}W]\\
&\xrightarrow{O_{a_L}}
R_{q,W}(L).
\end{aligned}
}
\]

The two branches are exact. The next problem is to make them meet in a single K-finite representative.

---

## References

- Harish-Chandra, harmonic analysis and orbital-integral inversion for real semisimple groups; in rank one see the explicit `SL(2,R)` orbital formulas.
- S. Helgason, *Orbital Integrals, Symmetric Fourier Analysis and Eigenspace Representations*; explicit `SL(2,R)` formulas relating characters and orbital transforms.
- Standard `SL(2,R)` pseudo-coefficient construction for discrete series via K-finite test functions and Paley--Wiener theory.
- R. A. Herb, *Weighted orbital integrals on SL(2,R)*, for the distinct Arthur-weighted setting. The FCIG symbol is not identified with the Arthur weight.
