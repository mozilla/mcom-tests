#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.desktop.mission import Mission
from tests.base_test import BaseTest


class TestMission(BaseTest):

    @pytest.mark.nondestructive
    def test_midpage_links(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        for link in mission_page.midpage_links_list:
            url = mission_page.midpage_link_href(link)
            Assert.true(mission_page.is_valid_link(url), url + ' did not return a 200 status code.')

    @pytest.mark.xfail(reason='Bug 790493 - One of the video srcs is invalid')
    # https://bugzilla.mozilla.org/show_bug.cgi?id=790493
    @pytest.mark.nondestructive
    def test_video(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.true(mission_page.is_video_visible)
        for src in mission_page.video_srcs:
            Assert.true(mission_page.is_valid_link(src), src + ' did not return a 200 status code.')

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        self.verify_footer_section(mission_page)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        Assert.true(mission_page.header.is_tabzilla_panel_visible)
        mission_page.header.toggle_tabzilla_dropdown()
        Assert.true(mission_page.header.are_tabzilla_links_visible)
