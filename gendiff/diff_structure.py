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


def get_children(nested):
    '''Return children of node.'''
    return nested.get('children')


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
        elif isinstance(d2[key], dict) and isinstance(d1[key], dict):
            temp['state'] = 'nested'
            temp['children'] = diff_tree(d1[key], d2[key])
        else:
            temp['state'] = 'changed'
            temp['value'] = (d1[key], d2[key])
        tree.append(temp)
    return tree
