import os
from .utils import collect_files, write_json, write_txt
from .prompts import transcription_prompt
import llmwrap
import time

def transcribe(pdf_file, output_folder, **kwargs):
    failed_files = []
    source_folder = os.path.join(output_folder, "images", os.path.splitext(os.path.basename(pdf_file))[0], "preprocessed-small")
    
    source_files = collect_files(source_folder, ["jpeg", "jpg"])
    
    output_dest = os.path.join(output_folder, "text", os.path.splitext(os.path.basename(pdf_file))[0], "transcription")
    if os.path.isdir(output_dest) == False:
        os.makedirs(output_dest)

    for i, source_file in enumerate(source_files):
        print(f"Treating {source_file}")
        
        txt_path = os.path.join(output_dest, f"{os.path.splitext(os.path.basename(source_file))[0]}.md")
        
        prompt = llmwrap.Prompt(transcription_prompt, images = [source_file])
            
        if kwargs.get("model", "ollama") == "ollama":
            model = llmwrap.ClaudeWrapper(
                "claude-3-7-sonnet-20250219", 
                api_key = kwargs.get("api_key", ""),
                system_prompt = "You are a tool for the transcription of textual data from scanned images.",
                max_tokens = 3000
            )

        response = model.process(prompt)

        if isinstance(response, dict):
            failed_files.append({"file" : txt_path, "error" : response["content"]})
            write_json(os.path.join(output_dest, "_failed_files.json"), {"fails" : failed_files})
        else:
            response.write(output_dest)
            write_txt(txt_path, response.content)

        time.sleep(kwargs.get("cooldown_time", 1))