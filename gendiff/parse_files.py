import json
import yaml
from yaml.scanner import ScannerError
from json import JSONDecodeError
import os
import sys


def parsing_file(filename):
    YAML_EXTENSIONS = ('.yml', '.yaml')

    if not os.path.exists(filename):
        print('File not found.')
        sys.exit(1)

    _, ext = os.path.splitext(filename)
    try:
        if ext.lower() == '.json':
            with open(filename, 'r') as jsonfile:
                return json.load(jsonfile)
        if ext.lower() in YAML_EXTENSIONS:
            with open(filename) as ymlfile:
                return yaml.load(ymlfile, Loader=yaml.FullLoader)
    except (JSONDecodeError, ScannerError):
        print("Invalid file type.")
        sys.exit(1)
