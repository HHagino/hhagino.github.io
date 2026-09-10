# A Semiclassical Atlas and Schwartz Closure for Holomorphic Discrete-Series Matrix Coefficients in FCIG

**Version 1.0 — frozen research draft, 2026-09-10**

## Abstract

Let
\[
M_{m,n}^{(q)}(t)=\langle e_m,\pi_q(a_t)e_n\rangle,
\qquad \pi_q=D^+_{2q-1},
\]
be a radial K-type matrix coefficient of the holomorphic discrete series of `SU(1,1)` in the FCIG normalization. We combine two complementary descriptions. First, in the semiclassical regime `q -> infinity`, `m/q -> alpha`, `n/q -> beta`, the exact Jacobi representation yields an explicit two-sheet caustic geometry, forbidden rate functions, Airy fold charts, a Bessel identity-endpoint contraction, and a Hermite--Gaussian lowest-K sheet-merger contraction. Second, using Harish--Chandra Schwartz Fourier theory for the discrete-series block together with Cowling--Haagerup--Howe and the explicit derived-representation action, we obtain polynomially weighted Harish--Chandra Schwartz seminorm bounds uniformly over all `q,m,n`. Thus the sharp local proportional-K atlas and the coarse global unrestricted-K Schwartz topology fit into one representation-side closure theorem. No novelty claim is made for the classical asymptotic or Harish--Chandra Fourier machinery; the purpose is to record the FCIG normalization, exact saddle geometry, boundary contractions, and the crosswalk between local and global descriptions.

---

## 1. Exact representation

For `n >= m`, up to the fixed compact phase convention,

\[
\boxed{
M_{m,n}^{(q)}(t)
=
\mathcal N_{m,n}(q)
\left(\cosh\frac t2\right)^{-2q}
\left(\tanh\frac t2\right)^{n-m}
P_m^{(n-m,2q-1)}
\left(1-2\tanh^2\frac t2\right)
}
\]

with

\[
\mathcal N_{m,n}(q)
=
\left(
\frac{m!\Gamma(2q+n)}{n!\Gamma(2q+m)}
\right)^{1/2}.
\]

The case `m >= n` is obtained by the conjugation/exchange convention fixed in `phase-convention.md`.

Set

\[
r=\tanh\frac t2,
\qquad
m=\alpha q+o(q),
\qquad
n=\beta q+o(q).
\]

The coefficient-extraction phase is

\[
\boxed{
\Psi_{\alpha,\beta,r}(z)
=
\beta\log(z+r)
-(\beta+2)\log(1+rz)
-\alpha\log z.
}
\]

Its saddle equation is

\[
\boxed{
\frac{\beta}{z+r}
-
\frac{r(\beta+2)}{1+rz}
-
\frac{\alpha}{z}=0.
}
\]

---

## 2. Theorem A — exact caustic geometry and leading canonical atlas

Define

\[
\alpha+1=\cosh u_\alpha,
\qquad
\beta+1=\cosh u_\beta.
\]

Then the saddle discriminant factorizes as

\[
\boxed{
\Delta_{\rm sad}
=(\alpha+\beta+2)^2(r^2-r_-^2)(r^2-r_+^2)
}
\]

with

\[
\boxed{
r_-=	anh\frac{|u_\alpha-u_\beta|}{2},
\qquad
r_+=\tanh\frac{u_\alpha+u_\beta}{2}.}
\]

Therefore the caustic sheets are

\[
\boxed{
t_-=|u_\alpha-u_\beta|,
\qquad
t_+=u_\alpha+u_\beta.}
\]

For positive `alpha,beta` away from the boundary degenerations,

\[
\boxed{
\begin{array}{ccl}
0<t<t_-&:&\text{inner forbidden},\\
t_-<t<t_+&:&\text{oscillatory},\\
t>t_+&:&\text{outer forbidden}.
\end{array}}
\]

At both sheets the two saddles coalesce at

\[
\boxed{z_*=-\sqrt{\frac{\alpha}{\alpha+2}}.}
\]

Moreover,

\[
\boxed{
\partial_t\Psi'(z_*,t_-)
=
\partial_t\Psi'(z_*,t_+)
=-(\alpha+2),
}
\]

while the cubic coefficients have opposite sign. Hence each nondegenerate sheet is a simple fold and has the standard Airy scaling

