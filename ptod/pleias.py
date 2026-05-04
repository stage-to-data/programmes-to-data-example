import os
import json
from .utils import write_json, collect_files, read_txt
from vllm import LLM, SamplingParams

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

PLEIAS_SYSTEM_PROMPT = "You annotate French theater programmes from the Festival d'Avignon against the Linked Art performing-arts ontology. Extract structured JSON-LD entities from programme markdown."

PLEIAS_ENTITY_INSTRUCTIONS = {
    "A": "Extract the Work entity (A) from this theater programme. Output valid Linked Art JSON-LD for the Work as a PropositionalObject, including title, creator with BnF role, source attribution, and any adaptation/influence links.",
    "B_meta": "Extract the Production metadata from this theater programme. Output valid Linked Art JSON-LD for the Production as an Activity, including title, classification, genre, venue, date range, festival link, and source attribution. Do not include the cast/crew list.",
    "B_cast": "Extract all performers (actors, dancers, musicians) from this theater programme's Production. Output as Linked Art JSON-LD produced_by block, with each performer's name, BnF controlled role, verbatim role, and character if applicable.",
    "B_crew": "Extract all creative and technical crew members (director, lighting, costumes, set design, etc.) from this theater programme's Production. Output as Linked Art JSON-LD produced_by block, with each person's name, BnF controlled role, and verbatim role as transcribed from the programme.",
    "C": "Extract a single Performance entity (C) for one specific date from this theater programme. Output valid Linked Art JSON-LD for the Performance as an Activity, including the exact date/time, venue, and link to the parent Production.",
    "Festival": "Extract the Festival/Overall Event entity from this theater programme. Output valid Linked Art JSON-LD for the festival as an Activity, including title, year, venue city, and classification.",
    "Text": "Extract the source Text entity (Play/Inspired-by) referenced in this theater programme. Output valid Linked Art JSON-LD for the source text as a LinguisticObject, including title and original author.",
}

class PleiasModel:
    def __init__(self, **kwargs):
        self.model_id = kwargs.get("model_id", "Pclanglais/POntAvignon-4b")
        self.verbose = kwargs.get("verbose", True)
        self.llm = None
        self.tokenizer = None
        self.system_prompt = PLEIAS_SYSTEM_PROMPT
        self.entity_instructions = PLEIAS_ENTITY_INSTRUCTIONS
        self.max_tokens = kwargs.get("max_tokens", 2048)
        self.device = kwargs.get("device", "cpu")

        self._load_model()

    def _load_model(self):
        if self.verbose:
            print("\nLoading model...\n")
        self.llm = LLM(
            model = self.model_id, 
            dtype = "half", 
            max_model_len = 4096, 
            gpu_memory_utilization = 0.95, 
            enforce_eager = True
        )
        self.tokenizer = self.llm.get_tokenizer()
        if self.verbose:
            print("\nReady!\n")

    def annotate(self, input_text, source_name = "programme"):
        results = {}
        for et in self.entity_instructions:
            if self.verbose:
                print(f"Extracting {et}...")
            results[et] = self._annotate_entity(input_text, et, source_name)
        return results

    def _annotate_entity(self, input_text, entity_type, source_name = "programme"):
        instruction = self.entity_instructions[entity_type]
        user_msg = f"{instruction}\n\nSource: {source_name}\n\n---\n\n{input_text}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_msg},
        ]

        prompt = self.tokenizer.apply_chat_template(messages, tokenize = False, add_generation_prompt = True)
        prompt += "<think>\n"
        params = SamplingParams(
            max_tokens = self.max_tokens,
            temperature = 0.7,
            top_p = 0.9,
            repetition_penalty = 1.1
        )
        output = self.llm.generate([prompt], params)[0].outputs[0].text
        think_end = output.find("</think>")

        if think_end > 0:
            reasoning = output[:think_end].strip()
            jsonld_str = output[think_end + 8:].strip()
        else:
            reasoning = output
            jsonld_str = ""
        valid = False

        try:
            json.loads(jsonld_str)
            valid = True
        except:
            pass
        return {"reasoning": reasoning, "output": jsonld_str, "valid_json": valid}
    
    def write_result(self, result, path):
        export = {}
        for et, r in result.items():
            if r['valid_json']:
                export[et] = json.loads(r['output'])
            else:
                export[et] = {"_error": "invalid JSON", "_raw": r['output'][:500]}
        write_json(path, result)

def extract_data(pleias_model, pdf_file, output_folder):
    source_folder = os.path.join(output_folder, "text", os.path.splitext(os.path.basename(pdf_file))[0], "transcription")
    
    source_files = collect_files(source_folder, ["md"])
    
    output_dest = os.path.join(output_folder, "text", os.path.splitext(os.path.basename(pdf_file))[0], "linked-art")
    if os.path.isdir(output_dest) == False:
        os.makedirs(output_dest)

    full_text = ""

    for source_file in source_files:
        read = read_txt(source_file)
        full_text = full_text + read + "\n\n"
    
    result = pleias_model.annotate(full_text, os.path.basename(pdf_file))
    pleias_model.write_result(result, os.path.join(output_dest, "data.json"))