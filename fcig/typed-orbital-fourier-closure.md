# Typed Orbital/Fourier Closure

## OSB-B — the canonical typed statement

**Status (2026-09-10).**

The earlier `orbital-semiclassical-bridge.md` left OSB-B open as a request for a typed relative/Harish--Chandra transform. The intervening notes have now separated and solved the pieces needed for the correct statement:

- `discrete-series-invariant-inversion.md`: explicit noncommutative discrete-series Fourier block;
- `relative-invariantization.md`: exact diagonal relative invariance;
- `orbital-lift-closure.md`: scalar hyperbolic orbital lift modulo the orbital-transform kernel;
- `operator-kernel-interpolation.md` and `schwartz-completion.md`: cuspidal corrections with prescribed smoothing operator Fourier block and zero regular split-hyperbolic orbital transform.

The result is not a pointwise equality between orbital variables and spectral variables. It is a commuting interpolation statement in the Harish--Chandra Schwartz category.

\[
\boxed{\textbf{OSB-B1: PASS — typed orbital/Fourier interpolation in the smoothing sector.}}
\]

A unique canonical representative is not claimed; the natural invariant object is a quotient by the hyperbolic-orbital kernel.

---

## 1. The two exact data attached to a symbol

Let

\[
\pi_q=D^+_{2q-1},\qquad d_q=\frac{2q-1}{4\pi}.
\]

For an admissible FCIG symbol `W`, there are two independently exact outputs.

### Fourier/Toeplitz datum

The coherent-state group kernel has

\[
\boxed{
\widehat F_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)}.
}
\tag{1.1}
\]

### Hyperbolic relative-orbital datum

For `a_L` regular hyperbolic,

\[
\boxed{
\mathscr R_q(a_L;W)=d_q\mathcal J_{q,L}[W].
}
\tag{1.2}
\]

For a primitive closed geodesic of length `ell`, `L=m ell`,

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=\ell\,\mathscr R_q(a_L;W).
}
\tag{1.3}
\]

These are differently typed data and must remain so.

---

## 2. Orbital lift

Let

\[
\mathcal O_{\rm hyp}(f)(L):=O_{a_L}(f).
\]

For admissible Weyl-normalized response profiles, rank-one orbital inversion gives a Schwartz/test representative `f_0` such that

\[
\boxed{
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
}
\tag{2.1}
\]

The representative is determined only modulo

\[
\ker\mathcal O_{\rm hyp}
=\{h:O_{a_L}(h)=0\text{ for all regular split }a_L\}.
\]

Thus the scalar orbital datum canonically determines the quotient class

\[
\boxed{
[f_0]_{\rm hyp}\in\mathcal C(G)/\ker\mathcal O_{\rm hyp}.
}
\tag{2.2}
\]

---

## 3. Cuspidal Fourier correction

Let

\[
A_W:=d_q^{-1}T_W^{(q)}-\widehat f_0(\pi_q).
\tag{3.1}
\]

Assume

\[
A_W\in\mathscr S(\mathcal H_q),
\]

the rapid/smoothing operator ideal of `schwartz-completion.md`.

Discrete-series Schwartz synthesis gives a cuspidal function `h_{A_W}` satisfying simultaneously

\[
\boxed{
\widehat h_{A_W}(\pi_q)=A_W,
\qquad
O_{a_L}(h_{A_W})=0
\quad(L\ne0).
}
\tag{3.2}
\]

Define

\[
\boxed{
f_{q,W}:=f_0+h_{A_W}.
}
\tag{3.3}
\]

Then

\[
\boxed{
O_{a_L}(f_{q,W})=d_q\mathcal J_{q,L}[W]
}
\tag{3.4}
\]

and

\[
\boxed{
\widehat f_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)}.
}
\tag{3.5}
\]

This is the desired simultaneous typed bridge.

---

## 4. Commuting FCIG diagram

The result is best stated as

\[
\boxed{
\begin{array}{ccc}
& f_{q,W}\in\mathcal C(G) &\\[1mm]
\swarrow\scriptstyle{\mathcal O_{\rm hyp}} &&
\searrow\scriptstyle{\mathcal F_G|_{\pi_q}}\\[1mm]
d_q\mathcal J_{q,L}[W] && d_q^{-1}T_W^{(q)}.
\end{array}}
\tag{4.1}
\]

After primitive centralizer periodization, the left leg becomes

\[
\ell\,d_q\mathcal J_{q,m\ell}[W]
=
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W].
\]

Thus the exact cyclic Bergman orbital and the exact Toeplitz discrete-series block admit a common Harish--Chandra-Schwartz representative whenever the Fourier defect is smoothing.

