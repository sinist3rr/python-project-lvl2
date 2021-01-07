# -*- coding:utf-8 -*-

"""Simple json diff tests."""

import pytest
from gendiff import generate_diff


@pytest.fixture
def sample_paths_json():
    return ('tests/fixtures/before.json', 'tests/fixtures/after.json', 'tests/fixtures/before2.json', 'tests/fixtures/before_nested.json', 'tests/fixtures/after_nested.json')


@pytest.fixture
def sample_paths_yaml():
    return ('tests/fixtures/before.yml', 'tests/fixtures/after.yml', 'tests/fixtures/before2.yml', 'tests/fixtures/before_nested.yml', 'tests/fixtures/after_nested.yml')


@pytest.fixture
def sample_result():
    filepath = 'tests/fixtures/sample_result1.txt'
    with open(filepath) as fp:
        line = fp.read()
        return line


@pytest.fixture
def sample_result2():
    filepath = 'tests/fixtures/sample_result2.txt'
    with open(filepath) as fp:
        line = fp.read()
        return line


@pytest.fixture
def sample_nested_result():
    filepath = 'tests/fixtures/sample_nested_result.txt'
    with open(filepath) as fp:
        line = fp.read()
        return line


@pytest.fixture
def sample_nested_result_plain():
    filepath = 'tests/fixtures/sample_nested_result_plain.txt'
    with open(filepath) as fp:
        line = fp.read()
        return line


def test_simple_json(sample_paths_json, sample_result):
    """Check that json diff works."""
    assert generate_diff(sample_paths_json[0], sample_paths_json[1], 'json') == sample_result


def test_simple_json2(sample_paths_json, sample_result2):
    """Check that json diff works."""
    assert generate_diff(sample_paths_json[2], sample_paths_json[2], 'json') == sample_result2


def test_simple_yaml(sample_paths_yaml, sample_result):
    """Check that yaml diff works."""
    assert generate_diff(sample_paths_yaml[0], sample_paths_yaml[1], 'json') == sample_result


def test_simple_yaml2(sample_paths_yaml, sample_result2):
    """Check that yaml diff works."""
    assert generate_diff(sample_paths_yaml[2], sample_paths_yaml[2], 'json') == sample_result2


def test_nested_json(sample_paths_json, sample_nested_result):
    """Check that json diff works."""
    assert generate_diff(sample_paths_json[3], sample_paths_json[4], 'json') == sample_nested_result


def test_nested_yaml(sample_paths_yaml, sample_nested_result):
    """Check that yaml diff works."""
    assert generate_diff(sample_paths_yaml[3], sample_paths_yaml[4], 'json') == sample_nested_result


def test_nested_json_plain(sample_paths_json, sample_nested_result_plain):
    """Check that json diff works in plain format."""
    assert generate_diff(sample_paths_json[3], sample_paths_json[4], 'plain') == sample_nested_result_plain
