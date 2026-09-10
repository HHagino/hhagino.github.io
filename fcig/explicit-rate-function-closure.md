# Explicit Rate-Function Closure in the Diagonal Proportional K-Type Sector

## Status

This note closes the next step after `steepest-descent-rate-closure.md`. We stay in the diagonal proportional regime

\[
m=n=\lambda q,\qquad \lambda>0,
\]

and make the forbidden-region rate function and the turning-point Airy normalization explicit.

The starting coefficient-extraction phase is

\[
\Psi_{\lambda,r}(z)
=\lambda\log(z+r)-(\lambda+2)\log(1+rz)-\lambda\log z,
\qquad r=\tanh\frac t2,
\]

with the global Bergman factor \(\cosh(t/2)^{-2q}\).

The diagonal normalization ratio cancels at exponential order.

---

## 1. Saddle equation and turning point

The saddle equation is

\[
\Psi'_{\lambda,r}(z)=0
\]

or

\[
\boxed{
(\lambda+2)z^2+2r(\lambda+1)z+\lambda=0.
}
\]

Hence

\[
\boxed{
z_\pm
=\frac{-r(\lambda+1)\pm
\sqrt{r^2(\lambda+1)^2-\lambda(\lambda+2)}}{\lambda+2}.
}
\]

The turning point is determined by saddle collision:

\[
r_*^2(\lambda+1)^2=\lambda(\lambda+2).
\]

Equivalently,

\[
\boxed{
\cosh\frac{t_*}{2}=\lambda+1,
\qquad
t_*(\lambda)=2\operatorname{arcosh}(\lambda+1).
}
\]

At collision,

\[
\boxed{
z_*=-\sqrt{\frac{\lambda}{\lambda+2}}.}
\]

This agrees with the turning-point condition in the varying-parameter Jacobi asymptotics after the standard Jacobi symmetry reduction.

---

## 2. Forbidden-region variables

Assume

\[
t>t_*(\lambda).
\]

Write

\[
C=\cosh\frac t2,\qquad
S=\sinh\frac t2,\qquad
a=\lambda+1,
\]

and

\[
\boxed{
Q=\sqrt{C^2-a^2}>0.
}
\]

Then

\[
\sqrt{r^2a^2-\lambda(\lambda+2)}=\frac{Q}{C}.
\]

The contour-accessible decaying saddle is the root nearer the origin,

\[
\boxed{
z_{\mathrm{dec}}
=\frac{-aS+Q}{C(\lambda+2)}.}
\]

Set \(x=-z_{\mathrm{dec}}>0\). Thus

\[
\boxed{x=\frac{aS-Q}{C(\lambda+2)}.}
\]

Useful exact identities are

\[
\boxed{
r-x=\frac{S+Q}{C(\lambda+2)},}
\]

and, using

\[
(S-Q)(S+Q)=\lambda(\lambda+2),
\]

one obtains

\[
\boxed{
1-rx
=\frac{(S+Q)(aS-Q)}{\lambda C^2(\lambda+2)}.
}
\]

---

## 3. Explicit forbidden-region rate

The exponential rate is

\[
\Phi_\lambda(t)
=2\log C-\Re\Psi_{\lambda,r}(z_{\mathrm{dec}}).
\]

Substituting the identities above gives the elementary logarithmic closed form

\[
\boxed{
\begin{aligned}
\Phi_\lambda(t)
={}&2\log(S+Q)
+2(\lambda+1)\log(aS-Q)\\
&-2(\lambda+1)\log C
-(\lambda+2)\log\lambda
-(\lambda+2)\log(\lambda+2).
\end{aligned}}
\]

where

\[
a=\lambda+1,
\qquad
Q=\sqrt{\cosh^2(t/2)-(\lambda+1)^2}.
\]

At the turning point \(Q=0\), the identities

\[
C_*=a,
\qquad
S_*^2=\lambda(\lambda+2)
\]

imply exactly

\[
\boxed{\Phi_\lambda(t_*)=0.}
\]

