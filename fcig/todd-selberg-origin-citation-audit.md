# Todd–Selberg Origin — Citation Audit

**Date:** 2026-09-10  
**Note:** [`todd-selberg-origin.md`](todd-selberg-origin.md)  
**Bibliography:** [`todd-selberg-origin.bib`](todd-selberg-origin.bib)

This audit separates characteristic-class facts, spectral/geodesic results, and FCIG deductions. In particular, three distinct zeta functions are never identified with one another.

| Claim | Status | Source(s) | Audit boundary |
| --- | --- | --- | --- |
| `Td(T_pi)=x/(e^x-1)` for `x=c1(K_{X/B})` in relative complex dimension one | **Established** | GRR standard; [BGS88] for differential-form refinement | Uses `T_pi=K^{-1}`. |
| `x/(e^x-1)=1-x/2+x^2/12-...` and `1/12=B_2/2!=-zeta_R(-1)` | **Established arithmetic identity** | standard Bernoulli/zeta identity | This does **not** identify Riemann zeta with Selberg zeta. |
| `e^{qx}Td(T_pi)` has degree-two coefficient `q-1/2` and degree-four coefficient `(6q^2-6q+1)/12` | **Derived here / elementary expansion** | GRR input | Direct multiplication of characteristic series. |
| `h^0(X,K^q)=(2q-1)(g-1)` for `q>=2` | **Established** | Riemann--Roch + Serre duality | Degree-two projection of the same GRR integrand. |
| `c1(det R pi_* K^q)=[(6q^2-6q+1)/12] pi_*(x^2)` in cohomology, up to determinant convention | **Established GRR consequence** | [BGS88], standard GRR | Sign/dualization convention must be declared. |
| Quillen curvature is the degree-two fiber integral of Chern--Weil representatives of `Td(T_pi) ch(K^q)` | **Established** | [BGS88] | Differential-form refinement of GRR. |
| The compact hyperbolic local-index coefficient is proportional to `6q^2-6q+1` times the Weil--Petersson form | **Established** | [TZ87; FRZ20] | Numerical `pi` factors depend on whether one writes Hermitian pairings, `(1,1)` forms, or first Chern forms. |
| The Mumford determinant relation has exponent `6q^2-6q+1` | **Established global determinant-line relation** | [Eri08], background [Mum83] | The note uses a rational/canonical determinant-line form and does not claim Mumford 1983 as the unique original source. |
| Selberg zeta is an Euler product over primitive closed geodesics | **Established** | [FRZ20] | This is the global hyperbolic-dynamical zeta function, distinct from Riemann zeta. |
| Spectral zeta regularization gives `det' A=exp[-zeta_A'(0)]` | **Established** | Quillen/Ray--Singer background; [Qui85; BGS88] | This is the determinant-regularization zeta, distinct from both Riemann and Selberg zeta. |
| For the hyperbolic shifted Laplacian, the zeta-regularized determinant is Selberg zeta times Gamma/Barnes-double-Gamma factors independent of Teichmueller moduli | **Established** | [FRZ20] | Hence the moduli Hessian of the determinant equals that of the Selberg factor. |
| `dbar_mu d_mu log Z_Sel(q)=-Chern^(q)+(6q(q-1)+1)/(12pi) G_WP` in the repository Hermitian normalization | **Established after normalization translation** | [FRZ20; TZ87] | The source formula and repository convention must not be mixed without the stated normalization firewall. |
| `dbar d log Z_Sel(q)=O(q^2 exp(-q ell_0))` on a fixed compact hyperbolic surface | **Established** | [FRZ20] | `ell_0` is the shortest closed geodesic length. |
| Constant-curvature diagonal Bergman kernels have exponentially small high-power errors | **Established** | [Ber12] | Berman's theorem is stated in his Kähler-volume normalization. |
| `B_q^{dA}=(2q-1)/(4pi)+O(exp(-delta_X q))` for the canonical hyperbolic model | **Derived normalization conversion** | [Ber12] | Uses `omega=c1(K)=dA/(2pi)`, curvature normalization and tensor-power index `k=q`. |
| Exact remainder identity `Bfrak_q-Kfrak_q-1/(12pi)G_WP = 2 dbar d log Z_Sel(q) + integral (|mu|^2+2(q-1)f_mu) beta_q` | **Derived here** | exact inputs: [FRZ20] + definitions | Main local/global algebraic decomposition; no source is claimed to state it. |
| `Bfrak_q-Kfrak_q=1/(12pi)G_WP+O(q^2 exp(-c_X q))` | **Derived here** | [FRZ20; Ber12] | Fixed-surface statement; uniform moduli version requires thick-part control. |
| There are no further inverse-power corrections to this difference on a fixed compact hyperbolic surface | **Derived consequence** | previous row | Exponential remainder is beyond all algebraic orders. |
| `I_HBF,q^KE-Kfrak_q` obeys the same exponential-offset formula | **Derived through companion FCIG result** | BLS/HBF companion notes + previous row | Uses the separately audited identification `I_HBF,q^KE=Bfrak_q`. |
| The offset has an arithmetic Riemann--Roch / Arakelov height interpretation | **OPEN** | — | Suggested research direction only. |
| Riemann zeta, spectral zeta and Selberg zeta are the same object | **Explicitly FALSE / NOT claimed** | — | They enter three different layers of the argument. |
| The exponential terms are literal physical instantons | **NOT claimed** | — | “Nonperturbative” means beyond all powers of `q^{-1}`; closed-geodesic exponentials are the rigorous content. |

