# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from bs4 import BeautifulSoup
import pytest
import requests


class TestNotes:

    @pytest.mark.link_check
    @pytest.mark.nondestructive
    def test_that_all_links_are_valid(self, base_url):
        bad_urls = []
        r = requests.get('{0}/en-US/firefox/notes'.format(base_url))
        for link in BeautifulSoup(r.content, 'html.parser').findAll('a'):
            # see both blog.mozilla.com and blog.mozilla.org domains
            if 'blog.mozilla.' in link['href']:
                # skip for issue 408: blog.m.o links not working via jenkins
                continue
            url = self.make_absolute(link['href'], base_url)
            r = requests.get(url, verify=False, allow_redirects=True)
            if requests.codes.ok != r.status_code:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, r.status_code))
        assert [] == bad_urls

    def make_absolute(self, url, base_url):
        url = url.strip(" ")
        if url.startswith('http'):
            return url
        elif url.startswith('//'):
            return 'http:' + url

        return base_url + url
