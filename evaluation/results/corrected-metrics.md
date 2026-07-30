# Corrected evaluation metrics

**This file is the authoritative source for the figures of this evaluation.** All are weighted by page
word count.

The `scores.md` report in each run folder was produced before a pairing bug in `eval_utils.py` was
fixed. `match_units` returned two sets, which `compute_wer_cer` recombined with `zip`; since the
iteration order of a set of integers is arbitrary in CPython, each prediction was compared against an
unrelated reference. Precision and recall depend only on set cardinality and were unaffected. The
WER/CER/Levenshtein-on-matches columns were understated, sometimes heavily. Those reports are kept as
they were produced; read their matched-unit figures here instead.

## Unit level (lines/sentences)

Recomputed from the transcriptions against the ground truth, so available for every run whose
`transcriptions/` folder is kept here.

| Run | GT commit | Lev. full doc. | P/R | Lev. matches published | Lev. matches corrected | WER corrected | CER corrected |
|---|---|---|---|---|---|---|---|
| final-tests / prompt-1 | `c7fc5733` | 0.9817 | 0.79/0.84 | 0.9080 | **0.9856** | 0.0612 | 0.0239 |
| final-tests / prompt-2 | `c7fc5733` | 0.9774 | 0.79/0.85 | 0.9157 | **0.9860** | 0.0584 | 0.0231 |
| final-tests / prompt-3 | `c7fc5733` | 0.9845 | 0.80/0.85 | 0.9014 | **0.9864** | 0.0581 | 0.0225 |
| final-tests / prompt-4 | `c7fc5733` | 0.9818 | 0.82/0.86 | 0.9295 | **0.9868** | 0.0576 | 0.0219 |
| third-pass / prompt-1 | `0d40e2fc` | 0.9833 | 0.78/0.85 | 0.8996 | — | — | — |
| third-pass / prompt-1-gpt | `0d40e2fc` | 0.9699 | 0.79/0.82 | 0.9104 | — | — | — |

The `third-pass` transcriptions were not kept, so those runs cannot be recomputed. Their published
Levenshtein-on-matches values carry the bug and should not be quoted.

## Named entity level

| Run | GT commit | P/R NER | Lev. matches published | Lev. matches corrected |
|---|---|---|---|---|
| final-tests / prompt-1 | `c7fc5733` | 0.94/0.91 | 0.9428 | **0.9954** |
| final-tests / prompt-2 | `c7fc5733` | 0.93/0.91 | 0.9356 | **0.9958** |
| final-tests / prompt-3 | `c7fc5733` | 0.94/0.91 | 0.9439 | **0.9956** |
| final-tests / prompt-4 | `c7fc5733` | 0.94/0.91 | 0.9442 | **0.9958** |
| third-pass / prompt-1 | `0d40e2fc` | 0.94/0.91 | 0.9424 | **0.9954** |
| third-pass / prompt-1-gpt | `0d40e2fc` | 0.85/0.87 | 0.9118 | **0.9934** |

The corrected NER figures were obtained by re-pairing the matched entity lists recorded in each run's
`scores.json`. Those files were pruned from the repository for every run except `final-tests/prompt-4`
and the two `third-pass` runs, so **for prompts 1–3 this table is the only remaining record** of the
corrected values; re-running the notebook regenerates them.

## Reading these numbers

Once the pairing is corrected, the Levenshtein-on-matches columns saturate between 0.985 and 0.996 and
no longer separate the configurations — including Claude from GPT-4o (0.9934 against 0.9954 on the same
ground truth). What discriminates is precision and recall: prompt 4 gains over three points of
unit-level precision on prompt 1, and Claude leads GPT-4o by nine points of NER precision. Coverage,
not fidelity, is where the configurations differ; what these models transcribe, they transcribe almost
exactly.

## Ground truth states

| Commit | Date | Corpus |
|---|---|---|
| `0d40e2fc` | 2 May 2025 | 151 pages, 36,417 words, 249,500 characters |
| `c7fc5733` | 5 May 2025 | 151 pages, 37,466 words, 256,585 characters — the copy in `../ground-truth/md` |

Runs scored against different states are not comparable. See `../ground-truth/README.md`.
