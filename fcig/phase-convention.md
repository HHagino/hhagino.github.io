# FCIG Radial Phase Convention

## Publication convention for the semiclassical preprint

**Status (2026-09-10): FROZEN for the semiclassical branch.**

This note fixes the minimum phase convention needed to state the radial semiclassical theorem without conflating convention-dependent compact phases with invariant radial amplitudes.

Let \(\pi_q\) be the holomorphic discrete-series representation in the normalized monomial basis \(e_n\), and define

\[
M_{m,n}^{(q)}(t):=\langle e_m,\pi_q(a_t)e_n\rangle,
\qquad t\ge0,
\]

for the positive Cartan representative \(a_t\). We choose the basis phases so that the radial coefficient for \(n\ge m\) is the real Jacobi expression

\[
\boxed{
M_{m,n}^{(q)}(t)=
\mathcal N_{m,n}(q)
\left(\cosh\frac t2\right)^{-2q}
\left(\tanh\frac t2\right)^{n-m}
P_m^{(n-m,2q-1)}\left(1-2\tanh^2\frac t2\right),
}
\]

with positive normalization

\[
\mathcal N_{m,n}(q)=
\left(\frac{m!\Gamma(2q+n)}{n!\Gamma(2q+m)}\right)^{1/2}.
\]

For the opposite index ordering we do **not** introduce a second independent asymptotic formula. We use unitarity/adjoint symmetry:

\[
\boxed{
M_{m,n}^{(q)}(-t)=\overline{M_{n,m}^{(q)}(t)}.
}
\]

Equivalently, after restricting to the positive radial chamber \(t\ge0\), the \(m>n\) sector is obtained from the \(n>m\) sector by swapping the indices together with the representation-theoretic adjoint/orientation reversal. In the frozen real radial gauge this reduces all modulus, caustic, and rate statements to the ordered pair

\[
\boxed{\alpha_{\max}=\max(m,n)/q,\qquad\alpha_{\min}=\min(m,n)/q.}
\]

Hence the invariant caustic statement is

\[
\boxed{
t_-=|u_m-u_n|,\qquad t_+=u_m+u_n,}
\]

where

\[
\cosh u_m=1+\frac mq,\qquad\cosh u_n=1+\frac nq
\]

at the semiclassical level.

For a full Cartan decomposition \(g=k_{\theta_1}a_tk_{\theta_2}\), the compact variables contribute basis-character phases. These are deliberately factored away in the radial theorem. Changing the phase convention of the K-type basis multiplies \(M_{m,n}\) by a unit complex scalar depending on the two indices, but leaves

\[
|M_{m,n}^{(q)}(t)|,
\quad t_\pm,
\quad \Phi_\pm,
\quad \text{and the canonical Airy/Bessel/Hermite type}
\]

unchanged.

## Orientation firewall

The following are distinct operations and must not be silently identified:

1. swapping \(m\) and \(n\);
2. reversing the Cartan orientation \(t\mapsto-t\);
3. complex conjugating a matrix coefficient;
4. reversing an oriented closed geodesic on the orbital side.

For radial representation theory, (1)--(3) are tied by the adjoint identity above. Operation (4) belongs to the orbital/cyclic-trace sector and requires its own geometric orientation convention.

Therefore the preprint uses the phrase **"up to the frozen compact K-phase"** whenever only the radial canonical model is relevant, and never transfers this phase statement directly to the orbital trace.

## Consequence for boundary charts

The Bessel chart is written for \(n=m+k\), \(k\ge0\). The opposite ordering follows by the adjoint convention, so the invariant boundary parameter is

\[
\boxed{k=|n-m|.}
\]

Likewise the lowest-K Hermite chart is stated with the smaller index fixed. Under index exchange the same canonical Hermite--Gaussian modulus is obtained after applying the adjoint/orientation convention.

## Claim firewall

- This note fixes a **publication convention**, not a new representation-theoretic theorem.
- The radial Jacobi formula is convention-dependent by a unit phase; its modulus and saddle geometry are not.
- The orientation of a closed geodesic in the FCIG orbital sector is not determined by this K-type phase convention.
- No Harish--Chandra character is being treated as an ordinary Hilbert-space trace.
