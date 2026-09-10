# RF-B2 — Two-Sheet Airy Normalization

## Status

**PASS in the proportional off-diagonal sector, modulo the usual steepest-descent contour/phase convention.**

This note closes the local Airy normalization on both caustic sheets of the proportional K-type regime

\[
m=\alpha q,\qquad n=\beta q,
\]

for the holomorphic discrete-series radial matrix coefficient written through the Cauchy phase

\[
\Psi_{\alpha,\beta,r}(z)
=
\beta\log(z+r)
-(\beta+2)\log(1+rz)
-\alpha\log z,
\qquad r=\tanh(t/2).
\]

We assume \(\alpha\ge \beta>0\). The case \(\beta>\alpha\) follows by interchanging the K-type indices and using the corresponding transpose/unitarity symmetry of the radial coefficient.

---

## 1. Saddle polynomial and caustic sheets

The saddle equation is

\[
\Psi'(z)=0,
\]

or equivalently

\[
r(\alpha+2)z^2
+
\Bigl[(\alpha-\beta)+(\alpha+\beta+2)r^2\Bigr]z
+\alpha r=0.
\]

Set

\[
p_\alpha=\sqrt{\alpha(\alpha+2)},\qquad
p_\beta=\sqrt{\beta(\beta+2)}.
\]

The discriminant factorizes as

\[
\Delta_{\rm sad}
=(\alpha+\beta+2)^2(r^2-r_-^2)(r^2-r_+^2),
\]

with

\[
r_-=
\frac{p_\alpha-p_\beta}{\alpha+\beta+2},
\qquad
r_+=
\frac{p_\alpha+p_\beta}{\alpha+\beta+2}.
\]

Introduce hyperbolic K-type coordinates

\[
\alpha+1=\cosh u_\alpha,
\qquad
\beta+1=\cosh u_\beta.
\]

Then

\[
r_- = \tanh\frac{u_\alpha-u_\beta}{2},
\qquad
r_+ = \tanh\frac{u_\alpha+u_\beta}{2},
\]

and therefore

\[
\boxed{
 t_- = u_\alpha-u_\beta,
 \qquad
 t_+ = u_\alpha+u_\beta.
}
\]

Thus the oscillatory chamber is

\[
\boxed{t_-<t<t_+.}
\]

The regions \(0<t<t_-\) and \(t>t_+\) are respectively the inner and outer forbidden chambers.

---

## 2. The same coalescing saddle lies on both sheets

Let

\[
x:=\tanh\frac{u_\alpha}{2}
=\sqrt{\frac{\alpha}{\alpha+2}},
\qquad
y:=\tanh\frac{u_\beta}{2}
=\sqrt{\frac{\beta}{\beta+2}}.
\]

For \(\alpha\ge\beta\), both caustic equations satisfy

\[
(\alpha-\beta)+(\alpha+\beta+2)r_\pm^2
=2p_\alpha r_\pm.
\]

Hence the double root is the same on both sheets:

\[
\boxed{
z_*^-=z_*^+
=-\frac{p_\alpha}{\alpha+2}
=-\sqrt{\frac{\alpha}{\alpha+2}}
=-x.
}
\]

This is a useful structural fact: the two caustics are not produced by two unrelated saddle points. They are two unfoldings of the same projective saddle location, distinguished by the sign of the cubic coefficient.

---

## 3. Exact cubic coefficient

Write the saddle numerator as

\[
N(z,r)
=
r(\alpha+2)z^2
+
\Bigl[(\alpha-\beta)+(\alpha+\beta+2)r^2\Bigr]z
+\alpha r.
\]

Since

\[
\Psi'(z)
=-\frac{N(z,r)}{z(z+r)(1+rz)},
\]

at a double root \(N=N_z=0\), and therefore

\[
\boxed{
\Psi'''(z_*)
=-\frac{2r(\alpha+2)}{z_*(z_*+r)(1+rz_*)}.
}
\]

Substituting \(z_*=-x\) and

\[
r_+=\frac{x+y}{1+xy},
\qquad
r_- =\frac{x-y}{1-xy},
\]

gives the two exact values

\[
\boxed{
\Psi'''_+
=
\frac{4(x+y)(1+xy)}{xy(1-x^2)^3}>0,
}
\]

and

\[
\boxed{
\Psi'''_-
=
-\frac{4(x-y)(1-xy)}{xy(1-x^2)^3}<0.
}
\]

Thus the outer and inner caustics have opposite cubic orientation.

Define

\[
\sigma_+=+1,
\qquad
\sigma_-=-1,
\]

and

\[
\boxed{
\kappa_\pm
:=
\left(\frac{|\Psi'''_\pm|}{2}\right)^{1/3}.
}
\]

Explicitly,

\[
\boxed{
\kappa_+
=
\left[
\frac{2(x+y)(1+xy)}{xy(1-x^2)^3}
\right]^{1/3},
}
\]

\[
\boxed{
\kappa_-
=
\left[
\frac{2(x-y)(1-xy)}{xy(1-x^2)^3}
\right]^{1/3}.
}
\]

---

## 4. Exact radial unfolding coefficient

