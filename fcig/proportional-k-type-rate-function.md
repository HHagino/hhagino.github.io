# Proportional K-Type Rate Function: Saddle Geometry for the Holomorphic Discrete Series

## Status

This note advances JA-B. The goal is to replace the fixed-K-window estimate by a genuine semiclassical analysis in the proportional regime

\[
m\sim \alpha q,\qquad n\sim \beta q,
\qquad q\to\infty.
\]

Rather than importing a black-box Jacobi asymptotic, we derive the saddle equation directly from the weighted Bergman model. This produces an explicit algebraic critical-point equation and isolates the rate function that must be compared with the FCIG orbital Gamma window.

The saddle equation is exact. A global steepest-descent theorem across all turning regimes remains open.

---

## 1. Weighted Bergman model

Use the holomorphic discrete-series realization with orthonormal monomials

\[
e_n(z)=c_{n,q}z^n,
\qquad
c_{n,q}^2=\frac{\Gamma(n+2q)}{\Gamma(2q)\,\Gamma(n+1)}.
\]

Let

\[
r=\tanh\frac t2\in(0,1),
\qquad
C=\cosh\frac t2=(1-r^2)^{-1/2}.
\]

For a standard positive hyperbolic element one may write the action, up to the fixed convention for inverse/phase, as

\[
(\pi_q(a_t)f)(z)
=(C+Sz)^{-2q}
 f\!\left(\frac{Cz+S}{Sz+C}\right),
\qquad S=rC.
\]

Hence

\[
\pi_q(a_t)e_n(z)
=
c_{n,q}C^{-2q}
(z+r)^n(1+rz)^{-n-2q}.
\]

The radial matrix coefficient is therefore the coefficient extraction

\[
\boxed{
M_{m,n}^{(q)}(t)
=
\frac{c_{n,q}}{c_{m,q}}C^{-2q}
[z^m]\,(z+r)^n(1+rz)^{-n-2q}.
}
\]

Equivalently, by Cauchy's formula,

\[
\boxed{
M_{m,n}^{(q)}(t)
=
\frac{c_{n,q}}{c_{m,q}}C^{-2q}
\frac1{2\pi i}
\oint
\frac{(z+r)^n}{(1+rz)^{n+2q}}
\frac{dz}{z^{m+1}}.
}
\]

This contour representation is the starting point for proportional asymptotics.

---

## 2. Proportional scaling

Set

\[
m=\alpha q+o(q),\qquad
n=\beta q+o(q),
\qquad \alpha,\beta\ge0.
\]

Ignoring the subleading \(z^{-1}\) amplitude, the contour exponent is

\[
\boxed{
\Psi_{\alpha,\beta,r}(z)
=
\beta\log(z+r)
-(\beta+2)\log(1+rz)
-\alpha\log z.
}
\]

Thus

\[
M_{m,n}^{(q)}(t)
\sim
\frac{c_{n,q}}{c_{m,q}}
\exp\!\left[-2q\log C\right]
\oint e^{q\Psi(z)}\frac{dz}{2\pi iz}.
\]

The large-q problem is therefore a one-complex-variable saddle problem.

---

## 3. Exact saddle equation

Differentiate:

\[
\Psi'(z)
=
\frac{\beta}{z+r}
-
\frac{r(\beta+2)}{1+rz}
-
\frac{\alpha}{z}.
\]

The critical points satisfy

\[
\boxed{
\frac{\beta}{z+r}
-
\frac{r(\beta+2)}{1+rz}
-
\frac{\alpha}{z}=0.
}
\]

Clearing denominators gives the quadratic equation

\[
\boxed{
r(\alpha+2)z^2
+\Bigl[\alpha(1+r^2)+2r^2-\beta(1-r^2)\Bigr]z
+\alpha r=0.}
\]

Define

\[
B(\alpha,\beta,r)
:=
\alpha(1+r^2)+2r^2-\beta(1-r^2).
\]

Then

\[
\boxed{
z_\pm
=
\frac{-B\pm\sqrt{\Delta_{\rm sad}}}
{2r(\alpha+2)},}
\]

with saddle discriminant

