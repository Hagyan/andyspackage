# Andy's Package: command cheat sheet

The printed column uses ordinary LaTeX notation, so it displays even
outside this package. Load andyspackage before andysnotes.
The package source is the authority if a row and implementation disagree.

For semantic consequence use `\entails`; for a structure satisfying a formula use `\satisfies`. Both look like a double turnstile, but the names keep the roles clear.

The complete LLM prompt below is maintained in docs/llm-prompt.txt and
printed in the quick-start PDF. To add a symbol, edit andyspackage.sty
and add one row to docs/commands.psv, then regenerate this file.

## LLM quick-start prompt

```text
Typeset my handwritten mathematics and logic notes as a LaTeX handout for
Overleaf. This project contains andyspackage.sty and andysnotes.sty. Load
andyspackage before andysnotes; enable the [kripke] option only for Kripke
helpers and [prooftrees] only for bussproofs derivations. Load andyspics only
if a figure, diagram, or plot needs it.

Use commands actually defined in andyspackage wherever they fit. For
semantic consequence write \Gamma\entails\varphi; for truth in a structure
write \Str\satisfies\varphi; for syntactic derivability write
\Gamma\proves\varphi; for Kripke forcing write w\forces\varphi. Use
\NN, \ZZ, \QQ, \RR, \CC for number systems, and \tuple, \struc, \set
when appropriate. Prefer these aliases to bare \vDash, \models, \vdash,
or \mathbb{R}; use ordinary LaTeX if no custom command exists. Never
invent a package command. Consult docs/cheatsheet.md for the command list.

Preserve the order and mathematical claims in the notes. Mark illegible
writing in source comments beginning "% UNCLEAR:" and list ambiguities
after the complete main.tex. Do not silently repair a proof or change a
definition. Use an ordinary proof environment for long proofs, or
ProofBlock for a proof nested in a boxed statement so pages can break.
Return the complete main.tex and a brief list of required project files.
```

## Delimiters

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $(x)$ | `\parens{x}` | `\left(x\right)` | parentheses |
| $[x]$ | `\bracks{x}` | `\left[x\right]` | square brackets |
| $\{x\}$ | `\braces{x}` | `\left\{x\right\}` | braces |
| $\langle x\rangle$ | `\angles{x}` | `\left\langle x\right\rangle` | angle brackets |
| $\lvert x\rvert$ | `\abs{x}` | `\lvert x\rvert` | absolute value |
| $\lVert x\rVert$ | `\norm{x}` | `\lVert x\rVert` | norm |
| $\lceil x\rceil$ | `\ceil{x}` | `\left\lceil x\right\rceil` | ceiling |
| $\lfloor x\rfloor$ | `\floor{x}` | `\left\lfloor x\right\rfloor` | floor |
| $\{x,y\}$ | `\set{x,y}` | `\left\{x,y\right\}` | set |

## Logic

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\vdash$ | `\proves` | `\vdash` | syntactic derivability |
| $\nvdash$ | `\notproves` | `\nvdash` | non-derivability |
| $\vDash$ | `\entails` | `\vDash` | semantic consequence |
| $\nvDash$ | `\notentails` | `\nvDash` | non-entailment |
| $\models$ | `\satisfies` | `\models` | truth in one structure |
| $\not\models$ | `\notsatisfies` | `\not\models` | non-satisfaction |
| $\Vdash$ | `\forces` | `\Vdash` | forcing |
| $\nVdash$ | `\notforces` | `\nVdash` | non-forcing |
| $\bot$ | `\contradiction` | `\bot` | contradiction |
| $\Longrightarrow\bot$ | `\impliesbottom` | `\Longrightarrow\bot` | implication to bottom |
| $\Longrightarrow\bot$ | `\impliesbot` | `\Longrightarrow\bot` | alias |
| $\bot$ | `\bottom` | `\bot` | bottom |
| $\top$ | `\yippee` | `\top` | top |
| $p\Vdash_P\varphi$ | `\forcesP{P}{p}{\varphi}` | `p\Vdash_P\varphi` | forcing indexed by poset |
| $\Gamma\vdash_S\Delta$ | `\turnstile[S]{\Gamma}{\Delta}` | `\Gamma\vdash_S\Delta` | labeled sequent |
| $\vdash$ | `\fCenter` | `\vdash` | bussproofs center symbol |

