# FCIG: Toeplitz Orbital Insertion for the Weighted Discrete-Series Trace

**Status:** geometric Toeplitz-orbital closure established; representation-theoretic relative-character closure open  
**Date:** 2026-09-10  
**Depends on:** [`bls-position-transport.md`](bls-position-transport.md), [`systolic-bergman-orbital.md`](systolic-bergman-orbital.md), [`disk-transported-bergman.md`](disk-transported-bergman.md), [`centralizer-spectral-window.md`](centralizer-spectral-window.md), [`cyclic-relative-trace.md`](cyclic-relative-trace.md), [`character-trace-firewall.md`](character-trace-firewall.md).

> **Claim firewall.** The compact Bergman trace identity is elementary operator theory. On the universal-cover discrete-series model, the object below is a **centralizer-reduced kernel trace**, not an ordinary Hilbert-space trace of `pi_q(a_L)`. The latter is forbidden by the character-trace firewall.

---

## 0. Main observation

Let `P_q` be the Bergman projection and `M_W` multiplication by a geometric weight. The canonical quantization already present in the BLS/Bergman formalism is

\[
\boxed{T_W^{(q)}=P_qM_WP_q.}
\]

For

\[
W_q=|\mu|^2+2(q-1)(1+\square_0)^{-1}|\mu|^2,
\]

the FCIG insertion is therefore the Toeplitz observable `T_{W_q}^{(q)}`. More economically, after Casimir transmutation one may use

\[
f_\mu=(1+\square_0)^{-1}|\mu|^2,
\qquad T_{f_\mu}^{(q)},
\]

and let `D_{q,L}` act on the conjugacy-length variable.

The structural map is

\[
\boxed{
\text{deformation weight}
\xrightarrow{PMP}
\text{Toeplitz observable}
\xrightarrow{\text{centralizer-reduced transported kernel}}
\text{hyperbolic information orbital}.
}
\]

---

# Part I. Compact trace identity

On a compact surface,

\[
\boxed{
\operatorname{Tr}(T_W^{(q)})
=\int_XW(x)B_q(x)dA(x).
}
\]

Likewise, whenever the product is trace class,

\[
\operatorname{Tr}(T_W^{(q)}U_g^{(q)})
=\operatorname{Tr}(M_WP_qU_g^{(q)}P_q),
\]

whose diagonal is a weighted transported Bergman kernel.

This fixes the operator **type** of the FCIG insertion without representation-theory guesswork.

---

# Part II. Exact hyperbolic kernel

The disk calculation in [`disk-transported-bergman.md`](disk-transported-bergman.md) proves that, in the stated orientation convention,

\[
\boxed{
\mathcal K_q(g_L;u)
=C_q\kappa_{q,L}(u),
\qquad
C_q=\frac{2q-1}{4\pi},
}
\]

where

\[
\boxed{
\kappa_{q,L}(u)
=\left(\cosh\frac L2-iu\sinh\frac L2\right)^{-2q}.
}
\]

The automorphy/Chern phase is essential; orientation reversal complex-conjugates the kernel.

Therefore:

\[
\boxed{\textbf{TOI-A: PASS.}}
\]

---

# Part III. Exact cyclic relative trace

Let `delta` be primitive of length `ell`, let `L=m ell`, and set

\[
Y_\delta=\langle\delta\rangle\backslash\mathbb H.
\]

Define the geometric cyclic relative trace by

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}
[T_W^{(q)}U_{\delta^m}^{(q)}]
:=
\Re\int_{Y_\delta}W(x)\mathcal K_q(\delta^m;x,x)dA(x).
}
\]

In Fermi coordinates `dA=dt du` and the transported diagonal is independent of `t`. Hence

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}
[T_W^{(q)}U_{\delta^m}^{(q)}]
=C_q\ell\,\mathcal J_{q,m\ell}[W].
}
\]

Thus the previously unknown normalization is exactly

\[
\boxed{\mathcal N_{c,m,q}=C_q\ell_c}
\]

