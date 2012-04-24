#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page


class MenuBarBillboard(Page):

    _name_locator = (By.CSS_SELECTOR, ' > a')

    def __init__(self, testsetup, web_element):
        Page.__init__(self, testsetup)
        self._root_element = web_element

    @property
    def menu_name(self):
        return self._root_element.text
