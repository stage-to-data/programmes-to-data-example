# Ground truth

Manually annotated transcriptions of theatre programmes from the Festival d'Avignon, used as the
reference against which VLM transcriptions are scored.

30 programmes, **151 pages** in `md/`: 37,466 words, 256,585 characters
(15 to 5,438 characters per page).

The corpus deliberately spans the history of the festival and mixes digitised with born-digital
documents, including awkward cases: upside-down text, poor-quality scans, multi-column layouts,
pages in several languages and in older French.

## Annotation conventions

Each page is one markdown file, named `<programme>_page_<n>.md`. Annotation was produced manually with
initial VLM assistance, and distinguishes only two things:

- **titles**, marked with a single `#` regardless of hierarchical level;
- **non-title text**, unmarked.

No other structure is encoded. The evaluation strips `#` before comparing, so the marker affects the
title/non-title distinction only, not the character-level metrics.

## Provenance and versioning

Mirrored from [stage-to-data/corpus-show-prog-avignon](https://github.com/stage-to-data/corpus-show-prog-avignon)
(`transcriptions/ground-truth/md`), at commit **`c7fc5733`** (5 May 2025).
That repository remains the upstream source; this copy exists so that `evaluation.ipynb` runs without a
second clone.

The ground truth is revised over time, and **runs scored against different states of it are not
comparable**. Two states matter for the published results:

| Commit | Date | Corpus | Scored runs |
|---|---|---|---|
| `0d40e2fc` | 2 May 2025 | 151 pages, 36,417 words, 249,500 characters | `../results/third-pass/` |
| `c7fc5733` | 5 May 2025 | 151 pages, 37,466 words, 256,585 characters | `../results/final-tests/` — **this copy** |

The difference is commit `c7fc5733`, which transcribed four pages of *Le Cercle de craie caucasien*
(dir. Benno Besson, 1978) that had been left empty; the per-page minimum rises from 0 to 15 characters.
To reproduce the `third-pass` figures, check out `0d40e2fc` of the upstream repository.

## Source documents

The programme scans and PDFs behind these transcriptions are **not** redistributed here or upstream:
the transcriptions are, the source documents are not. Requests for access to the originals should go
through the [STAGE project](https://stage-to-data.huma-num.fr/).

## A note on file names

Accented file names exist on disk in both composed (NFC) and decomposed (NFD) Unicode form, depending
on the operating system and sync client that last wrote them — `...MiseEnScèneDePatriceChéreau...` may
be either. The two forms are different byte strings and will not compare equal.

`evaluation.ipynb` therefore pairs transcriptions with their reference by NFC-normalised file name. Any
tooling added here should do the same, or roughly half the corpus will be silently dropped as
"missing".