This is the precise transform-theoretic sense in which the two FCIG branches meet.

---

## 5. Weyl normalization and character comparison

Let

\[
\Delta(L)=2\sinh(L/2).
\]

The hyperbolic response may be written

\[
O_{a_L}(f_{q,W})
=
\frac{1}{\Delta(L)}
\underbrace{\left[d_q\Delta(L)\mathcal J_{q,L}[W]\right]}_{\text{FCIG Weyl-normalized numerator}}.
\tag{5.1}
\]

The holomorphic discrete-series character has

\[
\Theta_{2q-1}^{+}(a_{L/2})
=
\frac{e^{-(q-1/2)L}}{\Delta(L)}.
\tag{5.2}
\]

Therefore the denominator comparison is exact, while the numerators remain different typed transforms:

\[
\boxed{
\begin{array}{rcl}
\text{FCIG numerator}&:&d_q\Delta(L)\mathcal J_{q,L}[W],\\
\text{character numerator}&:&e^{-(q-1/2)L}.
\end{array}}
\tag{5.3}
\]

No equality of these numerators is asserted.

---

## 6. Relation to the exact Gamma window

The left leg has the already-proved transverse representation

\[
\mathcal J_{q,L}[W]
=\Re\int_{\mathbb R}\bar W(u)\kappa_{q,L}(u)\,du,
\]

and

\[
\widehat{\Re\kappa}_{q,L}(\xi)
\propto
\left(\frac{|\xi|}{\tau_L}\right)^{2q-1}
 e^{-|\xi|/\tau_L},
\qquad
\tau_L=\tanh(L/2).
\]

Thus the orbital leg is a Gamma-windowed transverse Fourier moment, whereas the right leg is a noncommutative group Fourier coefficient at `pi_q`.

The common test object `f_{q,W}` connects the two **without identifying**

\[
\xi,\quad L,\quad n,\quad\text{or a Harish--Chandra spectral parameter}.
\]

That separation is the content of the typed closure.

---

## 7. Canonical quotient versus noncanonical representative

If `f_{q,W}` and `f'_{q,W}` have the same hyperbolic orbital data, their difference lies in `ker O_hyp`. Prescribing the `pi_q` Fourier block removes the required `pi_q` component of this ambiguity, but there may still be components invisible to both selected outputs.

Therefore the canonical theorem is an existence/interpolation theorem, not uniqueness of a pointwise group function.

A natural object is the double-data quotient class determined by

\[
\left(
\mathcal O_{\rm hyp}(f),
\widehat f(\pi_q)
\right).
\]

This is exactly sufficient for FCIG's cyclic response plus Toeplitz block.

---

## 8. Gate status

The old OSB-B request is now split as follows.

\[
\boxed{\textbf{OSB-B1: PASS — common Schwartz representative for orbital and }\pi_q\textbf{ Fourier data.}}
\]

The pass holds for the smoothing defect class

\[
A_W\in\mathscr S(\mathcal H_q),
\]

which is the natural domain already fixed by SC-A.

A stronger question remains:

\[
\boxed{
\textbf{OSB-B2: OPEN — canonical/minimal representative and full automorphic multiplicity compatibility.}
}
\]

The latter is not needed for the local representation-theoretic bridge proved here.

---

## 9. Consequence for FCIG architecture

The hyperbolic information channel may now be written

\[
\boxed{
\begin{aligned}
W
&\longrightarrow T_W^{(q)}\\
&\longleftrightarrow
\widehat f_{q,W}(\pi_q),\\[1mm]
W
&\longrightarrow
\mathcal J_{q,L}[W]\\
&\longleftrightarrow
O_{a_L}(f_{q,W})\\
&\longrightarrow
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W].
\end{aligned}}
\]

The same Schwartz test object realizes both branches. The character/Weyl machinery may now be applied to this group-level object with the existing character/trace firewall intact.

## Claim firewall

- `OSB-B1` is an interpolation/existence theorem, not a pointwise equality of orbital and spectral variables.
- The transverse Fourier variable `xi` is not the noncommutative group Fourier parameter.
- The cyclic deformation mode `n` is not a Harish--Chandra spectral variable.
- The common Weyl denominator does not identify FCIG and character numerators.
- The smoothing hypothesis is essential to the stated Schwartz synthesis theorem.
- Compact automorphic Toeplitz blocks require a separate multiplicity identification before they are literally the universal-cover operator `T_W^(q)`.
- No novelty claim is made for standard Harish--Chandra Fourier/orbital machinery.