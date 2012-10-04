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
        Assert.contains(b2g_page.footer.expected_footer_logo_destination,
                        b2g_page.footer.footer_logo_destination)
        Assert.contains(b2g_page.footer.expected_footer_logo_img,
                        b2g_page.footer.footer_logo_img)
        for link in BootToGecko.Footer.footer_links_list:
            url = b2g_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        Assert.true(b2g_page.header.is_tabzilla_panel_visible)
        b2g_page.header.toggle_tabzilla_dropdown()
        for link in BootToGecko.Header.tabzilla_links_list:
            url = b2g_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_headings_are_present(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        Assert.true(b2g_page.is_firefox_os_header_visible)
        Assert.true(b2g_page.is_welcome_section_visible)
        Assert.true(b2g_page.is_developer_opportunities_header_visible)
        Assert.true(b2g_page.is_customizations_for_oems_header_visible)
        Assert.true(b2g_page.is_consumer_freedom_header_visible)
        Assert.true(b2g_page.is_new_web_standards_header_visible)
        Assert.true(b2g_page.is_freedom_platforms_header_visible)

    @pytest.mark.nondestructive
    def test_navbar_links_are_correct(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        for link in b2g_page.b2g_nav_links_list:
            url = b2g_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))
            Assert.true(b2g_page.is_valid_link(url), '%s is not a valid url.' % url)

    @pytest.mark.nondestructive
    def test_images_are_correct(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        for image in b2g_page.images_list:
            src = b2g_page.image_source(image.get('locator'))
            Assert.true(src.endswith(image.get('img_name_suffix')),
                        '%s does not end with %s' % (src, image.get('img_name_suffix')))
            Assert.true(b2g_page.is_valid_link(src), '%s is not a valid url' % src)
