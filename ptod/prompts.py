import os
import re

transcription_prompt = """
This image corresponds to a page in a theater program.
You will perform a complete and detailed OCR analysis of this image. 
DO NOT generate or use any code, do not use Tesseract or pytesseract — only use your internal vision to read the image.
Extract all visible text WITHOUT changing it.
DO NOT summarize, paraphrase, or infer missing text. DO NOT invent people's names.
Retain all spacing, punctuation, and formatting exactly as in the image.

You MUST follow the following rules when dealing with these specific cases:
- All titles are indicated with a preceding # with no hierarchy (example: # Title content). If the title contains line breaks, recompose the title into one single line.
- Exponents are given as lower case roman characters (example: XVe)
- Footnotes are given as special characters (example: word¹)
- When you detect the number of a page, return it at the start of the text using the word "PAGE"' followed by the number (example: PAGE 13)
- Do not describe images or logos, simply extract any text within them.
- Do not insert special characters for things like columns and page separation
- For distribution: if you detect a table-like stucture, typography variation that could be interpreted as a function/name or name/function pairing, or a string of points linking a function and name, apply the following structure:
Element 1 : Associated element 1, Associated element 2
Element 2 and Element 3, description : Associated element 3 and Associated element 4
(Note that in the case of enumeration, there are NO line breaks, there are commas)
- If you detect any other function/name or name/function pairs that are separated by a character like | or /, chnage the character to a : (example: element 1 : associated element 1)
- If you detect a completely empty page, or if the page is much too faint or blurry to confidently transcribe, simply return: [UNABLE TO TRANSCRIBE]
- Some pages may include texts of different languages, or old languages (for example old French). It is very important to NOT CHANGE the content, simply trnscribe the letters you see.

Check the overall readability of your transcription and make sure it reflects the structure of the original document.
The output should be ONLY the trancribed content (DO NOT add comments like "this is a theatre program" or "I was unable to reliably transcribe this").
"""


# ---------------------------------------------------------------------------
# LA-PA extraction (stage 3)
#
# The specification lives in lapa_extraction_prompt.md, which is a verbatim copy
# of the prompt used in production. It is read from disk rather than duplicated
# here: two copies of a 60 KB specification drift apart, and the executable one
# is not necessarily the one that gets read.
#
# The document is split at its own headings. Everything that describes the task
# and the target schema becomes the system prompt; the short instruction that
# introduces the programme text becomes the user prompt, with the placeholder
# rewritten to llmwrap's && convention.
# ---------------------------------------------------------------------------

_SPEC_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "lapa_extraction_prompt.md")

MARKDOWN_PLACEHOLDER = "MARKDOWN_CONTENT"


def _split_sections(text):
    """Map level-2 headings to their body."""
    parts = re.split(r"^## +(.+?)\s*$", text, flags = re.M)
    # parts = [preamble, title1, body1, title2, body2, ...]
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def _build_extraction_prompts(path = None):
    """Return (system_prompt, user_prompt) built from the specification file."""
    with open(path or _SPEC_FILE, encoding = "utf-8") as f:
        spec = f.read()

    sections = _split_sections(spec)
    missing = {"System Prompt", "User Prompt"} - set(sections)
    if missing:
        raise ValueError(f"{_SPEC_FILE} is missing section(s): {sorted(missing)}")

    # The system prompt carries the task framing plus the whole target schema:
    # output format, the nine model definitions, and the extraction rules.
    schema = [f"## {title}\n{body}" for title, body in sections.items()
              if title not in ("System Prompt", "User Prompt")]
    system_prompt = sections["System Prompt"].strip() + "\n\n" + "\n".join(schema).strip()

    # The user prompt is where the programme text is injected. The specification
    # writes the placeholder as {MARKDOWN_CONTENT}, sometimes with the underscore
    # escaped for markdown; llmwrap substitutes &&KEY.
    user_prompt = sections["User Prompt"].strip()
    user_prompt = re.sub(r"\{MARKDOWN\\?_CONTENT\}", f"&&{MARKDOWN_PLACEHOLDER}", user_prompt)

    if f"&&{MARKDOWN_PLACEHOLDER}" not in user_prompt:
        raise ValueError(
            f"No {{{MARKDOWN_PLACEHOLDER}}} placeholder found in the User Prompt "
            f"section of {_SPEC_FILE}."
        )

    return system_prompt, user_prompt


data_extraction_system_prompt, data_extraction_prompt = _build_extraction_prompts()
