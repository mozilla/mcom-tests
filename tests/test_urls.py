# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests


@pytest.mark.nondestructive
@pytest.mark.parametrize('path', [
    'firefox/',
    'firefox/all/',
    'firefox/android/',
    'firefox/android/faq/',
    'firefox/aurora/all/',
    'firefox/beta/all/',
    'firefox/brand/',
    'firefox/channel/',
    'firefox/channel/android/',
    'firefox/desktop/',
    'firefox/developer/',
    'firefox/geolocation/',
    'firefox/installer-help/',
    'firefox/interest-dashboard/',
    'firefox/latest/releasenotes/',
    'firefox/mobile/',
    'firefox/new/',
    'firefox/nightly/firstrun/',
    'firefox/organizations/',
    'firefox/os/',
    'firefox/os/notes/1.1',
    'firefox/partners/',
    'firefox/releases/',
    'firefox/speed/',
    'firefox/sync/',
    'firefox/tiles/',
    'firefox/unsupported-systems/',
    'firefox/unsupported/EOL/',
    # Legacy URLs (Bug 1110927)
    'firefox/panorama/',
    'firefox/start/central.html',
    'firefox/sync/firstrun.html',
    # Thunberbird URLs
    'thunderbird/all/',
    'thunderbird/releases/'])
def test_url(path, base_url):
    url = '/'.join([base_url, 'en-US', path])
    r = requests.get(url, timeout=3)
    assert len(r.history) <= 2
    assert requests.codes.ok == r.status_code, url
