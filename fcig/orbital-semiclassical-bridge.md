# Orbital--Semiclassical Bridge

## OSB-A — exact kernel, spectral window, and representation-side caustics

**Status (2026-09-10).**

This note reconnects the exact Bergman/Sun orbital branch to the holomorphic-discrete-series semiclassical atlas.  It is a typed bridge theorem: exact equalities are kept separate from semiclassical scale compatibilities, and no Fourier/spectral variables are identified without a transform theorem.

\[
\boxed{\textbf{OSB-A1: PASS — exact Bergman/orbital kernel bridge.}}
\]

\[
\boxed{\textbf{OSB-A2: PASS — exact Gamma transverse spectral window.}}
\]

\[
\boxed{\textbf{OSB-A3: PASS — quantitative compatibility with the representation semiclassical radial coordinate.}}
\]

A stronger identification with Harish--Chandra spectral variables remains explicitly excluded.

---

## 1. Exact geometric kernel

For a hyperbolic translation of length \(L\), put

\[
C_L=\cosh\frac L2,\qquad S_L=\sinh\frac L2.
\]

The transported disk Bergman coherent overlap, including the canonical unitary \(q\)-differential phase, is exactly

\[
\boxed{
C_q^{-1}\mathcal K_q(g_L;u)
=\kappa_{q,L}(u)
=(C_L-iS_Lu)^{-2q},
}
\]

where

\[
C_q=\frac{2q-1}{4\pi}.
\]

Thus the Sun cylinder kernel is literally the gauge-corrected coherent-state Bergman matrix coefficient in the chosen disk convention.

This is an exact identity, not a semiclassical approximation.

---

## 2. Exact cyclic relative trace

For a primitive oriented hyperbolic element \(\delta\) of primitive length \(\ell\), with \(L=m\ell\), the cyclic relative trace is

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[W]
=C_q\ell\,\mathcal J_{q,L}[W],
}
\]

where

\[
\mathcal J_{q,L}[W]
=\Re\int_{\mathbb R}\overline W(u)\kappa_{q,L}(u)\,du.
\]

For the quadratic deformation source,

\[
\boxed{
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}[f_\mu]
=C_q\ell\sum_n|b_n|^2\Lambda_n^{(q,m)}(\ell).
}
\]

The longitudinal index \(n\) is the diagonal deformation mode surviving the zero centralizer-character projection.  It is not a Harish--Chandra spectral parameter.

---

## 3. Exact transverse Fourier window

Set

\[
\tau_L=\tanh\frac L2.
\]

With Fourier convention

\[
\widehat h(\xi)=\int_\mathbb R h(u)e^{i\xi u}\,du,
\]

the oriented kernel has exact transform

\[
\boxed{
\widehat\kappa_{q,L}(\xi)
=
\frac{2\pi C_L^{-2q}}{\Gamma(2q)\tau_L}
\left(\frac{-\xi}{\tau_L}\right)^{2q-1}
 e^{\xi/\tau_L}\mathbf1_{\xi<0}.
}
\]

The orientation-paired real kernel therefore has the positive even Gamma density

\[
\boxed{
\widehat{\Re\kappa_{q,L}}(\xi)
=
\frac{\pi C_L^{-2q}}{\Gamma(2q)\tau_L}
\left(\frac{|\xi|}{\tau_L}\right)^{2q-1}
 e^{-|\xi|/\tau_L}.
}
\]

Consequently the normalized positive-frequency window has

\[
\boxed{
\mathbb E|\xi|=2q\tau_L,
\qquad
\operatorname{Var}(|\xi|)=2q\tau_L^2,
}
\]

and relative width

\[
\boxed{(2q)^{-1/2}.}
\]

Hence

\[
\boxed{|\xi|\sim2q\tanh(L/2)}
\]

is an exact finite-\(q\) Gamma localization statement.

---

## 4. Representation-side radial atlas

For radial matrix coefficients

\[
M_{m,n}^{(q)}(t)
=\langle e_m,\pi_q(a_t)e_n\rangle,
\]
put

\[
\alpha=m/q,\qquad\beta=n/q,
\]
and

