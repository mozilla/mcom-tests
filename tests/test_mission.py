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
    @pytest.mark.xfail(reason="https://bugzilla.mozilla.org/show_bug.cgi?id=773787")
    def test_footer_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.contains(mission_page.footer.expected_footer_logo_destination,
            mission_page.footer.footer_logo_destination)
        Assert.contains(mission_page.footer.expected_footer_logo_img,
            mission_page.footer.footer_logo_img)
        for link in Mission.Footer.footer_links_list:
            Assert.contains(link.get('href'), mission_page.footer.footer_link_destination(link.get('text')))

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.true(mission_page.header.is_tabzilla_panel_visible)
        mission_page.header.toggle_tabzilla_dropdown()
        Assert.true(mission_page.header.are_tabzilla_links_visible)
