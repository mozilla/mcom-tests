#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.partners import Partners
from unittestzero import Assert

@pytest.mark.xfail(reason='bug 745033')
class TestPartners:

    @pytest.mark.nondestructive
    @pytest.mark.bedrock
    def test_footer_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        Assert.contains(partners_page.footer.expected_footer_logo_destination,
                        partners_page.footer.footer_logo_destination)
        Assert.contains(partners_page.footer.expected_footer_logo_img,
                        partners_page.footer.footer_logo_img)
        bad_links = []
        for link in Partners.Footer.footer_links_list:
            url = partners_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        Assert.true(partners_page.header.is_tabzilla_panel_visible)
        partners_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Partners.Header.tabzilla_links_list:
            url = partners_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_links_are_visible(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        bad_links = []
        for link in partners_page.billboard_links_list:
            if not partners_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_destinations_are_correct(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        bad_links = []
        for link in partners_page.billboard_links_list:
            url = partners_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_urls_are_valid(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        bad_urls = []
        for link in partners_page.billboard_links_list:
            url = partners_page.link_destination(link.get('locator'))
            if not partners_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_mdn_apps_link_destination_is_correct(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        url = partners_page.mdn_apps_link_destination
        Assert.contains('developer.mozilla.org', url)
        Assert.contains('/apps', url)
        Assert.true(partners_page.is_valid_link(url), '%s is not a valid url' % url)

    @pytest.mark.nondestructive
    def test_partner_images_are_present(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        Assert.true(partners_page.is_opening_soon_image_visible)
        Assert.true(partners_page.are_pointer_images_visible)