## Metavariables

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\mathcal{V}$ | `\Var` | `\mathcal{V}` | variables |
| $\mathcal{F}$ | `\Frm` | `\mathcal{F}` | formulas |
| $\mathcal{M}$ | `\Str` | `\mathcal{M}` | structure |
| $\mathcal{L}$ | `\Lang` | `\mathcal{L}` | language |
| $\mathrm{Th}$ | `\Th` | `\mathrm{Th}` | theory |

## Maps and arrows

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\rightarrowtail$ | `\inj` | `\rightarrowtail` | injection |
| $\twoheadrightarrow$ | `\surj` | `\twoheadrightarrow` | surjection |
| $\hookrightarrow$ | `\incl` | `\hookrightarrow` | inclusion map |
| $\not\hookrightarrow$ | `\notincl` | `\not\hookrightarrow` | not inclusion map |
| $\xrightarrow{\sim}$ | `\isoarrow` | `\xrightarrow{\sim}` | isomorphism arrow |
| $\leftrightarrow$ | `\bij` | `\leftrightarrow` | bijection-exists convention |
| $\rightarrowtail\!\twoheadrightarrow$ | `\isbij` | `\rightarrowtail\mkern-14.75mu\twoheadrightarrow` | composite bijection arrow |
| $\Longleftrightarrow$ | `\iffarrow` | `\Longleftrightarrow` | logical iff |
| $\hookrightarrow\!\twoheadrightarrow$ | `\barbbij` | `\mathrlap{\hookrightarrow}\mkern4.5mu\twoheadrightarrow` | barbed bijection |
| $\not\hookrightarrow\!\twoheadrightarrow$ | `\notbarbbij` | `\not\!(\mathrlap{\hookrightarrow}\mkern4.5mu\twoheadrightarrow)` | negated barbed bijection |
| $\leftrightarrow$ | `\hbij` | `\rotatebox{180}{\hookrightarrow}\ \hookrightarrow` | hooked two-way arrow |

## Coding and vectors

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\ulcorner\varphi\urcorner$ | `\gcode{\varphi}` | `\ulcorner\varphi\urcorner` | Gödel corners |
| $\ulcorner$ | `\gcodel` | `\ulcorner` | left corner |
| $\urcorner$ | `\gcoder` | `\urcorner` | right corner |
| $\llcorner\varphi\lrcorner$ | `\gfloor{\varphi}` | `\llcorner\varphi\lrcorner` | lower corners |
| $\ulcorner\varphi\urcorner$ | `\tarski{\varphi}` | `\ulcorner\varphi\urcorner` | coding alias |
| $\overset{\rightharpoonup}{v}$ | `\harpvec{v}` | `\accentset{\rightharpoonup}{v}` | harpoon vector |
| $\overset{\rightharpoonup}{\mathbf0}$ | `\zerovec` | `\accentset{\rightharpoonup}{\mathbf0}` | zero vector |

