#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.privacy import Privacy


class TestPrivacy:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        Assert.contains(privacy_page.footer.expected_footer_logo_destination,
                        privacy_page.footer.footer_logo_destination)
        Assert.contains(privacy_page.footer.expected_footer_logo_img,
                        privacy_page.footer.footer_logo_img)
        bad_links = []
        for link in Privacy.Footer.footer_links_list:
            url = privacy_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        Assert.true(privacy_page.header.is_tabzilla_panel_visible)
        privacy_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Privacy.Header.tabzilla_links_list:
            url = privacy_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_privacy_policy_list(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        bad_links = []
        for link in privacy_page.privacy_policy_list:
            url = privacy_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_page_sections(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        privacy_page.click_principles_section()
        Assert.contains('#principle', privacy_page.url_current_page)
        privacy_page.click_information_section()
        Assert.contains('#your-information', privacy_page.url_current_page)
        privacy_page.click_choices_section()
        Assert.contains('#choices', privacy_page.url_current_page)
        privacy_page.click_share_section()
        Assert.contains('#info-sharing', privacy_page.url_current_page)
        privacy_page.click_back_to_top()
        privacy_page.click_contact_us_section()
        Assert.contains('#contactus', privacy_page.url_current_page)
