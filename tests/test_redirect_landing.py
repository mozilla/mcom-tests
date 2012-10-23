#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import requests
import pytest


@pytest.mark.skip_selenium
class TestRedirectLanding(object):
    DE_LOCALE = {'Accept-Language': 'de'}
    FIREFOX = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:16.0) Gecko/16.0 Firefox/16.0'}
    OLD_FIREFOX = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:15.0) Gecko/12.0 Firefox/15.0'}
    NON_FIREFOX = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.4 Safari/537.1'}
    MOBILE = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    IOS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405'}

    def _test_one_redirect(self, mozwebqa, origin, final, headers):
        url = mozwebqa.base_url + origin
        response = requests.get(url, headers=headers)
        result = mozwebqa.base_url + final
        Assert.equal(result, response.url)
        Assert.equal(len(response.history), 1)

        vary = response.history[0].headers['Vary']
        Assert.contains('User-Agent', vary)
        if 'Accept-Language' in headers:
            Assert.contains('Accept-Language', vary)

    @pytest.mark.nondestructive
    def test_redirect_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.FIREFOX)
        self._test_one_redirect(mozwebqa, '/firefox/', '/en-US/firefox/fx/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_locale_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.FIREFOX)
        self._test_one_redirect(mozwebqa, '/de/firefox/', '/de/firefox/fx/',
            headers)

        headers.update(self.DE_LOCALE)
        self._test_one_redirect(mozwebqa, '/firefox/', '/de/firefox/fx/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_old_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.OLD_FIREFOX)
        self._test_one_redirect(mozwebqa, '/firefox/', '/en-US/firefox/new/',
            headers)
        self._test_one_redirect(mozwebqa, '/en-US/firefox/', '/en-US/firefox/new/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_locale_old_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.OLD_FIREFOX)
        self._test_one_redirect(mozwebqa, '/de/firefox/', '/de/firefox/new/',
            headers)

        headers.update(self.DE_LOCALE)
        self._test_one_redirect(mozwebqa, '/firefox/', '/de/firefox/new/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_non_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.NON_FIREFOX)
        self._test_one_redirect(mozwebqa, '/firefox/', '/en-US/firefox/new/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_locale_non_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.NON_FIREFOX)
        self._test_one_redirect(mozwebqa, '/de/firefox/', '/de/firefox/new/',
            headers)

        headers.update(self.DE_LOCALE)
        self._test_one_redirect(mozwebqa, '/firefox/', '/de/firefox/new/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_mobile(self, mozwebqa):
        headers = {}
        headers.update(self.MOBILE)
        self._test_one_redirect(mozwebqa, '/firefox/', '/en-US/firefox/fx/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_locale_mobile(self, mozwebqa):
        headers = {}
        headers.update(self.MOBILE)
        self._test_one_redirect(mozwebqa, '/de/firefox/', '/de/mobile/',
            headers)

        headers.update(self.DE_LOCALE)
        self._test_one_redirect(mozwebqa, '/firefox/', '/de/mobile/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_ios(self, mozwebqa):
        headers = {}
        headers.update(self.IOS)
        self._test_one_redirect(mozwebqa, '/firefox/', '/en-US/mobile/',
            headers)
        self._test_one_redirect(mozwebqa, '/', '/en-US/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_locale_ios(self, mozwebqa):

        headers = {}
        headers.update(self.IOS)
        self._test_one_redirect(mozwebqa, '/de/firefox/', '/en-US/mobile/',
            headers)

        headers.update(self.DE_LOCALE)
        self._test_one_redirect(mozwebqa, '/firefox/', '/en-US/mobile/',
            headers)

    @pytest.mark.nondestructive
    def test_redirect_homepage_mobile(self, mozwebqa):
        headers = {}
        url = mozwebqa.base_url
        result = mozwebqa.base_url + '/en-US/'

        headers.update(self.MOBILE)
        response = requests.get(url, headers=headers)
        Assert.equal(result, response.url)

        headers.update(self.IOS)
        response = requests.get(url, headers=headers)
        Assert.equal(result, response.url)

        headers.update(self.DE_LOCALE)
        response = requests.get(url, headers=headers)
        Assert.equal(result, response.url)

        headers.update(self.MOBILE)
        response = requests.get(url, headers=headers)
        Assert.equal(result, response.url)
