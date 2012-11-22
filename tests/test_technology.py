#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.desktop.technology import Technology


class TestTechnologyPage:

    @pytest.mark.nondestructive
    def test_billboard_links_are_visible(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        bad_links = []
        for link in technology_page.billboard_links_list:
            if not technology_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_destinations_are_correct(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        bad_links = []
        for link in technology_page.billboard_links_list:
            url = technology_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_urls_are_valid(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        bad_urls = []
        for link in technology_page.billboard_links_list:
            url = technology_page.link_destination(link.get('locator'))
            if not technology_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_more_info_links_are_visible(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        bad_links = []
        for link in technology_page.more_info_links_list:
            if not technology_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_more_info_link_destinations_are_correct(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        bad_links = []
        for link in technology_page.more_info_links_list:
            url = technology_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_more_info_link_urls_are_valid(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        bad_urls = []
        for link in technology_page.more_info_links_list:
            url = technology_page.link_destination(link.get('locator'))
            if not technology_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        Assert.contains(technology_page.footer.expected_footer_logo_destination,
                        technology_page.footer.footer_logo_destination)
        Assert.contains(technology_page.footer.expected_footer_logo_img,
                        technology_page.footer.footer_logo_img)
        bad_links = []
        for link in Technology.Footer.footer_links_list:
            url = technology_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        Assert.true(technology_page.header.is_tabzilla_panel_visible)
        technology_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Technology.Header.tabzilla_links_list:
            url = technology_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_download_button_section(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        Assert.true(technology_page.downloadRegion.is_download_link_visible)
        Assert.true(technology_page.downloadRegion.are_secondary_links_visible)
