#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class TestLocalisedDownloadLinks:

    link_check_url = '/firefox/organizations/all.html'

    def test_links_on_firefox_organization_all(self, language_link):
        response = requests.head(language_link['url'], allow_redirects=True, timeout=20)
        Assert.contains(language_link['id'], response.url)
        response = requests.head(language_link['url'], allow_redirects=False, timeout=20)
        Assert.true(300 < response.status_code <= 302,
                    "Lang '%s' %s link: status %s"
                    % (language_link['id'], language_link['url'], response.status_code))
