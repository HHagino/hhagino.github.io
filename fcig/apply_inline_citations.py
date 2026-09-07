from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

POLICY = """> **Citation policy.** Bracketed keys such as `[BF86a]` cite established background only. Statements marked **Derived here** are calculations performed in these FCIG notes; statements marked **FCIG interpretation/conjecture** are not attributed to the cited literature. Full entries are collected at the end of this note and in [`references.bib`](references.bib).\n"""

REFS = {
    "ADH21": "Amabel, Debray & Haine, *Differential Cohomology* (2021 notes/preprint).",
    "BF86a": "J.-M. Bismut & D. S. Freed, “The Analysis of Elliptic Families. I. Metrics and Connections on Determinant Bundles,” *Commun. Math. Phys.* **106** (1986).",
    "BF86b": "J.-M. Bismut & D. S. Freed, “The Analysis of Elliptic Families. II. Dirac Operators, Eta Invariants, and the Holonomy Theorem,” *Commun. Math. Phys.* **107** (1986).",
    "BL04": "C. Birkenhake & H. Lange, *Complex Abelian Varieties*, 2nd ed., Springer (2004).",
    "Bry93": "J.-L. Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser (1993).",
    "DLMF20": "NIST Digital Library of Mathematical Functions, Chapter 20, especially §20.7(viii), theta-function modular transformations.",
    "Fri85": "S. Friedberg, “Theta Functions, Weil Representations, and the Eighth Root of Unity,” *J. Number Theory* **21** (1985).",
    "Jac95": "T. Jacobson, “Thermodynamics of Spacetime: The Einstein Equation of State,” *Phys. Rev. Lett.* **75** (1995), 1260–1263.",
    "Katz73": "N. Katz, “p-adic Properties of Modular Schemes and Modular Forms,” in *Modular Functions of One Variable III*, LNM 350, Springer (1973).",
    "Lu00": "Z. Lu, “On the Lower Order Terms of the Asymptotic Expansion of Tian–Yau–Zelditch,” *Amer. J. Math.* **122** (2000).",
    "MM07": "X. Ma & G. Marinescu, *Holomorphic Morse Inequalities and Bergman Kernels*, Birkhäuser (2007).",
    "Mum83": "D. Mumford, *Tata Lectures on Theta I*, Birkhäuser (1983).",
    "Qui85": "D. Quillen, “Determinants of Cauchy–Riemann Operators over a Riemann Surface,” *Funct. Anal. Appl.* **19** (1985).",
    "Stacks-GRR": "The Stacks Project, Tag 02UO, “Grothendieck–Riemann–Roch.”",
    "SW76": "D. J. Simms & N. M. J. Woodhouse, *Lectures on Geometric Quantisation*, Lecture Notes in Physics 53, Springer (1976).",
    "ThetaHeat": "Classical Jacobi theta heat equation; see also modern expositions of heat equations for theta/sigma functions.",
    "Zel98": "S. Zelditch, “Szegő Kernels and a Theorem of Tian,” *Int. Math. Res. Notices* (1998), no. 6, 317–331.",
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
    block = ["\n---\n", marker, ""]
    for key in keys:
        block.append(f"- **[{key}]** {REFS[key]}")
    block.append("")
    return text.rstrip() + "\n" + "\n".join(block) + "\n"


def research_note(text: str) -> str:
    text = add_policy(text)
    text = insert_after(text, "is global (with the chosen standard normalization) and represents \\(c_1(\\mathscr L)\\) in de Rham cohomology.", "**Established.** This is standard Hermitian holomorphic line-bundle/Chern-connection geometry; see [Bry93]. The subsequent reading of these local weights as information potentials is an **FCIG interpretation**.", "research hermitian weights")
    text = insert_after(text, "should be regarded as differential-cohomological rather than merely de Rham data. Schematically,", "**Established.** Degree-two differential/Deligne cohomology models line bundles with connection and retains both curvature and flat-holonomy information; see [Bry93; ADH21]. Calling the two sectors “local anomaly” and “global anomaly” is **FCIG terminology**.", "research differential cohomology")
    text = insert_after(text, "For \\(k\\ge1\\), define the fiberwise holomorphic state space", "**Established background.** Holomorphic sections of a polarized/prequantum line bundle form the standard state space in holomorphic geometric quantization under the usual positivity and polarization hypotheses; see [SW76]. The family-theoretic passage to derived direct images is used below.", "research quantization")
    text = insert_after(text, "Relative Grothendieck–Riemann–Roch gives", "**Established.** The relative GRR identity for the alternating derived direct image is standard; see [Stacks-GRR]. The interpretation of degree zero as a capacity sector and degree two as an anomaly sector is **FCIG interpretation**.", "research grr")
    text = insert_after(text, "Equip \\(\\lambda_k\\) with a Hermitian metric, for instance of Quillen type when an appropriate determinant-line construction is available.", "**Established background.** Determinant lines and Quillen metrics originate in [Qui85]; natural determinant-bundle connections and their curvature/holonomy for elliptic families are developed in [BF86a; BF86b]. Calling the logarithmic norm below a free-energy potential is **FCIG interpretation**.", "research determinant")
    text = insert_after(text, "For a positive line bundle, the Tian–Catlin–Zelditch–Lu expansion has the schematic form", "**Established.** The diagonal Bergman/Szegő asymptotic expansion and its curvature coefficients are standard; see [Zel98; Lu00; MM07]. The coefficient is deliberately left as \\(c_{\\mathrm{BK}}\\) because it depends on curvature and \\(2\\pi\\) normalization conventions.", "research bergman")
    text = insert_after(text, "Riemann–Roch gives", "**Established background.** Standard line-bundle and polarization theory on elliptic and abelian varieties is collected in [BL04; Mum83]. The specific “single-bundle no-go” conclusion below is **derived here** from those standard facts.", "research abelian RR")
    text = insert_after(text, "This establishes a mathematically controlled direction", "**Established background.** Families index theory controls determinant-line curvature and holonomy from geometric/gauge curvature data; see [BF86a; BF86b]. No inverse map from determinant anomaly to spacetime curvature is asserted by those references.", "research families index")
    text = insert_after(text, "A more physical alternative is inspired by Jacobson's local horizon thermodynamics.", "**Established reference point.** Jacobson derives the Einstein equation as an equation of state from the Clausius relation applied to local Rindler horizons together with an entropy-area assumption [Jac95]. The FCIG entropy functional sought here is **not** supplied by that paper.", "research jacobson")
    return append_refs(text, ["Bry93","ADH21","SW76","Stacks-GRR","Qui85","BF86a","BF86b","Zel98","Lu00","MM07","BL04","Mum83","Jac95"])


def elliptic_model(text: str) -> str:
    text = add_policy(text)
    text = insert_after(text, "Take the classical degree-one theta line \\(L\\to E_\\tau\\).", "**Established background.** The theta line, theta characteristics, quasi-periodicity, and their relation to line bundles on elliptic/abelian varieties are classical; see [Mum83; BL04; DLMF20].", "elliptic theta line")
    text = insert_after(text, "By Riemann–Roch,", "**Established.** For a positive degree-\\(k\\) line bundle on an elliptic curve, \\(h^0=k\\); see the standard abelian-variety treatment in [BL04].", "elliptic h0")
    text = insert_after(text, "We obtain the exact Gram matrix", "**Derived here.** The exact normalization of the \\(L^2\\) Gram matrix in the present coordinates and metric is computed in this note; it is not attributed to [Mum83], [BL04], or the determinant-line literature.", "elliptic gram")
    text = insert_after(text, "Poisson summation gives the exact Fourier expansion", "**Derived here.** The Poisson-resummed lattice formula below is obtained directly from the explicit theta basis. For comparison with the general local asymptotic theory, see [Zel98; Lu00; MM07].", "elliptic poisson")
    text = insert_after(text, "Thus, for fixed \\(\\tau\\),", "**Derived here.** The exponentially small lattice correction and the normalized-systole bound below are consequences of the exact lattice sum in this note. Calling this a “nonperturbative global sector” is **FCIG terminology**.", "elliptic exp sector")
    text = insert_after(text, "The Jacobi theta function satisfies the heat equation", "**Established.** The classical theta heat equation is standard; see [Mum83; ThetaHeat]. The level-\\(k\\) rescaling used below is **derived here**.", "elliptic heat")
    text = insert_after(text, "The Hodge line over the upper half-plane is", "**Established background.** The Hodge bundle is the standard line bundle whose powers encode modular forms in the moduli interpretation; see [Katz73]. The specific metric normalization and curvature computation below are **derived here**.", "elliptic hodge")
    text = insert_after(text, "Therefore", "**Derived here (elliptic normalization).** The determinant/Hodge curvature coefficient \\(-k/2\\) below follows from the exact Gram determinant computed in this note. [Qui85; BF86a] provide determinant-line context, not this specific coefficient.", "elliptic determinant identity")
    return append_refs(text, ["Mum83","BL04","DLMF20","Zel98","Lu00","MM07","ThetaHeat","Katz73","Qui85","BF86a"])


def modular_holonomy(text: str) -> str:
    text = add_policy(text)
    text = insert_after(text, "We first derive the action of the modular generators", "**Established background.** Classical theta functions transform under \\(S\\) and \\(T\\) with characteristic permutations and square-root automorphy factors; see [DLMF20; Mum83]. Exact finite matrices below are then derived in our convention.", "modular ST background")
    text = insert_after(text, "Thus the finite matrix is", "**Derived here (our convention).** The finite Fourier/phase matrices below are computed from the chosen level-\\(k\\) theta basis. [Fri85] is cited for the general Weil/metaplectic framework, not for these exact sign and normalization conventions.", "modular finite matrices")
    text = insert_after(text, "A direct Gauss-sum calculation gives", "**Derived here (our convention).** The phase in the following relation is obtained from the explicit finite matrices. [Fri85] supports the general Weil-representation/eighth-root phenomenon.", "modular gauss")
    text = insert_after(text, "For odd \\(k\\), the situation changes.", "**Established background.** The classical \\(T\\)-move permutes theta-characteristic sectors; see [DLMF20; Mum83]. The exact level-\\(k\\) swap and \\(T^2\\) closure below are **derived here**.", "modular odd k")
    text = insert_after(text, "Define the corrected anomaly line", "**Derived here.** The flat line below is formed by combining the elliptic determinant/Hodge curvature identity from Explicit Model I. The general principle that flat differential-cohomological data may retain nontrivial holonomy is standard [Bry93; ADH21]; the phrase “flat anomaly line” is **FCIG terminology**.", "modular flat anomaly")
    return append_refs(text, ["DLMF20","Mum83","Fri85","Bry93","ADH21"])


JOBS = {"research-note.md": research_note, "elliptic-model.md": elliptic_model, "modular-holonomy.md": modular_holonomy}
for name, fn in JOBS.items():
    path = ROOT / name
    original = path.read_text(encoding="utf-8")
    updated = fn(original)
    if updated == original:
        print(f"{name}: no changes")
    else:
        path.write_text(updated, encoding="utf-8")
        print(f"{name}: updated")
