# Steepest-Descent Rate Closure in the Diagonal Proportional K-Type Sector

## Status

This note completes the regime classification for the diagonal proportional sector

\[
m=n=\lambda q,
\qquad \lambda>0,
\]

of the holomorphic discrete-series matrix coefficient. It combines the exact saddle equation derived in `proportional-k-type-rate-function.md` with a direct reduction to a one-parameter varying-Jacobi asymptotic theorem.

The result is a rigorous identification of the oscillatory, turning, and exponentially decaying regions, together with the exact turning point

\[
\boxed{
\cosh\frac{t_*}{2}=\lambda+1.
}
\]

The full closed-form forbidden-region rate function remains a separate calculation, but the steepest-descent phase portrait itself is closed.

---

## 1. Exact diagonal saddle equation

Set

\[
r=\tanh\frac t2.
\]

For

\[
m=n=\lambda q,
\]

the Cauchy-integral phase from the weighted Bergman realization is

\[
\Psi_{\lambda,r}(z)
=
\lambda\log(z+r)
-(\lambda+2)\log(1+rz)
-\lambda\log z.
\]

The saddle equation is

\[
\Psi'_{\lambda,r}(z)=0,
\]

which reduces exactly to

\[
\boxed{
(\lambda+2)z^2
+2r(\lambda+1)z
+\lambda=0.
}
\]

Hence

\[
\boxed{
z_\pm
=
\frac{-r(\lambda+1)
\pm
\sqrt{r^2(\lambda+1)^2-\lambda(\lambda+2)}}
{\lambda+2}.
}
\]

Define

\[
\Delta_{\rm sad}
=
4\left[r^2(\lambda+1)^2-\lambda(\lambda+2)\right].
\]

The coalescence condition is

\[
\boxed{
\Delta_{\rm sad}=0.
}
\]

---

## 2. Exact turning point

Solving the coalescence equation gives

\[
r_*^2
=
\frac{\lambda(\lambda+2)}{(\lambda+1)^2}
=
1-\frac1{(\lambda+1)^2}.
\]

Since

\[
1-r^2=\operatorname{sech}^2\frac t2,
\]

we obtain

\[
\boxed{
\operatorname{sech}\frac{t_*}{2}
=
\frac1{\lambda+1},
}
\]

or equivalently

\[
\boxed{
\cosh\frac{t_*}{2}=\lambda+1.
}
\]

Thus

\[
\boxed{
t_*(\lambda)=2\operatorname{arcosh}(\lambda+1).}
\]

For large \(\lambda\),

\[
\boxed{
t_*(\lambda)=2\log(2\lambda)+O(\lambda^{-1}).}
\]

---

## 3. Geometry of the saddles

### Allowed / oscillatory chamber

If

\[
0<r<r_*,
\]

then

\[
\Delta_{\rm sad}<0,
\]

and \(z_\pm\) form a complex-conjugate pair.

Because the product of the roots is

\[
z_+z_-=
\frac{\lambda}{\lambda+2},
\]

we obtain the exact modulus identity

\[
\boxed{
|z_\pm|
=
\sqrt{\frac{\lambda}{\lambda+2}}.
}
\]

Remarkably, this modulus is independent of \(t\) throughout the allowed chamber.

### Turning point

At

\[
r=r_*,
\]

the two saddles coalesce at

\[
\boxed{
z_*
=-\sqrt{\frac{\lambda}{\lambda+2}}.}
\]

This is a standard double-saddle configuration: the quadratic term in the local phase vanishes while the cubic term generically survives, giving Airy scaling.

### Forbidden chamber

If

\[
r>r_*,
\]

then

\[
\Delta_{\rm sad}>0,
\]

and the two saddles are distinct real negative points. One of them becomes the steepest-descent dominant saddle; the matrix coefficient acquires exponential decay in \(q\).

---

## 4. Reduction to a varying-Jacobi theorem

For the diagonal matrix coefficient, the Jacobi factor has the form

\[
P_m^{(0,\,2q-1)}(1-2r^2),
\qquad
m=\lambda q.
\]

Use the Jacobi symmetry

