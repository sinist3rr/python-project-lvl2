from gendiff.diff_structure import (
    is_nested,
    is_added,
    is_deleted,
    is_unchanged,
    is_changed,
    get_children
)


def set_sign(string, spaces, sign, name, value):
    if isinstance(value, dict):
        string += '{}{} {}: {{\n'.format(spaces * ' ', sign, name)
        string += nested_values(value, spaces + 6)
        string += '{}  }}\n'.format(spaces * ' ')
    else:
        string += '{}{} {}: {}\n'.format(
            spaces * ' ', sign, name, transform(value)
        )
    return string


def nested_values(item, spaces, result=''):
    for key in item:
        if isinstance(item[key], dict):
            result += '{}{}: {{\n'.format(spaces * ' ', key)
            result = nested_values(item[key], spaces + 4, result)
            result += '{}}}\n'.format(spaces * ' ')
        else:
            result += '{}{}: {}\n'.format(spaces * ' ', key, item[key])
    return result


def transform(item):
    if item is True:
        return 'true'
    elif item is False:
        return 'false'
    elif item is None:
        return 'null'
    else:
        return str(item)


def stylish_format(diff_tree, result='{\n', spaces=2):
    diff_tree.sort(key=lambda x: x['name'])
    for node in diff_tree:
        name = node.get('name')
        value = node.get('value')
        if is_nested(node):
            result += '{}  {}: {{\n'.format(spaces * ' ', node['name'])
            result = stylish_format(get_children(node), result, spaces + 4)
            result += '{}  }}\n'.format(spaces * ' ')
        elif is_added(node):
            result = set_sign(result, spaces, '+', name, value)
        elif is_deleted(node):
            result = set_sign(result, spaces, '-', name, value)
        elif is_unchanged(node):
            result = set_sign(result, spaces, ' ', name, value)
        elif is_changed(node):
            result = set_sign(result, spaces, '-', name, value[0])
            result = set_sign(result, spaces, '+', name, value[1])
    return result
