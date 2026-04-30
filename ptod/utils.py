import os
import json

def collect_files(path, acceptedFormats = [], recursive = True):
    """Collect all files of accepted format in a given directory."""
    
    acceptedFormatsLower = {ext.lower() for ext in acceptedFormats}
    finalList = []
    
    if recursive:
        for root, _, files in os.walk(path):
            for file in files:
                if not acceptedFormats or os.path.splitext(file)[1][1:].lower() in acceptedFormatsLower:
                    finalList.append(os.path.join(root, file))
    else:
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                if not acceptedFormats or os.path.splitext(file)[1][1:].lower() in acceptedFormatsLower:
                    finalList.append(full_path)

    return finalList

def write_json(path : str, content : dict, indent : int = 4) -> None:
    """
    Write to json. Will create folder if doesn't exist.
    """
    if os.path.splitext(path)[1] == ".json":
        check_dir_exists(path)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii = False, indent = indent)
    else:
        print(f"{path} needs to be a json file.")

def write_txt(path : str, content : str) -> None:
    """
    Write to raw text. Will create folder if doesn't exist.
    """
    check_dir_exists(path)

    with open(path, 'w') as f:
        f.write(content)

def check_dir_exists(filepath):
    """Check if folder exists, if not, create it."""
    if os.path.isdir(os.path.dirname(filepath)) == False:
        os.makedirs(os.path.dirname(filepath))

def read_txt(path : str) -> str:
    """Read a file as raw text."""
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return f.read()
    else:
        print(f"{path} doesn't exist.")
        return None