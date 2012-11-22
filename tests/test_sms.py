#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.sms import SMS


class TestSMSPage():

    @pytest.mark.nondestructive
    def test_send_sms(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        Assert.true(sms_page.is_google_play_link_visible)
        Assert.true(sms_page.is_textbox_visible)
        Assert.true(sms_page.submit_sms_form())

    @pytest.mark.nondestructive
    def test_info_links_are_visible(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        bad_links = []
        for link in sms_page.info_links_list:
            if not sms_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_info_link_destinations_are_correct(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        bad_links = []
        for link in sms_page.info_links_list:
            url = sms_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_info_link_urls_are_valid(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        bad_urls = []
        for link in sms_page.info_links_list:
            url = sms_page.link_destination(link.get('locator'))
            if not sms_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        Assert.contains(sms_page.footer.expected_footer_logo_destination,
                        sms_page.footer.footer_logo_destination)
        Assert.contains(sms_page.footer.expected_footer_logo_img,
                        sms_page.footer.footer_logo_img)
        bad_links = []
        for link in sms_page.Footer.footer_links_list:
            url = sms_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        Assert.true(sms_page.header.is_tabzilla_panel_visible)
        sms_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in sms_page.Header.tabzilla_links_list:
            url = sms_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
