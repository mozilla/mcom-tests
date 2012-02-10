#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium import selenium
from unittestzero import Assert
from pages.desktop.technology import TechnologyPage


class TestTechnology:

    def test_technology_icons(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        technology_pg = TechnologyPage(mozwebqa)
        technology_pg.open("/firefox/technology/")
        Assert.true(technology_pg.innovation_button)
        Assert.true(technology_pg.css_button)
        Assert.true(technology_pg.api_button)
        Assert.true(technology_pg.dev_button)
        Assert.true(technology_pg.svg_button)
        Assert.true(technology_pg.security_button)
        Assert.true(technology_pg.rollover_button)

    def test_all_sections(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        technology_pg = TechnologyPage(mozwebqa)
        technology_pg.open("/firefox/technology/")
        Assert.true(technology_pg.html5_section)
        Assert.true(technology_pg.css_section)
        Assert.true(technology_pg.api_section)
        Assert.true(technology_pg.tools_section)
        Assert.true(technology_pg.svg_section)
        Assert.true(technology_pg.security_section)

    def test_html_sections(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        technology_pg = TechnologyPage(mozwebqa)
        technology_pg.open("/firefox/technology/")
        Assert.true(technology_pg.forms)
        Assert.true(technology_pg.parser)
        Assert.true(technology_pg.webm)
