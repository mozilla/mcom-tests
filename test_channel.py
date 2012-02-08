#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium import selenium
from unittestzero import Assert
from pages.desktop.channel import ChannelPage
import pytest


class TestChannelPage:


    def test_that_logos_are_present(self, mozwebqa):
        channel_pg = ChannelPage(mozwebqa)
        channel_pg.go_to_channel_page()
        Assert.true(channel_pg.is_beta_logo_present)
        Assert.true(channel_pg.is_firefox_logo_present)
        Assert.true(channel_pg.is_aurora_logo_present)

    def test_beta_sub_page(self, mozwebqa):
        channel_pg = ChannelPage(mozwebqa)
        channel_pg.go_to_channel_page()
        channel_pg.click_beta_logo()

    def test_aurora_sub_page(self, mozwebqa):
        channel_pg = ChannelPage(mozwebqa)
        channel_pg.go_to_channel_page()
        channel_pg.click_aurora_logo()

    def test_firefox_sub_page(self, mozwebqa):
        channel_pg = ChannelPage(mozwebqa)
        channel_pg.go_to_channel_page()
        channel_pg.click_firefox_logo()

    def test_that_carousels_are_present(self, mozwebqa):
        channel_pg = ChannelPage(mozwebqa)
        channel_pg.go_to_channel_page()
        Assert.true(channel_pg.is_right_carousel_present)
        Assert.true(channel_pg.is_left_carousel_present)