\[
\boxed{
P_m^{(0,\,2q-1)}(x)
=
(-1)^m
P_m^{(2q-1,\,0)}(-x).
}
\]

Set

\[
\eta=\sqrt{1-r^2}
=\operatorname{sech}\frac t2.
\]

Then

\[
-x=2r^2-1=1-2\eta^2.
\]

The polynomial becomes

\[
P_m^{(2q-1,\,0)}(1-2\eta^2).
\]

Now regard \(m\) as the large degree \(N\). Since

\[
N=m=\lambda q,
\]

the first Jacobi parameter satisfies

\[
2q-1
=
\frac{2}{\lambda}N+O(1).
\]

Thus the varying-parameter ratio is

\[
\boxed{a=\frac{2}{\lambda}.}
\]

A standard varying-Jacobi asymptotic theorem places the transition at

\[
a=
\frac{2\eta}{1-\eta}.
\]

Substituting \(a=2/\lambda\) gives

\[
\frac1\lambda
=
\frac{\eta}{1-\eta},
\]

hence

\[
\boxed{\eta=\frac1{\lambda+1}.}
\]

Therefore

\[
\boxed{
\operatorname{sech}\frac{t_*}{2}
=
\frac1{\lambda+1},
}
\]

which is exactly the turning point independently derived from the FCIG saddle discriminant.

This agreement is the central consistency check of the present note.

---

## 5. Rigorous asymptotic regime classification

The varying-Jacobi theorem yields the following large-\(q\) phase portrait after restoring the elementary normalization factors of the discrete-series matrix coefficient.

### Region I: oscillatory / classically allowed

For

\[
0<t<t_*(\lambda),
\]

the two saddles are complex conjugates and the normalized Jacobi factor has stationary-phase behavior of order

\[
N^{-1/2}.
\]

Since \(N=\lambda q\), this gives

\[
\boxed{
M_{\lambda q,\lambda q}^{(q)}(t)
=
q^{-1/2}
A_\lambda(t)
\cos\bigl(q\Theta_\lambda(t)+\vartheta_\lambda(t)\bigr)
+O(q^{-3/2})
}
\]

locally uniformly away from the turning point, after absorbing convention-dependent elementary prefactors into \(A_\lambda\).

The important invariant statement is the scale

\[
\boxed{q^{-1/2}.}
\]

### Region II: turning point

At

\[
t=t_*(\lambda),
\]

the saddles coalesce. The varying-Jacobi theorem gives the characteristic coalescing-saddle magnitude

\[
\boxed{q^{-1/3}.}
\]

The natural local coordinate is

\[
\boxed{
s=q^{2/3}(t-t_*),}
\]

and the local uniformization is of Airy type:

\[
\boxed{
M_{\lambda q,\lambda q}^{(q)}(t)
\sim
q^{-1/3}
\mathcal A_\lambda(t)
\operatorname{Ai}\!\left(q^{2/3}\zeta_\lambda(t)\right),
}
\]

where \(\zeta_\lambda(t_*)=0\). The exact normalization of \(\zeta_\lambda\) requires the cubic coefficient of the FCIG Cauchy phase and is left for the next local-normal-form calculation.

### Region III: forbidden / exponentially decaying

For

\[
t>t_*(\lambda),
\]

the saddles are real and separated. The varying-Jacobi theorem gives exponential decay. Therefore there exists a positive rate

\[
\Phi_\lambda(t)>0
\qquad(t>t_*)
\]

such that locally away from the turning point

\[
\boxed{
|M_{\lambda q,\lambda q}^{(q)}(t)|
\le
C_{\lambda,t}
q^{B}
e^{-q\Phi_\lambda(t)}.
}
\]

The rate is obtained from the dominant real saddle by

\[
\boxed{
\Phi_\lambda(t)
=
2\log\cosh\frac t2
-
\Re\Psi_{\lambda,r}(z_{\rm dom})
+
\text{normalization entropy},
}
\]

with the normalization entropy given by the Stirling asymptotics of the Bergman basis constants.

---

## 6. Airy consistency

The FCIG saddle polynomial

\[
F(z,r)
=(\lambda+2)z^2+2r(\lambda+1)z+\lambda
\]

