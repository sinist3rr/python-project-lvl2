import json
import yaml
from yaml.scanner import ScannerError
from json import JSONDecodeError
import os


JSON_EXT = '.json'
YAML_EXT = ('.yml', '.yaml')


def parse_file(filename):
    _, ext = os.path.splitext(filename)
    lowercase_extension = ext.lower()
    try:
        with open(filename, 'r') as file:
            if lowercase_extension == JSON_EXT:
                return json.load(file)
            elif lowercase_extension in YAML_EXT:
                return yaml.load(file, Loader=yaml.FullLoader)
            else:
                print('Incorrect extension {}'.format(ext))
    except (JSONDecodeError, ScannerError):
        raise ValueError("Invalid file type.")
    except OSError:
        raise ValueError("File is not available.")