## Kripke and structures

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\langle a,b\rangle$ | `\tuple{a,b}` | `\langle a,b\rangle` | tuple |
| $\langle A,R\rangle$ | `\struc{A,R}` | `\langle A,R\rangle` | structure |
| $\succeq$ | `\kripkesucceq` | `\succeq` | accessibility orientation |
| $\succ$ | `\kripkesucc` | `\succ` | strict accessibility |
| $\preceq$ | `\kripkepreceq` | `\preceq` | converse |
| $\prec$ | `\kripkeprec` | `\prec` | strict converse |
| $\mathcal W$ | `\Worlds` | `\mathcal W` | worlds; kripke option |
| $\succeq$ | `\Acc` | `\succeq` | legacy alias; kripke option |
| $\mathcal F$ | `\Frame` | `\mathcal F` | frame; kripke option |
| $\mathcal M$ | `\Model` | `\mathcal M` | model; kripke option |
| $\langle W,R\rangle$ | `\kripkeframe{W}{R}` | `\langle W,R\rangle` | frame; kripke option |
| $\langle W,R,V\rangle$ | `\kripkemodel{W}{R}{V}` | `\langle W,R,V\rangle` | model; kripke option |
| $\succ$ | `\AccS` | `\succ` | strict legacy alias |
| $\preceq$ | `\AccInv` | `\preceq` | converse legacy alias |
| $\prec$ | `\AccInvS` | `\prec` | strict converse legacy alias |
| $\geqslant$ | `\gecurly` | `\geqslant` | slanted greater-or-equal |

## Blackboard bold

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\mathbb N$ | `\NN` | `\mathbb N` | naturals |
| $\mathbb Z$ | `\ZZ` | `\mathbb Z` | integers |
| $\mathbb Q$ | `\QQ` | `\mathbb Q` | rationals |
| $\mathbb R$ | `\RR` | `\mathbb R` | reals |
| $\mathbb C$ | `\CC` | `\mathbb C` | complex numbers |
| $\mathbb F$ | `\FF` | `\mathbb F` | field |
| $\mathbb P$ | `\PP` | `\mathbb P` | context-dependent P |
| $\mathbb A$ | `\AAA` | `\mathbb A` | blackboard A |
| $\mathbb B$ | `\BBB` | `\mathbb B` | blackboard B |
| $\mathbb S$ | `\SSS` | `\mathbb S` | blackboard S |
| $\mathbb X$ | `\XXX` | `\mathbb X` | blackboard X |
| $\mathbb R$ | `\Reals` | `\mathbb R` | verbose alias |
| $\mathbb N$ | `\Naturals` | `\mathbb N` | verbose alias |
| $\mathbb Z$ | `\Integers` | `\mathbb Z` | verbose alias |
| $\mathbb Q$ | `\Rationals` | `\mathbb Q` | verbose alias |
| $\mathbb C$ | `\Complexes` | `\mathbb C` | verbose alias |

## Alphabets

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\mathcal L$ | `\MathCal{L}` | `\mathcal L` | calligraphic |
| $\mathbb R$ | `\MathBB{R}` | `\mathbb R` | blackboard bold |
| $\mathbf v$ | `\MathBold{v}` | `\mathbf v` | bold |
| $\mathrm{Th}$ | `\MathRoman{Th}` | `\mathrm{Th}` | upright |
| $\mathscr L$ | `\MathScript{L}` | `\mathscr L` | script; fallback calligraphic |

## Model and set theory

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\mathrm{FOL}$ | `\FOL` | `\mathrm{FOL}` | first-order logic |
| $f\upharpoonright_A$ | `\restrict{f}{A}` | `f\!\upharpoonright_A` | restriction |
| $\operatorname{dom}$ | `\dom` | `\operatorname{dom}` | domain |
| $\operatorname{ran}$ | `\ran` | `\operatorname{ran}` | range |
| $\operatorname{field}$ | `\field` | `\operatorname{field}` | field |
| $\operatorname{rank}$ | `\rank` | `\operatorname{rank}` | rank |
| $\operatorname{TC}$ | `\TC` | `\operatorname{TC}` | transitive closure |
| $\operatorname{cf}$ | `\cf` | `\operatorname{cf}` | cofinality |
| $\operatorname{otp}$ | `\otp` | `\operatorname{otp}` | order type |
| $\mathrm{Ord}$ | `\Ord` | `\mathrm{Ord}` | ordinals |
| $\mathcal P(X)$ | `\Pow{X}` | `\mathcal P\!\left(X\right)` | power set |
| $\operatorname{Mod}$ | `\Mod` | `\operatorname{Mod}` | models operator |

