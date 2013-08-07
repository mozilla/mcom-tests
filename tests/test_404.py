#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
import requests
from unittestzero import Assert


@pytest.mark.skip_selenium
class TestStatus(object):

    @pytest.mark.nondestructive
    @pytest.mark.nonbedrock
    def test_status_code_returns_404(self, mozwebqa):
        url = mozwebqa.base_url + '/abck'
        response = requests.get(url)
        Assert.equal(response.status_code, 404)

    @pytest.mark.xfail(reason='Bug 744671 - x-robots-tag header not set after redirect')
    @pytest.mark.nondestructive
    def test_xrobots_tag_is_present(self, mozwebqa):
        """Test for X-Robots-Tag header"""
        url = mozwebqa.base_url
        response = requests.get(url)
        Assert.contains('x-robots-tag', response.headers.keys())
        Assert.contains('noodp', response.headers.values())
