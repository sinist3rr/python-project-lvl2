from gendiff.parse_files import parsing_file
from gendiff.formaters.stylish_format import stylish_format
from gendiff.formaters.plain_format import plain_format
from gendiff.formaters.json_format import json_format


def diff_tree(d1, d2):
    keys = d1.keys() | d2.keys()
    tree = []
    for key in keys:
        temp = {}
        temp['name'] = key
        if key not in d1:
            temp['state'] = 'added'
            temp['value'] = d2[key]
        elif key not in d2:
            temp['state'] = 'deleted'
            temp['value'] = d1[key]
        elif d1[key] == d2[key]:
            temp['state'] = 'unchanged'
            temp['value'] = d1[key]
        else:
            if isinstance(d2[key], dict) and isinstance(d1[key], dict):
                temp['state'] = 'nested'
                temp['children'] = diff_tree(d1[key], d2[key])
            else:
                temp['state'] = 'changed'
                temp['value'] = (d1[key], d2[key])
        tree.append(temp)
    return tree


def generate_diff(file1, file2, format='stylish'):
    file1_dict = parsing_file(file1)
    file2_dict = parsing_file(file2)

    try:
        tree = diff_tree(file1_dict, file2_dict)
    except AttributeError:
        print('Cannot make diff tree.')
        print('File is not found or empty.')
        return

    if format == 'stylish':
        final_result = '{}}}'.format(stylish_format(tree))
    elif format == 'plain':
        final_result = plain_format(tree)[:-1]
    elif format == 'json':
        final_result = json_format(tree)
    else:
        final_result = '{}}}'.format(stylish_format(tree))
    return final_result
