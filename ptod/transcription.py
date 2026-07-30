import os
from .utils import collect_files, write_json, write_txt
from .prompts import transcription_prompt
import llmwrap
import time

SYSTEM_PROMPT = "You are a tool for the transcription of textual data from scanned images."

DEFAULT_MODEL_IDS = {
    "ollama": "llama3.2-vision:11b",
    "claude": "claude-3-7-sonnet-20250219",
    "openai": "gpt-4o",
}


def _build_model(**kwargs):
    """Instantiate the requested VLM wrapper.

    kwargs:
    - model: "ollama" (default), "claude" or "openai".
    - model_id: overrides the default model identifier for that provider.
    - api_key: required for "claude" and "openai".
    - max_tokens: defaults to 3000.
    """
    provider = kwargs.get("model", "ollama")
    if provider not in DEFAULT_MODEL_IDS:
        raise ValueError(
            f"Unknown model provider {provider!r}. "
            f"Expected one of {sorted(DEFAULT_MODEL_IDS)}."
        )

    model_id = kwargs.get("model_id", DEFAULT_MODEL_IDS[provider])
    common = {
        "system_prompt": kwargs.get("system_prompt", SYSTEM_PROMPT),
        "max_tokens": kwargs.get("max_tokens", 3000),
    }

    if provider == "ollama":
        return llmwrap.OllamaWrapper(model_id, **common)

    api_key = kwargs.get("api_key")
    if api_key is None:
        raise ValueError(f"An api_key is required for the {provider!r} provider.")

    wrapper = llmwrap.ClaudeWrapper if provider == "claude" else llmwrap.OpenAIWrapper
    return wrapper(model_id, api_key = api_key, **common)


def transcribe(pdf_file, output_folder, **kwargs):
    failed_files = []
    source_folder = os.path.join(output_folder, "images", os.path.splitext(os.path.basename(pdf_file))[0], "preprocessed-small")
    
    source_files = collect_files(source_folder, ["jpeg", "jpg"])
    
    output_dest = os.path.join(output_folder, "text", os.path.splitext(os.path.basename(pdf_file))[0], "transcription")
    os.makedirs(output_dest, exist_ok = True)

    # The raw API responses are archived alongside, but in their own folder: the
    # transcription folder must hold nothing but the .md pages, since the next
    # stage of the pipeline collects it wholesale.
    raw_dest = os.path.join(output_dest, "_raw-responses")

    # One wrapper for the whole document rather than one per page.
    model = _build_model(**kwargs)

    for source_file in source_files:
        print(f"treating {source_file}")

        txt_path = os.path.join(output_dest, f"{os.path.splitext(os.path.basename(source_file))[0]}.md")

        prompt = llmwrap.Prompt(transcription_prompt, images = [source_file])
        response = model.process(prompt)

        if isinstance(response, dict):
            failed_files.append({"file" : txt_path, "error" : response["content"]})
            write_json(os.path.join(output_dest, "_failed_files.json"), {"fails" : failed_files})
        else:
            response.write(raw_dest)
            write_txt(txt_path, response.content)

        time.sleep(kwargs.get("cooldown_time", 1))

    return failed_files