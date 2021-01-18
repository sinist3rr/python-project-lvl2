from gendiff.diff_structure import (
    is_nested,
    is_added,
    is_deleted,
    is_changed,
    get_children
)


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


def plain_format(diff_tree, result='', name=''):
    diff_tree.sort(key=lambda x: x['name'])
    for node in diff_tree:
        if is_nested(node):
            result = plain_format(
                get_children(node),
                result,
                "{f1}{f2}".format(
                    f1="" if not name else name + ".", f2=node['name']
                )
            )
        elif is_added(node):
            result += "Property '{f1}{f2}' was added with value: {f3}\n".format(
                f1='' if not name else name + '.', f2=node['name'], f3=is_complex(node['value'])
            )
        elif is_deleted(node):
            result += "Property '{f1}{f2}' was removed\n".format(
                f1='' if not name else name + '.', f2=node['name']
            )
        elif is_changed(node):
            result += "Property '{f1}{f2}' was updated. From {f3} to {f4}\n".format(
                f1='' if not name else name + '.',
                f2=node['name'],
                f3=is_complex(node['value'][0]),
                f4=is_complex(node['value'][1])
            )
    return result
