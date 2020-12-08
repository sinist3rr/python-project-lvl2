# -*- coding:utf-8 -*-

"""Simple json diff tests."""

import pytest
from gendiff import generate_diff


@pytest.fixture
def sample_paths_json():
    return ('tests/fixtures/before.json', 'tests/fixtures/after.json')


@pytest.fixture
def sample_result():
    filepath = 'tests/fixtures/sample_result1.txt'
    with open(filepath) as fp:
        line = fp.read()
        return line


def test_foo():
    assert True


def test_simple_json(sample_paths_json, sample_result):
    """Check that json diff works."""
    assert generate_diff(sample_paths_json[0], sample_paths_json[1]) == sample_result
