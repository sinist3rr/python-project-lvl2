from gendiff.file_parser import parse_file
from gendiff.formaters.helpers import select_formater, STYLISH_STYLE
from gendiff.diff_structure import create_diff_tree


def generate_diff(file1, file2, format=STYLISH_STYLE):
    file1_dict = parse_file(file1)
    file2_dict = parse_file(file2)
    tree = create_diff_tree(file1_dict, file2_dict)
    return select_formater(format, tree)
