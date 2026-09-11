# Compact Automorphic Closure for FCIG

## Master statement — 2026-09-11

Let

\[
X=\Gamma\backslash\mathbb H
\]

be a compact torsion-free hyperbolic surface, let

\[
G=PSL(2,\mathbb R),
\qquad
\pi_q=D^+_{2q-1},
\]

and let \(H^0(X,K_X^q)\) be the compact holomorphic \(q\)-differential space.

The compact FCIG representation-theoretic architecture is now separated into the correct tensor factors and kernel categories.

### Theorem A — automorphic multiplicity

\[
\boxed{
L^2(\Gamma\backslash G)
\simeq
\widehat\bigoplus_\pi
\mathcal M_\pi\widehat\otimes\mathcal H_\pi,
}
\]

and the holomorphic \(q\)-differentials are the lowest-K automorphic vectors in the \(\pi_q\)-isotypic summand:

\[
\boxed{
H^0(X,K_X^q)
\simeq
\mathcal M_q\otimes\ell_q^{\rm low}.
}
\]

Thus

\[
\dim\mathcal M_q
=
\begin{cases}
g,&q=1,\\
(2q-1)(g-1),&q\ge2.
\end{cases}
\]

### Theorem B — convolution no-go

A scalar group convolution acts as

\[
I_{\mathcal M_q}\otimes\pi_q(f).
\]

After lowest-K compression it is a scalar multiple of the identity on \(\mathcal M_q\). Therefore a generic compact Toeplitz operator

\[
T_W^{X,q}\in\operatorname{End}(\mathcal M_q)
\]

cannot be represented as the \(\pi_q\)-Fourier block of one scalar group convolution kernel.

### Theorem C — two-point compact Toeplitz kernel

The correct compact object is

\[
\boxed{
\mathbb K_W^{X,q}(x,y)
=
\int_XB_{X,q}(x,z)W(z)B_{X,q}(z,y)dA(z).
}
\]

It acts directly on \(H^0(X,K_X^q)\) and retains the full multiplicity matrix \(T_W^{X,q}\).

### Theorem D — closed-geodesic trace shadow

The scalar trace is

\[
\boxed{
\operatorname{Tr}T_W^{X,q}
=
\int_XW(x)B_{X,q}(x,x)dA(x).
}
\]

For \(q\ge2\), periodizing the universal Bergman kernel and regrouping nonidentity deck transformations by primitive conjugacy class yields

\[
\boxed{
\operatorname{Tr}T_W^{X,q}
=
\text{identity/local term}
+
\sum_{[\delta]\in\mathcal P_{\rm or}}
\sum_{m\ge1}
C_q\ell_\delta\mathcal J_{q,m\ell_\delta}[W_\delta],
}
\]

with

\[
C_q=\frac{2q-1}{4\pi}.
\]

Thus the exact Sun/cyclic orbital contribution is the **Selberg shadow of the compact two-point Toeplitz kernel**.

---

## 1. Correct master diagram

The compact FCIG diagram is

\[
\boxed{
\begin{array}{ccccc}
&&\mathbb K_W^{X,q}(x,y)&&\\[1mm]
&\swarrow&&\searrow&\\[1mm]
T_W^{X,q}\in\operatorname{End}(\mathcal M_q)
&&&&
\operatorname{Tr}T_W^{X,q}\\[1mm]
&&&&\downarrow\\[-1mm]
&&&&
\{C_q\ell\mathcal J_{q,m\ell}[W]\}_{[\delta],m}.
\end{array}}
\]

The full matrix and the closed-geodesic scalar data are not equal-information objects. They are different shadows of the same two-point kernel.

---

## 2. Relation to the universal semiclassical branch

On the universal disk, the discrete-series Hilbert space \(\mathcal H_{\pi_q}\) still supplies the exact local coherent/Bergman kernel and the semiclassical matrix-coefficient atlas:

\[
\boxed{
\text{ordinary saddle}
\cup\operatorname{Ai}
\cup J_k
\cup H_\nu e^{-\tau^2/2}.
}
\]