## Primary-source metadata checked

The following were checked against publisher, author, arXiv, or archival pages on 2026-09-10:

- Bismut--Gillet--Soulé, *Communications in Mathematical Physics* **115** (1988), 301--351, DOI `10.1007/BF01466774`.
- Zograf--Takhtajan, *Russian Mathematical Surveys* **42**(6) (1987), 169--190, DOI `10.1070/RM1987V042N06ABEH001501`.
- Fedosova--Rowlett--Zhang, *Annals of Global Analysis and Geometry* **57** (2020), 23--60, DOI `10.1007/s10455-019-09687-4`, arXiv:1709.03841.
- Berman, *International Mathematics Research Notices* **2012**(22), 5031--5062, DOI `10.1093/imrn/rnr229`, arXiv:1106.4902.
- Wan--Zhang, *Geometriae Dedicata* **214** (2021), 489--517, DOI `10.1007/s10711-021-00625-y`.
- Mumford, *Arithmetic and Geometry II*, Progress in Mathematics **36** (1983), 271--328, DOI `10.1007/978-1-4757-9286-7_12`.
- Eriksson, *A Deligne--Riemann--Roch Isomorphism*, Thèses d'Orsay no. 752 (2008), NUMDAM archive.

## The three-zeta firewall

### Riemann zeta

`zeta_R(-1)=-1/12` is the Bernoulli special value underlying the Todd coefficient. Its role is local arithmetic/characteristic-class bookkeeping.

### Spectral zeta

`zeta_A(s)` regularizes elliptic determinants. It is the analytic determinant bridge used in Ray--Singer/Quillen theory.

### Selberg zeta

`Z_Sel(s)` packages primitive closed-geodesic lengths. Its moduli variation supplies the exponentially small global correction to the local-index polynomial in the compact hyperbolic problem.

The argument uses a chain of relations among these roles; it never equates the functions.

## Degree-projection firewall

For a relative complex curve, fiber integration lowers real degree by two. Therefore:

- degree two of `e^{qx} Td(T_pi)` gives the virtual rank/state count;
- degree four gives `c1` of the determinant/direct-image line.

The degree-four computation only needs the `x^2` Todd coefficient. This is why the local determinant polynomial is exactly quadratic in `q`. It is not, by itself, a general theorem that every other observable has a truncated asymptotic expansion.

## Exponential-remainder firewall

The exponential theorem is safest for a fixed compact hyperbolic surface. Uniform estimates on a compact subset of the thick part are plausible with bounded-geometry constants but are not asserted here. Near the Deligne--Mumford boundary the systole tends to zero, so the exponential scale degenerates and boundary corrections must be treated separately.

## Novelty firewall

The ingredients are classical or established: GRR/Todd classes, Quillen curvature, Mumford determinant relations, Selberg zeta variation, and constant-curvature Bergman asymptotics. The FCIG contribution in this note is the assembled exact remainder formula and its information-geometric interpretation. A targeted search did not reveal this exact package, but that is **not** a novelty certification. A publication version requires broader MathSciNet/zbMATH/reference-chain and expert review.