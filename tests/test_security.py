#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.security import Security
from unittestzero import Assert


class TestSecurity:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.contains(security_page.footer.expected_footer_logo_destination,
                        security_page.footer.footer_logo_destination)
        Assert.contains(security_page.footer.expected_footer_logo_img,
                        security_page.footer.footer_logo_img)
        for link in Security.Footer.footer_links_list:
            url = security_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.header.is_tabzilla_panel_visible)
        security_page.header.toggle_tabzilla_dropdown()
        for link in Security.Header.tabzilla_links_list:
            url = security_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_download_button_section(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.downloadRegion.is_download_link_visible)
        Assert.true(security_page.downloadRegion.are_secondary_links_visible)

    @pytest.mark.nondestructive
    def test_are_menus_visible(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.are_menus_visible)

    @pytest.mark.nondestructive
    def test_are_screenshots_visible(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.are_screenshots_visible)
