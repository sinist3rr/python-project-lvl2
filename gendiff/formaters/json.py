import json
import copy
from gendiff.diff_structure import (
    is_nested,
    get_children,
)


def sort_diff_tree(diff_tree):
    diff_tree.sort(key=lambda x: x['name'])
    for node in diff_tree:
        if is_nested(node):
            sort_diff_tree(get_children(node))
    return diff_tree


def json_format(diff_tree):
    new_structure = copy.deepcopy(diff_tree)
    return json.dumps(sort_diff_tree(new_structure))
