# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from pages.desktop.nightlyfirstrun import NightlyFirstRun


class TestNightlyFirstRun:

    @pytest.mark.nondestructive
    def test_footer_link_destinations_are_correct(self, base_url, selenium):
        page = NightlyFirstRun(base_url, selenium).open()
        bad_links = []
        for link in NightlyFirstRun.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.link_check
    @pytest.mark.nondestructive
    def test_footer_links_are_valid(self, base_url, selenium):
        page = NightlyFirstRun(base_url, selenium).open()
        bad_urls = []
        for link in NightlyFirstRun.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            response_code = page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @pytest.mark.nondestructive
    def test_are_sections_visible(self, base_url, selenium):
        page = NightlyFirstRun(base_url, selenium).open()
        assert page.is_test_section_visible
        assert page.is_code_section_visible
        assert page.is_localize_section_visible
        assert page.is_nightly_badge_visible
        assert page.is_code_button_visible
        assert page.is_test_button_visible
        assert page.is_localize_button_visible