The universal theorem acts on \(\mathcal H_{\pi_q}\). The compact theorem acts on the multiplicity space \(\mathcal M_q\). Their relation is through periodization of the **kernel**, not identification of the operator factors:

\[
\boxed{
\text{universal Bergman/discrete-series kernel}
\xrightarrow{\Gamma\text{-periodization}}
\mathbb K^{X,q}
\xrightarrow{\text{operator/trace projections}}
\begin{cases}
T_W^{X,q},\\
\text{closed-geodesic trace data}.
\end{cases}}
\]

This is the correct local-to-global bridge.

---

## 3. Fisher/Bergman interpretation

The identity element in the periodized diagonal produces the local Bergman term. In the FCIG information-geometry branch this is the source of the local Fisher/Bergman response and its large-q Weil--Petersson scaling.

The nonidentity elements produce the closed-geodesic correction:

\[
\boxed{
\text{identity deck term}
\leftrightarrow
\text{local Fisher/Bergman geometry},
}
\]

\[
\boxed{
\text{nonidentity conjugacy classes}
\leftrightarrow
\text{global cyclic/Selberg response}.
}
\]

Thus the local/global decomposition is literally the identity/nonidentity decomposition of the same automorphic Bergman kernel.

---

## 4. Information lost by taking the trace

For

\[
s_i,s_j\in H^0(X,K_X^q),
\]

the exact matrix entry is

\[
\boxed{
\langle s_i,T_W^{X,q}s_j\rangle
=
\int_XW(x)\langle s_i(x),s_j(x)\rangle dA(x).
}
\]

The ordinary Selberg conjugacy decomposition appears only after taking a trace/diagonal. Therefore it cannot generically reconstruct all matrix entries.

The state-decorated problem belongs to a relative/pre-trace theory with external automorphic states; see `matrix-element-trace-firewall.md`.

---

## 5. Status ledger

\[
\boxed{\textbf{AM-A1: PASS — automorphic multiplicity.}}
\]
\[
\boxed{\textbf{AM-A2: PASS — scalar-convolution no-go.}}
\]
\[
\boxed{\textbf{AM-B1: PASS — compact two-point Toeplitz kernel.}}
\]
\[
\boxed{\textbf{AM-B2: PASS — closed-geodesic trace descent.}}
\]
\[
\boxed{\textbf{AM-C1: PASS — matrix-element/trace firewall.}}
\]
\[
\boxed{\textbf{AM-C2: OPEN — state-decorated relative trace theory.}}
\]

At the structural level, the **compact automorphic FCIG branch is closed through the scalar trace/Selberg layer**.

The open AM-C2 is a stronger matrix-reconstruction problem, not a missing step in the scalar trace theorem.

---

## 6. Slogan

\[
\boxed{
\textbf{The universal representation controls the local kernel; the automorphic multiplicity controls the compact matrix; the diagonal conjugacy trace controls the Selberg shadow.}
}
\]

## Claim firewall

- \(H^0(X,K_X^q)\) is not the universal discrete-series Hilbert space.
- Compact Toeplitz matrices and universal group-Fourier blocks act on different tensor factors.
- Periodization is performed at the kernel level.
- Closed-geodesic scalar data are trace shadows and are not claimed to determine the full Toeplitz matrix.
- The high-weight \(q\ge2\) periodized-kernel statement is the safe absolutely convergent regime used here; \(q=1\) requires a separate low-weight treatment.
- No novelty claim is made for standard automorphic decomposition, Riemann--Roch, Bergman periodization, or pre-trace theory.

## Cross-references

- `automorphic-multiplicity-firewall.md`
- `automorphic-two-point-kernel-closure.md`
- `matrix-element-trace-firewall.md`
- `typed-orbital-fourier-closure.md`
- `schwartz-completion.md`
- `disk-transported-bergman.md`
- `cyclic-relative-trace.md`
- `semiclassical-atlas-closure.md`