for one orientation, and `2 C_q ell_c` after pairing orientations.

The primitive length, not `m ell`, occurs because the centralizer of `delta^m` is the primitive cyclic group `\langle\delta\rangle`.

Therefore:

\[
\boxed{\textbf{TOI-B: PASS at the geometric cyclic-kernel level.}}
\]

---

# Part IV. Exact meaning of the cyclic multipliers

The holomorphic deformation has longitudinal Fourier coefficients `b_n`. Its quadratic source contains terms

\[
b_n\overline{b_r}e^{i(\nu_n-\nu_r)t}.
\]

The zero centralizer character selected by the ordinary cyclic trace imposes `n=r`. Therefore

\[
\overline f_\mu(u)=\sum_n|b_n|^2F_{n,\ell}(u)
\]

and

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}
[T_{f_\mu}^{(q)}U_{\delta^m}^{(q)}]
=C_q\ell\sum_n|b_n|^2\Lambda_n^{(q,m)}(\ell),
}
\]

with

\[
\Lambda_n^{(q,m)}(\ell)
=\Re\int_{\mathbb R}F_{n,\ell}(u)\kappa_{q,m\ell}(u)du.
\]

This corrects the provisional idea that `Lambda_n` should be a `k=n` projected trace of the quadratic symbol: it is instead the `n=r` diagonal deformation summand inside the **zero-character** cyclic relative trace.

The companion spectral-window note further proves that each `Lambda_n` is an exact Gamma-windowed transverse spectral moment.

Therefore:

\[
\boxed{\textbf{TOI-C: PASS at the geometric kernel level.}}
\]

---

# Part V. Global reconstruction

The exact Sun--Selberg unfolding can now be written directly as a sum of relative traces:

\[
\boxed{
\mathcal B_q[W]
=\sum_{[\delta]\in\mathcal P_{\rm or}}\sum_{m\ge1}
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}
[T_W^{(q)}U_{\delta^m}^{(q)}].
}
\]

Equivalently, summing over primitive unoriented geodesics gives twice the chosen-orientation cyclic trace.

Thus the nonidentity Bergman correction is literally a sum of deformation-inserted cyclic relative traces at the geometric kernel level.

---

# Part VI. What remains open

The old TOI-D proposal attempted to recover

\[
\frac{e^{-qL}}{1-e^{-L}}
\]

from a literal descendant Hilbert-space trace. This is rejected: `pi_q(a_L)` is unitary on an infinite-dimensional discrete-series Hilbert space and is not trace class. The Harish--Chandra character is distributional.

The correct next gate is therefore not another cylinder integral.

## RC-A — relative-distribution identification

Identify the cyclic kernel functional

\[
W\mapsto
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}
[T_W^{(q)}U_{\delta^m}^{(q)}]
\]

as a canonical relative distribution for the pair `(G,A)`, with `G=PSL(2,R)` and `A` the split Cartan.

## RC-B — invariant transform

Construct the corresponding test function/operator-valued distribution on `G` and compute its invariant Harish--Chandra/Selberg transform.

## RC-C — Weyl denominator

Show that the standard hyperbolic Weyl/Jacobian machinery produces the Selberg/discrete-series denominator rather than inserting it by hand.

---

## Current theorem target

The geometric part can now be stated as an exact closure:

\[
\boxed{
\textbf{Geometric Toeplitz Orbital Closure:}\quad
\mathcal J_{q,L}[W]
\text{ is, up to the exact primitive centralizer factor }C_q\ell,
\text{ the cyclic relative kernel trace of }
P_qM_WP_q\,U_{a_L}.
}
\]

The remaining frontier is representation-theoretic:

\[
\boxed{
\text{Toeplitz observable}
\to
\text{cyclic relative kernel trace}
\to
\text{relative }(G,A)\text{ distribution}
\to
\text{Harish--Chandra/Selberg transform}.
}
\]

That is now the sharpest nonperturbative FCIG target.
