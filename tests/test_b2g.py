#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.b2g import BootToGecko
from unittestzero import Assert


class TestBootToGecko:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        for link in BootToGecko.Footer.footer_links_list:
            Assert.true(b2g_page.is_element_visible(*link), link[1])

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        Assert.true(b2g_page.header.is_tabzilla_panel_visible)
        b2g_page.header.toggle_tabzilla_dropdown()
        Assert.true(b2g_page.header.are_tabzilla_links_visible)

    @pytest.mark.nondestructive
    def test_navbars_and_headings(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        Assert.true(b2g_page.is_about_navbar_visible)
        Assert.true(b2g_page.is_faq_navbar_visible)
        Assert.true(b2g_page.is_mobile_devices_header_visible)
        Assert.true(b2g_page.is_welcome_section_visible)
        Assert.true(b2g_page.is_welcome_section_image_visible)
        Assert.true(b2g_page.is_freedom_platforms_header_visible)
        Assert.true(b2g_page.is_developer_opportunities_header_visible)
        Assert.true(b2g_page.is_customizations_for_oems_header_visible)
        Assert.true(b2g_page.is_more_information_section_visible)

    @pytest.mark.nondestructive
    def test_about_page(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.about_page.go_to_page()
        Assert.true(b2g_page.is_home_navbar_visible)
        Assert.true(b2g_page.is_faq_navbar_visible)
