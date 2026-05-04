import os
import json
from .prompts import data_extraction_prompt
import llmwrap
from .utils import write_json, collect_files, read_txt

def extract_data_claude(pdf_file, output_folder, **kwargs):
    source_folder = os.path.join(output_folder, "text", os.path.splitext(os.path.basename(pdf_file))[0], "transcription")
    source_files = collect_files(source_folder, ["md"])
    output_dest = os.path.join(output_folder, "text", os.path.splitext(os.path.basename(pdf_file))[0], "linked-art")
    if os.path.isdir(output_dest) == False:
        os.makedirs(output_dest)

    for i, source_file in enumerate(source_files):
        print(f"Treating {source_file}")

        full_text = ""

        for source_file in source_files:
            read = read_txt(source_file)
            full_text = full_text + read + "\n\n"
        
        prompt = llmwrap.Prompt(data_extraction_prompt)

        model = llmwrap.ClaudeWrapper(
            "claude-3-7-sonnet-20250219", 
            api_key = kwargs.get("api_key", ""),
            system_prompt = "You are a tool for the transcription of textual data from scanned images.",
            max_tokens = 3000
        )

        response = model.process(prompt)

        txt_path = os.path.join(output_dest, "data.json")
        write_json(txt_path, response.content)