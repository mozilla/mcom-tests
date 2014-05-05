#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from bs4 import BeautifulSoup
from unittestzero import Assert


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class TestLocalisedDownloadLinks:

    def get_language_rows(self, mozwebqa, link='/firefox/all.html'):
        '''
            Get all links for each locale on the page under test.
            The default page under test is /firefox/all.html .
        '''
        url = "%s/%s" % (mozwebqa.base_url, link)
        page_response = requests.get(url)
        html = BeautifulSoup(page_response.content)
        language_rows = html.findAll('tr', id=True)
        return language_rows

    def get_locale_code_from_links(self, mozwebqa, language_rows):
        '''
           Check that bouncer links have the right locale code.
        '''
        bad_links = []
        for language in language_rows:
            links = language.findAll('a')
            for link in links:
                url = link['href']
                response = requests.head(url, allow_redirects=True)
                if language['id'] not in response.url:
                    bad_links.append("Lang '%s' not in response: %s \n"
                                     % (language['id'], response.url))
        return bad_links

    def get_302_response_code_from_links(self, mozwebqa, language_rows):
        '''
            Check that download links return a status 302.
        '''
        bad_links = []
        for language in language_rows:
            links = language.findAll('a')
            for link in links:
                url = link['href']
                response = requests.head(url, allow_redirects=False)
                status = response.status_code
                if not (300 < status <= 302):
                    bad_links.append("Lang '%s' %s link: status %s"
                                     % (language['id'], link['href'], status))
        return bad_links

    def test_links_on_firefox_all(self, mozwebqa):
        language_rows = self.get_language_rows(mozwebqa)
        result = self.get_locale_code_from_links(mozwebqa, language_rows)
        Assert.equal(0, len(result), " ".join(result))
        second_result = self.get_302_response_code_from_links(mozwebqa, language_rows)
        Assert.equal(0, len(second_result),
                     "Expected status code 302.  " + ",  ".join(second_result))

    def test_links_on_firefox_organization_all(self, mozwebqa):
        language_rows = self.get_language_rows(mozwebqa, link='/firefox/organizations/all.html')
        result = self.get_locale_code_from_links(mozwebqa, language_rows)
        Assert.equal(0, len(result), " ".join(result))
        second_result = self.get_302_response_code_from_links(mozwebqa, language_rows)
        Assert.equal(0, len(second_result),
                     "Expected status code 302.  " + ",  ".join(second_result))
