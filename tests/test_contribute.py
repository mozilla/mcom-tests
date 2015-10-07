# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from pages.desktop.contribute import Contribute

link_check = pytest.mark.link_check
nondestructive = pytest.mark.nondestructive


class TestContribute:

    @nondestructive
    def test_footer_section(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_links = []
        for link in Contribute.Footer.footer_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @nondestructive
    def test_major_link_destinations_are_correct(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_links = []
        for link in contribute_page.major_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_major_link_urls_are_valid(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_urls = []
        for link in contribute_page.major_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            response_code = contribute_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls
