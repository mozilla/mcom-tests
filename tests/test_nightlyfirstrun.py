# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from pages.desktop.nightlyfirstrun import NightlyFirstRun


link_check = pytest.mark.link_check
nondestructive = pytest.mark.nondestructive


class TestNightlyFirstRun:

    @nondestructive
    def test_footer_link_destinations_are_correct(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        bad_links = []
        for link in NightlyFirstRun.Footer.footer_links_list:
            url = nightly_fr_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_footer_links_are_valid(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        bad_urls = []
        for link in NightlyFirstRun.Footer.footer_links_list:
            url = nightly_fr_page.link_destination(link.get('locator'))
            response_code = nightly_fr_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @nondestructive
    def test_are_sections_visible(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        assert nightly_fr_page.is_test_section_visible
        assert nightly_fr_page.is_code_section_visible
        assert nightly_fr_page.is_localize_section_visible
        assert nightly_fr_page.is_nightly_badge_visible
        assert nightly_fr_page.is_code_button_visible
        assert nightly_fr_page.is_test_button_visible
        assert nightly_fr_page.is_localize_button_visible
