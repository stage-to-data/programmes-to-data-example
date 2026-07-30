# Extracted data — Hamlet, dir. Patrice Chéreau, Festival d'Avignon 1988

Stage 3 of the pipeline turns the markdown transcription (`../transcription/`) into structured
Linked Art / LA-PA data. Three approaches were tried; the output of each is kept here.

| File | Approach | Model | Output shape |
|---|---|---|---|
| `*-POntAvignon-annotations.json` | Reinforcement learning on Pleias-350m | [LLMDH/POntAvignon](https://huggingface.co/LLMDH/POntAvignon) (0.4B) | per-entity JSON-LD fragments |
| `*-POntAvignon-4b-annotations.json` | Supervised fine-tuning on Qwen3-4B | [Pclanglais/POntAvignon-4b](https://huggingface.co/Pclanglais/POntAvignon-4b) | seven sequential entity queries |
| `hamlet_fda1988_lapa-tabular.json` | Prompt-encoded ontology — **current pipeline** | `claude-opus-4-8` | flat 58-column record, one row per production |

`extraction-input.md` is the markdown actually submitted for the third: the six transcription pages
concatenated into one document.

## The current output

The extraction prompt (`../../../../../ptod/lapa_extraction_prompt.md`, 447 lines) defines the nine
LA-PA models, but only as the **semantics** of each field. What the model returns is a single
consolidated, denormalised table — one row per Production — whose 58 columns flatten those models
behind the prefixes `prod__`, `work__`, `event__`, `programme__`, `performance__`, `play__` and
`tour__`. Multivalued cells serialise their objects with ` | ` and their sub-fields with `\`.

For this programme the row records 33 performers, 67 team members, 10 performances (9–19 July 1988,
21:30, Cour d'honneur du Palais des Papes) and 1 play.

An earlier state of the prompt delivered the per-model JSON instead — one object keyed by model, one
array of instances per model — together with an HTML rendering and a page-by-page traceability
document. Those three files have been removed: the repository now documents one state, the current one.
They remain in the git history.

## Provenance

Run `output-opus-17ex` of the `claude-md-to-la` pipeline, submitted 28 June 2026 via the Anthropic
batch API, model `claude-opus-4-8`, with 10 few-shot examples. It is the retained run of that work
(held-out combined score 0.987).

**`extraction-input.md` differs from `../transcription/` by one line.** The BnF shelfmark at the head
of page 1 was read as `AFA. 1997(2,65)` in the extraction input and as `PFA. 1987(2,65)` in the
versioned transcription — two VLM readings of the same faint stamp. The file is kept as it was
actually submitted rather than silently aligned, since it is what produced the output next to it.

## An important caveat on this particular programme

**The Chéreau 1988 Hamlet is one of the ten few-shot examples embedded in the extraction prompt.**
The model was shown the expected answer for this exact source before being asked to extract it.

Its output is therefore an illustration of the target format, not a measurement of performance. Any
accuracy figure computed on this programme is inflated by construction. The honest measure is the
held-out evaluation, which excludes the ten example sources; it lives in the `claude-md-to-la`
repository and is not reproduced here.

## Reproducing

The extraction pipeline is not part of this repository. `ptod.extract_data` implements the earlier
POntAvignon approach and writes `linked-art/data.json`; the Claude-based extraction that produced
`hamlet_fda1988_lapa-tabular.json` is run from `claude-md-to-la`. The prompt is versioned here so that
the output can be read against the specification that produced it.
