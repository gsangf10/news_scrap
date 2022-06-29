import json

def save_json(file_path, d_list):
    with open(file_path, "w", encoding='utf-8-sig') as f:
        json.dump(d_list, f, ensure_ascii=False)

def load_json(file_path):
    with open(file_path, "r", encoding='utf-8-sig') as f:
        d_list = json.load(f)
        return d_list