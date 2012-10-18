#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
import pytest
from pages.desktop.mozillabased import MozillaBasedPage
from unittestzero import Assert


class TestMozillaBasedPagePage:

    @pytest.mark.nondestructive
    def test_product_images_links(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        bad_links = []
        links = page.get_product_list + page.get_billboard_product_list
        for link in links:
            response = requests.get(link['logo'])
            status = response.status_code
            if status > 400:
                bad_links.append('Broken logo %s  product %s' % (link['logo'], link['text']))
        Assert.equal(0, len(bad_links),
            ''.join(bad_links))

    @pytest.mark.nondestructive
    def test_footer_section_links(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        Assert.contains(page.footer.expected_footer_logo_destination,
                        page.footer.footer_logo_destination)
        Assert.contains(page.footer.expected_footer_logo_img,
                        page.footer.footer_logo_img)
        bad_links = []
        for link in MozillaBasedPage.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        Assert.true(page.header.is_tabzilla_panel_visible)
        page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in MozillaBasedPage.Header.tabzilla_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_visible(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        Assert.true(page.header.is_tabzilla_panel_visible)
        page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in page.header.tabzilla_links_list:
            if not page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_navbar_links_are_visible(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        bad_links = []
        for link in page.Header.nav_links_list:
            if not page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
