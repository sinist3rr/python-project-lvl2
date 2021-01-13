from gendiff.formaters.helpers import (
                                        is_nested,
                                        is_added,
                                        is_complex,
                                        is_deleted,
                                        is_changed,
                                        get_children
                                      )


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
            if not name:
                result += "Property '{}' was added with value: {}\n".format(
                        node['name'], is_complex(node['value'])
                        )
            else:
                result += "Property '{}' was added with value: {}\n".format(
                        name + '.' + node['name'], is_complex(node['value'])
                        )
        elif is_deleted(node):
            if not name:
                result += "Property '{}' was removed\n".format(node['name'])
            else:
                result += "Property '{}' was removed\n".format(
                        name + '.' + node['name']
                        )
        elif is_changed(node):
            if not name:
                result += "Property '{}' was updated. From {} to {}\n".format(
                        node['name'],
                        is_complex(node['value'][0]),
                        is_complex(node['value'][1])
                        )
            else:
                result += "Property '{}' was updated. From {} to {}\n".format(
                        name + '.' + node['name'],
                        is_complex(node['value'][0]),
                        is_complex(node['value'][1])
                        )
    return result[:-1]
