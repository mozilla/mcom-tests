#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium import selenium
from unittestzero import Assert
from pages.mobile.mobile import MobilePage
import pytest
xfail = pytest.mark.xfail


class TestMobile:

    @xfail(reason='Bug 699985 - push updated basket-dev')
    def test_sub_sections_are_present(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        mobile_pg = MobilePage(mozwebqa)
        mobile_pg.open('/mobile/')
        Assert.true(mobile_pg.get_firefox_for_android_button)
        Assert.true(mobile_pg.newsletter_link)
        Assert.true(mobile_pg.facebook_link)
        Assert.true(mobile_pg.twitter_link)
        Assert.equal(mobile_pg.click_facebook_link, \
                    u"http://www.facebook.com/firefoxformobile")
