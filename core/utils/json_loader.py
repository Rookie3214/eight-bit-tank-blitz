# core/utils/json_loader.py

import json

def load_json(filepath):
    """
    Loads JSON data from a file.
    Returns the parsed Python object or None if there's an error.
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading JSON from {filepath}: {e}")
        return None
