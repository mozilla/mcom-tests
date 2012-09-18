#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.performance import Performance
import pytest


class TestPerformance:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        performance_page = Performance(mozwebqa)
        performance_page.go_to_page()
        Assert.contains(performance_page.footer.expected_footer_logo_destination,
                        performance_page.footer.footer_logo_destination)
        Assert.contains(performance_page.footer.expected_footer_logo_img,
                        performance_page.footer.footer_logo_img)
        for link in Performance.Footer.footer_links_list:
            url = performance_page.footer.footer_link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')))
            Assert.true(performance_page.is_valid_link(url))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        performance_page = Performance(mozwebqa)
        performance_page.go_to_page()
        Assert.true(performance_page.header.is_tabzilla_panel_visible)
        performance_page.header.toggle_tabzilla_dropdown()
        for link in Performance.Header.tabzilla_links_list:
            url = performance_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

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
