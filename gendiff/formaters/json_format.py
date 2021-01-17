import json
from gendiff.diff_structure import (
    is_nested,
    get_children,
)


def json_prepare(diff_tree):
    diff_tree.sort(key=lambda x: x['name'])
    for node in diff_tree:
        if is_nested(node):
            json_format(get_children(node))
    return diff_tree


def json_format(sorted_tree):
    return json.dumps(json_prepare(sorted_tree))
