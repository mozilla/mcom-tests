import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--nonbedrock',
        action='store',
        dest='nonbedrock',
        metavar='nonbedrock',
        help='marks tests so they do not use Bedrock branch')


def pytest_configure(config):
    config.addinivalue_line(
    'markers',
    'nonbedrock: marks tests so they do not use Bedrock branch')


def pytest_runtest_setup(item):
    if 'nonbedrock' in item.keywords:
        item.config.option.base_url = item.config.option.base_url.replace('/b', '')
    else:
        pass
