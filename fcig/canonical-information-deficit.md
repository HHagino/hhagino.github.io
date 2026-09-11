# Canonical Information Deficit

## OIG-B2a — a coefficient-free state-sector functional

**Status (2026-09-11).**

The general effective information functional contains constitutive coefficients. One important part, however, admits a canonical normalization without introducing any free coefficient: compare the FCIG mixed state with the maximally mixed state on the automorphic multiplicity space.

We record
\[
\boxed{\textbf{OIG-B2a: PASS — canonical state-sector information deficit.}}
\]

---

## 1. Maximally mixed reference

Let
\[
\mathcal M_q\simeq H^0(X,K_X^q),
\qquad d_q^X:=\dim\mathcal M_q,
\]
and for a nonnegative symbol \(W\) with \(\operatorname{Tr}T_W>0\), let
\[
\rho_W=\frac{T_W}{\operatorname{Tr}T_W}.
\]
Define the basis-independent maximally mixed state
\[
\boxed{\sigma_q:=\frac{I_{\mathcal M_q}}{d_q^X}.}
\tag{1.1}
\]

---

## 2. Exact relative-entropy identity

The quantum relative entropy is
\[
D(\rho\Vert\sigma)
:=\operatorname{Tr}\rho(\log\rho-\log\sigma).
\]
Since
\[
\log\sigma_q=-(\log d_q^X)I,
\]
we obtain
\[
\boxed{
D(\rho_W\Vert\sigma_q)
=\log d_q^X-S_{\rm mix}(\rho_W).
}
\tag{2.1}
\]
Thus the state-counting quantity \(\log\dim H^0\) and the mixed-state entropy are not equal; they combine canonically into an information deficit.

Define
\[
\boxed{
\mathfrak I_q(W):=D(\rho_W\Vert I/d_q^X).
}
\tag{2.2}
\]
Then
\[
\boxed{\mathfrak I_q(W)\ge0.}
\tag{2.3}
\]
Equality holds iff
\[
\rho_W=I/d_q^X.
\]

---

## 3. Constant-symbol normalization

For the constant symbol \(W\equiv1\),
\[
T_1=P_qI P_q=I_{\mathcal M_q}.
\]
Hence
\[
\rho_1=I/d_q^X
\]
and therefore
\[
\boxed{\mathfrak I_q(1)=0.}
\tag{3.1}
\]
So the canonical deficit measures deviation of the normalized Toeplitz response from the completely mixed baseline.

---

## 4. Exact first variation

For a smooth variation of \(W\), the dimension \(d_q^X\) is fixed, hence
\[
\delta\mathfrak I_q=-\delta S_{\rm mix}.
\]
Using the exact entropy variation from `effective-information-functional.md`,
\[
\boxed{
\delta\mathfrak I_q
=\frac1{Z_W}
\operatorname{Tr}\left[
T_{\delta W}(\log\rho_W+S_{\rm mix}I)
\right].
}
\tag{4.1}
\]
Equivalently,
\[
\boxed{
\frac{\delta\mathfrak I_q}{\delta W(x)}
=\frac1{Z_W}
\operatorname{Tr}\left[
\varrho_q(x)(\log\rho_W+S_{\rm mix}I)
\right].
}
\tag{4.2}
\]

---

## 5. Moduli no-go for bare state counting

For a smooth family of compact genus-\(g\) curves at fixed \(q\ge2\), Riemann--Roch gives
\[
\boxed{d_q^X=(2q-1)(g-1),}
\tag{5.1}
\]
which is constant on Teichmüller/moduli space as long as genus and \(q\) are fixed. Therefore
\[
\boxed{d\log d_q^X=0}
\tag{5.2}
\]
along ordinary moduli deformations.

Consequently, a proposal of the form
\[
\text{moduli force}=\nabla\log\dim H^0(X,K_X^q)
\]
is identically zero on each fixed-topology fixed-\(q\) component.

This is a decisive typing correction:
\[
\boxed{
\log\dim H^0
\text{ can measure state-counting across }q\text{/topology sectors, but cannot by itself generate nontrivial smooth moduli dynamics.}
}
\tag{5.3}
\]
Nontrivial moduli response must instead come from metric-dependent objects such as Bergman projectors, determinant metrics, analytic torsion, or Quillen curvature.

---

## 6. Relation to Quillen geometry

The canonical state deficit and the Quillen potential live on different variables:
\[
\mathfrak I_q(W;b)=D(\rho_W(b)\Vert I/d_q^X),
\]
while
\[
\Phi_Q(b;\Sigma)=-\log h_Q(\Sigma,\Sigma).
\]
Even though \(d_q^X\) is constant, \(\rho_W(b)\) generally varies because the Bergman projector and coherent states vary with \(b\). Thus
\[
\partial_b\mathfrak I_q
=-\partial_bS_{\rm mix}(\rho_W(b))
\]
may be nonzero.

There is no canonical numerical coefficient relating \(\mathfrak I_q\) and \(\Phi_Q\) supplied by the preceding mathematics. Any scalar combination still requires a constitutive principle.

---

## 7. Canonical state-sector slogan

The corrected FCIG entropy statement is
\[
\boxed{
\text{state-counting capacity}
-\text{actual mixing entropy}
=\text{relative information to the maximally mixed state}.
}
\tag{7.1}
\]
This is exact and basis-independent.

---

## 8. Gate ledger

\[
\boxed{\textbf{OIG-B2a: PASS.}}
\]
\[
\boxed{\textbf{OIG-B2b: PASS WITH NO-GO — bare }\log\dim H^0\textbf{ has zero smooth fixed-}q\textbf{ moduli gradient.}}
\]
\[
\boxed{\textbf{OIG-B2c: OPEN — derive a canonical coupling between state deficit and Quillen/moduli response.}}
\]

## Claim firewall

- Relative entropy to the maximally mixed state is canonical once the Hilbert space \(\mathcal M_q\) is fixed.
- Constancy of \(\dim H^0\) on a smooth fixed-genus family does not mean the Bergman kernel or Toeplitz state is constant.
- The no-go concerns smooth moduli gradients at fixed topology and fixed \(q\); jumps can occur when the geometric/topological sector changes.
- No gravitational field equation follows from the information deficit alone.