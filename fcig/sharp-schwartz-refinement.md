# Sharp Harish--Chandra--Schwartz Refinement

## From structural closure to explicit parameter exponents

**Status (2026-09-10).**

The preceding note `unrestricted-schwartz-closure.md` closes the existence/topological part of the unrestricted discrete-series Schwartz problem.  This note begins the quantitative refinement requested after that closure.

The main correction is conceptual:

\[
\boxed{
\text{existence of a polynomial parameter bound}
\neq
\text{knowledge of its optimal exponents}.
}
\]

The derivative exponents can be made explicit and sharp immediately.  The additional cost produced by arbitrary spatial Schwartz weights is subtler; the exact lowest-vector model shows that this cost is naturally logarithmic in the K-type displacement, suggesting that a raw polynomial estimate is far from optimal.

No novelty claim is made.

---

## 1. Setup

Let

\[
\pi_q=D^+_{2q-1},
\qquad
M_{m,n}^{(q)}(g)=\langle e_m,\pi_q(g)e_n\rangle,
\]

with the orthonormal holomorphic K-type basis \(e_n\), \(n\ge0\).

For

\[
D,E\in U(\mathfrak g_\mathbb C),
\qquad
r=\deg D,
\quad
s=\deg E,
\]

define

\[
p_{D,E,N}(f)
=
\sup_{g\in G}
(1+\sigma(g))^N\Xi(g)^{-1}|L_DR_Ef(g)|.
\]

The generators act by

\[
K_0e_j=(q+j)e_j,
\]

\[
K_+e_j=\sqrt{(j+1)(2q+j)}\,e_{j+1},
\]

\[
K_-e_j=\sqrt{j(2q+j-1)}\,e_{j-1}.
\]

---

## 2. Exact polynomial degree of invariant derivatives

For \(q\ge1\) and \(j\ge0\),

\[
\sqrt{(j+1)(2q+j)}\le q+j+1,
\]

and

\[
\sqrt{j(2q+j-1)}\le q+j.
\]

Therefore every fixed word \(D\) of degree \(r\) satisfies

\[
\boxed{
\|d\pi_q(D)e_j\|
\le C_D(1+q+j)^r,
}
\]

with \(C_D\) independent of \(q,j\).  The same statement holds on the other side for \(E\).

Since \(K=SO(2)\) and every K-type occurring here is one-dimensional, the Cowling--Haagerup--Howe tempered matrix-coefficient estimate has no K-dimension loss.  Hence

\[
\boxed{
|L_DR_EM_{m,n}^{(q)}(g)|
\le
C_{D,E}
(1+q+m)^r(1+q+n)^s\Xi(g).
}
\tag{2.1}
\]

Equivalently,

\[
\boxed{
p_{D,E,0}(M_{m,n}^{(q)})
\le
C_{D,E}(1+q+m)^r(1+q+n)^s.}
\tag{2.2}
\]

This improves the previous unspecified polynomial \(P_{D,E,0}\) to an explicit degree.

---

## 3. Sharpness in derivative degree

The exponents \(r\) and \(s\) cannot be lowered uniformly over all enveloping-algebra elements of those degrees.

Indeed, for

\[
D=K_0^r,
\qquad
E=K_0^s,
\]

one has exactly

\[
L_DR_EM_{m,n}^{(q)}(e)
=(q+m)^r(q+n)^s\delta_{mn}
\]

up to the fixed left/right sign convention.  On the diagonal \(m=n\), this gives the matching lower growth.

Thus

\[
\boxed{
\textbf{SR-A1: PASS — derivative parameter degrees }(r,s)\textbf{ are sharp.}
}
\]

The only non-explicit part of the full Schwartz seminorm is therefore the cost of the spatial factor \((1+\sigma)^N\).

---

## 4. Exact lowest-vector benchmark for the spatial weight

The coefficient with one lowest K-type has the exact radial square

\[
\boxed{
|M_{0,m}^{(q)}(t)|^2
=
\frac{\Gamma(2q+m)}{m!\Gamma(2q)}
\operatorname{sech}^{4q}\frac t2
\tanh^{2m}\frac t2.
}
\tag{4.1}
\]

