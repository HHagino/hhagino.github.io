# Global Off-Diagonal Rate Closure

## RF-C: exact forbidden-branch action for proportional K-types

We continue the proportional K-type regime

\[
m=\alpha q,\qquad n=\beta q,
\]

with \(\alpha,\beta>0\), and use the coefficient-extraction phase

\[
\Psi_{\alpha,\beta,r}(z)
=
\beta\log(z+r)
-(\beta+2)\log(1+rz)
-\alpha\log z,
\qquad
r=\tanh\frac t2.
\]

The normalization exponent coming from the Bergman basis is

\[
s(\gamma)
=
\frac12\Big[(\gamma+2)\log(\gamma+2)-\gamma\log\gamma-2\log2\Big],
\]

so for a real saddle branch \(z=z_*(t)\) the exponential rate is

\[
\boxed{
\Phi_{\alpha,\beta}(t;z_*)
=
2\log\cosh\frac t2
+s(\alpha)-s(\beta)
-\beta\log|z_*+r|
+(\beta+2)\log|1+rz_*|
+\alpha\log|z_*|.
}
\]

This formula is exact at the exponential scale. It should not be confused with a Harish--Chandra spectral parameter or with the transverse Fourier variable in the orbital Gamma window.

---

## 1. Saddle polynomial and caustic sheets

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
r(\alpha+2)z^2+Bz+\alpha r=0,
\]

with

\[
\boxed{
B=(\alpha-\beta)+(\alpha+\beta+2)r^2.
}
\]

Its discriminant is

\[
\boxed{
\Delta
=B^2-4\alpha(\alpha+2)r^2.
}
\]

Writing

\[
\alpha+1=\cosh u_\alpha,
\qquad
\beta+1=\cosh u_\beta,
\]

the two turning sheets are

\[
\boxed{
t_-=|u_\alpha-u_\beta|,
\qquad
t_+=u_\alpha+u_\beta.
}
\]

Thus

\[
0<t<t_-
\]

is the inner forbidden chamber,

\[
t_-<t<t_+
\]

is the oscillatory chamber, and

\[
t>t_+
\]

is the outer forbidden chamber.

For definiteness assume \(\alpha\ge\beta\); the opposite ordering is obtained by Hermitian symmetry / exchange of K-type labels.

---

## 2. The two real saddle branches

For \(\Delta\ge0\), set

\[
d=\sqrt\Delta.
\]

The algebraic roots are

\[
z_\pm
=
\frac{-B\pm d}{2r(\alpha+2)}.
\]

The decaying branch is not the same root in the two forbidden chambers.

### Inner forbidden chamber

For \(0<t<t_-\), the physical exponentially small branch is

\[
\boxed{
z_{\rm in}
=
\frac{-B-d}{2r(\alpha+2)}.
}
\]

Near \(t=0\), this is the large negative saddle and yields the positive rate associated with K-type mismatch. The other root produces the opposite saddle action and is not the decaying branch.

### Outer forbidden chamber

For \(t>t_+\), the physical decaying branch is

\[
\boxed{
z_{\rm out}
=
\frac{-B+d}{2r(\alpha+2)}.
}
\]

This is the continuation of the diagonal decaying saddle obtained previously when \(\alpha=\beta\).

Therefore the global rate is naturally two-sheeted:

\[
\boxed{
\Phi_-(\alpha,\beta,t)
=
\Phi_{\alpha,\beta}(t;z_{\rm in}),
\qquad 0<t<t_-,
}
\]

and

\[
\boxed{
\Phi_+(\alpha,\beta,t)
=
\Phi_{\alpha,\beta}(t;z_{\rm out}),
\qquad t>t_+.
}
\]

---

## 3. Closed algebraic-logarithmic form

For either branch define \(\varepsilon=-1\) in the inner chamber and \(\varepsilon=+1\) in the outer chamber, so

\[
z_\varepsilon
=
\frac{-B+\varepsilon d}{2r(\alpha+2)}.
\]

Then

\[
|z_\varepsilon|
=
\frac{B-\varepsilon d}{2r(\alpha+2)},
\]

and

\[
z_\varepsilon+r
=
\frac{2(\alpha+2)r^2-B+\varepsilon d}
{2r(\alpha+2)},
\]

\[
1+rz_\varepsilon
=
\frac{2(\alpha+2)-B+\varepsilon d}
{2(\alpha+2)}.
\]

Consequently the forbidden rate admits the completely elementary form

\[
\boxed{
\begin{aligned}
\Phi_\varepsilon(\alpha,\beta,t)
={}&2\log\cosh\frac t2+s(\alpha)-s(\beta)\\
&-\beta\log\left|
\frac{2(\alpha+2)r^2-B+\varepsilon d}
{2r(\alpha+2)}
\right|\\
&+(\beta+2)\log\left|
\frac{2(\alpha+2)-B+\varepsilon d}
{2(\alpha+2)}
\right|\\
&+\alpha\log\left(
\frac{B-\varepsilon d}
{2r(\alpha+2)}
\right),
\end{aligned}
}
\]

with

\[
\varepsilon=
\begin{cases}
-1,&0<t<t_-,\\
+1,&t>t_+.
\end{cases}
\]

This is the desired global off-diagonal closed form. No Jacobi polynomial remains in the exponent.

---

## 4. Positivity and matching at the caustics

The selected branches satisfy

\[
\boxed{
\Phi_-(\alpha,\beta,t)>0
\quad(0<t<t_-),
}
\]

and

\[
\boxed{
\Phi_+(\alpha,\beta,t)>0
\quad(t>t_+).
}
\]