\[
\boxed{z-z_*=O(q^{-1/3}),
\qquad t-t_\pm=O(q^{-2/3}).}
\]

The two boundary critical scales are

\[
\boxed{q|\alpha-\beta|=O(1)}
\]

and

\[
\boxed{q\min(\alpha,\beta)=O(1).}
\]

They require separate canonical charts.

---

## 3. Forbidden rate functions

Write

\[
B=(\alpha-\beta)+(\alpha+\beta+2)r^2,
\qquad
\Delta=B^2-4\alpha(\alpha+2)r^2.
\]

For `alpha >= beta > 0`, the selected decaying saddles are

\[
\boxed{
z_{\rm in}=\frac{-B-\sqrt\Delta}{2r(\alpha+2)},
\qquad 0<t<t_-,}
\]

\[
\boxed{
z_{\rm out}=\frac{-B+\sqrt\Delta}{2r(\alpha+2)},
\qquad t>t_+.}
\]

With

\[
s(\gamma)=\frac12\left[(\gamma+2)\log(\gamma+2)-\gamma\log\gamma-2\log2\right],
\]

define

\[
\boxed{
\begin{aligned}
\Phi_{\alpha,\beta}(t;z_*)
={}&2\log\cosh\frac t2+s(\alpha)-s(\beta)\\
&-\beta\log|z_*+r|
+(\beta+2)\log|1+rz_*|
+\alpha\log|z_*|.
\end{aligned}}
\]

Then

\[
\Phi_-=\Phi_{\alpha,\beta}(t;z_{\rm in}),
\qquad
\Phi_+=\Phi_{\alpha,\beta}(t;z_{\rm out}),
\]

are positive in the corresponding forbidden chambers and vanish at `t_-` and `t_+`. Near a simple fold,

\[
\boxed{\Phi_\pm(t)\asymp C_\pm|t-t_\pm|^{3/2}.}
\]

Away from the folds the standard saddle expansion gives `q^{-1/2}` amplitudes; in an Airy layer the leading scale is `q^{-1/3}`.

---

## 4. Theorem A1 — Bessel boundary chart

Let

\[
n-m=k\in\mathbb Z_{\ge0}\quad\text{fixed},
\qquad
\frac mq\to\alpha>0,
\qquad
t=\frac{s}{q}.
\]

Then the exact terminating hypergeometric representation contracts to `{}_0F_1`, and

\[
\boxed{
M_{m,m+k}^{(q)}(s/q)
\longrightarrow
J_k\!\left(\sqrt{\alpha(\alpha+2)}\,s\right)
}
\]

uniformly for bounded `s`, modulo the fixed unitary phase convention.

The collapsing inner caustic satisfies

\[
\boxed{
\sqrt{\alpha(\alpha+2)}\,q t_-\to k,
}
\]

so the large-order Bessel turning point matches the generic inner Airy chart.

---

## 5. Theorem A2 — Hermite--Gaussian boundary chart

Let

\[
n=\nu\in\mathbb Z_{\ge0}\quad\text{fixed},
\qquad
\frac mq\to\alpha>0,
\qquad
t=u_\alpha+\frac{\tau}{\sqrt q}.
\]

Then the fixed-degree Jacobi equation contracts to the Hermite equation and the normalized matrix coefficient obeys

\[
\boxed{
q^{1/4}M_{\nu,m}^{(q)}
\left(u_\alpha+\frac{\tau}{\sqrt q}\right)
\longrightarrow
[\pi\alpha(\alpha+2)]^{-1/4}
\frac{H_\nu(-\tau)}{\sqrt{2^\nu\nu!}}e^{-\tau^2/2}.
}
\]

Equivalently,

\[
\boxed{
[\pi\alpha(\alpha+2)]^{-1/4}
\frac{D_\nu(-\sqrt2\tau)}{\sqrt{\nu!}}.
}
\]

The two generic caustics become

\[
\boxed{\tau_\pm\to\pm\sqrt{2\nu},}
\]

which are the large-order Hermite turning scales. Thus the Hermite chart resolves the merger of both Airy sheets at the lowest-K boundary.

---

## 6. Corollary A — local semiclassical atlas

The leading canonical charts are

