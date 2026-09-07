from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

POLICY = """> **Citation policy.** Bracketed keys cite established background only. Statements marked **Derived here** are calculations carried out in these FCIG notes; statements marked **FCIG interpretation/conjecture** are not attributed to the cited literature. Full entries are collected at the end of this note and in [`references.bib`](references.bib).\n"""

REFS = {
    "ADH21": "A. Amabel, A. Debray & P. J. Haine, *Differential Cohomology: Categories, Characteristic Classes, and Connections* (2021), arXiv:2109.12250.",
    "BF86a": "J.-M. Bismut & D. S. Freed, “The Analysis of Elliptic Families. I. Metrics and Connections on Determinant Bundles,” *Communications in Mathematical Physics* **106** (1986), 159–176.",
    "BF86b": "J.-M. Bismut & D. S. Freed, “The Analysis of Elliptic Families. II. Dirac Operators, Eta Invariants, and the Holonomy Theorem,” *Communications in Mathematical Physics* **107** (1986), 103–163.",
    "BL04": "C. Birkenhake & H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer (2004).",
    "Bry93": "J.-L. Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser (1993).",
    "DLMF20": "NIST Digital Library of Mathematical Functions, Chapter 20, especially §20.7(viii), transformations of the lattice parameter.",
    "Fri85": "S. Friedberg, “Theta Function Transformation Formulas and the Weil Representation,” *Journal of Number Theory* **20**(2) (1985), 121–127.",
    "Jac95": "T. Jacobson, “Thermodynamics of Spacetime: The Einstein Equation of State,” *Physical Review Letters* **75**(7) (1995), 1260–1263.",
    "Katz73": "N. M. Katz, “p-adic Properties of Modular Schemes and Modular Forms,” in *Modular Functions of One Variable III*, LNM 350, Springer (1973), 69–190.",
    "Lu00": "Z. Lu, “On the Lower Order Terms of the Asymptotic Expansion of Tian–Yau–Zelditch,” *American Journal of Mathematics* **122**(2) (2000), 235–273.",
    "MM07": "X. Ma & G. Marinescu, *Holomorphic Morse Inequalities and Bergman Kernels*, Progress in Mathematics 254, Birkhäuser (2007).",
    "Mum83": "D. Mumford, *Tata Lectures on Theta I*, Progress in Mathematics 28, Birkhäuser (1983).",
    "Qui85": "D. Quillen, “Determinants of Cauchy–Riemann Operators over a Riemann Surface,” *Functional Analysis and Its Applications* **19**(1) (1985), 31–34.",
    "Stacks-GRR": "The Stacks Project, Tag 02UO, “Grothendieck–Riemann–Roch.”",
    "SW76": "D. J. Simms & N. M. J. Woodhouse, *Lectures on Geometric Quantization*, Lecture Notes in Physics 53, Springer (1976).",
    "Zel98": "S. Zelditch, “Szegő Kernels and a Theorem of Tian,” *International Mathematics Research Notices* **1998**(6), 317–331.",
}


