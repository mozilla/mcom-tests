import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--bedrock',
        action='store',
        dest='bedrock',
        metavar='bedrock',
        help='marks tests so they use Bedrock branch')
    parser.addoption(
        '--skipsprod',
        action='store',
        dest='skipsprod',
        metavar='skip',
        help='marks tests as staging only and skips them on production')


def pytest_configure(config):
    config.addinivalue_line(
    'markers',
    'bedrock: marks tests so they use Bedrock branch')


def pytest_runtest_setup(item):
    if  hasattr(item.obj, 'bedrock') and \
        '/b' not in item.config.option.base_url:
        item.config.option.base_url = item.config.option.base_url + '/b'
    else:
        item.config.option.base_url = item.config.option.base_url.replace('/b', '')
    if  hasattr(item.obj, 'skipsprod') \
        and 'allizom.org' not in item.config.option.base_url:
        pytest.skip("skipping tests marked staging only")
