#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.dnt import DoNotTrack
from unittestzero import Assert


class TestDoNotTrack:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        dnt_page = DoNotTrack(mozwebqa)
        dnt_page.go_to_page()
        bad_links = []
        for link in DoNotTrack.Footer.footer_links_list:
            url = dnt_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        dnt_page = DoNotTrack(mozwebqa)
        dnt_page.go_to_page()
        Assert.true(dnt_page.header.is_tabzilla_panel_visible)
        dnt_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in DoNotTrack.Header.tabzilla_links_list:
            url = dnt_page.link_destination(link.get('locator'))
            if url.find(link.get('url_suffix')) < 1:
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_status_section(self, mozwebqa):
        dnt_page = DoNotTrack(mozwebqa)
        dnt_page.go_to_page()
        Assert.true(dnt_page.is_status_wrapper_visible)
        Assert.true(dnt_page.is_status_text_visible)
        Assert.true(dnt_page.is_enable_dnt_image_visible)
        Assert.true(dnt_page.is_enable_dnt_text_visible)
        bad_links = []
        for link in dnt_page.tracking_protection_links_list:
            url = dnt_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        for link in dnt_page.tracking_protection_links_list:
            Assert.true(dnt_page.are_tracking_protection_links_visible(link.get('locator')))
