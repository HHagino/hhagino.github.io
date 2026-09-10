# FCIG: K-Type Orbital Interpolation

**Status:** scalar discrete-series trace interpolation pass; full operator-valued interpolation open  
**Date:** 2026-09-10  
**Depends on:** [`orbital-lift-closure.md`](orbital-lift-closure.md), [`discrete-series-invariant-inversion.md`](discrete-series-invariant-inversion.md), [`relative-invariantization.md`](relative-invariantization.md), [`coherent-state-discrete-series-closure.md`](coherent-state-discrete-series-closure.md).

> **Claim firewall.** A discrete-series pseudo-coefficient controls traces against irreducible tempered representations. It does not, by itself, prescribe an arbitrary operator-valued Fourier block. The exact result below therefore closes scalar trace interpolation while leaving the full Toeplitz-block interpolation problem open.

---

## 0. Problem

The previous stages produced two exact branches for a deformation symbol `W`.

The Fourier/Toeplitz branch gives

\[
\widehat F_{q,W}(\pi_q)=d_q^{-1}T_W^{(q)},
\tag{0.1}
\]

while the hyperbolic orbital branch gives an orbital lift `L_q^{orb}W` satisfying

\[
O_{a_L}(\mathcal L_q^{\rm orb}W)
=d_q\,\mathcal J_{q,L}[W]
=\mathscr R_q(a_L;W).
\tag{0.2}
\]

The K-type orbital interpolation problem asks whether one can impose both kinds of information on one test function without disturbing the already-correct hyperbolic orbital data.

---

# Part I. Pseudo-coefficient correction

## 1. Discrete-series pseudo-coefficient

Let `pi_q=D^+_{2q-1}` and choose a normalized pseudo-coefficient

\[
f_{\pi_q}\in C_c^\infty(G)
\]

with

\[
\operatorname{tr}\pi_q(f_{\pi_q})=1,
\qquad
\operatorname{tr}\sigma(f_{\pi_q})=0
\]

for the other tempered representations in the pseudo-coefficient normalization.

For regular non-elliptic semisimple elements, in particular regular split hyperbolic elements `a_L`, the standard Selberg-principle property is

\[
\boxed{
O_{a_L}(f_{\pi_q})=0.
}
\tag{1.1}
\]

For regular elliptic elements the orbital integral is instead governed by the discrete-series character, with convention-dependent inversion/sign factors. We do not use that elliptic formula below.

Thus a pseudo-coefficient lies in the kernel of the regular hyperbolic orbital transform while remaining nontrivial on the target discrete-series trace.

---

## 2. Scalar correction lemma

Let `f_0` be any admissible test function realizing the desired FCIG hyperbolic response:

\[
O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W].
\tag{2.1}
\]

Let `tau` be any desired scalar value for the `pi_q` trace. Set

\[
c:=\tau-\operatorname{tr}\pi_q(f_0)
\]

and define

\[
\boxed{
f_{W,\tau}:=f_0+c f_{\pi_q}.
}
\tag{2.2}
\]

Then, for every regular hyperbolic `a_L`,

\[
\begin{aligned}
O_{a_L}(f_{W,\tau})
&=O_{a_L}(f_0)+cO_{a_L}(f_{\pi_q})\\
&=d_q\mathcal J_{q,L}[W].
\end{aligned}
\]

At the same time,

\[
\begin{aligned}
\operatorname{tr}\pi_q(f_{W,\tau})
&=\operatorname{tr}\pi_q(f_0)+c\\
&=\tau.
\end{aligned}
\]

Hence

\[
\boxed{
\begin{cases}
O_{a_L}(f_{W,\tau})=d_q\mathcal J_{q,L}[W],\\[1mm]
\operatorname{tr}\pi_q(f_{W,\tau})=\tau.
\end{cases}
}
\tag{2.3}
\]

This is exact scalar interpolation.

---

# Part II. FCIG scalar specialization

## 3. Matching the Toeplitz trace

Whenever `T_W^{(q)}` is trace class, the natural scalar target is

\[
\tau_W:=d_q^{-1}\operatorname{Tr}T_W^{(q)}.
\tag{3.1}
\]

Choose any hyperbolic orbital lift `f_0=\mathcal L_q^{orb}W`. Then

\[
\boxed{
f_{q,W}^{\rm scal}
:=\mathcal L_q^{\rm orb}W
+
\left(
 d_q^{-1}\operatorname{Tr}T_W^{(q)}
-\operatorname{tr}\pi_q(\mathcal L_q^{\rm orb}W)
\right)f_{\pi_q}.
}
\tag{3.2}
\]

It satisfies simultaneously

\[
\boxed{
O_{a_L}(f_{q,W}^{\rm scal})
=d_q\mathcal J_{q,L}[W]
}
\tag{3.3}
\]

and

\[
\boxed{
\operatorname{tr}\pi_q(f_{q,W}^{\rm scal})
=d_q^{-1}\operatorname{Tr}T_W^{(q)}.
}
\tag{3.4}
\]

