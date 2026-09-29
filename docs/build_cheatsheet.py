#!/usr/bin/env python3
"""Build the Markdown command sheet from commands.psv; also check coverage."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
rows = []
for number, line in enumerate((root / "docs/commands.psv").read_text().splitlines(), 1):
    if not line or line.startswith("#"):
        continue
    fields = line.split("|")
    if len(fields) != 5:
        raise ValueError(f"commands.psv:{number}: expected five fields")
    rows.append(fields)

tick = chr(96)
out = [
    "# Andy's Package: command cheat sheet",
    "",
    "The printed column uses ordinary LaTeX notation, so it displays even",
    "outside this package. Load andyspackage before andysnotes.",
    "The package source is the authority if a row and implementation disagree.",
    "",
    "For semantic consequence use " + tick + r"\entails" + tick +
    "; for a structure satisfying a formula use " + tick + r"\satisfies" + tick +
    ". Both look like a double turnstile, but the names keep the roles clear.",
    "",
    "The complete LLM prompt below is maintained in docs/llm-prompt.txt and",
    "printed in the quick-start PDF. To add a symbol, edit andyspackage.sty",
    "and add one row to docs/commands.psv, then regenerate this file.",
    "",
    "## LLM quick-start prompt",
    "",
    "```text",
    (root / "docs/llm-prompt.txt").read_text().strip(),
    "```",
    "",
]
current = None
nonmath = {"rule", "text", "heading", "title", "title page", "page 0", "header",
           "metadata", "WLOG", "WTS", "WRT", "SFSoC", "drop cap", "statement", "proof"}
for category, source, display, ordinary, meaning in rows:
    if category != current:
        if current is not None:
            out.append("")
        out.extend([f"## {category}", "",
                    "| Printed | With package | Without package | Use |",
                    "|:--|:--|:--|:--|"])
        current = category
    render = "—" if display in nonmath else "$" + display + "$"
    if display in {"WLOG", "WTS", "WRT", "SFSoC"}:
        render = display
    out.append("| " + render + " | " + tick + source + tick + " | " +
               tick + ordinary + tick + " | " + meaning + " |")
out.append("")
(root / "docs/cheatsheet.md").write_text("\n".join(out))

# The same table also produces a printable LaTeX reference. Source snippets
# are detokenized, so braces and backslashes print without expansion.
tex = [
    r"\documentclass[9pt,letterpaper,twoside]{extarticle}",
    r"\usepackage[margin=.68in,headheight=40pt]{geometry}",
    r"\usepackage[kripke]{andyspackage}",
    r"\usepackage[header=book,font=times,accent=purple]{andysnotes}",
    r"\usepackage{longtable}",
    r"\usepackage{xurl}",
    r"\title{Andy's Package}",
    r"\AndySubtitle{Command cheat sheet}",
    r"\author{Andrew M. Hagy}",
    r"\date{}",
    r"\begin{document}",
    r"\setcounter{page}{0}",
    r"\AndyMakeTitle",
    r"\small",
    r"The printed column shows the symbol. The two source columns show how to",
    r"type it with and without the package. Commands marked as optional need",
    r"their named package option. For an LLM transcription prompt, copy",
    r"\path{docs/llm-prompt.txt}; it is printed in the quick-start guide.",
    r"\par\medskip",
]
current = None
for category, source, display, ordinary, meaning in rows:
    if category != current:
        if current is not None:
            tex += [r"\bottomrule", r"\end{longtable}", ""]
        tex += [
            r"\section{" + category + "}",
            r"\setlength{\tabcolsep}{3pt}",
            r"\begin{longtable}{@{}p{.13\textwidth}p{.25\textwidth}p{.34\textwidth}p{.22\textwidth}@{}}",
            r"\toprule",
            r"Printed & With package & Without package & Use \\",
            r"\midrule",
            r"\endfirsthead",
            r"\toprule",
            r"Printed & With package & Without package & Use \\",
            r"\midrule",
            r"\endhead",
        ]
        current = category
    if display in nonmath:
        printed = r"\textsc{" + display + "}" if display in {"WLOG", "WTS", "WRT", "SFSoC"} else r"\textemdash"
    else:
        printed = "$" + display + "$"
    tex.append(printed + r" & \texttt{\detokenize{" + source + r"}} & \texttt{\detokenize{" + ordinary + "}} & " + meaning + r" \\")
    tex.append(r"\addlinespace[.2em]")
tex += [r"\bottomrule", r"\end{longtable}", r"\end{document}", ""]
(root / "docs/cheatsheet.tex").write_text("\n".join(tex))

public = set()
for file in ("andyspackage.sty", "andysnotes.sty"):
    src = (root / file).read_text()
    for a, b in re.findall(
        r"\\(?:newcommand|providecommand|renewcommand|NewDocumentCommand|"
        r"DeclareMathOperator|DeclarePairedDelimiter)\s*"
        r"(?:\{\\([A-Za-z@]+)\}|\\([A-Za-z@]+))", src):
        name = a or b
        if "@" not in name and name not in {
            "sectionmark", "subsectionmark", "headrulewidth", "headrule",
            "thedefinition", "thecorollary", "qedsymbol",
        }:
            public.add(name)
listed = set()
for _, source, _, _, _ in rows:
    match = re.match(r"\\([A-Za-z]+)", source)
    if match:
        listed.add(match.group(1))
missing = public - listed
if missing:
    raise SystemExit("Unlisted public commands: " + ", ".join(sorted(missing)))
print(f"{len(rows)} documented rows; all {len(public)} public commands covered.")
