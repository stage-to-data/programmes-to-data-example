import os

import llmwrap

from .prompts import data_extraction_prompt, data_extraction_system_prompt
from .utils import collect_files, read_txt, write_json

DEFAULT_MODEL = "claude-opus-4-8"
DEFAULT_MAX_TOKENS = 16000


def extract_data_claude(pdf_file, output_folder, **kwargs):
    """Extract LA-PA data from a programme's transcription with a Claude model.

    The whole programme is sent in one request: the pages of a programme are not
    independent (a cast list on page 3 belongs to the production named on page 1),
    so extracting page by page would fragment the entities.

    kwargs:
    - api_key: required.
    - model: model identifier, defaults to DEFAULT_MODEL.
    - max_tokens: defaults to DEFAULT_MAX_TOKENS. A full programme extraction runs
      to several thousand tokens — a large cast and crew list will silently
      truncate under a low ceiling.
    """
    basename = os.path.splitext(os.path.basename(pdf_file))[0]
    source_folder = os.path.join(output_folder, "text", basename, "transcription")
    source_files = collect_files(source_folder, ["md"])

    if not source_files:
        print(f"No transcription found in {source_folder}")
        return None

    output_dest = os.path.join(output_folder, "text", basename, "linked-art")
    os.makedirs(output_dest, exist_ok = True)

    api_key = kwargs.get("api_key")
    if not api_key:
        raise ValueError("An api_key is required for extract_data_claude.")

    # One request for the whole programme, not one per page.
    print(f"Treating {basename} ({len(source_files)} pages)")
    full_text = ""
    for source_file in source_files:
        full_text = full_text + read_txt(source_file) + "\n\n"

    prompt = llmwrap.Prompt(
        data_extraction_prompt,
        options = {"MARKDOWN_CONTENT": full_text}
    )

    model = llmwrap.ClaudeWrapper(
        model = kwargs.get("model", DEFAULT_MODEL),
        api_key = api_key,
        system_prompt = data_extraction_system_prompt,
        max_tokens = kwargs.get("max_tokens", DEFAULT_MAX_TOKENS)
    )

    response = model.process(prompt)

    if isinstance(response, dict):
        print(f"Extraction failed: {response.get('content')}")
        return None

    txt_path = os.path.join(output_dest, "data.json")
    write_json(txt_path, response.content)
    return txt_path
