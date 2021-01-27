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
OPEN_BLOCK = '{}{} {}: {{\n'
VALUE_BLOCK = '{}{} {}: {}\n'
CLOSE_BLOCK = '{}  }}\n'


def stylish_format(diff_tree, spaces=START_SPACES, result='{\n'):
    sign = ' '
    diff_tree.sort(key=lambda x: x['name'])
    for node in diff_tree:
        name = node.get('name')
        value = node.get('value')
        if is_nested(node):
            result += OPEN_BLOCK.format(spaces * ' ', sign, name)
            result = stylish_format(get_children(node), spaces + REGULAR_SPACES, result)
            result += CLOSE_BLOCK.format(spaces * ' ')
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
        result += OPEN_BLOCK.format(spaces * ' ', sign, name)
        result += nested_values(spaces + REGULAR_SPACES, ' ', value)
        result += CLOSE_BLOCK.format(spaces * ' ')
    else:
        result += VALUE_BLOCK.format(
            spaces * ' ', sign, name, transform(value)
        )
    return result


def nested_values(spaces, sign, item, result=''):
    for name in item:
        value = item[name]
        if isinstance(value, dict):
            result += OPEN_BLOCK.format(spaces * ' ', sign, name)
            result = nested_values(spaces + REGULAR_SPACES, ' ', value, result)
            result += CLOSE_BLOCK.format(spaces * ' ')
        else:
            result += VALUE_BLOCK.format(spaces * ' ', sign, name, value)
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
