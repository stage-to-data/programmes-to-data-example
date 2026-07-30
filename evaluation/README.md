# Evaluation

Prompt and model evaluation for stage 2 of the pipeline (image → markdown transcription).

```
eval_utils.py           metrics
evaluation.ipynb        score a run against the ground truth
transcribe_batch.py     produce a run: batch-transcribe images via Claude's batch API
requirements.txt

ground-truth/           the reference corpus — see ground-truth/README.md
  md/                     151 pages, 30 programmes, 256,585 characters

prompts/                every prompt tried, by round of testing
  round-1/                3 early prompts
  round-2/                3 prompts
  round-3/                the 6 prompts of the final round, incl. prompt-4 (shipped)

results/                one folder per run, grouped by campaign
  corrected-metrics.md    ← authoritative metrics table, all runs
  final-tests/            scored against ground truth c7fc5733
    prompt-1/ prompt-2/ prompt-3/ prompt-4/
      scores.md             human-readable report
      scores.json           per-page detail (prompt-4 only)
      transcriptions/       the VLM output that was scored
      requests/             batch submission records
  third-pass/             scored against ground truth 0d40e2fc — earlier state
    prompt-1/ prompt-1-gpt/
      scores.md, scores.json    transcriptions not kept
```

A campaign groups runs scored against one state of the ground truth. **Runs from different campaigns
are not comparable** — see `ground-truth/README.md`.

## Method

Document-wide WER/CER is a poor fit here: a VLM may return the blocks of a page in a different order
than the reference without that being an error, and reading a performer's name correctly matters more
than preserving section order. Units are therefore **matched** first, then scored — precision and
recall measure coverage, WER/CER/Levenshtein on the matched pairs measure fidelity. The same procedure
is applied to lines/sentences and to named entities. Corpus-wide figures are weighted by page word
count.

Matching is greedy in the order of the prediction, so neither optimal nor symmetric: swapping
prediction and reference shifts precision and recall slightly. See `match_units` in `eval_utils.py`.

## Running it

```bash
pip install -r requirements.txt
pip install -e ..                       # for ptod.utils
python -m spacy download xx_ent_wiki_sm
jupyter notebook evaluation.ipynb       # set CAMPAIGN and TEST_PASS in cell 3
```

To produce a new run first:

```bash
export ANTHROPIC_API_KEY=...
python transcribe_batch.py \
    --images ../Hamlet_example/outputs/images/*/preprocessed-small \
    --pass-name prompt-5 --campaign new-tests
```

## Results

Claude 3.7 Sonnet, word-count-weighted, ground truth `c7fc5733`. P/R is precision/recall.

| Prompt | Lev. full page | P/R units | Lev. matched units | P/R entities | Lev. matched entities |
|---|---|---|---|---|---|
| 1 | 0.9817 | 0.79 / 0.84 | 0.9856 | 0.94 / 0.91 | 0.9954 |
| 2 | 0.9774 | 0.79 / 0.85 | 0.9860 | 0.93 / 0.91 | 0.9958 |
| 3 | 0.9845 | 0.80 / 0.85 | 0.9864 | 0.94 / 0.91 | 0.9956 |
| **4** | **0.9818** | **0.82 / 0.86** | **0.9868** | **0.94 / 0.91** | **0.9958** |

Prompt 4 ships in `../ptod/prompts.py`. It was chosen on coverage — it leads on unit-level precision
and recall — not on the Levenshtein columns, which saturate above 0.98 and separate the prompts poorly
(prompt 3 is marginally ahead on full-page Levenshtein).

The `third-pass` campaign compared models on prompt 1: Claude 3.7 Sonnet scored 0.9833 full-page
Levenshtein and 0.94/0.91 entity P/R, against 0.9699 and 0.85/0.87 for GPT-4o. Those GPT-4o
transcriptions were not kept, so the run cannot be re-scored against the current ground truth.

> **The `scores.md` reports predate a pairing-bug fix in `eval_utils.py`**, so their
> Levenshtein/WER/CER-on-matches figures are understated. `results/corrected-metrics.md` is the
> authoritative source and gives both published and corrected values. Precision and recall were
> unaffected.

Scatter plots are not versioned; regenerate them from `scores.json` with the plotting cell of the
notebook.