Put

\[
y=\tanh^2\frac t2.
\]

The radial logarithm is, modulo a constant independent of \(t\),

\[
2m\log\tanh\frac t2-4q\log\cosh\frac t2
=
m\log y+2q\log(1-y).
\]

Its unique maximum occurs at

\[
\boxed{
y_*=\frac{m}{m+2q}.}
\]

Therefore the natural radial center is exactly

\[
\boxed{
t_*(q,m)=\operatorname{arcosh}\left(1+\frac mq\right).}
\tag{4.2}
\]

For large \(m/q\),

\[
t_*(q,m)
=
\log\left(2\frac mq\right)+O(q/m).
\]

Hence the spatial Schwartz factor at the classical concentration radius is only

\[
\boxed{
(1+t_*)^N
\asymp
\left[1+\log\left(1+\frac mq\right)\right]^N.
}
\tag{4.3}
\]

This is an important diagnostic: a parameter polynomial inserted solely to pay for \((1+\sigma)^N\) is generically very crude.

---

## 5. Expected sharp spatial scale

The exact two-sheet caustic geometry of the SAC branch gives, in proportional variables,

\[
t_+=u_\alpha+u_\beta,
\qquad
u_\gamma:=\operatorname{arcosh}(1+\gamma),
\]

with \(\alpha=m/q\), \(\beta=n/q\).  Thus the largest natural radial scale is

\[
\boxed{
T_{q,m,n}
:=
\operatorname{arcosh}\left(1+\frac mq\right)
+
\operatorname{arcosh}\left(1+\frac nq\right).
}
\tag{5.1}
\]

For large K-types,

\[
T_{q,m,n}
=
O\!\left(
1+\log\left(1+\frac mq\right)
+
\log\left(1+\frac nq\right)
\right).
\]

This motivates the sharper target

\[
\boxed{
\begin{aligned}
p_{D,E,N}(M_{m,n}^{(q)})
\stackrel{?}{\le}
&C_{D,E,N}
(1+q+m)^r(1+q+n)^s\\
&\times
(1+T_{q,m,n})^N,
\end{aligned}}
\tag{5.2}
\]

or a normalization-equivalent variant with a fixed additional low-degree factor.

Equation (5.2) is **not yet claimed as proved**.  It is the quantitative form that the remaining analysis should test.  If true, it would replace the unspecified spatial polynomial of UQ-A2 by the geometrically natural logarithmic K-type cost.

---

## 6. Why the logarithmic target is compatible with SAC

The SAC atlas says that the large coefficient region is bounded by the caustics

\[
t_-\le t\le t_+
\]

with Airy, Bessel and Hermite charts at the degenerations.  Outside the outer caustic the coefficient acquires a positive forbidden rate

\[
M\sim e^{-q\Phi_+}.
\]

Thus the radial Schwartz weight should be paid primarily near the classically allowed/turning region, whose center moves only logarithmically with \(m/q,n/q\).

This is precisely the regime in which a bound such as (5.2) is stronger than an arbitrary parameter polynomial yet still compatible with the local asymptotics.

The remaining proof task is to make the words “outside the outer caustic” quantitative uniformly when \(q,m,n\) enter different scaling regimes, then patch with the Bessel and Hermite boundary charts.

---

## 7. Inverse Fourier constants

For a rank-one operator

\[
A=|e_n\rangle\langle e_m|,
\]

the discrete-series synthesis is

\[
h_{A,q}=d_qM_{m,n}^{(q)},
\qquad
d_q=\frac{2q-1}{4\pi}.
\]

Therefore every sharp matrix-coefficient seminorm immediately produces the corresponding inverse-Fourier bound

\[
\boxed{
p_{D,E,N}(h_{A,q})
=d_q\,p_{D,E,N}(M_{m,n}^{(q)}).}
\tag{7.1}
\]

In particular, the proven \(N=0\) estimate is

