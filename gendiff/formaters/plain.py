from gendiff.diff_structure import (
    is_nested,
    is_added,
    is_deleted,
    is_changed,
    get_children
)


def plain_format(diff_tree):
    return ''.join(_plain_format(diff_tree, [], []))[:-1]


def _plain_format(diff_tree, result, composite_key):
    sorted_diff_tree = sorted(diff_tree, key=lambda x: x['name'])
    for node in sorted_diff_tree:
        key = node['name']
        mixed_key = [*composite_key, key]
        formatted_mixed_key = '.'.join(mixed_key)
        if is_nested(node):
            result = _plain_format(
                get_children(node),
                result,
                mixed_key
            )
        elif is_added(node):
            result.append("Property '{}' was added with value: {}\n".format(
                formatted_mixed_key, format_plain_value(node['value'])
            ))
        elif is_deleted(node):
            result.append("Property '{}' was removed\n".format(
                formatted_mixed_key
            ))
        elif is_changed(node):
            result.append("Property '{}' was updated. From {} to {}\n".format(
                formatted_mixed_key,
                format_plain_value(node['value'][0]),
                format_plain_value(node['value'][1])
            ))
    return result


def format_plain_value(value):
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
