#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import requests
import pytest


@pytest.mark.skip_selenium
class TestRedirects(object):
    def _test_get_redirect(self, mozwebqa, origin, final):
        url = mozwebqa.base_url + origin
        response = requests.get(url)
        result = mozwebqa.base_url + final
        Assert.equal(result, response.url)

    @pytest.mark.nondestructive
    def test_redirects_from_mozilla_dot_com(self, mozwebqa):
        url = mozwebqa.base_url
        response = requests.get(url)
        Assert.contains(url, response.url)

    @pytest.mark.nondestructive
    def test_fennec_redirects_to_mobile(self, mozwebqa):
        url = mozwebqa.base_url + "/fennec/"
        response = requests.get(url)
        result = mozwebqa.base_url + "/en-US/mobile/"
        Assert.equal(result, response.url)

    @pytest.mark.nondestructive
    def test_firefox_mobile_redirects_to_mobile(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
            "/firefox/mobile/",
            "/en-US/firefox/fx/")

    @pytest.mark.nondestructive
    def test_aurora_redirects_to_firefox_aurora(self, mozwebqa):
        url = mozwebqa.base_url + "/aurora/"
        response = requests.get(url)
        result = mozwebqa.base_url + "/en-US/firefox/aurora/"
        Assert.equal(result, response.url)

    @pytest.mark.nondestructive
    def test_redirect_to_trailing_slash(self, mozwebqa):
        url = mozwebqa.base_url + "/community/"
        response = requests.get(url)
        result = mozwebqa.base_url + "/community/"
        Assert.equal(result, response.url)

    @pytest.mark.nondestructive
    def test_redirect_firefox_mobile_to_mobile(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
            "/firefox/mobile/releasenotes/",
            "/en-US/mobile/releasenotes/")

    @pytest.mark.nondestructive
    def test_redirect_mobile_to_firefox_mobile(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
            "/mobile/faq/",
            "/en-US/firefox/mobile/faq/")
        self._test_get_redirect(mozwebqa,
            "/mobile/features/",
            "/en-US/firefox/mobile/features/")
        self._test_get_redirect(mozwebqa,
            "/mobile/platforms/",
            "/en-US/firefox/mobile/platforms/")

    @pytest.mark.nondestructive
    def test_redirect_some_m_to_firefox_mobile(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
            "/m/faq/",
            "/en-US/firefox/mobile/faq/")
        self._test_get_redirect(mozwebqa,
            "/m/features/",
            "/en-US/firefox/mobile/features/")
        self._test_get_redirect(mozwebqa,
            "/m/platforms/",
            "/en-US/firefox/mobile/platforms/")

    @pytest.mark.nondestructive
    def test_redirect_m(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
            "/m/",
            "/en-US/firefox/fx/")
