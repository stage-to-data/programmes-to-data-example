"""Programmes to data: theatre programme PDFs to structured Linked Art data.

Part of the ERC-funded STAGE project (https://stage-to-data.huma-num.fr/).

The pipeline has three stages, with increasingly heavy dependencies:

1. ``pdf_to_img`` / ``preprocess_images`` — PDF to preprocessed images (pymupdf, pillow, opencv).
2. ``transcribe`` — images to markdown with a VLM (adds llmwrap).
3. ``PleiasModel`` / ``extract_data`` — markdown to Linked Art JSON-LD (adds vllm, needs a GPU).

Stages 2 and 3 are imported lazily so that stage 1, and the file helpers in
``ptod.utils``, remain usable without installing the heavy optional
dependencies. ``import ptod`` therefore always succeeds; the import error, if
any, surfaces only when the corresponding name is first used.
"""

from .preprocessing import pdf_to_img, preprocess_images
from .utils import collect_files, read_txt, write_json, write_txt

__all__ = [
    "collect_files",
    "read_txt",
    "write_json",
    "write_txt",
    "pdf_to_img",
    "preprocess_images",
    "transcribe",
    "PleiasModel",
    "extract_data",
]

_LAZY = {
    "transcribe": (".transcription", "llmwrap", "pip install ptod[transcription]"),
    "PleiasModel": (".pleias", "vllm", "pip install ptod[extraction]"),
    "extract_data": (".pleias", "vllm", "pip install ptod[extraction]"),
}


def __getattr__(name):
    """Import the heavy submodules only when their names are actually used."""
    if name not in _LAZY:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, dependency, install_hint = _LAZY[name]

    from importlib import import_module

    try:
        module = import_module(module_name, __name__)
    except ImportError as exc:
        raise ImportError(
            f"ptod.{name} requires the optional dependency '{dependency}', "
            f"which is not installed ({exc}). Install it with: {install_hint}"
        ) from exc

    return getattr(module, name)


def __dir__():
    return sorted(__all__)
