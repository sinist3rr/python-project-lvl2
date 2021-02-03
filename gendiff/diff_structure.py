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
        temp_structure = {}
        temp_structure['name'] = key
        if key not in before_dict:
            temp_structure[STATE] = ADDED
            temp_structure[VALUE] = after_dict[key]
        elif key not in after_dict:
            temp_structure[STATE] = DELETED
            temp_structure[VALUE] = before_dict[key]
        elif before_dict[key] == after_dict[key]:
            temp_structure[STATE] = UNCHANGED
            temp_structure[VALUE] = before_dict[key]
        elif isinstance(after_dict[key], dict) and isinstance(before_dict[key], dict):
            temp_structure[STATE] = NESTED
            temp_structure[CHILDREN] = create_diff_tree(before_dict[key], after_dict[key])
        else:
            temp_structure[STATE] = CHANGED
            temp_structure[VALUE] = (before_dict[key], after_dict[key])
        tree.append(temp_structure)
    return tree
