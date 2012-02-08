#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.features import FeaturesPage


class TestFeatures:

    def test_page(self, mozwebqa):
        features_pg = FeaturesPage(mozwebqa)
        features_pg.open("/firefox/features/")
        Assert.true(features_pg.made_easy)
        Assert.true(features_pg.high_performance)
        Assert.true(features_pg.advanced_security)
        Assert.true(features_pg.powerful_personalization)
        Assert.true(features_pg.universal_access)
        Assert.true(features_pg.cutting_edge)
        Assert.true(features_pg.made_easy_img)
        Assert.true(features_pg.app_tabs_img)
        Assert.true(features_pg.switch_tab_img)
        Assert.true(features_pg.panorama_img)
        Assert.true(features_pg.sync_img)
        Assert.true(features_pg.easy_search_img)
        Assert.true(features_pg.one_bookmark_img)
        Assert.true(features_pg.speed_img)
        Assert.true(features_pg.security_img)
        Assert.true(features_pg.private_browsing_img)
        Assert.true(features_pg.auto_update_img)
