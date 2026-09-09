# FCIG Model XXV — Green–Schwarz factorization and anomaly-lattice response audit

> **Citation policy.** Bracketed keys cite established six-dimensional anomaly / Green–Schwarz / F-theory results. Statements tagged **Derived here** are algebraic consequences worked out in this note. Statements tagged **No-go** are scope restrictions established for the FCIG threshold observable used in Models XX–XXIV.

## 1. Question

Model XXIV compared the finite elliptic threshold

\[
G_{VHT}^{\rm fin}
=\frac{K}{16\pi^3L^2}Z_\tau(2)g_{\rm hyp},
\qquad
K:=2n_V-n_H+2n_T,
\]

with the free-multiplet anomaly polynomial. Because the three independent free-multiplet anomaly coefficients form an invertible linear map on \((n_V,n_H,n_T)\), one can reconstruct \(K\) from the full coefficient vector. That was coefficient-space linear algebra, not a physical identification.

The present question is stricter:

\[
\boxed{
\text{Do genuinely new Green--Schwarz / string-charge-lattice data constrain }K
\text{ beyond the multiplet counts?}
}
\]

The new data include the tensor charge lattice, the Green--Schwarz bilinear form, the gravitational anomaly vector \(a\), gauge anomaly vectors \(b_i\), global gauge-group information and the characteristic / quantization conditions needed for a globally defined Green--Schwarz term.

---

## 2. Established local Green–Schwarz data

We use the standard six-dimensional \(\mathcal N=(1,0)\) local factorization convention of Kumar–Morrison–Taylor [KMT10, KMT10global]. The factorized one-loop anomaly polynomial may be written schematically as

\[
I_8^{\rm 1-loop}
=\frac12\,\Omega_{\alpha\beta}X_4^\alpha X_4^\beta,
\]

with

\[
X_4^\alpha
=\frac12a^\alpha\operatorname{tr}R^2
+\sum_i\frac{2b_i^\alpha}{\lambda_i}\operatorname{tr}F_i^2.
\]

The Green--Schwarz counterterm has the opposite anomalous variation. Here \(\Omega\) has signature \((1,T)\), \(T\) is the number of tensor multiplets, \(a\) is the gravitational anomaly coefficient and \(b_i\) are gauge-factor anomaly coefficients. Normalizations of \(\operatorname{tr}\) and \(\lambda_i\) are convention dependent, so all coefficient equations below are kept in this one convention.

The standard local anomaly equations include [KMT10global]

\[
\boxed{H-V=273-29T},
\]

\[
\boxed{a\cdot a=9-T},
\]

and, for each simple gauge factor,

\[
0=B_{\rm Adj}-\sum_R x_R B_R,
\]

\[
a\cdot b_i
=\frac{\lambda_i}{6}
\left(A_{\rm Adj}-\sum_R x_RA_R\right),
\]

\[
b_i\cdot b_i
=\frac{\lambda_i^2}{3}
\left(\sum_Rx_RC_R-C_{\rm Adj}\right),
\]

with analogous mixed \(b_i\cdot b_j\) equations for bifundamental matter.

These formulas already show that the gauge anomaly vectors depend on representation-level information \((x_R,A_R,B_R,C_R)\), not merely the totals \((H,V,T)\).

---

## 3. Established global lattice data

Local factorization is not the complete quantum consistency condition.

The string charges take values in an integral lattice \(\Lambda_S\) of signature \((1,T)\). In a consistent supergravity theory the lattice is required to obey additional global conditions. Monnier–Moore–Park obtain quantization constraints on gauge anomaly coefficients and identify the unimodular string-charge lattice as the natural target of those coefficients [MMP18]. Under their strongest assumptions, the gauge anomaly coefficient belongs to

\[
2H^4(BG;\mathbb Z)\otimes\Lambda_S.
\]

Monnier–Moore construct the Green--Schwarz term globally and show that the gravitational anomaly coefficient must be a **characteristic element** of the string-charge lattice [MM19]. Thus

\[
\boxed{
\Lambda_S,\ \Omega,\ a,\ \{b_i\},\ G_{\rm global}
}
\]

contain information that is not captured by the three multiplet totals.

For F-theory compactifications this lattice is geometrized by the intersection lattice of the base, and the anomaly vectors map to divisor classes [KMT10global, MMP18].

---

## 4. Derived here — threshold-blindness theorem

Model XXIII uses

\[
K=2V-H+2T,
\]

where \(V\) is the total number of vector multiplets, i.e. the dimension of the gauge algebra for ordinary nonabelian/abelian gauge sectors.

