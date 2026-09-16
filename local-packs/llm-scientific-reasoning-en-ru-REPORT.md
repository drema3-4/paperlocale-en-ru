# Corpus report: llm-scientific-reasoning-en-ru

Version 0.1.0; English (`en`) → Russian (`ru-RU`). Local pack, outside the Python package. Created 2026-09-16.

## Corpus and extraction

All 8 PDFs (201 physical PDF pages, including appendices) were opened read-only and processed locally with the repository virtual environment’s PyMuPDF. Both sorted text and block-order extraction were inspected; page-level text coverage was audited. Extracted text was temporary working data under `/tmp/paperlocale-corpus/`, not pack content. No OCR, provider call, embedded code execution, or PDF modification was performed. Page numbers below are physical PDF page numbers, not printed proceedings pagination.

| Ref | PDF in input_articles/ | Pages | Text-layer assessment |
|---|---|---:|---|
| P1 | Anchoring Depends on Confidence and Post-Training in Language Models.pdf | 7 | Usable on all pages; two-column interleaving, equations and table alignment need care. |
| P2 | Belief Revision. The Adaptability of Large Language Models Reasoning.pdf | 17 | Main text usable; p.16 has only caption text (98 non-whitespace characters), with annotation instructions/questions in raster screenshots. Figure text elsewhere may also be partial. |
| P3 | Competing Biases underlie Overconfidence.pdf | 22 | Main article pp.1–14 usable; pp.15–22 have zero extractable text. Rendered inspection identifies the appended Nature reporting-summary form; p.15 includes a raster image, later pages use vector outlines. These pages were excluded from lexical extraction. |
| P4 | DiscoverPhysics.pdf | 34 | Usable; tables, code listings and agent transcripts have fragmented line order and typographic substitutions. |
| P5 | Evolving Scientific Discovery by Unifying Data and.pdf | 38 | Usable; polynomial formulae, subscripts, superscripts and proof layouts are particularly fragile in plain text. |
| P6 | Experiments or Outcomes. Probing Scientific Feasibility in Large.pdf | 10 | Usable; pipeline figure merges labels and descriptions in sorted extraction. |
| P7 | From Evidence to Belief. A Bayesian Epistemology Approach to Language Models.pdf | 34 | Usable; dense tables, probability notation and appendix prompt templates require layout-aware reading. |
| P8 | PhysGym.pdf | 39 | Usable; figures and long model transcripts mix with narrative. P.39 has only 86 non-whitespace characters but is a genuine short continuation of a JSON example, not a scan. |

No entire article was unparseable. Coverage is partial for P2 and P3 as described above; the image-only content was not silently treated as parsed. Rendered spot checks were used to distinguish screenshots/forms from blank pages, not to transcribe them into the pack.

## Domain and scope

The common field is computational scientific reasoning and discovery, especially evaluation of large language models. Subfields: belief revision and defeasible logic; Bayesian epistemology and evidence quality; confidence calibration and cognitive biases; scientific-claim feasibility assessment; interactive physics discovery; symbolic regression, polynomial optimization and axiomatic law discovery. P5 supplies a mathematical discovery method rather than another LLM experiment, so the pack includes its optimization vocabulary without presenting AI-Hilbert as an LLM.

Physics coverage is limited to concepts used by the supplied discovery benchmarks: particle dynamics, generalized charges, screening, fractional operators, mechanics and electrostatics. Medical/biological examples in test questions do not justify a biomedical domain expansion. No taxon or gene was selected: particle species means particle type, while species names in unfilled publisher-form examples are not subject-area evidence.

## Pack inventory and gate design

