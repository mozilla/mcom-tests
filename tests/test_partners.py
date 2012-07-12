#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.partners import Partners
from unittestzero import Assert


class TestPartners:

    @pytest.mark.nondestructive
    @pytest.mark.bedrock
    def test_footer_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        Assert.contains(partners_page.footer.expected_footer_logo_destination,
            partners_page.footer.footer_logo_destination)
        Assert.contains(partners_page.footer.expected_footer_logo_img,
            partners_page.footer.footer_logo_img)
        for link in Partners.Footer.footer_links_list:
            Assert.contains(link.get('href'), partners_page.footer.footer_link_destination(link.get('text')))

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        Assert.true(partners_page.header.is_tabzilla_panel_visible)
        partners_page.header.toggle_tabzilla_dropdown()
        Assert.true(partners_page.header.are_tabzilla_links_visible)

    @pytest.mark.nondestructive
    def test_partner_billboard_links(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        Assert.true(partners_page.are_billboards_visible)
        Assert.true(partners_page.is_opening_soon_image_visible)

    @pytest.mark.nondestructive
    def test_submit_app_button_url(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        # changing url due to https://bugzilla.mozilla.org/show_bug.cgi?id=751903
        Assert.equal(partners_page.check_submit_apps_button_url,
        'https://marketplace.mozilla.org/ecosystem/')
