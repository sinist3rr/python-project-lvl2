from gendiff.diff_structure import (
    is_nested,
    is_added,
    is_deleted,
    is_unchanged,
    is_changed,
    get_children
)


REGULAR_SPACES = 4
START_SPACES = 2


def transform(item):
    if item is True:
        return 'true'
    elif item is False:
        return 'false'
    elif item is None:
        return 'null'
    else:
        return str(item)


def stylish_format(diff_tree, spaces=START_SPACES, result='{\n'):
    sign = ' '
    diff_tree.sort(key=lambda x: x['name'])
    for node in diff_tree:
        name = node.get('name')
        value = node.get('value')
        if is_nested(node):
            result += '{}{} {}: {{\n'.format(spaces * ' ', sign, name)
            result = stylish_format(get_children(node), spaces + REGULAR_SPACES, result)
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


def set_sign(result, spaces, sign, name, value):
    if isinstance(value, dict):
        result += '{}{} {}: {{\n'.format(spaces * ' ', sign, name)
        result += nested_values(spaces + REGULAR_SPACES, ' ', value)
        result += '{}  }}\n'.format(spaces * ' ')
    else:
        result += '{}{} {}: {}\n'.format(
            spaces * ' ', sign, name, transform(value)
        )
    return result


def nested_values(spaces, sign, item, result=''):
    for name in item:
        value = item[name]
        if isinstance(value, dict):
            result += '{}{} {}: {{\n'.format(spaces * ' ', sign, name)
            result = nested_values(spaces + REGULAR_SPACES, ' ', value, result)
            result += '{}  }}\n'.format(spaces * ' ')
        else:
            result += '{}{}: {}\n'.format((spaces + 2) * ' ', name, value)
    return result
