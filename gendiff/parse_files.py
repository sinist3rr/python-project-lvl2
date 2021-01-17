import json
import yaml


def parsing_file(filename):
    try:
        if filename.endswith('.json'):
            with open(filename, 'r') as jsonfile:
                return json.load(jsonfile)
        if filename.endswith('.yml'):
            with open(filename) as ymlfile:
                return yaml.load(ymlfile, Loader=yaml.FullLoader)
    except json.JSONDecodeError:
        print("Invalid file type.")
