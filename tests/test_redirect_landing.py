#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import requests
import pytest


nondestructive = pytest.mark.nondestructive
skip_selenium = pytest.mark.skip_selenium

@skip_selenium
class TestRedirectLanding(object):
    # List of the current supported locales on /firefox/new/
    LOCALES = (
        'ar', 'ast', 'bg', 'bn-IN', 'ca', 'cs', 'de', 'dsb', 'el', 'en-GB',
        'es-CL', 'es-ES', 'fr', 'fy-NL', 'gd', 'it', 'ja', 'ko', 'nl',
        'pt-BR', 'pt-PT', 'ru', 'sv-SE', 'tr', 'uk', 'zh-TW'
    )
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
        'ta-LK': 'ta',
    }
    ACCEPT_LANGUAGE = {'Accept-Language': 'en-US'}
    FIREFOX = {'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0'}
    ESR_FIREFOX = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:17.0) Gecko/17.0 Firefox/17.0.8'}
    OLD_FIREFOX = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:16.0) Gecko/16.0 Firefox/16.0'}
    MOBILE = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    NON_FIREFOX = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.4 Safari/537.1'}
    IOS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405'}

    def _test_redirect(self, mozwebqa, origin, final, headers):
        url = mozwebqa.base_url + origin
        response = requests.get(url, headers=headers)
        Assert.contains(final, response.url)

    @nondestructive
    def test_redirect_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.ACCEPT_LANGUAGE)
        headers.update(self.FIREFOX)
        self._test_redirect(mozwebqa, '/firefox/', 'en-US/firefox/new/', headers)

    @nondestructive
    def test_redirect_ios_using_en_US(self, mozwebqa):
        headers = {}
        headers.update(self.IOS)
        headers.update(self.ACCEPT_LANGUAGE)
        self._test_redirect(mozwebqa, '/firefox/', '/en-US/firefox/new/', headers)

    @nondestructive
    def test_redirect_esr_firefox_using_en_US(self, mozwebqa):
        headers = {}
        headers.update(self.ESR_FIREFOX)
        headers.update(self.ACCEPT_LANGUAGE)
        self._test_redirect(mozwebqa, '/firefox/', '/firefox/new/', headers)

    @nondestructive
    def test_redirect_non_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.NON_FIREFOX)
        headers.update(self.ACCEPT_LANGUAGE)
        self._test_redirect(mozwebqa, '/firefox/', '/en-US/firefox/new/', headers)

    @nondestructive
    def test_redirect_mobile_using_en_US(self, mozwebqa):
        headers = {}
        headers.update(self.ACCEPT_LANGUAGE)
        headers.update(self.MOBILE)
        self._test_redirect(mozwebqa, '/firefox/', '/firefox/new/', headers)

    @nondestructive
    def test_redirect_firefox_using_locale(self, mozwebqa):
        headers = {}
        headers.update(self.FIREFOX)
        for locale in self.LOCALES:
            headers.update({'Accept-Language': locale})
            final = '/%s/firefox/new/' % locale
            self._test_redirect(mozwebqa, '/firefox/', final, headers)

    @nondestructive
    def test_redirect_firefox_using_locale_variant(self, mozwebqa):
        headers = {}
        headers.update(self.FIREFOX)
        for variant, locale in self.LOCALE_VARIANTS.items():
            headers.update({'Accept-Language': variant})
            final = '/%s/firefox/new/' % locale
            self._test_redirect(mozwebqa, '/firefox/', final, headers)

    @nondestructive
    def test_redirect_mobile_using_locale(self, mozwebqa):
        headers = {}
        headers.update(self.MOBILE)
        for locale in self.LOCALES:
            headers.update({'Accept-Language': locale})
            self._test_redirect(mozwebqa, '/firefox/', '/firefox/new/', headers)

    @nondestructive
    def test_redirect_esr_firefox_using_locale(self, mozwebqa):
        headers = {}
        headers.update(self.ESR_FIREFOX)
        for locale in self.LOCALES:
            headers.update({'Accept-Language': locale})
            final = '/%s/firefox/new/' % locale
            self._test_redirect(mozwebqa, '/firefox/', final, headers)