Using the irreducible gravitational-anomaly equation

\[
H=273+V-29T,
\]

we obtain

\[
\boxed{
K=V+31T-273.
}
\]

### Theorem XXV.1 — threshold-blindness to fixed-\((V,T)\) lattice refinements

**Derived here.** In the restricted parity-even elliptic threshold of Model XXIII, once the six-dimensional gravitational-anomaly relation is imposed, \(K\) depends only on

1. the tensor-lattice signature through \(T\), and
2. the gauge-algebra dimension through \(V\).

It does **not** depend explicitly on

\[
a,\quad b_i,\quad
\text{their lattice embedding},\quad
\text{characteristic refinements},\quad
\text{the global form of }G,
\]

provided \(V\) and \(T\) are held fixed.

Equivalently, if two candidate theories have the same \((V,H,T)\) but differ only in Green--Schwarz/global lattice data, then Model XXIII assigns the same \(K\) to both.

This is not a statement that the theories are physically equivalent. The next example shows the opposite.

---

## 5. Same counts, different global consistency

Consider the even unimodular rank-two lattice

\[
U=(\mathbb Z^2,\Omega),
\qquad
\Omega=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

For \(T=1\), local gravitational anomaly cancellation requires

\[
a^2=8.
\]

Two vectors satisfying this local norm equation are

\[
a_{\rm good}=(2,2),
\qquad
a_{\rm bad}=(4,1).
\]

Indeed,

\[
a_{\rm good}^2=a_{\rm bad}^2=8.
\]

But the characteristic condition distinguishes them. For \(x=(m,n)\),

\[
x^2=2mn\equiv0\pmod2.
\]

The vector \(a_{\rm good}\) obeys

\[
a_{\rm good}\cdot x=2m+2n\equiv0\equiv x^2\pmod2
\]

for every \(x\in U\), while

\[
a_{\rm bad}\cdot(1,0)=1\not\equiv0=(1,0)^2\pmod2.
\]

Thus \(a_{\rm good}\) is characteristic and \(a_{\rm bad}\) is not.

Monnier–Moore–Park explicitly discuss the \(U\)-lattice candidate with

\[
a=(4,1),\qquad V=0,\qquad H=244,\qquad T=1,
\]

which satisfies the previously known local low-energy conditions but fails the characteristic-vector requirement and has no F-theory realization [MMP18].

By contrast, the standard elliptic \(\mathbb F_0\) F-theory geometry has

\[
\Omega=U,
\qquad
-a=K_{\mathbb F_0}=(-2,-2)
\]

up to the usual sign convention for \(a\); equivalently the characteristic vector has components \((2,2)\). A modern explicit compact elliptic \(\mathbb F_0\) model has

\[
H=244,\qquad V=0,\qquad T=1
\]

[HKKW25].

Both count vectors therefore give

\[
\boxed{K=-242}.
\]

### No-go XXV.2

**Derived here.** The finite threshold \(K\) cannot diagnose the global Green--Schwarz consistency of the theory: two candidates can have identical \((V,H,T)\) and identical \(K\), while the characteristic-lattice test accepts one and rejects the other.

---

## 6. Green–Schwarz consistency does not fix the sign of \(K\)

### 6.1 Negative consistent witness

For the elliptic \(\mathbb F_0\) model just discussed,

\[
(V,H,T)=(0,244,1),
\]

hence

\[
\boxed{K=-242<0}.
\]

This is an ordinary geometric F-theory realization, not an arithmetic spectrum invented to tune the sign.

### 6.2 Positive consistent witness

Wang constructs a six-dimensional F-theory model on a semi-toric generalized \(dP_9\) base with [Wang17]

\[
h^{1,1}(B)=10,\qquad T=9,
\]

and a generic elliptic threefold with

\[
h^{1,1}(X)=h^{2,1}(X)=19,
\qquad
G=U(1)^8.
\]

The standard F-theory counting gives

\[
V=8,
\qquad
H=20,
\qquad
T=9,
\]

consistent with

\[
H-V+29T=20-8+261=273.
\]

Therefore

\[
\boxed{
K=2(8)-20+2(9)=14>0.
}
\]

### No-go XXV.3 — no universal sign condition

**Derived here.** Geometrically realized F-theory models satisfying the Green--Schwarz framework occur with both

\[
K<0
\quad\text{and}\quad
K>0.
\]

Therefore Green--Schwarz factorization / anomaly-lattice consistency does not impose a universal positivity, negativity or vanishing condition on the Model-XXIII finite threshold coefficient.

---

## 7. What the new lattice data actually constrain

The preceding no-go does **not** make the lattice data redundant.

The extra data constrain objects such as

- whether the string-charge lattice is unimodular;
- whether \(a\) is characteristic;
- whether gauge anomaly coefficients satisfy integral / cohomological quantization conditions;
- whether a proposed local anomaly factorization can be promoted to a globally defined Green--Schwarz term;
- the global form of the gauge group and cocharacter lattice;
- possible global gauge and self-dual-field anomalies.

These are genuine quantum-consistency constraints [MMP18, MM19]. What fails is only the proposed implication

\[
\boxed{
\text{more refined GS/lattice consistency}
\Longrightarrow
\text{a new universal constraint on }K.
}
\]

The current FCIG threshold is simply too coarse: after gravitational anomaly cancellation it sees only \((V,T)\).

---

## 8. Why the failure is structurally expected in the current model

Models XX–XXIII set background gauge holonomies to zero. The finite automorphic tensor is a function only of the elliptic complex structure \(\tau\) and the field content:

\[
G_{VHT}^{\rm fin}
=\frac{K}{16\pi^3L^2}Z_\tau(2)g_{\rm hyp}.
\]

There is no variable in this expression on which \(b_i\), a gauge representation weight, or a cocharacter lattice can act.

### No-go XXV.4 — missing coupling channel

**Derived here.** In the gauge-blind background of Model XXIII there is no typed map

\[
\{b_i,\Lambda_{\rm cochar},\text{charge data}\}
\longrightarrow
G_{VHT}^{\rm fin}(\tau)
\]

except indirectly through the already fixed field multiplicities.

Thus it would be artificial to demand that Green--Schwarz gauge-lattice data constrain the threshold before a gauge-sensitive spectral observable has been introduced.

---

## 9. Positive next bridge: charged elliptic / Jacobi threshold

The no-go identifies the missing ingredient rather than merely stopping the program.

Introduce flat background gauge holonomies on the elliptic fiber. For a field of charge \(q\), the KK lattice is shifted schematically as

\[
(m,n)\mapsto(m+q\alpha,\,n+q\beta),
\]

or, in complex notation, by an elliptic variable

\[
z=\alpha\tau+\beta.
\]

The spectral functions then become theta/Jacobi-type objects rather than functions of \(\tau\) alone. In that enlarged model, charge lattices, representation weights and eventually Green--Schwarz gauge vectors can enter through an explicit coupling channel.

This is the appropriate next test. It is not performed in the present milestone.

---

## 10. Status table

\[
\boxed{
\begin{array}{c|c}
\text{Question}&\text{Model XXV result}\\ \hline
\text{Local GS factorization}&\text{Established}\\
\Lambda_S\text{ unimodular / }a\text{ characteristic}&\text{Established global refinement}\\
K=V+31T-273&\text{Derived here}\\
\text{Same counts, different lattice consistency}&\text{Explicit witness}\\
\text{GS consistency forces }K\ge0\text{ or }K=0&\text{False}\\
\text{Current threshold sees }b_i\text{ directly}&\text{False}\\
\text{Need gauge-sensitive/Jacobi extension}&\text{Open next gate}
\end{array}}
\]

---

## 11. Scope

This milestone compares the restricted parity-even finite elliptic threshold with six-dimensional Green--Schwarz / anomaly-lattice data. It does not claim that every spectrum satisfying local anomaly equations is a quantum theory. It explicitly distinguishes local factorization from global Green--Schwarz consistency.

No Einstein equation, horizon thermodynamics or UV-completion theorem is inferred.

---

## References used in this note

- **[KMT10]** Kumar, Morrison and Taylor, *Mapping 6D N=1 supergravities to F-theory* (2010).
- **[KMT10global]** Kumar, Morrison and Taylor, *Global aspects of the space of 6D N=1 supergravities* (2010).
- **[MMP18]** Monnier, Moore and Park, *Quantization of anomaly coefficients in 6D N=(1,0) supergravity* (2018).
- **[MM19]** Monnier and Moore, *Remarks on the Green--Schwarz Terms of Six-Dimensional Supergravity Theories* (2019).
- **[Wang17]** Wang, *Tuned and non-Higgsable U(1)s in F-theory* (2017).
- **[HKKW25]** Huang, Katz, Klemm and Wang, *Refined BPS numbers on compact Calabi--Yau threefolds from Wilson loops* (2025), elliptic \(\mathbb F_0\) spectrum example.

A machine-checkable arithmetic / lattice sanity script is in `green-schwarz-lattice.py`, and milestone BibTeX entries are in `green-schwarz-lattice.bib`.