For the accessible forbidden saddle and \(t>t_*\), the steepest-descent branch gives

\[
\boxed{\Phi_\lambda(t)>0.}
\]

Therefore, away from the turning layer,

\[
\boxed{
M_{\lambda q,\lambda q}^{(q)}(t)
=\mathcal A_\lambda(t,q)
\exp\bigl(-q\Phi_\lambda(t)\bigr),
}
\]

with \(\mathcal A_\lambda(t,q)\) admitting the usual algebraic steepest-descent expansion beginning at order \(q^{-1/2}\) on compact forbidden subregions.

---

## 4. A hyperbolic reparameterization

Define

\[
\boxed{
\chi=\operatorname{arcosh}\left(\frac{C}{\lambda+1}\right),
\qquad t>t_*.
}
\]

Then

\[
C=(\lambda+1)\cosh\chi,
\qquad
Q=(\lambda+1)\sinh\chi.
\]

Hence the same rate may be rewritten entirely in hyperbolic elementary functions by substituting these expressions into the boxed formula above. This reparameterization makes the distance from the caustic explicit: \(\chi=0\) at \(t=t_*\).

No claim is made that \(\chi\) is the Harish--Chandra spectral parameter; it is only a convenient turning-point coordinate.

---

## 5. Cubic coefficient at the saddle collision

The phase derivatives are

\[
\Psi'''(z)
=
\frac{2\lambda}{(z+r)^3}
-\frac{2r^3(\lambda+2)}{(1+rz)^3}
-\frac{2\lambda}{z^3}.
\]

At \((z_*,t_*)\), direct simplification yields

\[
\boxed{
\Psi'''(z_*,t_*)
=
2\sqrt{\frac{\lambda+2}{\lambda}}
\left(\lambda^3+5\lambda^2+8\lambda+4\right).
}
\]

The polynomial factor may also be written

\[
\lambda^3+5\lambda^2+8\lambda+4
=(\lambda+1)(\lambda+2)^2.
\]

Therefore the cubic coefficient has the cleaner form

\[
\boxed{
\Psi'''_*
=
2(\lambda+1)(\lambda+2)^2
\sqrt{\frac{\lambda+2}{\lambda}}.
}
\]

It is strictly positive for \(\lambda>0\).

---

## 6. Linear unfolding in the radial parameter

The derivative of the saddle equation with respect to \(t\), evaluated at the collision point, is especially simple:

\[
\boxed{
\partial_t\Psi'(z_*,t_*)=-(\lambda+2).
}
\]

Thus, with

\[
w=z-z_*,\qquad \tau=t-t_*,
\]

we obtain the local phase expansion

\[
\boxed{
\Psi(z,t)-\Psi(z_*,t_*)
=
\frac{\Psi'''_*}{6}w^3
-(\lambda+2)\tau w
+O(w^4+\tau w^2+\tau^2w).
}
\]

This is the canonical two-coalescing-saddles normal form.

---

## 7. Explicit Airy scaling

Set

