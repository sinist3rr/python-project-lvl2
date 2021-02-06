from gendiff.file_parser import parse_file
from gendiff.formaters import format_diff_tree, STYLISH_STYLE
from gendiff.diff_structure import create_diff_tree


def generate_diff(file1, file2, format=STYLISH_STYLE):
    parsed_file1 = parse_file(file1)
    parsed_file2 = parse_file(file2)
    tree = create_diff_tree(parsed_file1, parsed_file2)
    return format_diff_tree(format, tree)
