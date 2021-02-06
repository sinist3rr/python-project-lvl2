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


def create_diff_tree(before_dict, after_dict):
    keys = before_dict.keys() | after_dict.keys()
    tree = []
    for key in keys:
        diff_tree = {}
        diff_tree['name'] = key
        if key not in before_dict:
            diff_tree[STATE] = ADDED
            diff_tree[VALUE] = after_dict[key]
        elif key not in after_dict:
            diff_tree[STATE] = DELETED
            diff_tree[VALUE] = before_dict[key]
        elif before_dict[key] == after_dict[key]:
            diff_tree[STATE] = UNCHANGED
            diff_tree[VALUE] = before_dict[key]
        elif isinstance(after_dict[key], dict) and isinstance(before_dict[key], dict):
            diff_tree[STATE] = NESTED
            diff_tree[CHILDREN] = create_diff_tree(before_dict[key], after_dict[key])
        else:
            diff_tree[STATE] = CHANGED
            diff_tree[VALUE] = (before_dict[key], after_dict[key])
        tree.append(diff_tree)
    return tree
