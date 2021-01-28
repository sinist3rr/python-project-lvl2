from gendiff.formaters.stylish_format import stylish_format_wrapper
from gendiff.formaters.plain_format import plain_format_wrapper
from gendiff.formaters.json_format import json_format


def select_formater(format, tree):
    if format == 'stylish':
        return '{}}}'.format(stylish_format_wrapper(tree))
    elif format == 'plain':
        return plain_format_wrapper(tree)[:-1]
    elif format == 'json':
        return json_format(tree)
