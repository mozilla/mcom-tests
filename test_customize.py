#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from selenium import selenium
from unittestzero import Assert
from pages.desktop.customize import CustomizePage
xfail = pytest.mark.xfail


class TestCustomize:

    def test_customize_icons(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        customize_pg = CustomizePage(mozwebqa)
        customize_pg.open("/en-US/firefox/customize/")
        Assert.true(customize_pg.plugins_icon)
        Assert.true(customize_pg.interface_icon)
        Assert.true(customize_pg.sync_icon)
        Assert.true(customize_pg.style_icon)
        Assert.true(customize_pg.addons_icon)

    def test_customize_images(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        customize_pg = CustomizePage(mozwebqa)
        customize_pg.open("/en-US/firefox/customize/")
        #Assert.true(customize_pg.style_image)
        Assert.true(customize_pg.plugins_image)
        Assert.true(customize_pg.interface_image)
        Assert.true(customize_pg.sync_image)
        Assert.true(customize_pg.addons_feature)
        Assert.true(customize_pg.top_feature)
