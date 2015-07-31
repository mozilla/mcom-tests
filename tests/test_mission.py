#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from pages.desktop.mission import Mission
from unittestzero import Assert

link_check = pytest.mark.link_check
nondestructive = pytest.mark.nondestructive


class TestMission:

    @nondestructive
    def test_major_link_destinations_are_correct(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        bad_links = []
        for link in mission_page.major_links_list:
            url = mission_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @link_check
    @nondestructive
    def test_major_link_urls_are_valid(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        bad_urls = []
        for link in mission_page.major_links_list:
            url = mission_page.link_destination(link.get('locator'))
            response_code = mission_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @link_check
    @nondestructive
    def test_video_srcs_are_valid(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        bad_srcs = []
        for src in mission_page.video_sources_list:
            response_code = mission_page.get_response_code(src)
            if response_code != requests.codes.ok:
                bad_srcs.append('%s is not a valid url - status code: %s.' % (src, response_code))
        Assert.equal(0, len(bad_srcs), '%s bad urls found: ' % len(bad_srcs) + ', '.join(bad_srcs))

    @nondestructive
    def test_footer_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        bad_links = []
        for link in Mission.Footer.footer_links_list:
            url = mission_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