\[
\boxed{
p_{D,E,0}(h_{A,q})
\le
\frac{2q-1}{4\pi}
C_{D,E}(1+q+m)^r(1+q+n)^s.}
\tag{7.2}
\]

Thus the inverse Fourier normalization contributes **exactly one formal-degree factor**, asymptotic to \(q/(2\pi)\), and no hidden exponential parameter cost.

This isolates all remaining uncertainty in the spatially weighted seminorm itself.

\[
\boxed{
\textbf{SR-A2: PASS — rank-one inverse-Fourier }q\textbf{-normalization is explicit.}
}
\]

---

## 8. Relation between the sharp local and global estimates

There are now two complementary bounds:

1. global tempered majorant
   \[
   |L_DR_EM|\lesssim
   (1+q+m)^r(1+q+n)^s\Xi(t),
   \]
2. local semiclassical asymptotics
   \[
   M\sim
   q^{-1/2}A e^{-q\Phi_+}
   \]
   in the outer forbidden chamber, with Airy replacement near \(t_+\).

The natural stitch point is defined implicitly by comparing exponents:

\[
\boxed{
q\Phi_+(\alpha,\beta,t)
\approx
\frac t2
+N\log(1+t)
+\log P(q,m,n).
}
\tag{8.1}
\]

Near the caustic,

\[
\Phi_+(t)
\sim C_+(t-t_+)^{3/2},
\]

so the extra distance beyond the turning point at which the WKB bound beats a prescribed Schwartz weight satisfies schematically

\[
\boxed{
 t-t_+
\asymp
\left[
\frac{t_+/2+N\log(1+t_+)+\log P}{qC_+}
\right]^{2/3}.
}
\tag{8.2}
\]

This is a quantitative SAC-to-Schwartz overlap law.  It reduces to the familiar \(q^{-2/3}\) Airy scale when the numerator remains \(O(1)\), but automatically widens by logarithmic factors when the K-type center moves outward.

---

## 9. Current refinement ledger

\[
\boxed{
\begin{array}{ll}
\text{SR-A1} & \text{PASS — optimal derivative degrees},\\
\text{SR-A2} & \text{PASS — exact rank-one formal-degree cost},\\
\text{SR-B1} & \text{OPEN — prove logarithmic spatial-weight bound (5.2)},\\
\text{SR-B2} & \text{OPEN — make the stitch law (8.2) uniform across all charts}.
\end{array}}
\]

The earlier UQ-A2 structural closure remains valid as an existence/topology statement.  What remains open is its **sharp quantitative refinement**, not membership in the Harish--Chandra Schwartz space.

---

## References

1. M. Cowling, U. Haagerup, R. Howe, *Almost L2 matrix coefficients*, J. Reine Angew. Math. 387 (1988), 97--110.
2. W. H. Barker (with material of R. J. Stanton, P. A. Tomas and H. Schlichtkrull in the SL(2,R) harmonic-analysis program), *Lp Harmonic Analysis on SL(2,R)*, Memoirs AMS 76 (1988), no. 393.  In particular the chapters on discrete series, asymptotic approximation, inverse transform and zero-Schwartz space.
3. Harish-Chandra, foundational work on the Schwartz algebra and discrete series.
4. The FCIG notes `global-off-diagonal-rate-closure.md`, `uniform-remainder-closure.md`, `boundary-bessel-closure.md`, `lowest-k-hermite-closure.md`, and `semiclassical-preprint-v1.md`.

## Claim firewall

- CHH supplies the unweighted Xi-majorant for K-finite vectors in tempered representations; it does not by itself insert arbitrary powers of the radial length.
- The derivative degrees in (2.2) are proved and sharp in the stated sense.
- The exact lowest-vector concentration radius (4.2) is proved directly from the coefficient formula.
- The logarithmic spatial estimate (5.2) is a target, not yet a theorem.
- Barker/Stanton--Tomas support the Schwartz Fourier topology for SL(2,R); they are not cited here as having printed the FCIG-optimal exponents in (5.2).
- The SAC-to-Schwartz stitch equation is an exponent-comparison principle; full uniform constants still require a chart-by-chart remainder audit.
