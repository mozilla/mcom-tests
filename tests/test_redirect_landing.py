#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import requests
import pytest


@pytest.mark.skip_selenium
class TestRedirectLanding(object):
    LOCALES = (
        "ach", "af", "ak", "ar", "as", "ast", "be", "bg",
        "bn-BD", "bn-IN", "br", "bs", "ca", "cs", "csb", "cy", "da",
        "de", "el", "en-GB", "en-ZA", "eo", "es-AR", "es-CL", "es-ES",
        "es-MX", "et", "eu", "fa", "ff", "fi", "fr", "fy-NL", "ga-IE",
        "gd", "gl", "gu-IN", "he", "hi-IN", "hr", "hu", "hy-AM", "id",
        "is", "it", "ja", "kk", "km", "kn", "ko", "ku", "lg", "lij", " lt",
        "lv", "mai", "mk", "ml", "mr", "nb-NO", "nl", "nn-NO", "nso",
        "or", "pa-IN", "pl", "pt-BR", "pt-PT", "rm", "ro", "ru", "si", "sk",
        "sl", "son", "sq", "sr", "sv-SE", "sw", "ta", "ta-LK", "te", "th", "tr",
        "uk", "vi", "zh-CN", "zh-TW", "zu"
    )
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

    @pytest.mark.nondestructive
    def test_redirect_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.ACCEPT_LANGUAGE)
        headers.update(self.FIREFOX)
        self._test_redirect(mozwebqa, '/firefox/', 'en-US/firefox/new/', headers)

    @pytest.mark.nondestructive
    def test_redirect_ios_using_en_US(self, mozwebqa):
        headers = {}
        headers.update(self.IOS)
        headers.update(self.ACCEPT_LANGUAGE)
        self._test_redirect(mozwebqa, '/firefox/', '/en-US/firefox/new/', headers)

    @pytest.mark.nondestructive
    def test_redirect_esr_firefox_using_en_US(self, mozwebqa):
        headers = {}
        headers.update(self.ESR_FIREFOX)
        headers.update(self.ACCEPT_LANGUAGE)
        self._test_redirect(mozwebqa, '/firefox/', '/firefox/new/', headers)

    @pytest.mark.nondestructive
    def test_redirect_non_firefox(self, mozwebqa):
        headers = {}
        headers.update(self.NON_FIREFOX)
        headers.update(self.ACCEPT_LANGUAGE)
        self._test_redirect(mozwebqa, '/firefox/', '/en-US/firefox/new/', headers)

    @pytest.mark.nondestructive
    def test_redirect_mobile_using_en_US(self, mozwebqa):
        headers = {}
        headers.update(self.ACCEPT_LANGUAGE)
        headers.update(self.MOBILE)
        self._test_redirect(mozwebqa, '/firefox/', '/firefox/new/', headers)

    @pytest.mark.nondestructive
    def test_redirect_firefox_using_locale(self, mozwebqa, path='/firefox/'):
        headers = {}
        headers.update(self.FIREFOX)
        for locale in self.LOCALES:
            headers.update(self.ACCEPT_LANGUAGE)
            url = mozwebqa.base_url + path
            response = requests.get(url, headers=headers)
            assert '/firefox/fx/' or '/firefox/new/' in response.url

    @pytest.mark.nondestructive
    def test_redirect_mobile_using_locale(self, mozwebqa):
        headers = {}
        headers.update(self.MOBILE)
        for locale in self.LOCALES:
            headers.update(self.ACCEPT_LANGUAGE)
            self._test_redirect(mozwebqa, '/firefox/', '/firefox/new/', headers)

    @pytest.mark.nondestructive
    def test_redirect_esr_firefox_using_locale(self, mozwebqa):
        headers = {}
        headers.update(self.ESR_FIREFOX)
        for locale in self.LOCALES:
            if locale in ['zu', 'ak', 'lg', 'mai']:
                self.ACCEPT_LANGUAGE['Accept-Language'] = locale
                headers.update(self.ACCEPT_LANGUAGE)
                self._test_redirect(mozwebqa, '/firefox/', '/firefox/new/', headers)
            elif locale == 'mn':
                self.ACCEPT_LANGUAGE['Accept-Language'] = locale
                headers.update(self.ACCEPT_LANGUAGE)
                self._test_redirect(mozwebqa, '/firefox/', '/firefox/channel/', headers)
            elif locale in ["ja", "zh-TW"]:
                self.ACCEPT_LANGUAGE['Accept-Language'] = locale
                headers.update(self.ACCEPT_LANGUAGE)
                self._test_redirect(mozwebqa, '/firefox/', '/firefox/', headers)
            elif locale == "ko":
                self.ACCEPT_LANGUAGE['Accept-Language'] = locale
                headers.update(self.ACCEPT_LANGUAGE)
                self._test_redirect(mozwebqa, '/firefox/', '/ko/', headers)
            elif locale == "zh-CN":
                self.ACCEPT_LANGUAGE['Accept-Language'] = locale
                headers.update(self.ACCEPT_LANGUAGE)
                self._test_redirect(mozwebqa, '/firefox/', '/', headers)
            else:
                self.ACCEPT_LANGUAGE['Accept-Language'] = locale
                headers.update(self.ACCEPT_LANGUAGE)
                self._test_redirect(mozwebqa, '/firefox/', '/firefox/new/', headers)
