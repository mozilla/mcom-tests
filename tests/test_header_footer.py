#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.technology_page import TechnologyPage


class TestHeaderFooter:

    @pytest.mark.xfail("Selenium issue 3492")
    @pytest.mark.nondestructive
    def test_header_section_visible(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()

        technology_page.header.toggle_tabzilla_dropdown()
        Assert.true(technology_page.header.is_tabzilla_panel_visible)
        Assert.true(technology_page.header.is_tabzilla_searchbox_visible)

        technology_page.header.toggle_tabzilla_dropdown()
        Assert.false(technology_page.header.is_tabzilla_panel_visible)

    @pytest.mark.nondestructive
    def test_footer_section_visible(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()
        Assert.true(technology_page.footer.is_visible)