- Glossary: 118 entries; 6 required; 112 recommendations.
- Evaluation: 40 short, newly authored source/reference pairs. They test translation conventions, not reproduce or independently verify the papers’ experimental findings. Numerical examples are synthetic except the retained corpus DOI; they must not be read as reported results.
- The pack directory contains exactly manifest.json, prompt.txt, glossary.tsv and eval_cases.jsonl.
- Manifest inspected against src/paperlocale/domains.py and tests/fixtures/en-ru/manifest.json. The loader accepts ru and ru-RU; the fixture uses ru-RU and language_identity explicitly treats them as equivalent.
- source_term_is_present uses a case-insensitive left boundary excluding ASCII letters/digits and hyphen variants, followed by a literal source substring, with NO right boundary. Singular prefixes may match plurals or longer words. Required targets use casefolded substring containment; there is no lemmatization, stemming or grammatical analysis.
- Consequently no Russian lexical translation is a hard requirement. The six required entries are PyMC, SymPy, Belief-R, DiscoverPhysics, PHYSGYM and AI-Hilbert. They retain names in Russian prose, including constructions such as «в SymPy». Casefold matching tolerates all-caps branding. Acronyms remain soft entries because expansions and source-prefix collisions should not create extra glossary failures; the core abbreviation contract independently protects applicable tokens.
- The shared provider prompt serializes source/target glossary pairs, but not notes or required flags (providers/base.py). Therefore essential disambiguation and inflection policies are also in prompt.txt. Notes retain detailed scope and provenance for human review.
- All six required names appear in eval cases; removing each name from its reference is checked below. A glossary cannot force the first-use expansion globally: notes and prompt explain the policy without imposing an exact Russian expansion in every segment.

## Major decisions

1. Belief revision → «пересмотр убеждений», with premise → «посылка» and defeasible inference → «отменяемый вывод». Beliefs are operational model states, not evidence of consciousness. Modus ponens/tollens can remain Latin.
2. Confidence → «уверенность»; certainty in P1 → «определённость», specifically the maximum candidate probability in the control distribution, not entropy or factual accuracy. Confidence interval → «доверительный интервал». Over/underconfidence retains its reference baseline (empirical correctness versus Bayesian ideal observer).
3. P7 conflicting evidence replaces original statements; contradictory evidence adds negations to retained originals. The policy distinguishes «данные, противоречащие эталонным» from «внутренне противоречивые данные». Golden evidence → «эталонные данные»; coincidental evidence → «обоснование случайно верного ответа».
4. P6 scientific feasibility → «научная допустимость» of the claim, not practical engineering feasibility. FEASIBLE/INFEASIBLE remain machine labels. Experiments and outcomes are distinct evidence channels; withheld context does not remove parametric knowledge.
5. Symbolic regression → «символьная регрессия»; semidefinite optimization → «полуопределённое программирование». Mathematical certificates establish properties relative to assumptions, not unconditional empirical truth. Particle species → «тип частиц»; generalized charge is not necessarily electric charge.

## Other disambiguation and names

Prior may denote an earlier belief, a probability distribution, or provided knowledge. Accuracy is a fraction correct for classification, factual correctness in P1, or predictive accuracy measured by trajectory error in P4. MSE is not RMSE; standard error is not standard deviation. Likelihood and log odds are not probability. Anchor has a cognitive meaning in P1 and can denote a physical source/point in P4. Coupling can be statistical association or physical interaction. Scientific discovery in a benchmark may recover a known law. Confidence in the originally chosen option must not be silently changed to confidence in the final choice.

Retain model/version names (Llama, Qwen, Gemma and other exact original identifiers), dataset names (Belief-R, SciQ, TriviaQA, GSM8K, MATTER-OF-FACT, REASONS), method/platform names (DiscoverPhysics/DISCOVERPHYSICS, PHYSGYM, AI Hilbert/AI-Hilbert), and software names (PyMC, SymPy). Preserve the source spelling of versions and branding. Ordinary reasons remains translatable. Positivstellensatz is a German theorem name retained in Latin script; it is not a biological Latin name. Established Russian eponyms such as Кеплер, Гаген — Пуазейль and Грёбнер are appropriate in mathematical/physical terms.

Standard and local abbreviations are recorded without forcing an expansion: LLM, CoM, ECE, MAE, MSE, TVD, MCC, OUCS and BREU; the prompt also covers OLS, LME and CoT/COT. First-use expansions depend on document context; core token preservation still applies.

## Human review and unresolved wording

