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
        Assert.contains(contribute_page.footer.expected_footer_logo_destination,
                        contribute_page.footer.footer_logo_destination)
        Assert.contains(contribute_page.footer.expected_footer_logo_img,
                        contribute_page.footer.footer_logo_img)
        for link in Contribute.Footer.footer_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        Assert.true(contribute_page.header.is_tabzilla_panel_visible)
        contribute_page.header.toggle_tabzilla_dropdown()
        for link in Contribute.Header.tabzilla_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))
