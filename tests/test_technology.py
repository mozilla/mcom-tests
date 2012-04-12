#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

import pytest
from unittestzero import Assert

from pages.desktop.technology_page import TechnologyPage


class TestTechnologyPage:

    @pytest.mark.nondestructive
    def test_billboard_links_are_visible(self, mozwebqa):
        technology_page = TechnologyPage(mozwebqa)
        technology_page.go_to_page()

        Assert.true(technology_page.is_developer_tools_link_visible)
        Assert.true(technology_page.is_html5_link_visible)
        Assert.true(technology_page.is_css_link_visible)
        Assert.true(technology_page.is_apis_link_visible)
        Assert.true(technology_page.is_svg_link_visible)
        Assert.true(technology_page.is_security_link_visible)
