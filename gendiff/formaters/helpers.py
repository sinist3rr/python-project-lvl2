def is_nested(node):
    '''Check is node a nested.'''
    return node.get('state') == 'nested'


def is_added(node):
    '''Check is node a added.'''
    return node.get('state') == 'added'


def is_deleted(node):
    '''Check is node a deleted.'''
    return node.get('state') == 'deleted'


def is_changed(node):
    '''Check is node a changed.'''
    return node.get('state') == 'changed'


def is_unchanged(node):
    '''Check is node a unchanged.'''
    return node.get('state') == 'unchanged'


def is_dict(value):
    '''Check is value dictionary'''
    return isinstance(value, dict)


def get_children(nested):
    '''Return children of node.'''
    return nested.get('children')


def transform(item):
    if item is True:
        return 'true'
    elif item is False:
        return 'false'
    elif item is None:
        return 'null'
    else:
        return item


def nested_values(item, spaces, result=''):
    for key in item:
        if is_dict(item[key]):
            result += '{}{}: {{\n'.format(spaces * ' ', key)
            result = nested_values(item[key], spaces + 4, result)
            result += '{}}}\n'.format(spaces * ' ')
        else:
            result += '{}{}: {}\n'.format(spaces * ' ', key, item[key])
    return result


def set_sign(string, spaces, sign, name, value):
    if is_dict(value):
        string += '{}{} {}: {{\n'.format(spaces * ' ', sign, name)
        string += nested_values(value, spaces + 6)
        string += '{}  }}\n'.format(spaces * ' ')
    else:
        string += '{}{} {}: {}\n'.format(
            spaces * ' ', sign, name, transform(value)
        )
    return string


def is_complex(value):
    if is_dict(value):
        return '[complex value]'
    elif type(value) == int:
        return value
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return "'{}'".format(transform(value))