## Relations

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $\subseteq$ | `\containedin` | `\subseteq` | subset or equal |
| $\subset$ | `\propcontainedin` | `\subset` | author-dependent proper subset |
| $\subsetneq$ | `\emphpropcontainedin` | `\subsetneq` | unambiguous proper subset |
| $\nsubseteq$ | `\notcontainedin` | `\nsubseteq` | not subset or equal |
| $\not\subset$ | `\notpropcontainedin` | `\not\subset` | not proper subset |
| $\supseteq$ | `\containedby` | `\supseteq` | superset or equal |
| $\supset$ | `\propcontainedby` | `\supset` | author-dependent proper superset |
| $\supsetneq$ | `\emphpropcontainedby` | `\supsetneq` | unambiguous proper superset |
| $\nsupseteq$ | `\notcontainedby` | `\nsupseteq` | not superset or equal |
| $\not\supset$ | `\notpropcontainedby` | `\not\supset` | not proper superset |
| $\cong$ | `\isoto` | `\cong` | isomorphic |
| $\in$ | `\belongsto` | `\in` | membership |
| $\land$ | `\aand` | `\land` | conjunction |
| $\land$ | `\conjunction` | `\land` | conjunction alias |
| $\lor$ | `\oor` | `\lor` | disjunction |
| $\lor$ | `\disjunction` | `\lor` | disjunction alias |
| $\nexists$ | `\notexists` | `\nexists` | nonexistence |

## Proof trees

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| $rule label$ | `\rlabel{Cut}` | `\RightLabel{\scriptsize Cut}` | rule label helper; prooftrees option |
| — | `\WeakL{A}` | `\RightLabel{\scriptsize(Weak L)}\UnaryInfC{A}` | weakening left |
| — | `\WeakR{A}` | `\RightLabel{\scriptsize(Weak R)}\UnaryInfC{A}` | weakening right |
| — | `\ContrL{A}` | `\RightLabel{\scriptsize(Contr L)}\UnaryInfC{A}` | contraction left |
| — | `\ContrR{A}` | `\RightLabel{\scriptsize(Contr R)}\UnaryInfC{A}` | contraction right |
| — | `\ExchL{A}` | `\RightLabel{\scriptsize(Exch L)}\UnaryInfC{A}` | exchange left |
| — | `\ExchR{A}` | `\RightLabel{\scriptsize(Exch R)}\UnaryInfC{A}` | exchange right |
| — | `\Cut{A}` | `\RightLabel{\scriptsize(Cut)}\BinaryInfC{A}` | cut |
| — | `\ImpR{A}` | `\RightLabel{\scriptsize($\to$R)}\UnaryInfC{A}` | implication right |
| — | `\ImpL{A}` | `\RightLabel{\scriptsize($\to$L)}\BinaryInfC{A}` | implication left |
| — | `\AndR{A}` | `\RightLabel{\scriptsize($\wedge$R)}\BinaryInfC{A}` | and right |
| — | `\AndL{A}` | `\RightLabel{\scriptsize($\wedge$L)}\UnaryInfC{A}` | and left |
| — | `\OrRone{A}` | `\RightLabel{\scriptsize($\vee$R1)}\UnaryInfC{A}` | or right 1 |
| — | `\OrRtwo{A}` | `\RightLabel{\scriptsize($\vee$R2)}\UnaryInfC{A}` | or right 2 |
| — | `\OrL{A}` | `\RightLabel{\scriptsize($\vee$L)}\BinaryInfC{A}` | or left |
| — | `\NegR{A}` | `\RightLabel{\scriptsize($\neg$R)}\UnaryInfC{A}` | negation right |
| — | `\NegL{A}` | `\RightLabel{\scriptsize($\neg$L)}\UnaryInfC{A}` | negation left |
| — | `\TopR{A}` | `\RightLabel{\scriptsize($\top$R)}\UnaryInfC{A}` | top right |
| — | `\BotL{A}` | `\RightLabel{\scriptsize($\bot$L)}\UnaryInfC{A}` | bottom left |
| — | `\AllR{A}` | `\RightLabel{\scriptsize($\forall$R)}\UnaryInfC{A}` | forall right |
| — | `\AllL{A}` | `\RightLabel{\scriptsize($\forall$L)}\UnaryInfC{A}` | forall left |
| — | `\ExR{A}` | `\RightLabel{\scriptsize($\exists$R)}\UnaryInfC{A}` | exists right |
| — | `\ExL{A}` | `\RightLabel{\scriptsize($\exists$L)}\UnaryInfC{A}` | exists left |

