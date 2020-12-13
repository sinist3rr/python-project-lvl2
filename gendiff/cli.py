import argparse


def prompt_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(dest='first_file')
    parser.add_argument(dest='second_file')
    parser.add_argument('-f', '--format',
                        dest='FORMAT', help="set format of output")
    return parser.parse_args()
