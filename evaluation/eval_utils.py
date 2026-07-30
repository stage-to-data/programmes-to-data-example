"""Utilities for evaluating VLM transcriptions against a ground truth corpus.

Metrics are computed at two granularities:

- **file level**: Levenshtein distance/ratio over the whole page.
- **unit level**: units (lines, sentences, named entities) are first *matched*
  between prediction and reference, then WER/CER/Levenshtein are computed on the
  matched pairs.

The unit-level matching is deliberately order-insensitive: a VLM may return the
blocks of a programme page in a different order than the reference without that
being a transcription error. Precision and recall therefore measure *coverage*,
while WER/CER/Levenshtein on matches measure *fidelity* of the matched text.
"""

import os
import re
from difflib import SequenceMatcher

import Levenshtein
import matplotlib.pyplot as plt
from jiwer import cer, wer


# ---------------------------------------------------------------------------
# Text normalisation
# ---------------------------------------------------------------------------

def clean_text(text_in):
    """Drop markdown title markers and collapse all whitespace."""
    text_in = text_in.replace("#", "")
    text_in = re.sub(r"\s+", " ", text_in)
    return text_in.strip()


def split_text(text_in):
    """Split into comparison units on line breaks and full stops."""
    parts = re.split(r"\n|\.", text_in)
    return [part.strip() for part in parts if part.strip()]


# ---------------------------------------------------------------------------
# Unit matching
# ---------------------------------------------------------------------------

def match_units(predicted, reference, threshold=0.8, metric="l", skip_matched=True):
    """Greedily match predicted units to reference units.

    Each predicted unit is paired with the most similar *still unmatched*
    reference unit, and the pair is kept only if similarity >= ``threshold``.

    Args:
        predicted: list of predicted strings.
        reference: list of reference strings.
        threshold: minimum similarity for a pair to count as a match.
        metric: ``"l"`` for Levenshtein ratio, ``"d"`` for SequenceMatcher.
        skip_matched: if True a reference unit can only be matched once.

    Returns:
        ``(precision, recall, pairs)`` where ``pairs`` is a list of
        ``(predicted_index, reference_index)`` tuples.

    Note:
        ``pairs`` is returned as an explicit ordered list rather than as two
        separate sets. Returning sets loses the correspondence between the two
        sides: zipping them back together pairs units by set iteration order,
        which is arbitrary, and WER/CER/Levenshtein are then computed on
        unrelated pairs. Always pass ``pairs`` straight to
        :func:`compute_wer_cer`.

        Matching is greedy in the order of ``predicted`` and therefore neither
        optimal nor symmetric: swapping the arguments can change precision and
        recall. For an optimal assignment, see
        ``scipy.optimize.linear_sum_assignment``.
    """
    pairs = []
    matched_ref = set()

    for i, p in enumerate(predicted):
        best_match = -1
        best_score = 0

        for j, r in enumerate(reference):
            if j in matched_ref and skip_matched:
                continue

            if metric == "l":
                score = Levenshtein.ratio(p, r)
            elif metric == "d":
                score = SequenceMatcher(None, p, r).ratio()
            else:
                raise ValueError(f"Unknown metric {metric!r}, expected 'l' or 'd'.")

            if score > best_score:
                best_match = j
                best_score = score

        if best_score >= threshold and best_match >= 0:
            if skip_matched:
                matched_ref.add(best_match)
            pairs.append((i, best_match))

    matched_pred_count = len({i for i, _ in pairs})
    matched_ref_count = len({j for _, j in pairs})

    precision = matched_pred_count / len(predicted) if predicted else 0
    recall = matched_ref_count / len(reference) if reference else 0
    return precision, recall, pairs


def compute_wer_cer(predicted, reference, pairs, error_base=1, lev_base=0):
    """Mean WER, CER and Levenshtein ratio over matched pairs.

    Args:
        predicted: list of predicted strings.
        reference: list of reference strings.
        pairs: list of ``(predicted_index, reference_index)`` tuples, as
            returned by :func:`match_units`.
        error_base: value used for WER/CER when there is no match at all.
        lev_base: value used for the Levenshtein ratio when there is no match.

    Returns:
        ``(avg_wer, avg_cer, avg_lev)``.
    """
    wer_scores = []
    cer_scores = []
    leven_scores = []

    for i, j in pairs:
        p = predicted[i]
        r = reference[j]
        wer_scores.append(wer(r, p))
        cer_scores.append(cer(r, p))
        leven_scores.append(Levenshtein.ratio(r, p))

    avg_wer = sum(wer_scores) / len(wer_scores) if wer_scores else error_base
    avg_cer = sum(cer_scores) / len(cer_scores) if cer_scores else error_base
    avg_lev = sum(leven_scores) / len(leven_scores) if leven_scores else lev_base
    return avg_wer, avg_cer, avg_lev


def matched_strings(predicted, reference, pairs):
    """Return the matched pairs as aligned lists of strings, for reporting."""
    return {
        "matched_pred": [predicted[i] for i, _ in pairs],
        "matched_ref": [reference[j] for _, j in pairs],
    }


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------

def get_mean(data, key):
    """Unweighted mean of ``key`` over ``data["files"]``."""
    total = sum(item[key] for item in data["files"])
    return total / len(data["files"])


def get_weighted_mean(data, key, weight_key):
    """Mean of ``key`` weighted by ``weight_key`` over ``data["files"]``."""
    weight_total = sum(item[weight_key] for item in data["files"])
    item_val = sum(item[key] * item[weight_key] for item in data["files"])
    return item_val / weight_total


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def draw_scatter(data, x_key, y_key, title, outpath, col="blue", size=(20, 20)):
    """Scatter plot of ``y_key`` against ``x_key``.

    Pass ``x_key="&&FILE"`` to plot against file names instead of a metric.
    """
    per_file = x_key == "&&FILE"

    x = []
    y = []
    for item in data["files"]:
        x.append(os.path.basename(item["to_test_file"]) if per_file else item[x_key])
        y.append(item[y_key])

    plt.figure(figsize=size)
    plt.scatter(x, y, color=col, marker="o")
    plt.title(title)
    plt.xlabel("file" if per_file else x_key)
    plt.ylabel(y_key)

    if per_file:
        plt.xticks(rotation=90)
        plt.tight_layout()

    os.makedirs(os.path.dirname(os.path.abspath(outpath)), exist_ok=True)
    plt.savefig(outpath)
    plt.close()
