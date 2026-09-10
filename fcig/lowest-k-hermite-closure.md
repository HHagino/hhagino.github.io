# Lowest-K Hermite Closure

## BC-A2 — lowest-K sheet-merger double scaling

**Status (2026-09-10).**

\[
\boxed{\textbf{BC-A2: PASS — the }q\beta=O(1)\textbf{ sheet-merger chart is Hermite--Gaussian.}}
\]

This note closes the second boundary double scaling isolated in `uniform-remainder-closure.md`.  Together with the Bessel chart in `boundary-bessel-closure.md`, it completes the boundary atlas for the proportional-K semiclassical sector.

No literature-novelty claim is made.  Large-parameter Jacobi-to-Hermite limits are classical.  The precise FCIG scaling, normalization, and match to the previously derived caustic merger are derived here from the exact discrete-series matrix coefficient.

---

## 1. Regime and exact coefficient

Fix a nonnegative integer \(\nu\) and let

\[
m=m_q,\qquad \frac{m}{q}\to\alpha>0,\qquad n=\nu.
\]

Thus

\[
\beta=\frac{n}{q}=\frac{\nu}{q},
\qquad q\beta=\nu=O(1).
\]

For \(m\ge \nu\), the radial matrix coefficient can be written, up to the fixed unitary phase convention, as

\[
\boxed{
M_{\nu,m}^{(q)}(t)
=
\mathcal N_{\nu,m}(q)
\left(\cosh\frac t2\right)^{-2q}
\left(\tanh\frac t2\right)^{m-\nu}
P_\nu^{(m-\nu,2q-1)}
\left(1-2\tanh^2\frac t2\right),
}
\]

with

\[
\mathcal N_{\nu,m}(q)
=
\left(
\frac{\nu!\,\Gamma(2q+m)}
{m!\,\Gamma(2q+\nu)}
\right)^{1/2}.
\]

The Jacobi degree is now fixed while both parameters are large.

---

## 2. The merger point

Introduce

\[
\alpha+1=\cosh u_\alpha,
\qquad
p_\alpha=\sqrt{\alpha(\alpha+2)}=\sinh u_\alpha.
\]

When \(\beta\to0\), the two generic caustics

\[
t_-=u_\alpha-u_\beta,
\qquad
t_+=u_\alpha+u_\beta
\]

merge at

\[
\boxed{t=u_\alpha.}
\]

The correct local scale is

\[
\boxed{
t=u_\alpha+\frac{\tau}{\sqrt q}.}
\]

Set

\[
r=\tanh\frac t2,
\qquad
x(t)=1-2r^2.
\]

At the merger,

\[
r_\alpha^2=\frac{\alpha}{\alpha+2},
\qquad
x_0=x(u_\alpha)=\frac{2-\alpha}{\alpha+2}.
\]

Moreover

\[
\boxed{
x'(u_\alpha)
=-\frac{4\sqrt\alpha}{(\alpha+2)^{3/2}}.}
\]

Hence

\[
x(t)=x_0-rac{c_\alpha\tau}{\sqrt q}+O(q^{-1}),
\qquad
c_\alpha:=\frac{4\sqrt\alpha}{(\alpha+2)^{3/2}}.
\]

---

## 3. Fixed-degree Jacobi contraction

Let

\[
A_q=m-\nu=\alpha q+O(1),
\qquad
B_q=2q-1.
\]

The Jacobi differential equation is

\[
(1-x^2)y''+[B_q-A_q-(A_q+B_q+2)x]y'
+\nu(\nu+A_q+B_q+1)y=0.
\]

Its large-q equilibrium point is

\[
\frac{B_q-A_q}{A_q+B_q}
\longrightarrow
\frac{2-\alpha}{2+\alpha}=x_0.
\]

Write

\[
x=x_0+\frac{c_\alpha y}{\sqrt q}.
\]

Because

