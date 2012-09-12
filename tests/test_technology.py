#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.desktop.technology import Technology
from tests.base_test import BaseTest


class TestTechnologyPage(BaseTest):

    @pytest.mark.nondestructive
    def test_billboard_links_are_visible(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        Assert.true(technology_page.is_developer_tools_link_visible)
        Assert.true(technology_page.is_html5_link_visible)
        Assert.true(technology_page.is_css_link_visible)
        Assert.true(technology_page.is_apis_link_visible)
        Assert.true(technology_page.is_svg_link_visible)
        Assert.true(technology_page.is_security_link_visible)

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        self.verify_footer_section(technology_page)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        self.verify_header_section(technology_page)

    @pytest.mark.nondestructive
    def test_download_button_section(self, mozwebqa):
        technology_page = Technology(mozwebqa)
        technology_page.go_to_page()
        Assert.true(technology_page.downloadRegion.is_download_link_visible)
        Assert.true(technology_page.downloadRegion.are_secondary_links_visible)
