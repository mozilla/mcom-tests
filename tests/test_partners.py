#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.partners import Partners
from unittestzero import Assert


class TestPartners:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
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
            if url.find(link.get('url_suffix')) < 1:
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_partner_images_pager_one(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        bad_images = []
        Assert.true(partners_page.is_partner_with_us_button_visible)
        partners_page.click_partner_page_one_button()
        for image in partners_page.partner_images_pager_list_one:
            if not partners_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_partner_images_pager_two(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        bad_images = []
        Assert.true(partners_page.is_partner_with_us_button_visible)
        for image in partners_page.partner_images_pager_list_two:
            partners_page.click_partner_pager_button()
            partners_page.click_partner_pager_button()
            partners_page.click_partner_pager_button()
            partners_page.click_partner_pager_button()  # click the button a couple of times to override auto pager
            if not partners_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_overview_section_image(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.selenium.maximize_window()
        partners_page.go_to_page()
        Assert.true(partners_page.is_phone_overlay_visible)

    @pytest.mark.nondestructive
    def test_os_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        partners_page.click_os_menu()
        partners_page.click_operators_button()
        bad_images = []
        for image in partners_page._operators_image_list:
            if not partners_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))
