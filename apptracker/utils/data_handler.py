from pathlib import Path
import json

DATA_FILE_PATH = Path(__file__).resolve().parent.parent.parent / 'data' / 'activities.json'

def read_activities():
    if not DATA_FILE_PATH.exists():
        return {"activities": []}
    
    with open(DATA_FILE_PATH, 'r') as file:
        return json.load(file)

def write_activities(data):
    with open(DATA_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)