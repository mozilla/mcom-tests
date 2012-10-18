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
        bad_links = []
        for link in Security.Footer.footer_links_list:
            url = security_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.header.is_tabzilla_panel_visible)
        security_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Security.Header.tabzilla_links_list:
            url = security_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_download_button_section(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.downloadRegion.is_download_link_visible)
        Assert.true(security_page.downloadRegion.are_secondary_links_visible)

    @pytest.mark.nondestructive
    def test_billboard_links_are_visible(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_links = []
        for link in security_page.billboard_links_list:
            if not security_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_destinations_are_correct(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_links = []
        for link in security_page.billboard_links_list:
            url = security_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_urls_are_valid(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_urls = []
        for link in security_page.billboard_links_list:
            url = security_page.link_destination(link.get('locator'))
            if not security_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_section_links_are_visible(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_links = []
        for link in security_page.section_links_list:
            if not security_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_section_link_destinations_are_correct(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_links = []
        for link in security_page.section_links_list:
            url = security_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_section_link_urls_are_valid(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_urls = []
        for link in security_page.section_links_list:
            url = security_page.link_destination(link.get('locator'))
            if not security_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_images_are_visible(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_images = []
        for image in security_page.images_list:
            if not security_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_image_srcs_are_correct(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_images = []
        for image in security_page.images_list:
            src = security_page.image_source(image.get('locator'))
            if not image.get('img_name_contains') in src:
                bad_images.append('%s does not contain %s' % (src, image.get('img_name_contains')))
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_images_srcs_are_valid(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        bad_urls = []
        for image in security_page.images_list:
            url = security_page.image_source(image.get('locator'))
            if not security_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))
