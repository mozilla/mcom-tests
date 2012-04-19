#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert

from pages.desktop.customize import CustomizePage


class TestCustomize:

    expected_menu_bar_billboard = ["Add Style:\nPersonas", "Customize:\nAdd-ons", "Make It Work:\nPlugins",
                                  "Adapt Your\nInterface", "Stay In\nSync"]

    @pytest.mark.nondestructive
    def test_customize_menu_text(self, mozwebqa):
        customize_pg = CustomizePage(mozwebqa)
        customize_pg.go_to_page()

        Assert.equal(5, len(customize_pg.menu_bar_billboard))

        for idx, menu_item in enumerate(customize_pg.menu_bar_billboard):
            Assert.equal(self.expected_menu_bar_billboard[idx], menu_item.menu_name)
