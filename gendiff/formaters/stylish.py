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
ADDED = '+'
REMOVED = '-'
UNCHANGED = ' '


def stylish_format(diff_tree):
    return '{}}}'.format(''.join(_stylish_format(diff_tree, START_SPACES, ['{\n'])))


def _stylish_format(diff_tree, spaces, result):
    sign = ' '
    sorted_diff_tree = sorted(diff_tree, key=lambda x: x['name'])
    for node in sorted_diff_tree:
        name = node.get('name')
        value = node.get('value')
        if is_nested(node):
            result.append(OPEN_BLOCK.format(calculate_indentation(spaces), sign, name))
            result = _stylish_format(get_children(node), spaces + REGULAR_SPACES, result)
            result.append(CLOSE_BLOCK.format(calculate_indentation(spaces)))
        elif is_added(node):
            format_node(result, spaces, ADDED, name, value)
        elif is_deleted(node):
            format_node(result, spaces, REMOVED, name, value)
        elif is_unchanged(node):
            format_node(result, spaces, UNCHANGED, name, value)
        elif is_changed(node):
            format_node(result, spaces, REMOVED, name, value[0])
            format_node(result, spaces, ADDED, name, value[1])
    return result


def format_node(result, spaces, sign, name, value):
    if isinstance(value, dict):
        result.append(OPEN_BLOCK.format(calculate_indentation(spaces), sign, name))
        for key, nested in value.items():
            format_node(result, spaces + REGULAR_SPACES, ' ', key, nested)
        result.append(CLOSE_BLOCK.format(calculate_indentation(spaces)))
    else:
        result.append(VALUE_BLOCK.format(
            calculate_indentation(spaces), sign, name, format_stylish_value(value)
        ))


def calculate_indentation(recursion_depth):
    return ' ' * recursion_depth


def format_stylish_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)
