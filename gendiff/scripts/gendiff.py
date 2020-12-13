#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import prompt_args


def main():
    args = prompt_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