\[
\alpha+1=\cosh u_\alpha,
\qquad
\beta+1=\cosh u_\beta.
\]

The exact saddle discriminant gives

\[
\boxed{
t_-=|u_\alpha-u_\beta|,
\qquad
t_+=u_\alpha+u_\beta.}
\]

The same disk radial coordinate appears:

\[
\boxed{r=\tanh(t/2).}
\]

The canonical representation-side charts are ordinary saddles, Airy folds, the Bessel endpoint contraction, and the Hermite--Gaussian merger chart.

---

## 5. Quantitative compatibility theorem

The exact orbital window is organized by

\[
\tau_L=\tanh(L/2),
\]
while the exact representation coefficient extraction is organized by

\[
r_t=\tanh(t/2).
\]

Therefore both sides use the same bounded hyperbolic radial coordinate

\[
\boxed{\mathfrak r(s)=\tanh(s/2)\in[0,1).}
\]

At semiclassical order, the orbital branch concentrates at transverse frequency

\[
|\xi|=O(q\mathfrak r(L)),
\]
with width \(O(q^{1/2}\mathfrak r(L))\), while the representation branch develops caustics when the K-type moment variables satisfy the exact discriminant relation expressed in \(\mathfrak r(t)\).

Thus the common statement is

\[
\boxed{
\text{both FCIG transforms are organized by }q\text{ and the same hyperbolic radial coordinate }\tanh(s/2).
}
\]

This is a quantitative compatibility of scales and coordinates, not an equality of transform variables.

---

## 6. A typed semiclassical composition

The FCIG information response can now be displayed as the chain

\[
\boxed{
\text{deformation }\mu
\to
f_\mu
\to
T_{f_\mu}^{(q)}
\to
\operatorname{Tr}^{\rm cyc}_{\delta,m,q}
\to
\Lambda_n^{(q,m)}(\ell)
\to
\text{Gamma-windowed transverse moment}.
}
\]

Independently, the same holomorphic discrete-series block admits

\[
\boxed{
\pi_q
\to
M_{m,n}^{(q)}(t)
\to
\{\Phi_-,\Phi_+,\operatorname{Ai},J_k,H_\nu\}
}
\]

through the semiclassical atlas.

The exact Bergman identity places both chains in the same representation \(\pi_q\), but a further typed transform is required before one may compose the final scalar variables.

---

## 7. What is proved and what is not

The following are now exact/closed:

1. transported Bergman kernel = \(C_q\kappa_{q,L}\);
2. cyclic relative trace normalization = \(C_q\ell\);
3. transverse Fourier transform = exact Gamma density;
4. representation radial caustics = exact \(t_\pm\);
5. common hyperbolic radial coordinate = \(\tanh(s/2)\).

The following is **not** asserted:

\[
\xi=t,
\qquad
\xi=n,
\qquad
n=\text{Harish--Chandra spectral parameter},
\]

or any equivalent identification.

The next genuinely stronger theorem would construct a typed relative/Harish--Chandra transform carrying the cyclic orbital functional into the discrete-series spectral block.

---

## 8. Gate ledger

\[
\boxed{\textbf{OSB-A1: PASS — exact kernel crosswalk.}}
\]

\[
\boxed{\textbf{OSB-A2: PASS — exact Gamma transverse window.}}
\]

\[
\boxed{\textbf{OSB-A3: PASS — semiclassical coordinate/scale compatibility.}}
\]

\[
\boxed{\textbf{OSB-B: OPEN — typed relative/Harish--Chandra transform theorem.}}
\]

---

## Claim firewall

- Orbital integral, coherent-state matrix coefficient, K-type radial matrix coefficient, Harish--Chandra character, and cyclic relative trace are different typed objects.
- The common appearance of `tanh(s/2)` does not identify `L` with `t` in a transform-theoretic sense.
- The transverse Fourier variable `xi` remains distinct from every Harish--Chandra spectral parameter.
- The cyclic deformation index `n` remains distinct from both `xi` and the K-type label unless a formula explicitly introduces the same symbol in a typed role.
- Common Weyl denominators or common semiclassical scale `q` do not imply equality of numerators.
- No novelty claim is made for standard Bergman, Fourier, or Harish--Chandra structures.