\[
\boxed{
\kappa_\lambda
:=
\left(\frac{\Psi'''_*}{2}\right)^{1/3}
=
\left[
(\lambda+1)(\lambda+2)^2
\sqrt{\frac{\lambda+2}{\lambda}}
\right]^{1/3}.
}
\]

Introduce

\[
\boxed{
s=q^{1/3}\kappa_\lambda w.}
\]

Then

\[
q\frac{\Psi'''_*}{6}w^3=\frac{s^3}{3}.
\]

The linear term becomes

\[
-q(\lambda+2)\tau w
=
-\zeta\,s,
\]

where the Airy coordinate is

\[
\boxed{
\zeta
=
q^{2/3}
\frac{\lambda+2}{\kappa_\lambda}
(t-t_*).
}
\]

Therefore the local integral reduces, after the standard steepest contour normalization, to the Airy model

\[
\boxed{
\int e^{s^3/3-\zeta s}\,ds,
}
\]

up to the conventional contour-dependent factor and analytic amplitude.

The turning layer is consequently

\[
\boxed{
t-t_*=O(q^{-2/3}),}
\]

while

\[
\boxed{z-z_*=O(q^{-1/3}).}
\]

At \(\zeta=0\), the leading amplitude is of order \(q^{-1/3}\), matching the standard Airy turning-point law for varying Jacobi asymptotics.

---

## 8. Local rate expansion beyond the caustic

The Airy exponent shows that for \(t>t_*\) but close to the turning point, the forbidden-region rate has the universal \(3/2\)-law

\[
\boxed{
\Phi_\lambda(t)
\asymp
\frac{2}{3}
\left(\frac{\lambda+2}{\kappa_\lambda}\right)^{3/2}
(t-t_*)^{3/2},
}
\]

up to the branch/orientation convention of the canonical Airy coordinate.

Equivalently, the transition from oscillatory to exponentially decaying behavior is governed by the standard fold-caustic exponent \(3/2\).

This statement should be understood locally near \(t_*\); the exact global forbidden rate is the logarithmic expression in Section 3.

---

## 9. FCIG semiclassical interpretation

The orbital branch previously produced the exact Gamma spectral window

\[
|\xi|_{\mathrm{peak}}
\sim
2q\tanh\frac L2.
\]

The representation branch now has an explicit proportional-K-type phase diagram controlled by

\[
r=\tanh\frac t2,
\]

with caustic

\[
\cosh\frac{t_*}{2}=\lambda+1.
\]

Thus both branches organize their semiclassical geometry using the same hyperbolic disk coordinate \(\tanh(\cdot/2)\), while remaining different typed variables.

We retain the firewall

\[
\boxed{
\xi\neq t\neq n\neq\text{Harish--Chandra spectral parameter}.
}
\]

A transform theorem is still required before any equality of these variables may be asserted.

---

## 10. Gate status

We record

\[
\boxed{\textbf{RF-A: PASS — explicit diagonal forbidden rate and Airy normalization.}}
\]

More precisely, RF-A closes:

1. the exact algebraic forbidden saddle;
2. the explicit elementary logarithmic rate \(\Phi_\lambda(t)\);
3. the exact turning value \(\Phi_\lambda(t_*)=0\);
4. the cubic coefficient \(\Psi'''_*\);
5. the radial unfolding coefficient \(\partial_t\Psi'_*\);
6. the explicit Airy coordinate \(\zeta\sim q^{2/3}(t-t_*)\).

The next gate is off-diagonal:

\[
\boxed{\textbf{RF-B — Off-Diagonal Rate Surface Closure}.}
\]

Its target is the full \((\alpha,\beta,t)\) caustic surface defined by

\[
\Delta_{\mathrm{sad}}(\alpha,\beta,t)=0
\]

and explicit chamberwise rate functions for \(\alpha\neq\beta\).

---

## Claim firewall

- The explicit rate in this note is for the diagonal proportional sector \(m=n=\lambda q\).
- The decaying saddle is selected by the steepest-descent contour; the other algebraic root is not interpreted as an additional physical growth mode.
- The Airy scaling is local near the simple saddle collision and assumes the standard nondegeneracy \(\Psi'''_*\neq0\), verified above.
- Varying-Jacobi literature supports the oscillatory/turning/exponential regime structure and Airy transition, but the FCIG rate formula here comes from the Bergman coefficient-extraction phase.
- No novelty claim is made.

## References

1. O. Szehr and R. Zarouf, *On the asymptotic behavior of Jacobi polynomials with first varying parameter*, Journal of Approximation Theory **277** (2022), 105702.
2. A. Gil, J. Segura, and N. M. Temme, work on asymptotic expansions of Jacobi polynomials for large degree and parameters.
3. F. W. J. Olver, standard theory of coalescing saddle points and Airy uniform asymptotics.
4. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.

## FCIG cross-references

- `steepest-descent-rate-closure.md`
- `proportional-k-type-rate-function.md`
- `jacobi-asymptotic-closure.md`
- `parameter-uniform-matrix-decay.md`
- `uniform-q-schwartz-control.md`
