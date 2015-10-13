# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests


class TestStatus(object):

    @pytest.mark.nondestructive
    def test_status_code_returns_404(self, base_url):
        r = requests.get('{0}/abck'.format(base_url))
        assert requests.codes.not_found == r.status_code

    @pytest.mark.nondestructive
    def test_xrobots_tag_is_present(self, base_url):
        """Test for X-Robots-Tag header"""
        r = requests.get(base_url)
        assert 'noodp' == r.headers.get('x-robots-tag')
