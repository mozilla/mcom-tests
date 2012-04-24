import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--nonbedrock',
        action='store',
        dest='nonbedrock',
        metavar='nonbedrock',
        help='marks tests so they dont use bedrock branch')


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "nonbedrock: mark tests that are not using the bedrock branch on mozilla.org")


def pytest_runtest_setup(item):
    if '/b' in item.config.option.base_url:
        item.config.option.base_url = item.config.option.base_url.replace('/b', '')
    else:
        pass
