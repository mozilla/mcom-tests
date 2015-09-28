#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.partners import Partners

nondestructive = pytest.mark.nondestructive


class TestPartners(object):

    @nondestructive
    def test_footer_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        bad_links = []
        for link in Partners.Footer.footer_links_list:
            url = partners_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @nondestructive
    def test_overview_section_image(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.selenium.maximize_window()
        partners_page.go_to_page()
        assert partners_page.is_phone_overlay_visible

    @nondestructive
    def test_os_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        partners_page.click_os_menu()
        partners_page.click_operators_button()
