STATE = 'state'
VALUE = 'value'
CHILDREN = 'children'
NESTED = 'nested'
ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'
UNCHANGED = 'unchanged'


def is_nested(node):
    '''Check is node a nested.'''
    return node.get(STATE) == NESTED


def is_added(node):
    '''Check is node a added.'''
    return node.get(STATE) == ADDED


def is_deleted(node):
    '''Check is node a deleted.'''
    return node.get(STATE) == DELETED


def is_changed(node):
    '''Check is node a changed.'''
    return node.get(STATE) == CHANGED


def is_unchanged(node):
    '''Check is node a unchanged.'''
    return node.get(STATE) == UNCHANGED


def get_children(nested):
    '''Return children of node.'''
    return nested.get(CHILDREN)


def diff_tree(d1, d2):
    keys = d1.keys() | d2.keys()
    tree = []
    for key in keys:
        temp = {}
        temp['name'] = key
        if key not in d1:
            temp[STATE] = ADDED
            temp[VALUE] = d2[key]
        elif key not in d2:
            temp[STATE] = DELETED
            temp[VALUE] = d1[key]
        elif d1[key] == d2[key]:
            temp[STATE] = UNCHANGED
            temp[VALUE] = d1[key]
        elif isinstance(d2[key], dict) and isinstance(d1[key], dict):
            temp[STATE] = NESTED
            temp[CHILDREN] = diff_tree(d1[key], d2[key])
        else:
            temp[STATE] = CHANGED
            temp[VALUE] = (d1[key], d2[key])
        tree.append(temp)
    return tree