At the turning sheets the two real saddles coalesce and the exponential barrier disappears:

\[
\boxed{
\Phi_-(\alpha,\beta,t_-)=0,
\qquad
\Phi_+(\alpha,\beta,t_+)=0.
}
\]

Inside the oscillatory chamber the relevant saddles form a complex-conjugate pair with equal real action, so the leading exponential rate is zero and the asymptotic is oscillatory rather than exponentially small.

The branch switch between \(z_{\rm in}\) and \(z_{\rm out}\) is therefore essential. Using the same algebraic root in both forbidden chambers gives the wrong sign of the rate on one side.

---

## 5. Recovery of the Airy 3/2 law

The previous two-sheet Airy calculation gave the common unfolding coefficient

\[
\partial_t\Psi'(z_*,t_\pm)=-(\alpha+2)
\]

and cubic coefficients

\[
\Psi'''_+>0,
\qquad
\Psi'''_-<0.
\]

Define

\[
\kappa_\pm
=
\left(\frac{|\Psi'''_\pm|}{2}\right)^{1/3}.
\]

The Airy coordinate is

\[
\zeta_\pm
=
\sigma_\pm q^{2/3}
\frac{\alpha+2}{\kappa_\pm}
(t-t_\pm),
\qquad
\sigma_+=1,
\quad
\sigma_-=-1,
\]

so the forbidden side is \(\zeta_\pm>0\) on both sheets.

The global rates above therefore have the local expansions

\[
\boxed{
\Phi_-(\alpha,\beta,t)
\sim
\frac23
\left(\frac{\alpha+2}{\kappa_-}\right)^{3/2}
(t_--t)^{3/2},
\qquad t\uparrow t_-,
}
\]

and

\[
\boxed{
\Phi_+(\alpha,\beta,t)
\sim
\frac23
\left(\frac{\alpha+2}{\kappa_+}\right)^{3/2}
(t-t_+)^{3/2},
\qquad t\downarrow t_+.
}
\]

Thus the global saddle actions and the local Airy normal forms are compatible.

---

## 6. Semiclassical matrix-coefficient statement

Away from the two turning layers, the proportional K-type radial coefficient has the schematic steepest-descent form

\[
\boxed{
M_{\alpha q,\beta q}^{(q)}(t)
=
q^{-1/2}A_-(\alpha,\beta,t;q)
\exp[-q\Phi_-(\alpha,\beta,t)]
}
\]

for \(0<t<t_-\), and

\[
\boxed{
M_{\alpha q,\beta q}^{(q)}(t)
=
q^{-1/2}A_+(\alpha,\beta,t;q)
\exp[-q\Phi_+(\alpha,\beta,t)]
}
\]

for \(t>t_+\), with classical amplitude expansions in nondegenerate compact subchambers.

In the middle chamber,

\[
\boxed{
M_{\alpha q,\beta q}^{(q)}(t)
=
q^{-1/2}A_0(\alpha,\beta,t;q)
\cos\big(q\Theta(\alpha,\beta,t)+\vartheta\big)
}
\]

schematically, while in \(q^{-2/3}\) neighborhoods of \(t_\pm\) the correct uniform approximation is Airy-type and has \(q^{-1/3}\) scaling.

These regime types agree with the standard large-degree/varying-parameter Jacobi asymptotic picture; the formulas above are the FCIG saddle-action realization in the holomorphic discrete-series normalization.

---

## 7. Diagonal and boundary checks

### Diagonal limit

If \(\alpha=\beta=\lambda\), then

\[
t_-=0,
\qquad
t_+=2\operatorname{arcosh}(\lambda+1),
\]

so the inner forbidden chamber disappears and \(\Phi_+\) reduces to the previously derived diagonal forbidden rate.

### Lowest-type boundary

If \(\beta\to0^+\), then

\[
t_-\to t_+\to\operatorname{arcosh}(\alpha+1),
\]

and the oscillatory chamber collapses, as expected for the boundary between a proportional high K-type and the lowest K-type sector.

---

## 8. Gate status

\[
\boxed{\textbf{RF-C: PASS — global off-diagonal forbidden rate closure.}}
\]

What is now closed:

- exact inner and outer decaying saddle branches;
- explicit algebraic-logarithmic rate functions \(\Phi_-\) and \(\Phi_+\);
- positivity in both forbidden chambers;
- zero-rate matching at both caustic sheets;
- compatibility with the previously derived two-sheet Airy \(3/2\)-law;
- recovery of the diagonal limit.

What remains separate is a fully uniform error theorem over all \((\alpha,\beta,t)\), including simultaneous control as \(\alpha\) or \(\beta\) approach boundary values and as the two turning sheets merge. That is a parameter-uniform remainder problem, not a missing rate-function problem.

---

## 9. References and comparison literature

- O. Szehr and R. Zarouf, *On the asymptotic behavior of Jacobi polynomials with first varying parameter*, Journal of Approximation Theory 277 (2022), 105702. The paper gives oscillatory, turning/Airy, and exponential regimes for Jacobi polynomials with varying parameters.
- A. Gil, J. Segura, N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss--Jacobi quadrature for large degree and parameters in terms of elementary functions*, J. Math. Anal. Appl. 494 (2021), 124642.
- A. B. J. Kuijlaars and A. Martinez-Finkelshtein, *Strong asymptotics for Jacobi polynomials with varying nonstandard parameters*, J. Anal. Math. 94 (2004), 195--234.

The comparison literature supports the regime structure and Airy mechanism. The explicit FCIG rate above is derived directly from the Bergman coefficient-extraction saddle phase used in the preceding notes.