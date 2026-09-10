# Off-Diagonal Rate Surface Closure

## Status

This note extends the diagonal proportional K-type analysis to

\[
m=\alpha q,\qquad n=\beta q,\qquad \alpha,\beta\ge0,
\]

and derives the full turning/caustic surface of the coefficient-extraction saddle geometry.

The central result is unexpectedly simple after hyperbolic reparameterization: the oscillatory chamber is bounded by a **hyperbolic triangle window**

\[
\boxed{|u_\alpha-u_\beta|<t<u_\alpha+u_\beta,}
\]

where

\[
\boxed{u_\alpha=\operatorname{arcosh}(\alpha+1),\qquad
u_\beta=\operatorname{arcosh}(\beta+1).}
\]

The two boundary sheets are fold caustics. The diagonal result is recovered by \(\alpha=\beta\).

---

## 1. General proportional saddle equation

From the Bergman coefficient-extraction representation, with

\[
r=\tanh\frac t2,
\]

the exponential phase is

\[
\Psi_{\alpha,\beta,r}(z)
=
\beta\log(z+r)
-(\beta+2)\log(1+rz)
-\alpha\log z.
\]

The saddle equation is

\[
\frac{\beta}{z+r}
-
\frac{r(\beta+2)}{1+rz}
-
\frac{\alpha}{z}=0,
\]

or

\[
\boxed{
r(\alpha+2)z^2+Bz+\alpha r=0,}
\]

with

\[
\boxed{B=(\alpha-\beta)+(\alpha+\beta+2)r^2.}
\]

The saddle discriminant is therefore

\[
\boxed{
\Delta_{\rm sad}(\alpha,\beta,r)
=
\bigl[(\alpha-\beta)+(\alpha+\beta+2)r^2\bigr]^2
-4\alpha(\alpha+2)r^2.
}
\]

This formula is exact.

---

## 2. Exact factorization of the caustic equation

Set

\[
p_\alpha=\sqrt{\alpha(\alpha+2)},\qquad
p_\beta=\sqrt{\beta(\beta+2)},\qquad
C=\alpha+\beta+2.
\]

The equation \(\Delta_{\rm sad}=0\) is equivalent to

\[
(\alpha-\beta)+Cr^2=\pm2p_\alpha r.
\]

Solving the resulting quadratic in \(r\) gives the two nonnegative turning radii

\[
\boxed{
r_-=\frac{|p_\alpha-p_\beta|}{\alpha+\beta+2},}
\]

and

\[
\boxed{
r_+=\frac{p_\alpha+p_\beta}{\alpha+\beta+2}.}
\]

Thus the discriminant factorizes as

\[
\boxed{
\Delta_{\rm sad}
=(\alpha+\beta+2)^2
(r^2-r_-^2)(r^2-r_+^2).
}
\]

For \(\alpha,\beta>0\),

\[
0\le r_-<r_+<1.
\]

Hence there are generically **two** turning surfaces, not one.

---

## 3. Hyperbolic reparameterization

Introduce

\[
\boxed{
\alpha+1=\cosh u_\alpha,
\qquad
\beta+1=\cosh u_\beta,
}
\]

with \(u_\alpha,u_\beta\ge0\). Then

\[
p_\alpha=\sinh u_\alpha,
\qquad
p_\beta=\sinh u_\beta,
\]

and

\[
\alpha+\beta+2
=
\cosh u_\alpha+\cosh u_\beta.
\]

Using the hyperbolic sum identities,

\[
\frac{\sinh u_\alpha+\sinh u_\beta}
{\cosh u_\alpha+\cosh u_\beta}
=
\tanh\frac{u_\alpha+u_\beta}{2},
\]

while

\[
\frac{|\sinh u_\alpha-\sinh u_\beta|}
{\cosh u_\alpha+\cosh u_\beta}
=
\left|\tanh\frac{u_\alpha-u_\beta}{2}\right|.
\]

Therefore

\[
\boxed{
r_+=\tanh\frac{u_\alpha+u_\beta}{2},}
\]

\[
\boxed{
r_-=\tanh\frac{|u_\alpha-u_\beta|}{2}.}
\]

Since \(r=\tanh(t/2)\), the turning lengths are simply

\[
\boxed{
t_+=u_\alpha+u_\beta,}
\]

and

\[
\boxed{
t_-=|u_\alpha-u_\beta|.}
\]

Equivalently,

\[
\boxed{
|\operatorname{arcosh}(\alpha+1)-\operatorname{arcosh}(\beta+1)|
\le t\le
\operatorname{arcosh}(\alpha+1)+\operatorname{arcosh}(\beta+1).
}
\]

This is the exact off-diagonal caustic surface.

---

## 4. Hyperbolic triangle interpretation

The discriminant sign is now transparent:

\[
\boxed{
\Delta_{\rm sad}<0
\iff
t_-<t<t_+.
}
\]

In this chamber the two saddles are complex conjugates and one obtains the oscillatory/stationary-phase regime.

Outside it,

\[
\boxed{
\Delta_{\rm sad}>0
\iff
t<t_-\quad\text{or}\quad t>t_+,
}
\]

and the saddles are real, giving exponential/forbidden behavior after the appropriate contour branch is selected.

Thus the semiclassical support condition has exactly the form of the triangle inequality for three nonnegative hyperbolic radial variables:

\[
\boxed{
|u_\alpha-u_\beta|<t<u_\alpha+u_\beta.
}
\]

