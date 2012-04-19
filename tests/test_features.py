#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.desktop.features import FeaturesPage


class TestFeatures:

    expected_menu_bar_billboard = ["Browsing\nMade Easy", "High\nPerformance", "Advanced\nSecurity",
                                  "Powerful\nPersonalization", "The Cutting\nEdge", "Universal\nAccess"]

    @pytest.mark.nondestructive
    def test_menu_bar_billboard_names(self, mozwebqa):
        features_pg = FeaturesPage(mozwebqa)
        features_pg.go_to_page()

        for idx, menu_item in enumerate(features_pg.menu_bar_billboard):
            Assert.equal(self.expected_menu_bar_billboard[idx], menu_item.menu_name)
