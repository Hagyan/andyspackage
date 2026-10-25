# Andy's Package

A modular LaTeX starter for Andrew M. Hagy's mathematics and logic writing.

- andyspackage.sty: notation and optional Kripke/proof-tree commands.
- andysnotes.sty: titles, headings, running headers, theorem counters,
  breakable statement highlights, and prose abbreviations.
- andyspics.sty: TikZ, commutative diagrams, figures, and plots.
- main.tex: an Overleaf project to copy for each new handout.
- docs/quick-start.tex and docs/quick-start.pdf: setup and examples.
- docs/cheatsheet.md and docs/cheatsheet.pdf: custom source, rendered
  symbol, and ordinary LaTeX, generated from docs/commands.psv.
- docs/llm-prompt.txt: reusable instruction for transcribing notes.
- docs/ETIQUETTE.md: living writing, notation, proof-mark, and workflow preferences.
- examples/proof-marks.tex: examples of direction proofs, casework, and tombstones.
- notes/problems.tex: an uncompiled historical design note. Its final
  command is incomplete; do not input it into a document.
- beamer/README.md: reserved for a future slide theme.

## Start in Overleaf

Upload a ZIP of this project with main.tex and the three .sty files at
its root. Set main.tex as the main document. The default uses pdfLaTeX,
a portable Times-family font, purple accents, invisible section numbers,
visible subsection numbers, and facing-page headers. Recompile.

Keep one master Overleaf project and use Copy Project for a new
assignment. Every copy contains the styles. When you revise a package, copy its updated .sty file into older projects
that need the revision; existing copies do not automatically track the master.
To publish a local edit, commit and push it to the repository. In Overleaf,
replace the matching file in the project with the updated version and recompile.

In main.tex, leave one notation line and one style line uncommented.
The lines for book, plain, minimal, and no header are ready for selection by
moving the percent sign. The minimal header shows title, author, date, current
section index, and class; add `studentid=true` and set
`\AndyStudentID{...}` to show a student ID. Page numbers remain in the footer
when `header=none`. The course, assignment, due date, subtitle,
contents, title page, bibliography, and graphics are independent choices.
A zero-indexed page counter is shown by default.

## Proof marks and style preferences

See [docs/ETIQUETTE.md](docs/ETIQUETTE.md) for the living style guide and
[examples/proof-marks.tex](examples/proof-marks.tex) for the tombstone API.
The default font remains Times. Use `font=typewriter` for the alternate inspired
by the supplied 1967 dissertation; this pairs typewritten prose with traditional
mathematical symbols while preserving Times as the default.

## Existing documents

The original six-argument \AndyTitle still works; new documents use
\title, \author, optional \AndyCourse/\AndyDue, and
\AndyMakeTitle or \AndyMakeTitlePage. The old [ii] option is
accepted as a Kripke option. ProofBlock now uses slender separators
rather than a second nested frame, allowing a long proof to cross a page.

The notation package no longer creates theorem environments on its own.
Load andysnotes for theorems, definitions, and boxes. Proof trees need
the [prooftrees] option of andyspackage.

## Reference styles

For the recommended Angus-inspired alphabetic bibliography, see
docs/bibliography-biblatex.tex and docs/references.bib. This optional
version uses Biber; it is not loaded by the default handout. Replace
the sample .bib record before citing it. For a one-off handout, a
manual thebibliography list is also available in main.tex.

## Updating the command library

1. Add a documented public command to andyspackage.sty.
2. Add a mapping and a brief semantic note in docs/commands.psv,
   then run `python3 docs/build_cheatsheet.py` to regenerate both source
   formats; compile `docs/cheatsheet.tex` for the printable PDF.
3. Update docs/symbols.tex if the symbol needs an explanation beyond
   a one-line mapping.
4. Compile main.tex, the quick start, and examples/pagebreak-demo.tex.
5. Update the master Overleaf project and make a versioned repository
   commit when the change is ready.

This is a reviewable working version. Package and title names can be
revised before the first public release.

