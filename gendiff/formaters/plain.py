import copy
from gendiff.diff_structure import (
    is_nested,
    is_added,
    is_deleted,
    is_changed,
    get_children
)


def plain_format(diff_tree):
    return ''.join(_plain_format(diff_tree, []))[:-1]


def _plain_format(diff_tree, result, name=''):
    new_structure = copy.deepcopy(diff_tree)
    new_structure.sort(key=lambda x: x['name'])
    if not name:
        composite_key = ''
    else:
        composite_key = name + '.'
    for node in new_structure:
        key = node['name']
        if is_nested(node):
            result = _plain_format(
                get_children(node),
                result,
                "{}{}".format(composite_key, key)
            )
        elif is_added(node):
            result.append("Property '{}{}' was added with value: {}\n".format(
                composite_key, key, is_complex(node['value'])
            ))
        elif is_deleted(node):
            result.append("Property '{}{}' was removed\n".format(
                composite_key, key
            ))
        elif is_changed(node):
            result.append("Property '{}{}' was updated. From {} to {}\n".format(
                composite_key,
                key,
                is_complex(node['value'][0]),
                is_complex(node['value'][1])
            ))
    return result


def is_complex(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return "'{}'".format(value)
    else:
        return str(value)
