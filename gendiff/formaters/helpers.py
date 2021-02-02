from gendiff.formaters.stylish_format import stylish_format_wrapper
from gendiff.formaters.plain_format import plain_format_wrapper
from gendiff.formaters.json_format import json_format


STYLISH_STYLE = 'stylish'
PLAIN_STYLE = 'plain'
JSON_STYLE = 'json'


def select_formater(format, tree):
    if format == STYLISH_STYLE:
        return stylish_format_wrapper(tree)
    elif format == PLAIN_STYLE:
        return plain_format_wrapper(tree)
    elif format == JSON_STYLE:
        return json_format(tree)
