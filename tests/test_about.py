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
        Assert.contains(about_page.footer.expected_footer_logo_img,
                        about_page.footer.footer_logo_img)
        Assert.contains(about_page.footer.expected_footer_logo_destination,
                        about_page.footer.footer_logo_destination)
        for link in AboutPage.Footer.footer_links_list:
            url = about_page.footer.footer_link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))
            # Note we are only doing this valid link checking in this test as each page
            # has the same links
            Assert.true(about_page.is_valid_link(url), '%s is not a valid url.' % url)

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        for link in AboutPage.Header.tabzilla_links_list:
            url = about_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))
            # Note we are only doing this valid link checking in this test as each page
            # has the same links
            Assert.true(about_page.is_valid_link(url), '%s is not a valid url.' % url)

    @pytest.mark.nondestructive
    def test_navbar_links_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        for link in AboutPage.Header.nav_links_list:
            url = about_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))
            Assert.true(about_page.is_valid_link(url), '%s is not a valid url.' % url)

    @pytest.mark.nondestructive
    def test_major_links_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        for link in AboutPage.major_links_list:
            url = about_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))
            Assert.true(about_page.is_valid_link(url), '%s is not a valid url' % url)
