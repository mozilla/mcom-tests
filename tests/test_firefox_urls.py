#!/usr/bin/env python

import pytest
import requests


nondestructive = pytest.mark.nondestructive
skip_selenium = pytest.mark.skip_selenium

@nondestructive
@skip_selenium
class TestFirefoxURLs(object):

    paths = [
        '/firefox/',
        '/firefox/all/',
        '/firefox/android/',
        '/firefox/android/faq/',
        '/firefox/aurora/all/',
        '/firefox/beta/all/',
        '/firefox/brand/',
        '/firefox/channel/',
        '/firefox/channel/android/',
        '/firefox/desktop/',
        '/firefox/developer/',
        '/firefox/geolocation/',
        '/firefox/installer-help/',
        '/firefox/interest-dashboard/',
        '/firefox/latest/releasenotes/',
        '/firefox/mobile/',
        '/firefox/new/',
        '/firefox/nightly/firstrun/',
        '/firefox/organizations/',
        '/firefox/os/',
        '/firefox/os/notes/1.1',
        '/firefox/partners/',
        '/firefox/releases/',
        '/firefox/speed/',
        '/firefox/sync/',
        '/firefox/tiles/',
        '/firefox/unsupported-systems/',
        '/firefox/unsupported/EOL/',
        # Legacy URLs (Bug 1110927)
        '/firefox/panorama/',
        '/firefox/start/central.html',
        '/firefox/sync/firstrun.html',
    ]

    def test_urls_ok(self, mozwebqa):
        for path in self.paths:
            url = mozwebqa.base_url + '/en-US' + path
            response = requests.get(url, timeout=3)
            assert len(response.history) <= 2
            assert response.status_code == 200, 'got status {} from {}'.format(
                response.status_code, url)
