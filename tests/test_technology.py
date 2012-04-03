#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

from pages.desktop.technology_page import TechnologyPage
from unittestzero import Assert


class TestTechnologyPage:

    def test_header_section_present(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()
        technology_page.toggle_tabzilla_dropdown()
        Assert.equal(technology_page.are_tabzilla_links_present, True)

    def test_footer_section_present(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()
        Assert.equal(technology_page.are_footer_links_present, True)

    def test_billoard_links_are_present(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()
        Assert.equal(technology_page.are_billboard_links_present, True)
