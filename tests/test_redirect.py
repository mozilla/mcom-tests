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
        if origin.startswith('http'):
            url = origin
        else:
            url = mozwebqa.base_url + origin
        response = requests.get(url)
        if final.startswith('http'):
            result = final
        else:
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

    @pytest.mark.nondestructive
    def test_rhino_docs_redirect(self, mozwebqa):
        origin = mozwebqa.base_url + '/rhino/doc.html'
        result = 'https://developer.mozilla.org/en-US/docs/Rhino_documentation'
        self._test_get_redirect(mozwebqa, origin, result)

    @pytest.mark.nondestructive
    def test_rhino_download_redirect(self, mozwebqa):
        origin = mozwebqa.base_url + '/rhino/download.html'
        result = \
            'https://developer.mozilla.org/en-US/docs/Rhino/Download_Rhino?redirectlocale=en-US&redirectslug=RhinoDownload'
        self._test_get_redirect(mozwebqa, origin, result)

    @pytest.mark.nondestructive
    def test_rhino_redirect(self, mozwebqa):
        origin = mozwebqa.base_url + '/rhino/'
        result = \
            'https://developer.mozilla.org/en-US/docs/Rhino'
        self._test_get_redirect(mozwebqa, origin, result)

    @pytest.mark.nondestructive
    def test_redirect_firefox_home_the_product(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
                                "/mobile/home/",
                                "/en-US/mobile/")
        self._test_get_redirect(mozwebqa,
                                "/fr/mobile/home/",
                                "/fr/mobile/")

    @pytest.mark.nondestructive
    def test_notes_redirects_to_firefox_notes(self, mozwebqa):
        url = mozwebqa.base_url + "/firefox/notes/"
        response = requests.get(url)
        Assert.contains("/firefox/", response.url)
        Assert.contains("/releasenotes/", response.url)

    @pytest.mark.nondestructive
    def test_all_older_redirect(self, mozwebqa):
        url = mozwebqa.base_url + "/firefox/all-older.html"
        response = requests.get(url)
        Assert.contains("/firefox/new", response.url)
