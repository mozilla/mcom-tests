#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class NightlyFirstRun(Base):

    def go_to_page(self):
        self.open('/firefox/nightly/firstrun/')

    _test_section_locator = (By.CSS_SELECTOR, '.blue-box.test')
    _test_button_locator = (By.CSS_SELECTOR, '.test > .content > a')
    _code_section_locator = (By.CSS_SELECTOR, '.blue-box.code')
    _code_button_locator = (By.CSS_SELECTOR, '.code > .content > a')
    _localize_section_locator = (By.CSS_SELECTOR, '.blue-box.localize')
    _localize_button_locator = (By.CSS_SELECTOR, '.localize > .content > a')
    _nightly_badge_img_locator = (By.CSS_SELECTOR, '.blue-box.badge')
    _nightly_badge_link_locator = (By.CSS_SELECTOR, '.blue-box.badge > a')

    @property
    def is_test_section_visible(self):
        return self.is_element_visible(*self._test_section_locator)

    @property
    def is_code_section_visible(self):
        return self.is_element_visible(*self._code_section_locator)

    @property
    def is_localize_section_visible(self):
        return self.is_element_visible(*self._localize_button_locator)

    @property
    def is_nightly_badge_visible(self):
        return self.is_element_visible(*self._nightly_badge_img_locator)

    @property
    def is_localize_button_visible(self):
        return self.is_element_visible(*self._localize_button_locator)

    @property
    def is_code_button_visible(self):
        return self.is_element_visible(*self._code_button_locator)

    @property
    def is_test_button_visible(self):
        return self.is_element_visible(*self._test_button_locator)