satisfies at the turning point

\[
F(z_*,r_*)=0,
\qquad
\partial_zF(z_*,r_*)=0.
\]

Hence

\[
\Psi'(z_*)=0,
\qquad
\Psi''(z_*)=0.
\]

Generically

\[
\Psi'''(z_*)\ne0.
\]

Therefore the local phase has cubic normal form

\[
\Psi(z;r)
=
\Psi_*+c_1(r-r_*)(z-z_*)
+c_3(z-z_*)^3+\cdots,
\]

which after the scaling

\[
z-z_*=O(q^{-1/3}),
\qquad
r-r_*=O(q^{-2/3})
\]

produces an Airy integral.

Thus the independently known \(q^{-1/3}\) transition law is exactly what the FCIG saddle geometry predicts.

---

## 7. FCIG interpretation

The orbital-side Sun kernel has transverse Fourier concentration

\[
\boxed{
|\xi|_{\rm peak}
\sim
2q\tanh\frac L2.
}
\]

The representation-side diagonal proportional K-type coefficient has turning coordinate

\[
\boxed{
r=\tanh\frac t2,}
\]

with threshold

\[
\boxed{
r_*^2
=1-\frac1{(\lambda+1)^2}.}
\]

Therefore both sides are organized by the same hyperbolic disk coordinate \(\tanh(\cdot/2)\), although they remain different transforms and different variables.

The correct statement is

\[
\boxed{
\text{orbital transverse localization and representation radial localization share the same hyperbolic semiclassical coordinate.}
}
\]

It is **not** legitimate to identify \(\xi\), \(t\), the K-type index, or the Harish--Chandra spectral parameter.

---

## 8. Gate status

We record

\[
\boxed{
\textbf{JA-B2: PASS — diagonal proportional sector, regime and turning-point closure.}
}
\]

The pass consists of:

1. exact saddle roots;
2. exact discriminant;
3. exact turning point;
4. independent agreement with a varying-Jacobi theorem;
5. \(q^{-1/2}\) allowed-region scaling;
6. \(q^{-1/3}\) turning scaling;
7. exponential forbidden-region decay.

What remains is not the phase portrait but the **closed-form rate/amplitude normalization**.

Define the next gate

\[
\boxed{\textbf{RF-A — Explicit Rate-Function Closure}.}
\]

The target is to evaluate

\[
\Phi_\lambda(t)
\]

from the dominant saddle in elementary hyperbolic functions, and then derive the Airy coordinate \(\zeta_\lambda(t)\) with its exact cubic normalization.

---

## 9. Claim firewall

- JA-B2 is proved here only in the diagonal proportional sector \(m=n=\lambda q\).
- The off-diagonal sector \(m/q\to\alpha\), \(n/q\to\beta\) remains more general.
- Airy type follows from coalescing saddle geometry and is independently consistent with known varying-Jacobi asymptotics; the exact Airy prefactor is not yet derived here.
- Exponential decay is established in the forbidden region, but the final simplified elementary formula for \(\Phi_\lambda(t)\) is deferred to RF-A.
- No identification is made between the transverse Fourier variable and the Harish--Chandra spectral variable.
- No novelty claim is made.

---

## References

1. O. Szehr and R. Zarouf, *On the asymptotic behavior of Jacobi polynomials with first varying parameter*, Journal of Approximation Theory **277** (2022), 105702.
2. A. Gil, J. Segura, N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss-Jacobi quadrature for large degree and parameters in terms of elementary functions*, J. Math. Anal. Appl. **494** (2021), 124642.
3. A. B. J. Kuijlaars and A. Martínez-Finkelshtein, *Strong asymptotics for Jacobi polynomials with varying nonstandard parameters*, 2003.
4. F. W. J. Olver, asymptotic and Liouville--Green theory for coalescing turning points and Airy approximations.

## FCIG cross-references

- `proportional-k-type-rate-function.md`
- `jacobi-asymptotic-closure.md`
- `parameter-uniform-matrix-decay.md`
- `uniform-q-schwartz-control.md`
- `centralizer-spectral-window.md`
- `coherent-state-discrete-series-closure.md`