def insert_after(text: str, needle: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    if needle not in text:
        raise RuntimeError(f"missing insertion target: {label}")
    return text.replace(needle, needle + "\n\n" + addition, 1)


def add_policy(text: str) -> str:
    if "**Citation policy.**" in text:
        return text
    m = re.search(r"(\*\*Date:\*\*[^\n]*\n)", text)
    if m:
        return text[:m.end()] + "\n" + POLICY + text[m.end():]
    return text.replace("\n---\n", "\n---\n\n" + POLICY + "\n", 1)


def append_refs(text: str, keys: list[str]) -> str:
    marker = "## References cited in this note"
    if marker in text:
        return text
    block = ["\n---\n", marker, "", "Canonical BibTeX entries: [`references.bib`](references.bib).", ""]
    for key in keys:
        block.append(f"- **[{key}]** {REFS[key]}")
    block.append("")
    return text.rstrip() + "\n" + "\n".join(block) + "\n"


def research_note(text: str) -> str:
    text = add_policy(text)
    text = insert_after(text, "is global (with the chosen standard normalization) and represents \\(c_1(\\mathscr L)\\) in de Rham cohomology.", "**Established.** This is standard Hermitian holomorphic line-bundle/Chern-connection geometry; see [Bry93]. The subsequent reading of these local weights as information potentials is an **FCIG interpretation**.", "research hermitian weights")
    text = insert_after(text, "should be regarded as differential-cohomological rather than merely de Rham data. Schematically,", "**Established.** Differential/Deligne cohomology provides a model for line bundles with connection and retains curvature together with flat-holonomy data; see [Bry93; ADH21]. Calling the two sectors “local anomaly” and “global anomaly” is **FCIG terminology**.", "research differential cohomology")
    text = insert_after(text, "For \\(k\\ge1\\), define the fiberwise holomorphic state space", "**Established background.** Holomorphic sections of a polarized/prequantum line bundle form the standard state space in holomorphic geometric quantization under the usual positivity and polarization hypotheses; see [SW76].", "research quantization")
    text = insert_after(text, "Relative Grothendieck–Riemann–Roch gives", "**Established.** The relative GRR identity for the alternating derived direct image is standard; see [Stacks-GRR]. Reading degree zero as a capacity sector and degree two as an anomaly sector is an **FCIG interpretation**.", "research grr")
    text = insert_after(text, "Equip \\(\\lambda_k\\) with a Hermitian metric, for instance of Quillen type when an appropriate determinant-line construction is available.", "**Established background.** Determinant lines and Quillen metrics originate in [Qui85]; natural determinant-bundle connections and their curvature/holonomy for elliptic families are developed in [BF86a; BF86b]. Calling the logarithmic norm below a free-energy potential is an **FCIG interpretation**.", "research determinant")
    text = insert_after(text, "For a positive line bundle, the Tian–Catlin–Zelditch–Lu expansion has the schematic form", "**Established.** The diagonal Bergman/Szegő asymptotic expansion and its curvature coefficients are standard; see [Zel98; Lu00; MM07]. The coefficient is deliberately kept as \\(c_{\\mathrm{BK}}\\) because it depends on curvature and \\(2\\pi\\) normalization conventions.", "research bergman")
    text = insert_after(text, "### 11.3 Abelian variety", "**Established background.** Standard line-bundle, polarization, and theta-group theory on abelian varieties is developed in [BL04; Mum83]. The “single-bundle no-go” below is a short consequence **derived here**, not a named result from those sources.", "research abelian")
    text = insert_after(text, "This establishes a mathematically controlled direction", "**Established background.** Families index theory controls determinant-line curvature and holonomy from geometric/gauge curvature data; see [BF86a; BF86b]. Those references do **not** assert an inverse map from determinant anomaly to spacetime curvature.", "research families index")
    text = insert_after(text, "A more physical alternative is inspired by Jacobson's local horizon thermodynamics.", "**Established reference point.** Jacobson derives the Einstein equation as an equation of state from the Clausius relation on local Rindler horizons together with an entropy-area assumption [Jac95]. The FCIG entropy functional sought here is **not** supplied by that paper.", "research jacobson")
    return append_refs(text, ["Bry93","ADH21","SW76","Stacks-GRR","Qui85","BF86a","BF86b","Zel98","Lu00","MM07","BL04","Mum83","Jac95"])


def elliptic_model(text: str) -> str:
    text = add_policy(text)
    text = insert_after(text, "## 2. The degree-one theta line", "**Established background.** Theta series, quasi-periodicity, theta characteristics, and their relation to line bundles on elliptic/abelian varieties are classical; see [Mum83; BL04; DLMF20].", "elliptic theta")
    text = insert_after(text, "No asymptotic Riemann–Roch approximation is needed here.", "**Established.** The dimension \\(h^0(E_\\tau,L^k)=k\\) is the standard positive-degree elliptic-curve/abelian-variety case of Riemann–Roch; see [BL04].", "elliptic h0")
    text = insert_after(text, "## 4. Exact \\(L^2\\) Gram matrix of the theta basis", "**Derived here.** The exact \\(L^2\\) Gram normalization below is computed in the coordinates and Hermitian metric fixed in this note; it is not attributed to [Mum83], [BL04], or the determinant-line literature.", "elliptic gram")
    text = insert_after(text, "## 6. Poisson-resummed Bergman formula", "**Derived here.** The exact lattice Fourier formula below follows directly from the explicit theta basis and Poisson summation. For comparison with the general local Bergman asymptotic theory, see [Zel98; Lu00; MM07].", "elliptic poisson")
    text = insert_after(text, "## 7. Local curvature versus global lattice memory", "**Derived here.** The exponentially small lattice sector follows from the exact formula in §6. Calling it a “nonperturbative global sector” is **FCIG terminology**. The contrast with local power-series asymptotics uses [Zel98; Lu00; MM07].", "elliptic global")
    text = insert_after(text, "## 9. Heat equation and the theta-state connection", "**Established background.** The classical Jacobi theta heat equation is standard; see [Mum83]. The level-\\(k\\) rescaling and the FCIG interpretation of moduli variation as state evolution are **derived/interpreted here**.", "elliptic heat")
    text = insert_after(text, "## 10. The Hodge line over \\(\\mathbb H\\)", "**Established background.** The Hodge bundle is the standard line bundle whose powers encode modular forms in the moduli interpretation; see [Katz73]. The metric normalization \\(\\|dz\\|^2=Y\\) and the curvature calculation below are **derived here**.", "elliptic hodge")
    text = insert_after(text, "## 11. Determinant of the theta-state bundle", "**Derived here (elliptic normalization).** The determinant/Hodge curvature coefficient \\(-k/2\\) below follows from the exact Gram determinant in §4. [Qui85; BF86a] provide determinant-line context, not this specific coefficient.", "elliptic determinant")
    return append_refs(text, ["Mum83","BL04","DLMF20","Zel98","Lu00","MM07","Katz73","Qui85","BF86a"])


def modular_holonomy(text: str) -> str:
    text = add_policy(text)
    text = insert_after(text, "## 1. Setup and conventions", "**Established background.** Classical theta functions transform under modular \\(S\\) and \\(T\\) moves with characteristic permutations and square-root automorphy factors; see [DLMF20; Mum83]. The exact finite matrices used later are derived in this note's convention.", "modular setup")
    text = insert_after(text, "# 2. The \\(S\\)-transformation", "**Derived here (our convention), with standard background.** The finite Fourier matrix below is obtained directly from Poisson summation for the chosen level-\\(k\\) theta basis. [Fri85] is cited for the general Weil/metaplectic framework, not for our exact signs and normalizations.", "modular S")
    text = insert_after(text, "## 3.2 Odd \\(k\\)", "**Established background.** The modular \\(T\\)-move permutes theta-characteristic sectors in the classical theory [DLMF20; Mum83]. The exact level-\\(k\\) swap formulas and \\(T^2\\) closure below are **derived here**.", "modular odd")
    text = insert_after(text, "# 4. Finite Weil matrices at even level", "**Derived here (our convention).** The relations among \\(U_S\\), \\(U_T\\), charge conjugation, and the Gauss phase are verified from the explicit finite matrices below. [Fri85] supports the general Weil-representation and eighth-root-of-unity phenomenon.", "modular Weil")
    text = insert_after(text, "# 7. Hodge curvature and exact cancellation", "**Derived here.** The corrected line \\(\\mathscr A_k=\\det\\mathcal H_k\\otimes\\lambda_H^{k/2}\\) and its vanishing Chern curvature follow from Explicit Model I. The general principle that flat connection data may retain nontrivial holonomy is standard [Bry93; ADH21]; the phrase “flat anomaly line” is **FCIG terminology**.", "modular flat line")
    return append_refs(text, ["DLMF20","Mum83","Fri85","Bry93","ADH21"])


JOBS = {
    "research-note.md": research_note,
    "elliptic-model.md": elliptic_model,
    "modular-holonomy.md": modular_holonomy,
}

for name, fn in JOBS.items():
    path = ROOT / name
    original = path.read_text(encoding="utf-8")
    updated = fn(original)
    if updated == original:
        print(f"{name}: no changes")
    else:
        path.write_text(updated, encoding="utf-8")
        print(f"{name}: updated")
