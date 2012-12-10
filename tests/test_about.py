#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.about import AboutPage


class TestAboutPage:

    @pytest.mark.nondestructive
    def test_footer_section_links_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.contains(about_page.footer.expected_footer_logo_destination,
                        about_page.footer.footer_logo_destination)
        Assert.contains(about_page.footer.expected_footer_logo_img,
                        about_page.footer.footer_logo_img)
        about_page.are_links_correct(about_page.Footer.footer_links_list)

    @pytest.mark.nondestructive
    def test_footer_section_links_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.contains(about_page.footer.expected_footer_logo_destination,
                        about_page.footer.footer_logo_destination)
        Assert.contains(about_page.footer.expected_footer_logo_img,
                        about_page.footer.footer_logo_img)
        about_page.are_links_valid(about_page.Footer.footer_links_list)

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        about_page.are_links_correct(about_page.Header.tabzilla_links_list)

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        about_page.are_links_valid(about_page.Header.tabzilla_links_list)

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        about_page.are_links_visible(about_page.Header.tabzilla_links_list)

    @pytest.mark.nondestructive
    def test_navbar_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.are_links_visible(about_page.Header.nav_links_list)

    @pytest.mark.nondestructive
    def test_navbar_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.are_links_correct(about_page.Header.nav_links_list)

    @pytest.mark.nondestructive
    def test_navbar_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.are_links_valid(about_page.Header.nav_links_list)

    @pytest.mark.nondestructive
    def test_major_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.are_links_visible(about_page.major_links_list)

    @pytest.mark.nondestructive
    def test_major_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.are_links_correct(about_page.major_links_list)

    @pytest.mark.nondestructive
    def test_major_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.are_links_valid(about_page.major_links_list)