Therefore the scalar discrete-series trace and the entire regular hyperbolic orbital profile can be prescribed independently.

---

# Part III. Why this is not yet the full Toeplitz-block theorem

## 4. Trace versus operator-valued Fourier block

The stronger FCIG target is

\[
\boxed{
\widehat f(\pi_q)=d_q^{-1}T_W^{(q)}
}
\tag{4.1}
\]

as an operator identity on the discrete-series Hilbert space.

A pseudo-coefficient only fixes

\[
\operatorname{tr}\widehat f(\pi_q)
=\operatorname{tr}\pi_q(f).
\]

It does not imply

\[
\widehat{f_{\pi_q}}(\pi_q)=I,
\]

nor does it provide arbitrary finite-rank or trace-class operator corrections inside the `pi_q` block.

Hence the scalar construction (3.2) cannot be promoted to (4.1) without an additional operator-valued Paley--Wiener/interpolation theorem.

The missing question is:

> Given a target operator `A` in the `pi_q` Fourier block, can one find a sufficiently regular test function `h_A` such that all regular hyperbolic orbital integrals vanish while `\widehat h_A(\pi_q)=A`?

That is strictly stronger than ordinary pseudo-coefficient theory.

---

# Part IV. Correct decomposition of the problem

## 5. Two kernels

Let

\[
\mathcal K_{\rm hyp}
:=\{f:O_{a_L}(f)=0\text{ for all regular }L\neq0\}
\]

and let

\[
\mathfrak F_q(f):=\widehat f(\pi_q).
\]

Full KOI closure is equivalent to sufficient surjectivity of

\[
\boxed{
\mathfrak F_q\big|_{\mathcal K_{\rm hyp}}:
\mathcal K_{\rm hyp}\longrightarrow
\operatorname{End}_{\rm adm}(\mathcal H_{\pi_q}).
}
\tag{5.1}
\]

Pseudo-coefficient theory proves at least that the scalar functional

\[
f\mapsto\operatorname{tr}\mathfrak F_q(f)
\]

is nonzero on `K_hyp`.

Thus the scalar quotient direction is accessible, but operator-level surjectivity remains to be shown.

---

# Part V. Gate status

## 6. KOI-A

We now have the exact theorem:

\[
\boxed{
\text{regular hyperbolic orbital data can be held fixed while the target discrete-series scalar trace is corrected arbitrarily.}
}
\]

Therefore

\[
\boxed{\textbf{KOI-A1: PASS — scalar trace interpolation.}}
\]

But the stronger statement

\[
\boxed{
O_{a_L}(f)=d_q\mathcal J_{q,L}[W],
\qquad
\widehat f(\pi_q)=d_q^{-1}T_W^{(q)}
}
\]

remains unproved.

Hence

\[
\boxed{\textbf{KOI-A2: OPEN — full operator-valued interpolation.}}
\]

This is a deliberate strengthening of the claim firewall, not a failure of the scalar result.

---

# Part VI. Next target

## 7. Operator-kernel interpolation

The next gate is

\[
\boxed{\textbf{OKI-A — Operator Kernel Interpolation.}}
\]

A successful proof should construct, for a dense class of finite-rank or smoothing operators `A` on `H_{pi_q}`, a test kernel `h_A` satisfying

\[
\boxed{
O_{a_L}(h_A)=0
\quad\text{for all regular hyperbolic }a_L,
\qquad
\widehat h_A(\pi_q)=A.
}
\tag{7.1}
\]

Then with

\[
A_W=d_q^{-1}T_W^{(q)}-\widehat{\mathcal L_q^{orb}W}(\pi_q)
\]

one would obtain

\[
f_{q,W}=\mathcal L_q^{orb}W+h_{A_W}
\]

and hence the full simultaneous closure.

Likely tools are the noncommutative Paley--Wiener theorem, explicit `K`-finite matrix-valued transforms, and very-cuspidal/pseudo-coefficient constructions. The required statement is operator-valued; ordinary scalar pseudo-coefficients are not enough.

---

## 8. FCIG synthesis

The hyperbolic-information program now separates cleanly into three levels:

\[
\boxed{
\begin{array}{rcl}
\text{orbital lift} &:& O_{a_L}(f_0)=d_q\mathcal J_{q,L}[W],\\
\text{scalar correction} &:& f_0\mapsto f_0+c f_{\pi_q},\\
\text{operator correction} &:& \text{OKI-A, still open}.
\end{array}
}
\]

The pseudo-coefficient direction proves that there is no scalar-trace obstruction to joining the orbital and discrete-series branches. Any remaining obstruction is genuinely operator-valued.

## References

- J.-P. Labesse, *Pseudo-coefficients très cuspideaux et K-théorie*, Mathematische Annalen 291 (1991), 607--616.
- L. Clozel and P. Delorme, work on pseudo-coefficients and the invariant Paley--Wiener theorem for real reductive Lie groups.
- Standard Selberg principle for discrete-series pseudo-coefficients: regular non-elliptic orbital integrals vanish, whereas regular elliptic orbital integrals recover the corresponding discrete-series character up to the chosen conventions.
