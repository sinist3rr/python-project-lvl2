from gendiff.parse_files import parsing_file


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


def stylish(diff_tree, result='{\n', spaces=2):
    diff_tree.sort(key=lambda x: x['name'])
    for node in diff_tree:
        if is_nested(node):
            result += '{}  {}: {{\n'.format(spaces * ' ', node['name'])
            result = stylish(get_children(node), result, spaces + 4)
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


def diff_tree(d1, d2):
    keys = d1.keys() | d2.keys()
    tree = []
    for key in keys:
        temp = {}
        temp['name'] = key
        if key not in d1:
            temp['state'] = 'added'
            temp['value'] = d2[key]
        elif key not in d2:
            temp['state'] = 'deleted'
            temp['value'] = d1[key]
        elif d1[key] == d2[key]:
            temp['state'] = 'unchanged'
            temp['value'] = d1[key]
        else:
            if isinstance(d2[key], dict) and isinstance(d1[key], dict):
                temp['state'] = 'nested'
                temp['children'] = diff_tree(d1[key], d2[key])
            else:
                temp['state'] = 'changed'
                temp['value'] = (d1[key], d2[key])
        tree.append(temp)
    return tree


def generate_diff(file1, file2, FORMAT):
    file1_dict = parsing_file(file1)
    file2_dict = parsing_file(file2)
    tree = diff_tree(file1_dict, file2_dict)
    final_result = '{}}}\n'.format(stylish(tree))
    return final_result
