# -*- coding:utf-8 -*-

"""Various diff tests."""

import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
     'file_before,file_after,format,result',
     [(
             'tests/fixtures/before.json',
             'tests/fixtures/after.json',
             'stylish',
             'sample_result'
     ), (
             'tests/fixtures/before2.json',
             'tests/fixtures/before2.json',
             'stylish',
             'sample_result2'
     ), (
             'tests/fixtures/before.yml',
             'tests/fixtures/after.yml',
             'stylish',
             'sample_result'
     ), (
             'tests/fixtures/before2.yml',
             'tests/fixtures/before2.yml',
             'stylish',
             'sample_result2'
     ), (
             'tests/fixtures/before_nested.json',
             'tests/fixtures/after_nested.json',
             'stylish',
             'sample_nested_result'
     ), (
             'tests/fixtures/before_nested.yml',
             'tests/fixtures/after_nested.yml',
             'stylish',
             'sample_nested_result'
     ), (
             'tests/fixtures/before_nested.json',
             'tests/fixtures/after_nested.json',
             'plain',
             'sample_nested_result_plain'
     ), (
             'tests/fixtures/before_nested.json',
             'tests/fixtures/after_nested.json',
             'json',
             'sample_nested_result_json'
     )]
)
def test_gendiff(file_before, file_after, format, result):
    filepath = 'tests/fixtures/{}.txt'.format(result)
    with open(filepath) as fp:
        result_line = fp.read()

    assert generate_diff(file_before, file_after, format) == result_line
