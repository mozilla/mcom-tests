#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from selenium import selenium
from unittestzero import Assert
from pages.desktop.security import SecurityPage


class TestSecurity:

    def test_security_icons(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        security_pg = SecurityPage(mozwebqa)
        security_pg.open("/firefox/security/")
        Assert.true(security_pg.protecting_privacy_ico)
        Assert.true(security_pg.browser_security_ico)
        Assert.true(security_pg.in_control_ico)
        Assert.true(security_pg.mission_ico)

    def test_security_images(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        security_pg = SecurityPage(mozwebqa)
        security_pg.open("/firefox/security/")
        Assert.true(security_pg.privacy_img)
        Assert.true(security_pg.browser_security_img)
        Assert.true(security_pg.control_img)
        Assert.true(security_pg.mission_img)