## Document helpers

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| — | `\LogicLegend` | `\Gamma\vdash\varphi; \Gamma\vDash\varphi` | insert relation legend |
| — | `\KripkeLegend` | `manual explanatory paragraph` | insert Kripke legend; kripke option |
| — | `\IJSection{Heading}` | `\section{Heading} plus legends` | section with optional legends |

## Formatting

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| — | `\AndyMakeTitle` | `manual center environment` | flexible inline title |
| — | `\AndyMakeTitlePage` | `titlepage environment` | separate title page |
| — | `\AndyStartBodyPages` | `\clearpage\pagenumbering{arabic}\setcounter{page}{0}` | body pagination |
| — | `\AndySubtitle{Text}` | `manual title text` | optional subtitle |
| — | `\AndyCourse{Text}` | `manual title text` | optional course |
| — | `\AndyAssignment{Text}` | `manual title text` | optional assignment |
| — | `\AndyDue{Text}` | `manual title text` | optional due date |
| — | `\AndyAffiliation{Text}` | `manual title text` | optional affiliation |
| — | `\AndyTitle[]{A}{1}{Title}{Due}{Name}` | `manual center environment` | legacy six-argument title |
| WLOG | `\WLoG` | `\textsc{wlog}` | without loss of generality |
| WTS | `\WTS` | `\textsc{wts}` | want to show |
| WRT | `\WRT` | `\textsc{wrt}` | with respect to |
| SFSoC | `\SFSoC` | `\textsc{sfsoc}` | suppose for sake of contradiction |
| — | `\DearFriends{Name}{Text}` | `lettrine and calligra` | letter opening |
| — | `\AndyRunningTitle{Short title}` | `fancyhdr running head` | optional even-page short title |

## Environments

| Printed | With package | Without package | Use |
|:--|:--|:--|:--|
| — | `definition / DefinitionBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `lemma / LemmaBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `proposition / PropositionBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `claim / ClaimBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `example / ExampleBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `chaff / ChaffBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `aside / AsideBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `theorem / TheoremBlock` | `amsthm newtheorem / breakable tcolorbox` | separate theorem counter |
| — | `conjecture / ConjectureBlock` | `amsthm newtheorem / breakable tcolorbox` | separate conjecture counter |
| — | `corollary / CorollaryBlock` | `amsthm newtheorem / breakable tcolorbox` | roman under theorem |
| — | `proof / ProofBlock` | `amsthm proof / thin separators` | page-break-friendly |
| — | `remark / RemarkBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `note / NoteBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `exercise / ExerciseBlock` | `amsthm newtheorem / breakable tcolorbox` | shared subsection counter |
| — | `ntheorem / nlemma / ndefinition` | `theorem / lemma / definition` | legacy aliases |
| — | `nproposition / ncorollary / nremark` | `proposition / corollary / remark` | legacy aliases |
| — | `nchaff / naside / nclaim` | `chaff / aside / claim` | legacy aliases |
