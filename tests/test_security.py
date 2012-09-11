#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.desktop.security import Security
from tests.base_test import BaseTest


class TestSecurity(BaseTest):

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        self.verify_footer_section(security_page)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.header.is_tabzilla_panel_visible)
        security_page.header.toggle_tabzilla_dropdown()
        Assert.true(security_page.header.are_tabzilla_links_visible)

    @pytest.mark.nondestructive
    def test_download_button_section(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.downloadRegion.is_download_link_visible)
        Assert.true(security_page.downloadRegion.are_secondary_links_visible)

    @pytest.mark.nondestructive
    def test_are_menus_visible(self, mozwebqa):
        security_page = Security(mozwebqa)
        security_page.go_to_page()
        Assert.true(security_page.are_menus_visible)

        @pytest.mark.nondestructive
        def test_are_screenshots_visible(self, mozwebqa):
            security_page = Security(mozwebqa)
            security_page.go_to_page()
            Assert.true(security_page.are_screenshots_visible)
