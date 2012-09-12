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
        missionPage = Mission(mozwebqa)
        missionPage.go_to_page()
        Assert.true(missionPage.are_midpage_links_visible)
        Assert.true(missionPage.is_video_visible)

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        self.verify_footer_section(mission_page)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        mission_page = Mission(mozwebqa)
        mission_page.go_to_page()
        self.verify_header_section(mission_page)
