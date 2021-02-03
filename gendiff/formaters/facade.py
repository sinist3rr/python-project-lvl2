from gendiff.formaters.stylish import stylish_format
from gendiff.formaters.plain import plain_format
from gendiff.formaters.json import json_format


STYLISH_STYLE = 'stylish'
PLAIN_STYLE = 'plain'
JSON_STYLE = 'json'


def format_diff_tree(format_value, tree):
    if format_value == STYLISH_STYLE:
        return stylish_format(tree)
    elif format_value == PLAIN_STYLE:
        return plain_format(tree)
    elif format_value == JSON_STYLE:
        return json_format(tree)
    else:
        raise ValueError("Invalid format {}.".format(format_value))
