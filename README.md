# programmes-to-data

Turning printed theatre programmes into structured [Linked Art](https://linked.art/) data, by reading
them with a vision-language model rather than an OCR engine. Part of the ERC-funded
[STAGE](https://stage-to-data.huma-num.fr/) project on the history of the Festival d'Avignon.

[**Open the demo in Google Colab**](https://colab.research.google.com/github/stage-to-data/programmes-to-data-example/blob/main/Hamlet_example/full-pipeline.ipynb)
— a full run on *Hamlet*, directed by Patrice Chéreau, Festival d'Avignon 1988.

## Pipeline

| Stage | Input → output | Entry point |
|---|---|---|
| 1. Preprocessing | PDF → page images, greyscaled and compressed to fit VLM input limits | `ptod.pdf_to_img`, `ptod.preprocess_images` |
| 2. Transcription | page images → markdown, titles distinguished from body text | `ptod.transcribe` |
| 3. Extraction | markdown → Linked Art JSON-LD, via the [LA-PA extension](https://github.com/stage-to-data/linked-art-pa) | `ptod.PleiasModel`, `ptod.extract_data` |

## Installation

```bash
# Stage 1 only — light, installs anywhere
pip install git+https://github.com/stage-to-data/programmes-to-data-example.git

# + stage 2 (adds the llmwrap VLM wrapper)
pip install "ptod[transcription] @ git+https://github.com/stage-to-data/programmes-to-data-example.git"

# + stage 3 (adds vllm; requires a CUDA GPU)
pip install "ptod[extraction] @ git+https://github.com/stage-to-data/programmes-to-data-example.git"
```

Stages 2 and 3 are imported lazily, so `import ptod` succeeds without the optional dependencies.
Stage 2 defaults to [Ollama](https://ollama.com/) running locally (`ollama pull llama3.2-vision:11b`);
pass `model="claude"` or `model="openai"` with an `api_key` for a hosted model.

## Layout

```
ptod/                    the pipeline package
  preprocessing.py         stage 1
  transcription.py         stage 2
  prompts.py               the transcription prompt (= prompt 4); the extraction
                             prompts are built from the specification below
  pleias.py                stage 3, POntAvignon models (needs a GPU)
  data_extraction.py       stage 3, hosted Claude model
  lapa_extraction_prompt.md   the extraction specification: nine LA-PA models,
                             58 output columns, serialisation rules
  utils.py                 file helpers

Hamlet_example/          end-to-end demo on one programme
  full-pipeline.ipynb      the notebook opened by the Colab link
  sources/                 the source PDF
  outputs/images/          page images, raw and preprocessed
  outputs/text/…/transcription/   stage 2 output, one .md per page
  outputs/text/…/data/     stage 3 output — see its README for the three approaches

evaluation/              prompt and model evaluation for stage 2
  ground-truth/            the reference corpus, 151 annotated pages
  prompts/                 every prompt tried, by round of testing
  results/                 one folder per run, grouped by campaign
  evaluation.ipynb         score a run against the ground truth
  transcribe_batch.py      produce a run via Claude's batch API
  eval_utils.py            metrics
```

See [`evaluation/README.md`](evaluation/README.md) for the method and the full results, and
[`evaluation/ground-truth/README.md`](evaluation/ground-truth/README.md) for the corpus.

## Ground truth

30 programmes / 151 pages (37,466 words, 256,585 characters) spanning the history of the festival,
including awkward cases: upside-down text, poor scans, born-digital as well as digitised documents.
Each page is annotated in markdown, distinguishing only titles from non-title text.

The programme scans and PDFs behind the transcriptions are not redistributed —
the transcriptions are, the source documents are not.

The ground truth is revised over time and **runs scored against different states of it are not
comparable**, so every result records the commit it was scored against:

| Campaign | Ground truth | Corpus |
|---|---|---|
| `evaluation/results/final-tests/` | `c7fc5733` (5 May 2025) — the mirrored copy | 151 pages, 37,466 words, 256,585 characters |
| `evaluation/results/third-pass/` | `0d40e2fc` (2 May 2025) | 151 pages, 36,417 words, 249,500 characters |

## Results

Claude 3.7 Sonnet with prompt 4, word-count-weighted against ground truth `c7fc5733`: full-page
Levenshtein ratio 0.9818, unit-level precision/recall 0.82/0.86, named-entity precision/recall
0.94/0.91. Prompt 4 was chosen on coverage rather than on the Levenshtein measures, which saturate
above 0.98 and separate the prompts poorly. Per-prompt figures, method and caveats are in
[`evaluation/README.md`](evaluation/README.md); `evaluation/results/corrected-metrics.md` is the
authoritative metrics table.

## Known limitations

- **Hallucination.** A VLM occasionally invents plausible text, most often on faint or ornamented
  pages. The prompt instructs it to emit `[UNABLE TO TRANSCRIBE]` rather than guess; the worst-scoring
  pages in each report are where to look for failures.
- **Preprocessing quirks, left in place on purpose.** `max_dims` acts as a target rather than a
  ceiling, so pages rendering below it are enlarged and the model receives interpolated pixels (three
  of six pages in the *Hamlet* example); the greyscale conversion is then undone by the final JPEG
  re-encode. Both are documented in `ptod/preprocessing.py` — fixing either changes the bytes sent to
  the model and would invalidate the published results.
- **Unicode normalisation.** Accented file names exist on disk in both composed (NFC) and decomposed
  (NFD) form depending on the OS and sync client that wrote them. The evaluation pairs files by
  NFC-normalised name; tooling that pairs by raw name will drop pages silently.
- **Demo ≠ evaluated configuration.** The Colab demo uses `llama3.2-vision:11b` via Ollama so it runs
  without an API key. The evaluated configuration is Claude 3.7 Sonnet with prompt 4.
- **Stage 3 is exploratory, and the demo programme is a few-shot example.** Three extraction
  approaches were tried and all three outputs are kept in `Hamlet_example/…/data/`. The Chéreau 1988
  Hamlet is one of the ten few-shot examples embedded in the extraction prompt, so its output
  illustrates the target format rather than measuring performance; any accuracy figure computed on it
  is inflated by construction. The held-out evaluation of stage 3 is not reproduced here.

## Related

- [llm-wrap](https://github.com/stage-to-data/llm-wrap) — the LLM/VLM wrapper used here
- [linked-art-pa](https://github.com/stage-to-data/linked-art-pa) — the Linked Art extension for the performing arts

## Citation

If you use this pipeline or the ground truth corpus, please cite the STAGE project —
[stage-to-data.huma-num.fr](https://stage-to-data.huma-num.fr/).
