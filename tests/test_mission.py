#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.mission import Mission
from unittestzero import Assert


class TestMission:

    @pytest.mark.nondestructive
    def test_major_links_are_visible(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        bad_links = []
        for link in mission_page.major_links_list:
            if not mission_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(mission_page.is_video_overlay_visible)

    @pytest.mark.nondestructive
    def test_major_link_destinations_are_correct(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        bad_links = []
        for link in mission_page.major_links_list:
            url = mission_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_major_link_urls_are_valid(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        bad_urls = []
        for link in mission_page.major_links_list:
            url = mission_page.link_destination(link.get('locator'))
            if not mission_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_video_srcs_are_valid(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        bad_srcs = []
        for src in mission_page.video_sources_list:
            if not mission_page.is_valid_link(src):
                bad_srcs.append('%s is not a valid url' % src)
        Assert.equal(0, len(bad_srcs), '%s bad urls found: ' % len(bad_srcs) + ', '.join(bad_srcs))

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.contains(mission_page.footer.expected_footer_logo_destination,
                        mission_page.footer.footer_logo_destination)
        Assert.contains(mission_page.footer.expected_footer_logo_img,
                        mission_page.footer.footer_logo_img)
        bad_links = []
        for link in Mission.Footer.footer_links_list:
            url = mission_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.true(mission_page.header.is_tabzilla_panel_visible)
        mission_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Mission.Header.tabzilla_links_list:
            url = mission_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