This interpretation is algebraically derived here; it should not yet be identified with a geometric triangle theorem for FCIG without a separate representation/geometric correspondence.

---

## 5. Why the inner forbidden region is necessary

For \(\alpha\ne\beta\), the lower caustic satisfies

\[
t_->0.
\]

At the group identity \(t=0\), K-type orthogonality gives

\[
\langle e_m,e_n\rangle=0
\qquad(m\ne n).
\]

In the proportional regime \(|m-n|=O(q)\), the explicit matrix coefficient also contains a factor of the form

\[
\left(\tanh\frac t2\right)^{|m-n|},
\]

which is exponentially suppressing at fixed small \(t\). Thus the inner forbidden chamber

\[
0<t<t_-
\]

is not an artifact of the saddle algebra: it is consistent with exact K-type orthogonality at the identity.

The outer forbidden chamber

\[
t>t_+
\]

is the off-diagonal continuation of the diagonal radial decay studied in RF-A.

---

## 6. Diagonal recovery

Set

\[
\alpha=\beta=\lambda.
\]

Then

\[
u_\alpha=u_\beta=u_\lambda
=\operatorname{arcosh}(\lambda+1).
\]

Hence

\[
t_-=0,
\]

and

\[
\boxed{
t_+=2\operatorname{arcosh}(\lambda+1),}
\]

exactly recovering the diagonal turning point

\[
\cosh\frac{t_*}{2}=\lambda+1.
\]

Thus the earlier JA-B2/RF-A result is the diagonal slice of the full caustic surface.

---

## 7. Edge cases

If \(\beta=0\), then \(u_\beta=0\), so

\[
t_-=t_+=u_\alpha.
\]

The oscillatory chamber collapses. This is consistent with a lowest-K-type versus proportional-high-K-type transition having a single concentration radius rather than an extended oscillatory interval.

Likewise for \(\alpha=0\).

This boundary degeneration should be treated separately from the generic two-fold-caustic case.

---

## 8. Fold structure and Airy expectation

At either generic boundary \(t=t_\pm\), two simple saddles coalesce:

\[
\Psi'(z_*)=0,
\qquad
\Psi''(z_*)=0.
\]

Away from exceptional degenerate parameter values, one expects

\[
\Psi'''(z_*)\ne0,
\]

so each sheet is a fold caustic and admits an Airy uniformization with

\[
t-t_\pm=O(q^{-2/3}).
\]

The diagonal outer sheet was normalized explicitly in RF-A. The off-diagonal inner and outer Airy constants remain to be computed.

---

## 9. FCIG phase diagram

The proportional K-type semiclassical phase diagram is therefore

\[
\boxed{
\begin{array}{ccl}
0<t<t_-&:&\text{inner forbidden / K-type mismatch},\\[2mm]
t_-<t<t_+&:&\text{oscillatory / two complex-conjugate saddles},\\[2mm]
t>t_+&:&\text{outer forbidden / radial separation}.
\end{array}}
\]

with

\[
\boxed{
t_\pm=u_\alpha\pm u_\beta}
\]

where the lower sign is understood in absolute value.

This upgrades the diagonal one-turning-point picture to a two-sheet caustic geometry.

---

## 10. Relation to the orbital Gamma window

The FCIG orbital kernel has transverse Fourier concentration

\[
\frac{|\xi|_{\rm peak}}q
\sim
2\tanh\frac L2.
\]

The representation-side caustics are controlled by

\[
\tanh\frac{t_\pm}{2}
=
r_\pm.
\]

Thus both sides continue to use the same natural disk/hyperbolic coordinate \(\tanh(\cdot/2)\), now with a nontrivial two-boundary structure on the representation side.

This remains a structural comparison only:

\[
\boxed{
\xi\ne t\ne m,n\ne\text{Harish--Chandra spectral parameter}.
}
\]

No identification is made without an explicit transform theorem.

---

## 11. Gate status

We record

\[
\boxed{\textbf{RF-B1: PASS — exact off-diagonal caustic surface.}}
\]

Specifically, the pass includes:

1. the exact general saddle discriminant;
2. its factorization into two turning radii;
3. the hyperbolic parameterization
   \(t_-=|u_\alpha-u_\beta|\), \(t_+=u_\alpha+u_\beta\);
4. the exact oscillatory chamber as a triangle-inequality window;
5. diagonal and lowest-K-type boundary checks.

The next gate is

\[
\boxed{\textbf{RF-B2 — Two-Sheet Airy Normalization}.}
\]

Its target is to compute the coalesced saddle \(z_*^\pm\), cubic coefficient \(\Psi'''_*\), radial unfolding coefficient \(\partial_t\Psi'_*\), and hence the exact Airy coordinates on both off-diagonal caustic sheets.

---

## Claim firewall

- The triangle inequality is an exact algebraic statement about the saddle discriminant after hyperbolic reparameterization; no stronger geometric interpretation is asserted.
- The sign of the discriminant identifies saddle type. A full global steepest-descent theorem still requires contour accessibility and branch bookkeeping.
- The two edge sheets can degenerate when \(\alpha=0\) or \(\beta=0\).
- The orbital Gamma-window variable and the K-type/radial variables remain distinct.
- No novelty claim is made.

## FCIG cross-references

- `proportional-k-type-rate-function.md`
- `steepest-descent-rate-closure.md`
- `explicit-rate-function-closure.md`
- `jacobi-asymptotic-closure.md`
- `parameter-uniform-matrix-decay.md`
- `centralizer-spectral-window.md`
