#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.about import AboutPage


class TestAboutPage:

    @pytest.mark.nondestructive
    @pytest.mark.xfail(reason="https://bugzilla.mozilla.org/show_bug.cgi?id=773787")
    def test_footer_section(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        for link in AboutPage.Footer.footer_links_list:
            url = about_page.footer.footer_link_destination(link.get('text'))
            Assert.contains(link.get('href'), url)
            # the next line only exists for this page, to be a representative sample
            Assert.equal(about_page.get_response_code(url), 200)
        Assert.contains(about_page.footer.expected_footer_logo_img,
            about_page.footer.footer_logo_img)
        Assert.contains(about_page.footer.expected_footer_logo_destination,
            about_page.footer.footer_logo_destination)

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