\[
\boxed{
\Delta_{\rm sad}
=
B(\alpha,\beta,r)^2
-4\alpha(\alpha+2)r^2.}
\]

This discriminant is the natural bulk/turning-point separator.

---

## 4. Turning locus

The coalescence condition is

\[
\boxed{
\Delta_{\rm sad}(\alpha,\beta,r)=0.}
\]

This defines the semiclassical turning hypersurface in \((\alpha,\beta,t)\)-space.

Away from this locus, ordinary nondegenerate steepest descent should give a \(q^{-1/2}\) prefactor. On the turning locus, two saddles coalesce and an Airy-type uniformization is expected. Near endpoint/singularity collisions \(z=0,-r,-1/r\), a different local model may be required.

Accordingly the proportional regime naturally decomposes into:

1. nondegenerate bulk: \(\Delta_{\rm sad}\neq0\) and saddle separated from singularities;
2. turning regime: \(\Delta_{\rm sad}\approx0\);
3. endpoint/singularity regime: saddle approaches \(0,-r,-1/r\).

---

## 5. Stirling normalization

The monomial normalization contributes a nontrivial entropy term. With \(n=\beta q\), Stirling gives

\[
\frac1q\log c_{n,q}
=
\frac12\Bigl[(\beta+2)\log(\beta+2)
-\beta\log\beta
-2\log2\Bigr]
+o(1),
\]

where all \(\log q\) terms cancel.

Define

\[
\boxed{
s(\gamma)
:=
\frac12\Bigl[(\gamma+2)\log(\gamma+2)
-\gamma\log\gamma
-2\log2\Bigr],}
\]

with the continuous convention \(\gamma\log\gamma=0\) at \(\gamma=0\).

Then

\[
\boxed{
\frac1q\log\frac{c_{n,q}}{c_{m,q}}
=
s(\beta)-s(\alpha)+o(1).}
\]

---

## 6. Candidate rate function

Let \(z_*\) be the saddle selected by the contour deformation appropriate to the given regime. Combining the Bergman prefactor, Stirling normalization, and saddle exponent gives

\[
\frac1q\log M_{m,n}^{(q)}(t)
\sim
s(\beta)-s(\alpha)
-2\log C
+\Psi_{\alpha,\beta,r}(z_*),
\]

up to phase and the usual \(q^{-1/2}\) determinant factor.

Thus define the real decay rate

\[
\boxed{
\Phi(\alpha,\beta,t)
:=
2\log\cosh\frac t2
-s(\beta)+s(\alpha)
-\Re\Psi_{\alpha,\beta,r}(z_*),
\qquad r=\tanh\frac t2.
}
\]

In a nondegenerate decaying region the expected asymptotic form is

\[
\boxed{
M_{m,n}^{(q)}(t)
=
q^{-1/2}A(\alpha,\beta,t)
 e^{-q\Phi(\alpha,\beta,t)}
 e^{iq\vartheta(\alpha,\beta,t)}
\left(1+O(q^{-1})\right),}
\]

with the understanding that the exact amplitude and phase require the steepest-descent contour and Hessian.

This formula is a theorem target, not yet a global theorem.

---

## 7. Lowest K-type consistency check

For \(\alpha=\beta=0\), the matrix coefficient is known exactly:

\[
M_{0,0}^{(q)}(t)
=\left(\cosh\frac t2\right)^{-2q}.
\]

Hence

\[
\boxed{
\Phi(0,0,t)=2\log\cosh\frac t2.}
\]

This agrees with the coherent-state/Bergman kernel already derived in `coherent-state-discrete-series-closure.md`.

The generic saddle formula degenerates at \(\alpha=\beta=0\), because the contour integral then has no large polynomial coefficient-extraction exponent. The lowest-K case must therefore be treated as a boundary stratum, not by blindly substituting into the generic nondegenerate saddle approximation.

---

## 8. Diagonal proportional sector

For \(\alpha=\beta=\lambda\),

\[
B
=
\lambda(1+r^2)+2r^2-\lambda(1-r^2)
=
2r^2(\lambda+1).
\]

Therefore

\[
\Delta_{\rm sad}
=
4r^2\left[r^2(\lambda+1)^2-\lambda(\lambda+2)\right].
\]

Since

