#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from pages.desktop.mozillabased import MozillaBasedPage

link_check = pytest.mark.link_check
nondestructive = pytest.mark.nondestructive


class TestMozillaBasedPagePage:

    @nondestructive
    def test_breadcrumbs_link_destinations_are_correct(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.breadcrumbs_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_breadcrumbs_link_urls_are_valid(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_urls = []
        for link in mozillabased_page.breadcrumbs_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            response_code = mozillabased_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @nondestructive
    def test_main_feature_link_destinations_are_correct(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.main_feature_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_main_feature_link_urls_are_valid(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_urls = []
        for link in mozillabased_page.main_feature_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            response_code = mozillabased_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @nondestructive
    def test_featured_billboard_images_links_are_correct(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        bad_links = []
        links = page.get_billboard_product_list
        for link in links:
            response = requests.get(link['logo'])
            status = response.status_code
            if status > 400:
                bad_links.append('Broken logo %s  product %s' % (link['logo'], link['text']))
        assert [] == bad_links

    @nondestructive
    def test_featured_images_links_are_correct(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        bad_links = []
        links = page.get_product_list
        for link in links:
            response = requests.get(link['logo'])
            status = response.status_code
            if status > 400:
                bad_links.append('Broken logo %s  product %s' % (link['logo'], link['text']))
        assert [] == bad_links

    @nondestructive
    def test_footer_section_links(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        bad_links = []
        for link in MozillaBasedPage.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @nondestructive
    def test_navbar_links_are_visible(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        bad_links = []
        for link in page.Header.nav_links_list:
            if not page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        assert [] == bad_links
