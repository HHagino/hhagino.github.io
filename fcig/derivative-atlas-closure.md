# Derivative Semiclassical Atlas

## DA-A — invariant/radial derivatives across the SAC charts

**Status (2026-09-10).**

This note refines `semiclassical-atlas-closure.md`, `semiclassical-preprint-v1.md`, and the sharp Schwartz refinement.  It records the derivative scaling dictated by each canonical chart and corrects a previously informal statement about the Airy derivative cost.

\[
\boxed{\textbf{DA-A1: PASS — canonical radial derivative scales are explicit.}}
\]

The statement is local to the canonical charts and does not by itself give a single globally uniform all-orders remainder theorem.

---

## 1. Generic ordinary-saddle chart

Away from caustics and boundary degenerations the matrix coefficient has the form

\[
M_{m,n}^{(q)}(t)
= e^{-q\Phi(t)}\,q^{-1/2}\bigl(A_0(t)+q^{-1}A_1(t)+\cdots\bigr)
\]

in a forbidden chamber, and the corresponding conjugate-saddle oscillatory form in the allowed chamber.

For a fixed radial derivative order \(j\), differentiation of the phase gives at most a relative factor \(q^j\):

\[
\boxed{
\partial_t^j M
=e^{-q\Phi}\,q^{-1/2+j}\times(\text{smooth symbol})
}
\]

away from stationary points of the radial rate.  This is consistent with the enveloping-algebra bound because a fixed Lie word of degree \(j\) has polynomial cost of degree at most \(j\) in \(q+m+n\).

---

## 2. Simple Airy fold

Near either nondegenerate caustic,

\[
M(t)
=\mathcal E_q(t)
\left[
q^{-1/3}A_0(t)\operatorname{Ai}(q^{2/3}\zeta(t))
+q^{-2/3}B_0(t)\operatorname{Ai}'(q^{2/3}\zeta(t))
+\cdots
\right],
\]

with \(\zeta'(t_\pm)\neq0\).

Therefore

\[
\partial_t
=q^{2/3}\zeta'(t)\partial_{(q^{2/3}\zeta)}+O(1)
\]

on the canonical scale.  Hence the relative cost of \(j\) radial derivatives is

\[
\boxed{q^{2j/3}.}
\]

For the leading Airy term specifically,

\[
\boxed{
\partial_t^j\left[q^{-1/3}\operatorname{Ai}(q^{2/3}\zeta(t))\right]
=O\!\left(q^{(2j-1)/3}\right)
}
\]

on bounded Airy coordinate sets, modulo smooth parameter-dependent amplitudes.

This corrects the informal phrase `q^{1/3} per derivative`; the correct radial Airy scale is `q^{2/3} per derivative`.

---

## 3. Bessel boundary chart

When

\[
n-m=k\ \text{fixed},\qquad t=s/q,
\]

we have

\[
M_{m,m+k}^{(q)}(s/q)\to J_k(p_\alpha s),
\qquad p_\alpha=\sqrt{\alpha(\alpha+2)}.
\]

Since

\[
\partial_t=q\partial_s,
\]

fixed radial derivative order gives

\[
\boxed{
\partial_t^j M_{m,m+k}^{(q)}(s/q)
=q^j\,p_\alpha^j J_k^{(j)}(p_\alpha s)+o(q^j)
}
\]

on compact \(s\)-sets, provided the underlying boundary expansion is differentiated to the corresponding order.

Thus the Bessel chart carries relative derivative scale

\[
\boxed{q^j.}
\]

---

## 4. Hermite--Gaussian boundary chart

When one K-type remains fixed,

\[
n=\nu\quad\text{fixed},\qquad
t=u_\alpha+\tau/\sqrt q,
\]

we have

\[
q^{1/4}M_{\nu,m}^{(q)}(t)
\to C_\alpha\,\frac{H_\nu(-\tau)}{\sqrt{2^\nu\nu!}}e^{-\tau^2/2}.
\]

Since

\[
\partial_t=\sqrt q\,\partial_\tau,
\]

the relative derivative scale is

\[
\boxed{q^{j/2}.}
\]

More precisely,

\[
\boxed{
q^{1/4-j/2}\partial_t^j M_{\nu,m}^{(q)}
\left(u_\alpha+\frac\tau{\sqrt q}\right)
\longrightarrow
C_\alpha\,\partial_\tau^j
\left[
\frac{H_\nu(-\tau)}{\sqrt{2^\nu\nu!}}e^{-\tau^2/2}
\right].
}
\]

---

## 5. Derivative atlas

The leading derivative atlas is therefore

\[
\boxed{
\begin{array}{ccl}
\text{ordinary saddle} &:& q^j,\\
\text{simple Airy fold} &:& q^{2j/3},\\
\text{Bessel endpoint chart} &:& q^j,\\
\text{Hermite merger chart} &:& q^{j/2}.
\end{array}}
\]

These are **relative local radial derivative scales**.  They are not global powers in the Harish--Chandra-Schwartz seminorm; invariant derivatives also act on K-variables and are globally controlled by the exact derived-representation weights

\[
(1+q+m)^{\deg D}(1+q+n)^{\deg E}.
\]

---

## 6. Consequence for SAC--Schwartz stitching

Near a simple outer fold, a derivative of radial order \(j\) shifts the logarithmic matching equation by

\[
\frac{2j}{3}\log q
\]

at leading scale.  Thus the derivative-sensitive overlap law is

\[
\boxed{
q\Phi_+(t)
\approx
\frac t2+N\log(1+t)
+\log P_{D,E}(q,m,n)
+\frac{2j}{3}\log q,
}
\]

where the last term is used when \(j\) explicit radial differentiations are resolved inside the Airy chart rather than absorbed into the global enveloping-algebra polynomial.

If

\[
\Phi_+(t)\sim C_+(t-t_+)^{3/2},
\]
then

\[
\boxed{
\Delta t_{\rm stitch}^{(j)}
\asymp
\left[
\frac{t_+/2+N\log(1+t_+)+\log P_{D,E}+(2j/3)\log q}
{qC_+}
\right]^{2/3}.
}
\]

This is a sectorwise matching law, not yet a globally uniform theorem across all boundary degenerations.

---

## 7. Gate ledger

\[
\boxed{\textbf{DA-A1: PASS — local derivative scales across all SAC charts.}}
\]

\[
\boxed{\textbf{DA-A2: OPEN — one global differentiated remainder theorem across every overlap.}}
\]

---

## Claim firewall

- Airy radial differentiation costs `q^{2/3}` per derivative on the Airy scale, not `q^{1/3}`.
- Bessel and Hermite derivative limits require differentiated versions of the corresponding uniform boundary expansions; the displayed scalings follow from the exact rescaled variables and are leading canonical statements.
- Local radial derivative scales are distinct from global left/right invariant derivative weights.
- No claim is made that the displayed local powers are globally optimal for every enveloping-algebra direction.
- No novelty claim is made for the classical canonical-function differentiation rules.
