#!/usr/bin/env python3

from gendiff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(dest='first_file')
    parser.add_argument(dest='second_file')
    parser.add_argument('-f', '--format',
                        dest='FORMAT', help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
