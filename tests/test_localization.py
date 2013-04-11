#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from BeautifulSoup import BeautifulStoneSoup
from unittestzero import Assert


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class TestLocalizations:

    def test_that_download_links_return_302(self, mozwebqa):
        '''
            Check that download links return a status 302.
        '''
        url = "%s/firefox/all.html" % mozwebqa.base_url
        page_response = requests.get(url)
        html = BeautifulStoneSoup(page_response.content)
        bad_links = []
        language_rows = html.findAll('tr', id=True)
        for language in language_rows:
            links = language.findAll('a')
            for link in links:
                url = link['href']
                response = requests.head(url, allow_redirects=False)
                status = response.status_code
                if not (300 < status <= 302):
                    bad_links.append("Lang '%s' %s link: status %s"
                                     % (language['id'], link['href'], status))
        Assert.equal(0, len(bad_links),
                     "Expected status code 302.  " + ",  ".join(bad_links))
