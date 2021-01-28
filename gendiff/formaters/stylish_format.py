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
            result += OPEN_BLOCK.format(mult_space(spaces), sign, name)
            result = stylish_format(get_children(node), spaces + REGULAR_SPACES, result)
            result += CLOSE_BLOCK.format(mult_space(spaces))
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
        result += OPEN_BLOCK.format(mult_space(spaces), sign, name)
        for key, nested in value:
            result = set_sign(result, spaces + REGULAR_SPACES, ' ', key, nested)
        result += CLOSE_BLOCK.format(mult_space(spaces))
    else:
        result += VALUE_BLOCK.format(
            mult_space(spaces), sign, name, transform(value)
        )
    return result


def mult_space(count):
    return ' ' * count


def transform(item):
    if item is True:
        return 'true'
    elif item is False:
        return 'false'
    elif item is None:
        return 'null'
    else:
        return str(item)
