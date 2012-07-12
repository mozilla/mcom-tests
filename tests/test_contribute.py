#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.contribute import Contribute
from unittestzero import Assert


class TestContribute:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        # Assert.contains(contribute_page.footer.expected_footer_logo_destination,
        #     contribute_page.footer.footer_logo_destination)
        Assert.contains(contribute_page.footer.expected_footer_logo_img,
            contribute_page.footer.footer_logo_img)
        for link in Contribute.Footer.footer_links_list:
            Assert.contains(link.get('href'), contribute_page.footer.footer_link_destination(link.get('text')))

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        Assert.true(contribute_page.header.is_tabzilla_panel_visible)
        contribute_page.header.toggle_tabzilla_dropdown()
        Assert.true(contribute_page.header.are_tabzilla_links_visible)
