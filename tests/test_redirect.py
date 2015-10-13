# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

import pytest
import requests


@pytest.mark.nondestructive
@pytest.mark.parametrize('origin, destination, locale', [
    ('{base_url}/', '{base_url}/{locale}/', 'en-US'),
    ('{base_url}/firefox/', '{base_url}/{locale}/firefox/new/', 'en-US'),
    ('{base_url}/fennec/', '{base_url}/{locale}/firefox/partners/', 'en-US'),
    ('{base_url}/firefox/mobile/', '{base_url}/{locale}/firefox/android/', 'en-US'),
    ('{base_url}/aurora/', '{base_url}/{locale}/firefox/channel/', 'en-US'),
    ('{base_url}/beta/', '{base_url}/{locale}/firefox/channel/', 'en-US'),
    ('{base_url}/community/', '{base_url}/{locale}/contribute/', 'en-US'),
    ('{base_url}/mobile/37.0/releasenotes/', '{base_url}/{locale}/firefox/android/37.0/releasenotes/', 'en-US'),
    ('{base_url}/mobile/37.0beta/releasenotes/', '{base_url}/{locale}/firefox/android/37.0beta/releasenotes/', 'en-US'),
    ('{base_url}/mobile/37.0a2/auroranotes/', '{base_url}/{locale}/firefox/android/37.0a2/auroranotes/', 'en-US'),
    ('{base_url}/mobile/faq/', '{base_url}/{locale}/firefox/android/faq/', 'en-US'),
    ('{base_url}/mobile/features/', '{base_url}/{locale}/firefox/android/', 'en-US'),
    ('{base_url}/mobile/platforms/', 'https://support.mozilla.org/{locale}/kb/will-firefox-work-my-mobile-device', 'en-US'),
    ('{base_url}/m/faq/', '{base_url}/{locale}/firefox/android/faq/', 'en-US'),
    ('{base_url}/m/features/', '{base_url}/{locale}/firefox/android/', 'en-US'),
    ('{base_url}/m/platforms/', 'https://support.mozilla.org/{locale}/kb/will-firefox-work-my-mobile-device', 'en-US'),
    ('{base_url}/m/', '{base_url}/{locale}/firefox/new/', 'en-US'),
    ('{base_url}/rhino/doc.html', 'https://developer.mozilla.org/{locale}/docs/Mozilla/Projects/Rhino/Documentation', 'en-US'),
    ('{base_url}/rhino/download.html', 'https://developer.mozilla.org/{locale}/docs/Mozilla/Projects/Rhino/Download_Rhino', 'en-US'),
    ('{base_url}/rhino/', 'https://developer.mozilla.org/{locale}/docs/Mozilla/Projects/Rhino', 'en-US'),
    ('{base_url}/mobile/home/', 'https://blog.mozilla.org/services/2012/08/31/retiring-firefox-home/', 'en-US'),
    ('{base_url}/{locale}/mobile/home/', 'https://blog.mozilla.org/services/2012/08/31/retiring-firefox-home/', 'fr'),
    ('{base_url}/firefox/all-older.html', '{base_url}/{locale}/firefox/new/', 'en-US'),
    ('{base_url}/projects/firefox/3.6.13/firstrun/', '{base_url}/{locale}/firefox/new/', 'en-US'),
    ('{base_url}/projects/firefox/3.6.13/whatsnew/', '{base_url}/{locale}/firefox/new/', 'en-US'),
    ('{base_url}/b2g/', '{base_url}/{locale}/firefox/partners/', 'en-US'),
    ('{base_url}/metrofirefox/', '{base_url}/{locale}/firefox/new/', 'en-US'),
    ('{base_url}/newsletter/', '{base_url}/{locale}/newsletter/', 'en-US'),
    ('{base_url}/newsletter/', '{base_url}/{locale}/newsletter/', 'pl'),
    ('{base_url}/firefox/mobile/faq/?os=firefox-os', '{base_url}/{locale}/firefox/os/faq/', 'en-US'),
    ('{base_url}/firefox/accountmanager/', '{base_url}/{locale}/persona/', 'en-US'),
    ('{base_url}/apps/', 'https://marketplace.firefox.com/', 'en-US'),
    ('{base_url}/firefox/technology/', 'https://developer.mozilla.org/{locale}/docs/Tools', 'en-US'),
    ('{base_url}/firefox/performance/', '{base_url}/{locale}/firefox/desktop/fast/', 'en-US'),
    ('{base_url}/firefox/security/', '{base_url}/{locale}/firefox/desktop/trust/', 'en-US'),
    ('{base_url}/firefox/new/', '{base_url}/{locale}/firefox/new/', 'en-US'),
    ('{base_url}/firefox/new/', '{base_url}/{locale}/firefox/new/', 'son'),
    ('{base_url}/firefox/new/', '{base_url}/{locale}/firefox/new/', 'zh-CN'),
    ('{base_url}/firefox/new/', '{base_url}/{locale}/firefox/new/', 'ta'),
    ('{base_url}/privacy/archive/', '{base_url}/{locale}/privacy/archive/', 'en-US'),
    ('{base_url}/dnt/', '{base_url}/{locale}/firefox/dnt/', 'en-US'),
    ('{base_url}/firefox/os/notes/', 'https://developer.mozilla.org/{locale}/Firefox_OS/Releases', 'en-US'),
    ('{base_url}/firefox/os/notes/2.0/', 'https://developer.mozilla.org/{locale}/Firefox_OS/Releases/2.0', 'en-US'),
    ('https://www.mozilla.com/', 'https://www.mozilla.org/{locale}/firefox/new/', 'en-US'),
    ('https://aurora.mozilla.org/', 'https://www.mozilla.org/{locale}/firefox/channel/', 'en-US'),
    ('https://beta.mozilla.org/', 'https://www.mozilla.org/{locale}/firefox/channel/#beta', 'en-US')])
def test_redirect(origin, destination, locale, base_url):
    url = origin.format(base_url=base_url, locale=locale)
    headers = {'Accept-Language': locale}
    r = requests.get(url, allow_redirects=True, headers=headers)
    for h in r.history:
        assert h.status_code in [requests.codes.moved_permanently,
                                 requests.codes.found]
    assert destination.format(base_url=base_url, locale=locale) == r.url
    assert requests.codes.ok == r.status_code, r.url


@pytest.mark.nondestructive
@pytest.mark.parametrize('origin, destination, locale', [
    ('{base_url}/mobile/notes/', '{base_url}\/{locale}\/firefox\/android\/[\d\.]+\/releasenotes\/', 'en-US'),
    ('{base_url}/mobile/beta/notes/', '{base_url}\/{locale}\/firefox\/android\/[\d\.]+beta\/releasenotes\/', 'en-US'),
    ('{base_url}/mobile/aurora/notes/', '{base_url}\/{locale}\/firefox\/android\/[\d\.a-zA-Z]+\/auroranotes\/', 'en-US'),
    ('{base_url}/firefox/notes/', '{base_url}\/{locale}\/firefox\/[\d\.]+\/releasenotes\/', 'en-US')])
def test_redirect_regex(origin, destination, locale, base_url):
    url = origin.format(base_url=base_url, locale=locale)
    headers = {'Accept-Language': locale}
    r = requests.get(url, allow_redirects=True, headers=headers)
    for h in r.history:
        assert h.status_code in [requests.codes.moved_permanently,
                                 requests.codes.found]
    expected = destination.format(base_url=re.escape(base_url),
                                  locale=re.escape(locale))
    assert re.match(expected, r.url) is not None
    assert requests.codes.ok == r.status_code, r.url
