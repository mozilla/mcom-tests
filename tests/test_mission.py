#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.mission import Mission
from unittestzero import Assert


class TestMission:

    @pytest.mark.nondestructive
    def test_midpage_links(self, mozwebqa):
        missionPage = Mission(mozwebqa)
        missionPage.go_to_page()
        Assert.true(missionPage.are_midpage_links_visible)
        Assert.true(missionPage.is_video_visible)

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