\[
\boxed{
\begin{array}{ccl}
\text{generic forbidden bulk}&:&e^{-q\Phi_\pm}\times\text{saddle amplitude},\\
\text{generic allowed bulk}&:&\text{conjugate-saddle oscillation},\\
\text{simple caustic}&:&\operatorname{Ai},\\
q|\alpha-\beta|=O(1)&:&J_k,\\
q\min(\alpha,\beta)=O(1)&:&H_\nu e^{-\tau^2/2}/D_\nu.
\end{array}}
\]

with overlap relations

\[
\boxed{
\text{Bessel}\xrightarrow{k\to\infty}\text{Airy},
\qquad
\text{Hermite}\xrightarrow{\nu\to\infty}\text{two Airy folds}.}
\]

This is the FCIG gate

\[
\boxed{\textbf{SAC-A: PASS}.}
\]

---

## 7. Theorem B — unrestricted Harish--Chandra Schwartz closure

Let

\[
p_{D,E,N}(f)
=
\sup_{g\in G}(1+\sigma(g))^N\Xi(g)^{-1}|L_D R_Ef(g)|
\]

be a Harish--Chandra Schwartz seminorm.

Because every discrete-series representation is tempered, the Cowling--Haagerup--Howe estimate gives for normalized one-dimensional K-types

\[
\boxed{|M_{m,n}^{(q)}(g)|\le\Xi(g)}
\]

uniformly in `q,m,n`.

The derived representation satisfies

\[
K_0e_j=(q+j)e_j,
\]

\[
K_+e_j=\sqrt{(j+1)(2q+j)}e_{j+1},
\qquad
K_-e_j=\sqrt{j(2q+j-1)}e_{j-1},
\]

so every fixed enveloping-algebra operator has polynomial K-type cost.

The discrete-series summand of Harish--Chandra's Schwartz Fourier transform is a rapidly decreasing family of smoothing operator blocks. Continuity of the inverse Schwartz Fourier transform, specialized to the rank-one block

\[
A_{mn}^{(q)}=|e_n\rangle\langle e_m|,
\]

therefore gives, for every fixed `D,E,N`, constants and nonnegative integers `a,b,c` independent of `q,m,n` such that

\[
\boxed{
 p_{D,E,N}(M_{m,n}^{(q)})
 \le
 C_{D,E,N}
 (1+q)^a(1+q+m)^b(1+q+n)^c.
}
\]

Equivalently, there exists a polynomial `P_{D,E,N}` for which

\[
\boxed{
|L_D R_E M_{m,n}^{(q)}(g)|
\le
C_{D,E,N}P_{D,E,N}(q,m,n)
\Xi(g)(1+\sigma(g))^{-N}
}
\]

for all `q,m,n,g`.

This closes

\[
\boxed{\textbf{UQ-B2: PASS}}
\]

and hence

\[
\boxed{\textbf{UQ-A2: PASS}.}
\]

The theorem asserts finite polynomial parameter loss, not optimal exponents.

---

## 8. Corollary B — FCIG synthesis in Schwartz topology

For a smoothing block `A_q`, define

\[
h_{A,q}(g)=d_q\sum_{m,n\ge0}A_{mn}M_{n,m}^{(q)}(g),
\qquad
d_q=\frac{2q-1}{4\pi}.
\]

The exact Schur-orthogonality identity is

\[
\boxed{
\|L_D R_Eh_{A,q}\|_2^2
=d_q\|d\pi_q(D)A d\pi_q(E)\|_{HS}^2.
}
\]

If `(A_q)` is uniformly rapid with respect to the weighted number-operator seminorms, Theorem B implies absolute convergence in every Harish--Chandra Schwartz seminorm. Thus the FCIG discrete-series synthesis map is controlled both in `L^2`-Sobolev topology and in pointwise Harish--Chandra Schwartz topology.

---

## 9. Why Theorems A and B are complementary

Theorem A is sharp but local in semiclassical parameter space. It resolves precise saddles, caustics, rates, and canonical functions when K-types scale with `q`.

Theorem B is coarse but global. It covers all K-types, including regimes in which `m/q` or `n/q` is unbounded, at the cost of unspecified polynomial parameter weights.

Therefore

\[
\boxed{
\text{sharp local asymptotics}
\quad+\quad
\text{global Schwartz topology}
}
\]

is the correct closure statement. It would be mathematically stronger but unnecessary for structural closure to optimize the polynomial exponents in Theorem B or to build one single explicit WKB chart valid over every unbounded parameter ratio.

---

