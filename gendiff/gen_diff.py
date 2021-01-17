from gendiff.parse_files import parsing_file
from gendiff.formaters.helpers import select_formater
from gendiff.diff_structure import diff_tree


def generate_diff(file1, file2, format='stylish'):
    file1_dict = parsing_file(file1)
    file2_dict = parsing_file(file2)
    tree = diff_tree(file1_dict, file2_dict)
    return select_formater(format, tree)
