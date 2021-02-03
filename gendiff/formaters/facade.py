from gendiff.formaters.stylish_format import stylish_format_wrapper
from gendiff.formaters.plain_format import plain_format_wrapper
from gendiff.formaters.json_format import json_format


STYLISH_STYLE = 'stylish'
PLAIN_STYLE = 'plain'
JSON_STYLE = 'json'


def format_diff_tree(format_value, tree):
    if format_value == STYLISH_STYLE:
        return stylish_format_wrapper(tree)
    elif format_value == PLAIN_STYLE:
        return plain_format_wrapper(tree)
    elif format_value == JSON_STYLE:
        return json_format(tree)
    else:
        raise ValueError("Invalid format {}.".format(format_value))