## 10. Relation to the orbital side

The exact Sun/Bergman cylinder kernel has transverse Fourier transform localized at

\[
\boxed{|\xi|\sim2q\tanh(L/2)}
\]

with relative width `O(q^{-1/2})`. The representation-side radial geometry is organized by the same hyperbolic disk coordinate `tanh(t/2)`.

This is a compatibility of scales, not an identification:

\[
\boxed{\xi\neq t\neq m,n\neq\text{Harish--Chandra spectral parameter}.}
\]

Characters, orbital integrals, coherent-state matrix coefficients, and cyclic relative traces remain typed separately.

---

## 11. Final gate ledger for the representation-side semiclassical branch

\[
\boxed{
\begin{array}{ll}
\text{UQ-A1} & \text{PASS — exact }L^2\text{-Sobolev transfer},\\
\text{UQ-B1} & \text{PASS — fixed K-window Schwartz control},\\
\text{JA/RF/UR/BC} & \text{PASS — proportional-K asymptotic closure},\\
\text{SAC-A} & \text{PASS — canonical semiclassical atlas},\\
\text{UQ-B2} & \text{PASS — unrestricted K-type polynomial Schwartz bound},\\
\text{UQ-A2} & \textbf{PASS — full pointwise Schwartz-topology closure}.
\end{array}}
\]

What remains is quantitative refinement, not a structural gate: optimal polynomial exponents, explicit global inverse-Fourier seminorm constants, and sharper overlap estimates between Theorem B and the SAC rate functions.

---

## 12. Claim firewall

1. `M_{m,n}^{(q)}` is a matrix coefficient, not a Harish--Chandra character and not an ordinary trace.
2. Cowling--Haagerup--Howe supplies the uniform `Xi` majorant; arbitrary spatial Schwartz weights come from the discrete-series Schwartz Fourier theorem, not from CHH alone.
3. The polynomial exponents in Theorem B are not claimed optimal.
4. Airy, Bessel, Hermite, and parabolic-cylinder asymptotic structures are classical. The displayed FCIG scalings and exact saddle geometry are derived in the linked FCIG notes.
5. No identification is made between the transverse orbital Fourier variable and a Harish--Chandra spectral parameter.
6. Formal-degree constants depend on Haar normalization; FCIG uses `d_q=(2q-1)/(4 pi)`.
7. No literature-novelty claim is made by this frozen draft.

---

## References

1. Harish--Chandra, *Representations of Semisimple Lie Groups VI: Integrable and Square-Integrable Representations*, Amer. J. Math. **78** (1956), 564--628.
2. M. Cowling, U. Haagerup, R. Howe, *Almost L^2 matrix coefficients*, J. Reine Angew. Math. **387** (1988), 97--110.
3. R. J. Stanton, P. A. Tomas, *L^p Harmonic Analysis on SL(2,R)*, Memoirs AMS **76** (1988), no. 393.
4. G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS Colloquium Publications 23, 1975.
5. C. L. Frenzen, R. Wong, *A Uniform Asymptotic Expansion of the Jacobi Polynomials with Error Bounds*, Canad. J. Math. **37** (1985), 979--1007.
6. A. Gil, J. Segura, N. M. Temme, *Asymptotic expansions of Jacobi polynomials and of the nodes and weights of Gauss--Jacobi quadrature for large degree and parameters in terms of elementary functions*, J. Math. Anal. Appl. **494** (2021), 124642.
7. NIST Digital Library of Mathematical Functions, Chapter 10 (Bessel), Chapter 12 (parabolic cylinder), Chapter 18 (Jacobi/Hermite), and §2.4(v) (coalescing saddle points).
8. A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press, 1986.
9. N. R. Wallach, *Real Reductive Groups I/II*, Academic Press, 1988/1992.

## Proof-source map

- `phase-convention.md`
- `uniform-q-schwartz-control.md`
- `parameter-uniform-matrix-decay.md`
- `jacobi-asymptotic-closure.md`
- `proportional-k-type-rate-function.md`
- `off-diagonal-rate-surface.md`
- `two-sheet-airy-normalization.md`
- `global-off-diagonal-rate-closure.md`
- `uniform-remainder-closure.md`
- `boundary-bessel-closure.md`
- `lowest-k-hermite-closure.md`
- `semiclassical-atlas-closure.md`
- `unrestricted-schwartz-closure.md`
