#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.about import AboutPage

class TestAboutPage:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        for link in AboutPage.Footer.footer_links_list:
            Assert.true(about_page.is_element_present(*link), link[1])

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        Assert.true(about_page.header.are_tabzilla_links_visible)

    @pytest.mark.nondestructive
    def test_navbar_links_are_present(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        for link in AboutPage.nav_links_list:
            Assert.true(about_page.is_element_present(*link), link[1])

    @pytest.mark.nondestructive
    def test_major_links_are_present(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        for link in AboutPage.major_links_list:
            Assert.true(about_page.is_element_present(*link), link[1])
