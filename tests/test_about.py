#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.about import AboutPage

class TestAboutPage:

    @pytest.mark.nondestructive
    @pytest.mark.parametrize('link', AboutPage.Footer.footer_links_list)
    def test_footer_section(self, mozwebqa, link):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.is_link_present(link))

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        Assert.true(about_page.header.are_tabzilla_links_visible)

    @pytest.mark.nondestructive
    @pytest.mark.parametrize('link', AboutPage.nav_links_list)
    def test_navbar_links_are_present(self, mozwebqa, link):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.is_link_present(link))

    @pytest.mark.nondestructive
    @pytest.mark.parametrize('link', AboutPage.major_links_list)
    def test_major_links_are_present(self, mozwebqa, link):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.is_link_present(*link))
