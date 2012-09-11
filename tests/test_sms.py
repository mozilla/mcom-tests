#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.sms import Sms


class TestSmsPage:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        sms_page = Sms(mozwebqa)
        sms_page.go_to_page()
        Assert.contains(sms_page.footer.expected_footer_logo_destination,
            sms_page.footer.footer_logo_destination)
        Assert.contains(sms_page.footer.expected_footer_logo_img,
            sms_page.footer.footer_logo_img)
        for link in sms_page.Footer.footer_links_list:
            Assert.contains(link.get('href'), sms_page.footer.footer_link_destination(link.get('text')))

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        sms_page = Sms(mozwebqa)
        sms_page.go_to_page()
        Assert.true(sms_page.header.is_tabzilla_panel_visible)
        sms_page.header.toggle_tabzilla_dropdown()
        Assert.true(sms_page.header.are_tabzilla_links_visible)

    @pytest.mark.nondestructive
    def test_send_sms(self, mozwebqa):
        sms_page = Sms(mozwebqa)
        sms_page.go_to_page()
        Assert.true(sms_page.is_google_play_link_visible)
        Assert.true(sms_page.is_device_support_link_visible)
        Assert.true(sms_page.is_learn_more_link_visible)
        Assert.true(sms_page.is_textbox_visible)
        Assert.true(sms_page.submit_form())