\[
\lambda(\lambda+2)=(\lambda+1)^2-1,
\]

the turning condition becomes

\[
\boxed{
r^2
=1-\frac1{(\lambda+1)^2}.}
\]

Equivalently,

\[
\boxed{
\operatorname{sech}^2\frac{t_*}{2}
=\frac1{(\lambda+1)^2},
\qquad
\cosh\frac{t_*}{2}=\lambda+1.}
\]

Thus the diagonal proportional K-type sector has an explicit turning radius

\[
\boxed{
t_*(\lambda)=2\operatorname{arcosh}(\lambda+1).}
\]

This is a concrete new structural formula inside the FCIG derivation: increasing K-type ratio \(\lambda=n/q\) pushes the radial turning scale outward logarithmically.

For large \(\lambda\),

\[
t_*(\lambda)
=2\log(2\lambda)+O(\lambda^{-1}).
\]

No novelty claim is made; the formula is an algebraic consequence of the saddle discriminant above.

---

## 9. Comparison with the FCIG orbital Gamma window

The orbital Fourier calculation gave

\[
|\xi|_{\rm peak}
\sim
2q\tanh\frac L2.
\]

The representation-side saddle uses exactly the same hyperbolic coordinate

\[
r=\tanh\frac t2,
\]

but in the algebraic critical equation

\[
r(\alpha+2)z^2+Bz+\alpha r=0.
\]

Therefore the common quantity \(\tanh(\cdot/2)\) is now visible on both sides:

\[
\boxed{
\text{orbital side: }\frac{|\xi|}{q}\sim2\tanh\frac L2,
\qquad
\text{representation side: saddle geometry controlled by }r=\tanh\frac t2.}
\]

This is a genuine scale/coordinate correspondence, but not an identification of variables. In particular,

\[
\boxed{\xi\neq t\neq n\neq\text{Harish--Chandra spectral parameter}.}
\]

A transform theorem would be needed before interpreting the two saddle structures as dual.

---

## 10. Gate status

We record

\[
\boxed{\textbf{JA-B1: PASS — exact proportional-regime saddle equation and turning discriminant.}}
\]

We do **not** yet record a global rate-function theorem. The next gate is

\[
\boxed{\textbf{JA-B2 — Steepest-Descent Rate Closure}.}
\]

Required tasks:

- determine the admissible steepest-descent contour and dominant saddle in each chamber;
- prove \(\Phi\ge0\) in the decaying chambers, consistent with unitarity;
- compute the Hessian amplitude;
- construct Airy uniformization at \(\Delta_{\rm sad}=0\);
- control singularity/endpoint collisions;
- derive bounds uniform for \((\alpha,\beta)\) in compact subsets of the proportional cone.

Only after JA-B2 should one claim a global asymptotic

\[
M_{m,n}^{(q)}(t)\sim q^{-1/2}Ae^{-q\Phi+i q\vartheta}.
\]

---

## 11. Claim firewall

- The contour representation and saddle equation are exact within the stated Bergman-action convention.
- The discriminant and diagonal turning radius are exact algebraic consequences.
- The displayed \(q^{-1/2}e^{-q\Phi}\) formula is presently a theorem target away from degeneracies, not a globally proved FCIG theorem.
- The dominant saddle depends on contour topology and Stokes chambers; choosing an algebraic root is not enough.
- Orbital transverse frequency \(\xi\), group radial variable \(t\), K-type index, and Harish--Chandra spectral variable remain distinct.
- No novelty claim is made.

---

## References

1. NIST Digital Library of Mathematical Functions, Chapter 18: Orthogonal Polynomials — Jacobi hypergeometric and asymptotic formulas.
2. A. Gil, J. Segura, N. M. Temme, work on asymptotic computation of classical orthogonal polynomials for large degree and parameters.
3. R. J. Stanton and P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.
4. A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press, 1986.
5. Standard holomorphic discrete-series / SU(1,1) weighted Bergman realizations.

## FCIG cross-references

- `jacobi-asymptotic-closure.md`
- `parameter-uniform-matrix-decay.md`
- `uniform-q-schwartz-control.md`
- `coherent-state-discrete-series-closure.md`
- `centralizer-spectral-window.md`
