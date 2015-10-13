# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

# List of the current supported locales on /firefox/new/
LOCALES = (
    'ar', 'ast', 'bg', 'bn-IN', 'ca', 'cs', 'de', 'dsb', 'el', 'en-GB',
    'en-US', 'es-CL', 'es-ES', 'fr', 'fy-NL', 'gd', 'it', 'ja', 'ko', 'nl',
    'pt-BR', 'pt-PT', 'ru', 'sv-SE', 'tr', 'uk', 'zh-TW')

# List of some locale name variants including unsupported short names and
# obsolete ab-CD-style names, which could be included in the visitors'
# Accept-Language HTTP header and should be redirected to the respective
# canonical locales
LOCALE_VARIANTS = {
    'en': 'en-US',
    'en-CA': 'en-US',
    'es': 'es-ES',
    'es-419': 'es-ES',
    'fr-FR': 'fr',
    'ja-JP-mac': 'ja',
    'pt': 'pt-BR',
    'ta-LK': 'ta'}

USER_AGENTS = {
    'FIREFOX': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
    'ESR_FIREFOX': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:17.0) Gecko/17.0 Firefox/17.0.8',
    'OLD_FIREFOX': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:16.0) Gecko/16.0 Firefox/16.0',
    'MOBILE': 'Mozilla/5.0 (Linux; U; Android 4.0.3; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'NON_FIREFOX': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.4 Safari/537.1',
    'IOS': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405'}


def pytest_generate_tests(metafunc):
    argvalues = []
    for user_agent in USER_AGENTS.values():
        # check the landing page redirects for each user agent
        argvalues.append((
            '{base_url}/firefox/',
            '{base_url}/{locale}/firefox/new/',
            'en-US', user_agent))
    for locale in LOCALES:
        # check the landing page redirects for each locale
        for user_agent in [USER_AGENTS['FIREFOX'],
                           USER_AGENTS['ESR_FIREFOX'],
                           USER_AGENTS['MOBILE']]:
            argvalues.append((
                '{base_url}/firefox/',
                '{base_url}/{locale}/firefox/new/',
                locale, user_agent))
    for variant, locale in LOCALE_VARIANTS.items():
        # check the landing page redirects for each locale variant
        argvalues.append((
            '{base_url}/firefox/',
            '{base_url}/%s/firefox/new/' % locale,
            variant, USER_AGENTS['FIREFOX']))
    metafunc.parametrize('origin, destination, locale, user_agent', argvalues)


@pytest.mark.nondestructive
def test_redirect(origin, destination, locale, user_agent, base_url):
    url = origin.format(base_url=base_url, locale=locale)
    headers = {'Accept-Language': locale}
    if user_agent is not None:
        headers['User-Agent'] = user_agent
    r = requests.get(url, allow_redirects=True, headers=headers)
    for h in r.history:
        assert h.status_code in [requests.codes.moved_permanently,
                                 requests.codes.found]
    assert destination.format(base_url=base_url, locale=locale) == r.url
    assert requests.codes.ok == r.status_code, r.url
