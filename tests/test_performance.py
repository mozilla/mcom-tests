#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
import pytest

from pages.desktop.performance import Performance
from tests.base_test import BaseTest


class TestPerformance(BaseTest):

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        performance_page = Performance(mozwebqa)
        performance_page.go_to_page()
        self.verify_footer_section(performance_page)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        performance_page = Performance(mozwebqa)
        performance_page.go_to_page()
        self.verify_header_section(performance_page)

    @pytest.mark.nondestructive
    def test_download_button_section(self, mozwebqa):
        performance_page = Performance(mozwebqa)
        performance_page.go_to_page()
        Assert.true(performance_page.downloadRegion.is_download_link_visible)
        Assert.true(performance_page.downloadRegion.are_secondary_links_visible)

    @pytest.mark.nondestructive
    def test_performance_icons(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        performance_page = Performance(mozwebqa)
        performance_page.go_to_page()
        Assert.true(performance_page.video_overlay)
        Assert.true(performance_page.perf_web_ico)
        Assert.true(performance_page.perf_hardware_ico)

    @pytest.mark.nondestructive
    def test_performance_images(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        performance_page = Performance(mozwebqa)
        performance_page.go_to_page()
        Assert.true(performance_page.perf_hardware_img)
