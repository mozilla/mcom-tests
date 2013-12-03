import pytest
import requests
from unittestzero import Assert
from BeautifulSoup import BeautifulStoneSoup


def pytest_generate_tests(metafunc):
    if 'language_link' in metafunc.fixturenames:
        url = '%s%s' % (metafunc.config.option.base_url, metafunc.cls.link_check_url)
        r = requests.get(url, verify=False, timeout=20)
        Assert.equal(r.status_code, requests.codes.ok,
                     '{0.url} returned: {0.status_code} {0.reason}'.format(r))

        parsed_html = BeautifulStoneSoup(r.content)
        language_rows = parsed_html.findAll('tr', id=True)
        links = []
        for language in language_rows:
            lang_urls = [a['href'] for a in language.findAll('a')]
            lang_urls = map(lambda u: u if not u.startswith('/') else metafunc.config.option.base_url + u, lang_urls)
            for url in lang_urls:
                links.append({'id': language['id'], 'url': url})
        metafunc.parametrize('language_link', links)


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
    if hasattr(item.obj, 'bedrock') and '/b' not in item.config.option.base_url:
        item.config.option.base_url = item.config.option.base_url + '/b'
    else:
        item.config.option.base_url = item.config.option.base_url.replace('/b', '')
    if hasattr(item.obj, 'skipsprod') and 'allizom.org' not in item.config.option.base_url:
        pytest.skip("skipping tests marked staging only")
