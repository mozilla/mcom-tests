#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import requests
import pytest

xfail = pytest.mark.xfail


@pytest.mark.skip_selenium
class TestRedirects(object):

    def test_redirects_from_mozilla_dot_com(self, mozwebqa):
        url = mozwebqa.base_url
        response = requests.get(url)
        Assert.contains(url, response.url)

    def test_fennec_redirects_to_mobile(self, mozwebqa):
        url = mozwebqa.base_url + "/fennec"
        response = requests.get(url)
        result = mozwebqa.base_url + "en-US/mobile/"
        Assert.equal(result, response.url)

    def test_firefox_mobile_redirects_to_mobile(self, mozwebqa):
        url = mozwebqa.base_url + "/firefox/mobile"
        response = requests.get(url)
        result = mozwebqa.base_url + "en-US/mobile/"
        Assert.equal(result, response.url)

    def test_aurora_redirects_to_firefox_aurora(self, mozwebqa):
        url = mozwebqa.base_url + "/aurora"
        response = requests.get(url)
        result = mozwebqa.base_url + "en-US/firefox/aurora/"
        Assert.equal(result, response.url)

    def test_redirect_to_trailing_slash(self, mozwebqa):
        url = mozwebqa.base_url + "/community"
        response = requests.get(url)
        result = mozwebqa.base_url + "community/"
        Assert.equal(result, response.url)
