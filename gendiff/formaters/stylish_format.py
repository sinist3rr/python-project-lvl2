from gendiff.formaters.helpers import (
    is_nested,
    is_added,
    is_deleted,
    is_unchanged,
    is_changed,
    get_children,
    set_sign
)


def stylish_format(diff_tree, result='{\n', spaces=2):
    diff_tree.sort(key=lambda x: x['name'])
    for node in diff_tree:
        if is_nested(node):
            result += '{}  {}: {{\n'.format(spaces * ' ', node['name'])
            result = stylish_format(get_children(node), result, spaces + 4)
            result += '{}  }}\n'.format(spaces * ' ')
        elif is_added(node):
            result = set_sign(
                result, spaces, '+', node.get('name'), node.get('value')
            )
        elif is_deleted(node):
            result = set_sign(
                result, spaces, '-', node.get('name'), node.get('value')
            )
        elif is_unchanged(node):
            result = set_sign(
                result, spaces, ' ', node.get('name'), node.get('value')
            )
        elif is_changed(node):
            result = set_sign(
                result, spaces, '-', node.get('name'), node.get('value')[0]
            )
            result = set_sign(
                result, spaces, '+', node.get('name'), node.get('value')[1]
            )
    return result
