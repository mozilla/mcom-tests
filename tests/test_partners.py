#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.desktop.partners import Partners
from tests.base_test import BaseTest


class TestPartners(BaseTest):

    @pytest.mark.nondestructive
    @pytest.mark.bedrock
    def test_footer_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        self.verify_footer_section(partners_page)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        self.verify_header_section(partners_page)

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