\[
1-x_0^2=\frac{8\alpha}{(\alpha+2)^2},
\qquad
c_\alpha^2=\frac{16\alpha}{(\alpha+2)^3},
\]

the leading rescaled differential equation is

\[
\boxed{Y''-2yY'+2\nu Y=0.}
\]

Thus the canonical polynomial is the physicists' Hermite polynomial \(H_\nu(y)\).

Matching the leading coefficient of the Jacobi polynomial gives

\[
\boxed{
q^{-\nu/2}
P_\nu^{(m-\nu,2q-1)}
\left(x_0+\frac{c_\alpha y}{\sqrt q}\right)
\longrightarrow
\frac1{\nu!}
\left(\frac{\alpha}{\alpha+2}\right)^{\nu/2}
H_\nu(y).
}
\]

Since the FCIG radial scaling has \(y=-\tau+O(q^{-1/2})\),

\[
q^{-\nu/2}P_\nu^{(m-\nu,2q-1)}(x(t))
\longrightarrow
\frac1{\nu!}
\left(\frac{\alpha}{\alpha+2}\right)^{\nu/2}
H_\nu(-\tau).
\]

This is the fixed-degree Jacobi-to-Hermite contraction in the exact FCIG normalization.

---

## 4. Lowest-vector Gaussian envelope

For \(\nu=0\), the squared matrix coefficient is

\[
|M_{0,m}^{(q)}(t)|^2
=
\frac{\Gamma(2q+m)}{m!\Gamma(2q)}
\operatorname{sech}^{4q}\frac t2
\tanh^{2m}\frac t2.
\]

This is the negative-binomial mass function in \(m\).  At \(t=u_\alpha\),

\[
\mathbb E[m]=\alpha q,
\qquad
\operatorname{Var}(m)=\frac12q\alpha(\alpha+2).
\]

Under

\[
t=u_\alpha+\frac{\tau}{\sqrt q},
\qquad m=\alpha q+O(1),
\]

the standardized displacement is

\[
\frac{m-\mathbb E_t[m]}{\sqrt{\operatorname{Var}_t(m)}}
=-\sqrt2\,\tau+O(q^{-1/2}).
\]

Stirling's formula / the local central-limit expansion therefore gives

\[
\boxed{
q^{1/4}M_{0,m}^{(q)}
\left(u_\alpha+\frac{\tau}{\sqrt q}\right)
\longrightarrow
[\pi\alpha(\alpha+2)]^{-1/4}e^{-\tau^2/2}
}
\]

up to the fixed unitary phase.

---

## 5. Full Hermite--Gaussian limit

Relative to the \(\nu=0\) coefficient,

\[
\frac{\mathcal N_{\nu,m}(q)}{\mathcal N_{0,m}(q)}
=
\left(
\frac{\nu!\Gamma(2q)}{\Gamma(2q+\nu)}
\right)^{1/2}
\sim
\sqrt{\nu!}\,(2q)^{-\nu/2}.
\]

Also

\[
r^{-\nu}\to
\left(\frac{\alpha+2}{\alpha}\right)^{\nu/2}.
\]

Combining these factors with the Jacobi contraction gives the exact cancellation

\[
\boxed{
q^{1/4}M_{\nu,m}^{(q)}
\left(u_\alpha+\frac{\tau}{\sqrt q}\right)
\longrightarrow
[\pi\alpha(\alpha+2)]^{-1/4}
\frac{H_\nu(-\tau)}{\sqrt{2^\nu\nu!}}
e^{-\tau^2/2}.
}
\]

Equivalently, using

\[
D_\nu(z)=2^{-\nu/2}e^{-z^2/4}H_\nu(z/\sqrt2),
\]

we obtain

\[
\boxed{
q^{1/4}M_{\nu,m}^{(q)}
\left(u_\alpha+\frac{\tau}{\sqrt q}\right)
\longrightarrow
[\pi\alpha(\alpha+2)]^{-1/4}
\frac{D_\nu(-\sqrt2\tau)}{\sqrt{\nu!}}.
}
\]

Thus the canonical lowest-K sheet-merger model is Hermite--Gaussian, equivalently an integer-order parabolic-cylinder function.

---

## 6. Match to the two generic caustics

For \(\beta=\nu/q\),

\[
u_\beta=\operatorname{arcosh}(1+\beta)
=\sqrt{2\beta}+O(\beta^{3/2}).
\]

Therefore

\[
t_\pm
=u_\alpha\pm\sqrt{\frac{2\nu}{q}}+O(q^{-3/2}).
\]

In the merger coordinate \(\tau=\sqrt q(t-u_\alpha)\),

\[
\boxed{
\tau_\pm\to\pm\sqrt{2\nu}.
}
\]

The parabolic-cylinder/Hermite model therefore resolves both folds simultaneously on one \(O(q^{-1/2})\) chart.

For large \(\nu\), Hermite functions have their classical turning points at

\[
|\tau|\sim\sqrt{2\nu},
\]

with Airy transition layers.  Hence

\[
\boxed{
\text{fixed-}\nu\text{ Hermite merger chart}
\quad\xrightarrow{\nu\to\infty}\quad
\text{two separated generic Airy charts}.
}
\]

This is the required overlap with RF-B2 and UR-A1.

---

## 7. Completed proportional-K semiclassical atlas

The local canonical charts are now:

\[
\boxed{
\begin{array}{ccl}
q|\alpha-\beta|=O(1),\ t=O(q^{-1})
&\longrightarrow&\text{Bessel},\\[1mm]
\alpha,\beta>0\text{ away from boundary collapse}
&\longrightarrow&\text{saddle / Airy},\\[1mm]
q\beta=O(1),\ t-u_\alpha=O(q^{-1/2})
&\longrightarrow&\text{Hermite--Gaussian / parabolic cylinder}.
\end{array}}
\]

Together with the global forbidden rate functions and oscillatory chamber derived in RF-C, these charts cover the proportional-K semiclassical phase diagram, with standard overlap regions between Bessel--Airy and Hermite--Airy descriptions.

---

## 8. Gate status

\[
\boxed{\textbf{BC-A2: PASS — lowest-K sheet merger is Hermite--Gaussian.}}
\]

Consequently the two boundary gates isolated by UR-A2 are both closed:

\[
\boxed{\textbf{BC-A1: PASS},\qquad \textbf{BC-A2: PASS}.}
\]

The proportional-K local asymptotic atlas is therefore closed at the level of leading canonical models and generic Airy matching.

A stronger publication-level theorem should still state explicit uniform error constants on compact parameter sets and audit phase conventions globally.  Those are remainder/normalization refinements, not missing canonical regimes.

---

## References

1. NIST Digital Library of Mathematical Functions, §18.15(vi): large-parameter Jacobi approximations in terms of Hermite polynomials.
2. NIST Digital Library of Mathematical Functions, §18.7(iii): Jacobi-to-Hermite and related classical limit relations.
3. G. López and N. M. Temme, large-parameter approximations of Jacobi polynomials in terms of Hermite polynomials (cited by DLMF §18.15(vi)).
4. G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloquium Publications 23, 1975.

## Claim firewall

- The existence of large-parameter Jacobi/Hermite asymptotics is established literature.
- The FCIG scaling \(m/q\to\alpha\), fixed \(\nu\), \(t=u_\alpha+\tau/\sqrt q\), the constants \(c_\alpha\), the normalized Hermite--Gaussian limit, and the match \(\tau_\pm\to\pm\sqrt{2\nu}\) are derived here.
- The result concerns discrete-series radial matrix coefficients, not Harish--Chandra characters.
- The Hermite variable is a local sheet-merger coordinate; it is not a Harish--Chandra spectral parameter.
- Leading canonical closure does not by itself supply globally uniform numerical remainder constants at every parameter boundary.