Differentiate \(\Psi'(z,r)\) with respect to the radial variable \(t\). Since

\[
\frac{dr}{dt}=\frac{1-r^2}{2},
\]

one finds, at either caustic sheet and at the double saddle,

\[
\boxed{
\partial_t\Psi'(z_*,t_\pm)=-(\alpha+2).
}
\]

The striking point is that this coefficient is independent of \(\beta\) and independent of the choice of sheet.

Consequently, with

\[
w=z-z_*,
\qquad
\tau_\pm=t-t_\pm,
\]

the local phase has the universal form

\[
\boxed{
\Psi(z,t)-\Psi(z_*,t_\pm)
=
\frac{\Psi'''_\pm}{6}w^3
-(\alpha+2)\tau_\pm w
+O(w^4,\tau_\pm w^2,\tau_\pm^2w).
}
\]

---

## 5. Canonical Airy coordinates on the two sheets

Choose

\[
w
=
\sigma_\pm
\frac{s}{q^{1/3}\kappa_\pm}.
\]

Because

\[
\Psi'''_\pm
=
\sigma_\pm |\Psi'''_\pm|,
\]

the cubic term becomes

\[
q\frac{\Psi'''_\pm}{6}w^3
=
\frac{s^3}{3}.
\]

The linear unfolding term becomes

\[
-q(\alpha+2)\tau_\pm w
=-\zeta_\pm s,
\]

where

\[
\boxed{
\zeta_\pm
=
\sigma_\pm
q^{2/3}
\frac{\alpha+2}{\kappa_\pm}
(t-t_\pm).
}
\]

Hence the canonical local normal form is

\[
\boxed{
q\bigl(\Psi-\Psi_*\bigr)
=
\frac{s^3}{3}-\zeta_\pm s+\cdots.
}
\]

This choice has an important geometric advantage: **the forbidden side corresponds to \(\zeta_\pm>0\) on both sheets.** Indeed,

- outer sheet: forbidden means \(t>t_+\), so \(\zeta_+>0\);
- inner sheet: forbidden means \(t<t_-\), and \(\sigma_-=-1\), so again \(\zeta_->0\).

The oscillatory chamber \(t_-<t<t_+\) corresponds to \(\zeta_\pm<0\) when approached from either boundary.

Thus the two caustics are normalized by the same Airy convention.

---

## 6. Universal scaling

Both sheets have the standard coalescing-saddle scaling

\[
\boxed{
z-z_*=O(q^{-1/3}),
\qquad
t-t_\pm=O(q^{-2/3}).
}
\]

At the caustic itself, the matrix coefficient has the characteristic turning-point size

\[
\boxed{M_{\alpha q,\beta q}^{(q)}(t_\pm)=O(q^{-1/3})}
\]

up to the normalization/amplitude factors already present in the global Jacobi/Bergman representation.

On the forbidden side, the Airy tail produces the local \(3/2\)-law

\[
\boxed{
\Phi_\pm(t)
\sim
\frac23
\left(
\frac{\alpha+2}{\kappa_\pm}
\right)^{3/2}
|t-t_\pm|^{3/2},
}
\]

with the absolute value interpreted on the respective forbidden side.

---

## 7. Structural interpretation

The off-diagonal phase diagram is therefore

\[
0<t<t_-
\quad\vert\quad
t_-<t<t_+
\quad\vert\quad
t>t_+,
\]

with

\[
\text{forbidden}
\quad\vert\quad
\text{oscillatory}
\quad\vert\quad
\text{forbidden}.
\]

Both transitions occur at the same projective saddle point \(z_*=-\tanh(u_\alpha/2)\), while the sign reversal

\[
\Psi'''_-<0<\Psi'''_+
\]

encodes the opposite orientation of the two folds.

This is the precise two-sheet Airy geometry behind the caustic triangle inequalities

\[
|u_\alpha-u_\beta|<t<u_\alpha+u_\beta.
\]

### Firewall

This is a saddle/caustic statement for the radial discrete-series matrix coefficient. It is **not** an identification of the K-type coordinates \(u_\alpha,u_\beta\), the group radial variable \(t\), the FCIG transverse Fourier variable \(\xi\), or a Harish--Chandra spectral parameter.

---

## 8. Gate status

\[
\boxed{
\textbf{RF-B2: PASS — two-sheet Airy normalization.}
}
\]

What is now explicit:

1. both caustic sheets \(t_\pm\);
2. the common double saddle \(z_*\);
3. the exact signed cubic coefficients \(\Psi'''_\pm\);
4. the exact radial unfolding coefficient \(-\!(\alpha+2)\);
5. the normalized Airy variables \(\zeta_\pm\);
6. the common forbidden-side convention \(\zeta_\pm>0\);
7. the \(q^{-1/3}\)/\(q^{-2/3}\) turning scaling and local \(3/2\)-rate law.

The next natural gate is a **global off-diagonal rate-function closure**: evaluate the dominant real saddle in both forbidden chambers and match those global rate functions to the local Airy \(3/2\)-laws above.

---

## References

- O. Szehr and R. Zarouf, “On the asymptotic behavior of Jacobi polynomials with first varying parameter,” *Journal of Approximation Theory* 277 (2022), 105702. The paper analyzes varying-parameter Jacobi asymptotics, including stationary-phase, exponential, and \(n^{-1/3}\) transition regimes.
- A. Gil, J. Segura, N. M. Temme, “Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss-Jacobi quadrature for large degree and parameters in terms of elementary functions,” *J. Math. Anal. Appl.* 494 (2021), 124642.
- NIST Digital Library of Mathematical Functions, §2.8(iii), simple turning points and Airy-function uniformization; §18.15, Jacobi asymptotic approximations.
