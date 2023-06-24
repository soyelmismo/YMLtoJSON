import yaml
import json
import sys

def get_file():
    try:
        argumento = sys.argv[1]
        archivo = argumento
        return archivo
    except IndexError:
        return None

def convert_yaml_to_json(yaml_file, json_file):
    try:
        with open(yaml_file, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        return "File Not Found."

    try:
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        with open(json_file, "w", encoding="utf-8") as file:
            file.write(json_data)
    except Exception as e:
        raise f'{yaml_file} ❌ {json_file}: {e}'

    return f'{yaml_file} ✅ {json_file}'


archivo = get_file()
if archivo:
    yaml_file = f'{archivo}'
    json_file = f'{archivo.split(".")[0]}.json'
    comp = convert_yaml_to_json(yaml_file, json_file)
    print(comp)
else:
    print("No file specified.")
