import json
import yaml
import os


def parsing_file(filename):
    JSON_EXTENSIONS = ['.json', '.JSON']
    YAML_EXTENSIONS = ['.yml', '.yaml', '.YAML', '.YML']

    _, ext = os.path.splitext(filename)
    try:
        if ext in JSON_EXTENSIONS:
            with open(filename, 'r') as jsonfile:
                return json.load(jsonfile)
        if ext in YAML_EXTENSIONS:
            with open(filename) as ymlfile:
                return yaml.load(ymlfile, Loader=yaml.FullLoader)
    except json.JSONDecodeError:
        print("Invalid file type.")
