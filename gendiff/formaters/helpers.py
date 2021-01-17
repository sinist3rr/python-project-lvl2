from gendiff.formaters.stylish_format import stylish_format
from gendiff.formaters.plain_format import plain_format
from gendiff.formaters.json_format import json_format


def select_formater(format, tree):
    if format == 'stylish':
        return '{}}}'.format(stylish_format(tree))
    elif format == 'plain':
        return plain_format(tree)[:-1]
    elif format == 'json':
        return json_format(tree)
