#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.about import AboutPage
from unittestzero import Assert


class TestAboutPage:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.footer.are_footer_links_visible)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        Assert.true(about_page.header.are_tabzilla_links_visible)

    @pytest.mark.nondestructive
    def test_navbars_and_headings(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.are_nav_links_present)

    @pytest.mark.nondestructive
    def test_major_links(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.are_major_links_present)
