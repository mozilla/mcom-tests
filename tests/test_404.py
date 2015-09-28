#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests


nonbedrock = pytest.mark.nonbedrock
nondestructive = pytest.mark.nondestructive
skip_selenium = pytest.mark.skip_selenium


@skip_selenium
class TestStatus(object):

    @nonbedrock
    @nondestructive
    def test_status_code_returns_404(self, mozwebqa):
        url = mozwebqa.base_url + '/abck'
        response = requests.get(url)
        assert requests.codes.not_found == response.status_code

    @nondestructive
    def test_xrobots_tag_is_present(self, mozwebqa):
        """Test for X-Robots-Tag header"""
        url = mozwebqa.base_url
        response = requests.get(url)
        assert 'noodp' == response.headers.get('x-robots-tag')
