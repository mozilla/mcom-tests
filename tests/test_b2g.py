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
        bad_links = []
        for link in BootToGecko.Footer.footer_links_list:
            url = b2g_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        Assert.true(b2g_page.header.is_tabzilla_panel_visible)
        b2g_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in BootToGecko.Header.tabzilla_links_list:
            url = b2g_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

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
    def test_nav_links_are_visible(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        bad_links = []
        for link in b2g_page.b2g_nav_links_list:
            if not b2g_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_nav_link_destinations_are_correct(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        bad_links = []
        for link in b2g_page.b2g_nav_links_list:
            url = b2g_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_nav_link_urls_are_valid(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        bad_urls = []
        for link in b2g_page.b2g_nav_links_list:
            url = b2g_page.link_destination(link.get('locator'))
            if not b2g_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_images_are_visible(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        bad_images = []
        for image in b2g_page.images_list:
            if not b2g_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_images_are_correct(self, mozwebqa):
        b2g_page = BootToGecko(mozwebqa)
        b2g_page.go_to_page()
        bad_images = []
        for image in b2g_page.images_list:
            src = b2g_page.image_source(image.get('locator'))
            if not src.endswith(image.get('img_name_suffix')):
                bad_images.append('%s does not end with %s' % (src, image.get('img_name_suffix')))
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))
