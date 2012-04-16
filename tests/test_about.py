#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.about import AboutPage


class TestAbout:

    @pytest.mark.nondestructive
    def test_about_images(self, mozwebqa):
        about_pg = AboutPage(mozwebqa)
        about_pg.open("/en-US/about/")
        Assert.true(about_pg.participate_image)
        Assert.true(about_pg.communications_image)
        Assert.true(about_pg.careers_image)
        Assert.true(about_pg.partnerships_image)
        Assert.true(about_pg.legal_image)
        Assert.true(about_pg.contact_us_image)
        Assert.true(about_pg.store_image)
        Assert.true(about_pg.blog_image)

    @pytest.mark.nondestructive
    def test_about_text(self, mozwebqa):
        about_pg = AboutPage(mozwebqa)
        about_pg.open("/en-US/about/")
        Assert.true(about_pg.participate_text)
        Assert.true(about_pg.communications_text)
        Assert.true(about_pg.careers_text)
        Assert.true(about_pg.partnerships_text)
        Assert.true(about_pg.legal_text)
        Assert.true(about_pg.contact_us_text)
        Assert.true(about_pg.store_text)
        Assert.true(about_pg.blog_text)
