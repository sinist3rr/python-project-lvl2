# -*- coding:utf-8 -*-

"""Various diff tests."""

import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    'file_before,file_after,format,result',
    [
        (
            'tests/fixtures/before.json',
            'tests/fixtures/after.json',
            'stylish',
            'diff_stylish'
        ),
        (
            'tests/fixtures/before2.json',
            'tests/fixtures/before2.json',
            'stylish',
            'diff_stylish2'
        ),
        (
            'tests/fixtures/before.yml',
            'tests/fixtures/after.yml',
            'stylish',
            'diff_stylish'
        ),
        (
            'tests/fixtures/before2.yml',
            'tests/fixtures/before2.yml',
            'stylish',
            'diff_stylish2'
        ),
        (
            'tests/fixtures/before_nested.json',
            'tests/fixtures/after_nested.json',
            'stylish',
            'diff_nested_stylish'
        ),
        (
            'tests/fixtures/before_nested.yml',
            'tests/fixtures/after_nested.yml',
            'stylish',
            'diff_nested_stylish'
        ),
        (
            'tests/fixtures/before_nested.json',
            'tests/fixtures/after_nested.json',
            'plain',
            'diff_nested_plain'
        ),
        (
            'tests/fixtures/before_nested.json',
            'tests/fixtures/after_nested.json',
            'json',
            'diff_nested_json'
        )]
)
def test_gendiff(file_before, file_after, format, result):
    filepath = 'tests/fixtures/{}.txt'.format(result)
    with open(filepath) as fp:
        result_line = fp.read()

    assert generate_diff(file_before, file_after, format) == result_line
