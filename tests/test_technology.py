#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero_soft import SoftAsserter
from unittestzero import Assert

from pages.desktop.technology import Technology


class TestTechnologyPage:

    def setup_method(self, method):
        """
        Runs before each test execution, creating an instance of SoftAsserter
        """
        self.asserter = SoftAsserter()

    def teardown_method(self, method):
        """
        Runs at the end of each test execution, reporting the summary of failures
        """
        self.asserter.summarize()

    @pytest.mark.nondestructive
    def test_billboard_links_are_visible(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        for link in technology_page.billboard_links_list:
            self.asserter.true(technology_page.is_element_visible(*link.get('locator')), 'The link at %s is not visible' % link.get('locator')[1:])

    @pytest.mark.nondestructive
    def test_billboard_link_destinations_are_correct(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        for link in technology_page.billboard_links_list:
            url = technology_page.link_destination(link.get('locator'))
            self.asserter.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_billboard_link_urls_are_valid(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        for link in technology_page.billboard_links_list:
            url = technology_page.link_destination(link.get('locator'))
            self.asserter.true(technology_page.is_valid_link(url), '%s is not a valid url' % url)

    @pytest.mark.nondestructive
    def test_more_info_links_are_visible(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        for link in technology_page.more_info_links_list:
            self.asserter.true(technology_page.is_element_visible(*link.get('locator')), 'The link at %s is not visible' % link.get('locator')[1:])

    @pytest.mark.nondestructive
    def test_more_info_link_destinations_are_correct(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        for link in technology_page.more_info_links_list:
            url = technology_page.link_destination(link.get('locator'))
            self.asserter.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_more_info_link_urls_are_valid(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        for link in technology_page.more_info_links_list:
            url = technology_page.link_destination(link.get('locator'))
            self.asserter.true(technology_page.is_valid_link(url), '%s is not a valid url' % url)

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        Assert.contains(technology_page.footer.expected_footer_logo_destination,
                        technology_page.footer.footer_logo_destination)
        Assert.contains(technology_page.footer.expected_footer_logo_img,
                        technology_page.footer.footer_logo_img)
        for link in Technology.Footer.footer_links_list:
            url = technology_page.link_destination(link.get('locator'))
            self.asserter.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        Assert.true(technology_page.header.is_tabzilla_panel_visible)
        technology_page.header.toggle_tabzilla_dropdown()
        for link in Technology.Header.tabzilla_links_list:
            url = technology_page.link_destination(link.get('locator'))
            self.asserter.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_download_button_section(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        Assert.true(technology_page.downloadRegion.is_download_link_visible)
        Assert.true(technology_page.downloadRegion.are_secondary_links_visible)
