import argparse
from gendiff.formaters import STYLISH_STYLE, PLAIN_STYLE, JSON_STYLE


def prompt_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(dest='first_file')
    parser.add_argument(dest='second_file')
    parser.add_argument('-f', '--format',
                        dest='FORMAT', default=STYLISH_STYLE,
                        choices=[STYLISH_STYLE, PLAIN_STYLE, JSON_STYLE], help="set format of output")
    return parser
