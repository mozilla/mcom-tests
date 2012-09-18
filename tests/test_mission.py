#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.mission import Mission
from unittestzero import Assert


class TestMission:

    @pytest.mark.nondestructive
    def test_major_links_are_correct(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        for link in mission_page.major_links_list:
            url = mission_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))
            Assert.true(mission_page.is_valid_link(url), '%s is not a valid url' % url)
        Assert.true(mission_page.is_video_overlay_visible)

    @pytest.mark.xfail(reason='Bug 790493 - Mozilla 2011 story Theora file is a 404 on Mission page')
    # https://bugzilla.mozilla.org/show_bug.cgi?id=790493
    @pytest.mark.nondestructive
    def test_video_srcs_are_valid(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        for src in mission_page.video_sources_list:
            Assert.true(mission_page.is_valid_link(src), '%s is not a valid url' % src)

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.contains(mission_page.footer.expected_footer_logo_destination,
                        mission_page.footer.footer_logo_destination)
        Assert.contains(mission_page.footer.expected_footer_logo_img,
                        mission_page.footer.footer_logo_img)
        for link in Mission.Footer.footer_links_list:
            url = mission_page.footer.footer_link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.true(mission_page.header.is_tabzilla_panel_visible)
        mission_page.header.toggle_tabzilla_dropdown()
        for link in Mission.Header.tabzilla_links_list:
            url = mission_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))
