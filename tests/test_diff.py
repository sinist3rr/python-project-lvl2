# -*- coding:utf-8 -*-

"""Simple json diff tests."""

import pytest
from gendiff import generate_diff


@pytest.fixture
def sample_paths_json():
    return ('tests/fixtures/before.json', 'tests/fixtures/after.json')


def test_foo():
    assert True


def test_simple_json(sample_paths_json):
    """Check that json diff works."""
    sample1 = '{\n\t- follow: false\n\t  host: hexlet.io\n\t- proxy: 123.234.53.22\n\t- timeout: 50\n\t+ timeout: 20\n\t+ verbose: true\n}\n'
    assert generate_diff(sample_paths_json[0], sample_paths_json[1]) == sample1