- «Научная допустимость» for scientific feasibility is a deliberate local policy, not a claim of universally standardized Russian usage. A subject expert should check it against P6’s operational label definitions.
- Choice-supportive bias → «искажение в пользу сделанного выбора» is descriptive; confirm the preferred Russian cognitive-psychology term. Do not equate it automatically with confirmation bias.
- Delta reasoning → «дельта-рассуждение», the P7 evidence-category translations, «снижение подтверждённости», and «убедительность свидетельств» need expert/editorial agreement. They are soft recommendations.
- Review «оценка Брайера» versus «метрика Брайера» and Russian exposition of OUCS/BREU. Preserve names and definitions.
- In P3 the OUCS discussion, formula label MCS, sign conventions and apparent repeated terms in the corrected-ratio formula cannot be confidently standardized from extracted text. Compare the rendered original; do not silently repair the mathematics.
- P1 names its error MAE while writing the absolute difference between an expected response and truth. Do not replace that definition with an assumed conventional expectation of absolute errors.
- The P2 abstract has awkward wording about additional information and prior conclusions; the nonmonotonic example relies on contextual interpretation of conditions. Do not strengthen it into a formal entailment claim unsupported by the paper.
- P5 uses multiple Positivstellensatz versions and conditional complexity claims. A real-algebraic-geometry expert should review the exact certificate property and assumptions; retaining the German term avoids inventing a universal Russian theorem title.
- P4 non-coordinate-free physics, fractional operators and generalized charges require mathematical-physics review. Preserve intentionally noncanonical simulated laws.
- P8 model transcripts include failed/repetitive derivations. They are examples of model behaviour, not verified physics or translation guidance.

## Extraction and security review

All PDF text was treated as untrusted scientific data. Prompts, role-like text, JSON, Python listings, requested actions, annotation guidelines and model transcripts were not executed or obeyed. No path, command, URL or request in a PDF was used as authority to access local resources or contact a service. The corpus DOI in case 40 is inert test text. Local extraction commands and outputs were authored independently of PDF instructions. No credentials, secrets, unrelated user files or environment variables were accessed. No source PDF was written.

Sorted PyMuPDF text can interleave columns; block-order extraction improves paragraph continuity but still leaves line-break hyphenation, ligatures, superscripts, math glyph substitutions and flattened tables. Figure labels, all-caps names and code-like strings require care. Corpus presence checks normalize whitespace and line-break hyphens only for audit, never to alter protected article text. Blank text on P3 pp.15–22 means missing extraction, not blank content.

## Limited external terminology cross-check

