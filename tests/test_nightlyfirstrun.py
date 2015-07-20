#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert
from pages.desktop.nightlyfirstrun import NightlyFirstRun


link_check = pytest.mark.link_check
nondestructive = pytest.mark.nondestructive


class TestNightlyFirstRun:

    @nondestructive
    def test_footer_link_destinations_are_correct(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        bad_links = []
        for link in NightlyFirstRun.Footer.footer_links_list:
            url = nightly_fr_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @link_check
    @nondestructive
    def test_footer_links_are_valid(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        bad_urls = []
        for link in NightlyFirstRun.Footer.footer_links_list:
            url = nightly_fr_page.link_destination(link.get('locator'))
            response_code = nightly_fr_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad links found: ' % len(bad_urls) + ', '.join(bad_urls))

    @nondestructive
    def test_tabzilla_link_destinations_are_correct(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        Assert.true(nightly_fr_page.header.is_tabzilla_panel_visible)
        nightly_fr_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in NightlyFirstRun.Header.tabzilla_links_list:
            url = nightly_fr_page.link_destination(link.get('locator'))
            if url.find(link.get('url_suffix')) < 1:
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @link_check
    @nondestructive
    def test_tabzilla_links_are_valid(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        Assert.true(nightly_fr_page.header.is_tabzilla_panel_visible)
        nightly_fr_page.header.toggle_tabzilla_dropdown()
        bad_urls = []
        for link in NightlyFirstRun.Header.tabzilla_links_list:
            url = nightly_fr_page.link_destination(link.get('locator'))
            response_code = nightly_fr_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad links found: ' % len(bad_urls) + ', '.join(bad_urls))

    @nondestructive
    def test_tabzilla_links_are_visible(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        Assert.true(nightly_fr_page.header.is_tabzilla_panel_visible)
        nightly_fr_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in nightly_fr_page.header.tabzilla_links_list:
            if not nightly_fr_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @nondestructive
    def test_are_sections_visible(self, mozwebqa):
        nightly_fr_page = NightlyFirstRun(mozwebqa)
        nightly_fr_page.go_to_page()
        Assert.true(nightly_fr_page.is_test_section_visible)
        Assert.true(nightly_fr_page.is_code_section_visible)
        Assert.true(nightly_fr_page.is_localize_section_visible)
        Assert.true(nightly_fr_page.is_nightly_badge_visible)
        Assert.true(nightly_fr_page.is_code_button_visible)
        Assert.true(nightly_fr_page.is_test_button_visible)
        Assert.true(nightly_fr_page.is_localize_button_visible)
