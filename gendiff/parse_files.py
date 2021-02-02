import json
import yaml
from yaml.scanner import ScannerError
from json import JSONDecodeError
import os


def parsing_file(filename):
    _, ext = os.path.splitext(filename)
    try:
        with open(filename, 'r') as file:
            if ext.lower() == '.json':
                return json.load(file)
            if ext.lower() in ('.yml', '.yaml'):
                return yaml.load(file, Loader=yaml.FullLoader)
    except (JSONDecodeError, ScannerError):
        raise ValueError("Invalid file type.")
    except IOError:
        raise ValueError("File is not available.")
