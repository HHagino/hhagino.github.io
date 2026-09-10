# Two-Sided Forbidden Closure

## TF-A — inner/outer forbidden regions and the Schwartz obstruction

**Status (2026-09-10).**

This note combines the exact two-sheet caustic geometry with the sharp Schwartz refinement.

\[
\boxed{\textbf{TF-A1: PASS — the inner forbidden chamber creates no independent Schwartz-tail obstruction.}}
\]

\[
\boxed{\textbf{TF-A2: PASS — the two forbidden chambers are controlled by }\Phi_-\textbf{ and }\Phi_+\textbf{ respectively on SAC sectors.}}
\]

---

## 1. Two caustic radii

For

\[
\alpha=\frac mq,\qquad \beta=\frac nq,
\]

define

\[
u_m=\operatorname{arcosh}\left(1+\frac mq\right),
\qquad
u_n=\operatorname{arcosh}\left(1+\frac nq\right).
\]

The exact caustic radii are

\[
\boxed{
t_-=|u_m-u_n|,
\qquad
t_+=u_m+u_n.}
\]

Thus

\[
0<t<t_-
\]

is the inner forbidden chamber,

\[
t_-<t<t_+
\]

is oscillatory, and

\[
t>t_+
\]

is the outer forbidden chamber.

---

## 2. Inner chamber and Harish--Chandra weights

The weighted Schwartz seminorm contains

\[
(1+t)^N\Xi(a_t)^{-1}|M_{m,n}^{(q)}(t)|.
\]

Cowling--Haagerup--Howe gives

\[
|M_{m,n}^{(q)}(t)|\le\Xi(a_t)
\]

for the normalized one-dimensional K-types of the tempered holomorphic discrete series.

Since

\[
0<t<t_-\le t_+,
\]
we immediately get

\[
\boxed{
(1+t)^N\Xi(a_t)^{-1}|M_{m,n}^{(q)}(t)|
\le(1+t_+)^N
}
\]
throughout the entire inner forbidden chamber.

Therefore no extra tail estimate is needed there for the logarithmic spatial-weight theorem.

Because

\[
t_+
=\operatorname{arcosh}(1+m/q)+\operatorname{arcosh}(1+n/q),
\]
this is already the conjectured logarithmic K-type spatial cost.

Hence

\[
\boxed{\textbf{TF-A1: PASS.}}
\]

The only missing unrestricted spatial-tail estimate is genuinely the region

\[
t\ge t_++1.
\]

---

## 3. Sharp inner forbidden asymptotics

On proportional-K parameter sectors where the RF/SAC steepest-descent construction is uniform,

\[
\boxed{
M_{m,n}^{(q)}(t)
=e^{-q\Phi_-(\alpha,\beta,t)}
\times\text{ordinary-saddle amplitude}
}
\]
for

\[
0<t<t_-.
\]

The exact rate satisfies

\[
\Phi_->0,
\qquad
\Phi_-(t_-)=0.
\]

Near the inner fold,

\[
\boxed{
\Phi_-(t)\sim C_-(t_--t)^{3/2},
\qquad C_->0.
}
\]

Thus the inner chamber has a sharp large-deviation description even though this sharpness is not required merely to prove the spatial Schwartz weight.

---

## 4. Outer forbidden asymptotics

Likewise on uniform SAC sectors,

\[
\boxed{
M_{m,n}^{(q)}(t)
=e^{-q\Phi_+(\alpha,\beta,t)}
\times\text{ordinary-saddle amplitude}
}
\]
for

\[
t>t_+,
\]
with

\[
\Phi_+>0,
\qquad
\Phi_+(t_+)=0,
\]
and

\[
\boxed{
\Phi_+(t)\sim C_+(t-t_+)^{3/2}.
}
\]

Unlike the inner chamber, the outer chamber extends to infinite radial distance.  Consequently this is where the sharp unrestricted logarithmic Schwartz theorem needs a parameter-uniform tail slope or equivalent global rate estimate.

---

## 5. Two-sided atlas versus one-sided obstruction

The conceptual distinction is

\[
\boxed{
\text{asymptotic geometry is two-sided, but the global Schwartz obstruction is one-sided.}
}
\]

Both \(\Phi_-\) and \(\Phi_+\) matter for the semiclassical atlas.  Only \(\Phi_+\) matters for controlling arbitrary powers of radial distance because only the outer chamber reaches \(t=\infty\).

This removes a false extra gate from the refinement program.

---

## 6. Gate ledger

\[
\boxed{\textbf{TF-A1: PASS — inner chamber requires no extra Schwartz tail theorem.}}
\]

\[
\boxed{\textbf{TF-A2: PASS — two-sided forbidden rates assembled with the global spatial-weight logic.}}
\]

The remaining sharp spatial gate is exactly

\[
\boxed{\textbf{SR-B1b — unrestricted two-high-K outer tail.}}
\]

---

## Claim firewall

- CHH is used to control the inner chamber at the level of the Harish--Chandra majorant; it does not replace the sharper RF-C inner rate.
- The inner and outer forbidden rates are distinct branches.
- `t_-` and `t_+` are radial/caustic variables, not Harish--Chandra spectral parameters.
- No geometric hyperbolic triangle theorem is inferred merely from the algebraic formulas for `t_±`.