Corpus inclusion is based only on supplied PDFs. External checks were limited to Russian term usage, not adding new subject terms or verifying article claims. Russian primary research uses [«символьная регрессия» (Нейчев, Шибаев, Стрижов)](https://www.mathnet.ru/ia827) and [«полуопределённое программирование» (Жадан, Орлов)](https://www.mathnet.ru/php/archive.phtml?jrnid=zvmmf&option_lang=rus&paperid=9584&wshow=paper). These support the selected conventional mathematical wording; they do not validate the whole pack. Secondary search results were not used as technical authorities.

## Validation

Structural and contract validation only; no provider run or expert semantic certification.

```text
领域包通过：llm-scientific-reasoning-en-ru 0.1.0，术语 118 条，案例 40 条
```

Executed with the existing .venv:

| unittest discovery pattern | Tests | Result |
|---|---:|---|
| test_domain_pack.py | 3 | PASS |
| test_languages.py | 11 | PASS |
| test_evaluation.py | 3 | PASS |
| test_contracts.py | 24 | PASS |
| test_quantities.py | 7 | PASS |

48 tests passed. Commands: `.venv/bin/python -m unittest discover -s tests -p <pattern>` for each pattern above. Additional local audit checks UTF-8, exact four-column TSV rows, unique casefolded sources, nonempty notes, corpus occurrence, unique eval sources, reference contracts, required-name deletion failures, and inflected Russian references. Russian spelling and scope were reviewed manually; no specialist or dedicated Russian spell-checker was used. No core code or tests were changed.

## Commands for review and use

From the repository root (the model name follows the checkout’s README examples; availability in your account is not tested):

```bash
.venv/bin/paperlocale domain-check ./local-packs/llm-scientific-reasoning-en-ru

.venv/bin/paperlocale provider-eval \
  --domain ./local-packs/llm-scientific-reasoning-en-ru \
  --provider codex-local --model gpt-5.6-sol \
  --output ./local-packs/llm-scientific-reasoning-en-ru-provider-eval.json

.venv/bin/paperlocale run \
  "./input_articles/Anchoring Depends on Confidence and Post-Training in Language Models.pdf" \
  --run-dir ./runs/anchoring-en-ru \
  --source-language en --target-language ru-RU \
  --domain ./local-packs/llm-scientific-reasoning-en-ru \
  --provider codex-local --model gpt-5.6-sol
```

The commands were parser-checked, not executed against codex-local. The run command retains normal workflow review gates; PDF rendering/layout still requires human inspection. Provider-eval reports contract results and requires manual semantic review; exact reference matching is not a translation-quality score. Its output is outside the four-file pack directory. The repository already ignores local-packs/ via .git/info/exclude; no ignore rules were changed.

## Corpus fingerprints

SHA-256 recorded after read-only extraction for reproducible corpus identification:

- P1: `4f18076072ae04748abff668bb607a662b3618cc85ed6b5cca1de4cb0066ae7b`
- P2: `4de08cbedc6c64dc168d02fde9b26dc1a013b60872cc9fedf6c3f34aac4d9d07`
- P3: `d059e8540d5d8191b7a46e1faa4209720c7ce07ca2e8ce2587a8b018c7abc3e0`
- P4: `08a978b3e24e8059e00c045d11d8417d2ed50a2077db81046cf849a83b0cf306`
- P5: `62ec8102817ce79ce0c2d41ba6d0b13ad89e6b560f9b74af2a8abd694b68ae61`
- P6: `c3fa7d1c37b6a168a6d0e4ffe9df103ed015ab2af77f1d69ba45b0287b7861d5`
- P7: `64aabaa8f1f6f28be48afeccc22069ada7b416d1b7fb65317d8965ce8e44ed5f`
- P8: `65465092a2a932978ecd357ebb2a311d77d9a7b682d3f166916e597484509bef`

## Glossary traceability

P1–P8 in each glossary note refer to the inventory above. The following locations are automatically located first occurrences after whitespace/hyphen normalization; these are provenance pointers, not independent semantic endorsements. Bibliography-only mentions were not used to expand the field.

| Source term | First matching physical page per PDF |
|---|---|
| large language model | P1 p.1, P2 p.1, P3 p.1, P4 p.1, P5 p.2, P6 p.1, P7 p.1, P8 p.1 |
| scientific reasoning | P6 p.2, P8 p.1 |
| scientific discovery | P2 p.12, P4 p.2, P5 p.1, P6 p.6, P8 p.1 |
| belief revision | P2 p.1, P4 p.4, P8 p.12 |
| belief set | P2 p.3 |
| prior belief | P2 p.1, P3 p.13 |
| degree of belief | P7 p.1 |
| premise | P2 p.1 |
| defeasible inference | P2 p.1 |
| modus ponens | P2 p.2 |
| modus tollens | P2 p.2 |
| delta reasoning | P2 p.1 |
| Bayesian epistemology | P7 p.1 |
| justification | P6 p.2, P7 p.1, P8 p.15 |
| evidence | P1 p.1, P2 p.1, P3 p.1, P4 p.4, P5 p.4, P6 p.1, P7 p.1, P8 p.1 |
| golden evidence | P7 p.1 |
| conflicting evidence | P7 p.2 |
| contradictory evidence | P3 p.6, P7 p.1 |
| coincidental evidence | P7 p.2 |
| incomplete evidence | P6 p.2, P7 p.2 |
| irrelevant evidence | P7 p.2 |
| strength of evidence | P7 p.3 |
| confirmation | P3 p.4, P7 p.1 |
| disconfirmation | P7 p.1 |
| confidence | P1 p.1, P3 p.1, P5 p.14, P7 p.1, P8 p.7 |
| certainty | P1 p.1, P3 p.4, P6 p.1, P7 p.2, P8 p.9 |
| verbalized confidence | P7 p.1 |
| confidence calibration | P1 p.1, P7 p.9 |
| overconfidence | P3 p.1, P7 p.7 |
| underconfidence | P3 p.1 |
| anchoring bias | P1 p.1 |
| anchoring susceptibility | P1 p.1 |
| anchor | P1 p.1, P3 p.9, P4 p.17, P6 p.5, P8 p.24 |
| choice-supportive bias | P3 p.1 |
| change of mind | P3 p.2 |
| opposing advice | P3 p.1 |
| supporting advice | P3 p.1 |
| post-training | P1 p.1 |
| instruction tuning | P1 p.1, P6 p.7 |
| distillation | P1 p.4 |
| chain-of-thought | P2 p.7, P7 p.2 |
| prior knowledge | P4 p.4, P5 p.3, P7 p.1, P8 p.1 |
| background theory | P5 p.1 |
| parametric knowledge | P6 p.2, P7 p.5 |
| likelihood | P1 p.2, P3 p.5, P7 p.1 |
| log odds | P3 p.3 |
| accuracy | P1 p.1, P2 p.3, P3 p.2, P4 p.1, P5 p.7, P6 p.1, P7 p.1, P8 p.1 |
| mean absolute error | P1 p.2 |
| mean squared error | P8 p.7 |
| expected calibration error | P3 p.11, P7 p.3 |
| Matthews correlation coefficient | P6 p.3 |
| total variation distance | P1 p.3 |
| ordinary least squares | P1 p.3 |
| random intercept | P1 p.3 |
| fixed effects | P1 p.3 |
| confidence interval | P1 p.4, P8 p.17 |
| standard error | P1 p.3, P3 p.3, P4 p.6, P8 p.18 |
| standard deviation | P1 p.3, P8 p.18 |
| scientific feasibility | P6 p.1 |
| outcome | P2 p.14, P3 p.13, P4 p.4, P6 p.1, P7 p.9, P8 p.2 |
| experimental design | P3 p.2, P4 p.5, P6 p.1, P7 p.3, P8 p.4 |
| hypothesis-only | P6 p.2 |
| held-out | P4 p.1 |
| parameter fitting | P4 p.2 |
| symbolic regression | P4 p.2, P5 p.4, P8 p.4 |
| symbolic equivalence | P8 p.3 |
| data fidelity | P8 p.3 |
| polynomial optimization | P5 p.1 |
| semidefinite optimization | P5 p.1 |
| sum-of-squares | P5 p.3 |
| semialgebraic set | P5 p.2 |
| Positivstellensatz | P5 p.1 |
| Gröbner bases | P5 p.4 |
| mixed-integer | P5 p.1 |
| certificate | P5 p.1 |
| polynomial time | P5 p.1 |
| N-body | P4 p.1 |
| particle species | P4 p.2 |
| charge | P4 p.4, P5 p.35, P6 p.9, P8 p.27 |
| coupling | P1 p.1, P4 p.1 |
| screened | P4 p.1, P5 p.21 |
| fractional Laplacian | P4 p.2 |
| phase space | P4 p.4 |
| initial conditions | P4 p.5 |
| force law | P4 p.2 |
| impulse | P8 p.2 |
| torque | P4 p.22, P8 p.29 |
| electric field strength | P8 p.27 |
| surface charge density | P8 p.27 |
| center of mass | P5 p.21, P8 p.2 |
| Kepler’s Third Law | P5 p.1 |
| Hagen-Poiseuille | P5 p.1 |
| Brier score | P3 p.12 |
| LLM | P1 p.1, P2 p.5, P3 p.1, P4 p.1, P6 p.1, P7 p.1, P8 p.1 |
| CoM | P1 p.1, P2 p.1, P3 p.1, P4 p.1, P5 p.1, P6 p.1, P7 p.1, P8 p.1 |
| ECE | P2 p.1, P3 p.1, P4 p.2, P5 p.1, P6 p.2, P7 p.3, P8 p.1 |
| MSE | P3 p.4, P4 p.1, P8 p.4 |
| MAE | P1 p.2, P5 p.28, P7 p.16 |
| TVD | P1 p.3 |
| MCC | P2 p.11, P6 p.3, P7 p.10 |
| OUCS | P3 p.3 |
| BREU | P2 p.7 |
| FEASIBLE | P2 p.1, P5 p.11, P6 p.1 |
| INFEASIBLE | P6 p.1 |
| SciQ | P7 p.3 |
| TriviaQA | P7 p.3 |
| GSM8K | P3 p.6, P7 p.3 |
| MATTER-OF-FACT | P6 p.3 |
| REASONS | P2 p.2, P4 p.32, P5 p.11, P6 p.3, P8 p.25 |
| Llama | P1 p.1, P2 p.6, P3 p.2, P4 p.7, P7 p.10 |
| Qwen | P1 p.1, P4 p.7, P8 p.8 |
| Gemma | P3 p.2 |
| PyMC | P3 p.13 |
| SymPy | P8 p.6 |
| Belief-R | P2 p.1, P4 p.4, P8 p.12 |
| DiscoverPhysics | P4 p.1 |
| PHYSGYM | P4 p.4, P8 p.1 |
| AI-Hilbert | P5 p.1 |
