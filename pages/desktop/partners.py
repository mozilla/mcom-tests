#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.desktop.base import Base


class Partners(Base):

    def go_to_page(self):
        self.open('/apps/partners/')

    _marketplace_header_locator = (By.CSS_SELECTOR, '#masthead > h2 > a > img')
    _apps_platform_billboard = (By.CSS_SELECTOR, '.billboard.menu-bar > ul > li:nth-of-type(1) > a')
    _marketplace_billboard = (By.CSS_SELECTOR, '.billboard.menu-bar > ul > li:nth-of-type(2) > a')
    _submit_apps_button = (By.CSS_SELECTOR, '.billboard.menu-bar > ul > li:nth-of-type(3) > a')
    _mdn_apps_link = (By.CSS_SELECTOR, '#mdn-link > a')
    _opening_soon_image = (By.CSS_SELECTOR, '#sign')
    _test_apps_image = (By.CSS_SELECTOR, '#test')
    _build_fanbase_image = (By.CSS_SELECTOR, '#build')
    _target_consumers_image = (By.CSS_SELECTOR, '#target')

    @property
    def are_billboards_visible(self):
        return self.is_element_visible(*self._marketplace_header_locator) and \
        self.is_element_visible(*self._apps_platform_billboard)

    @property
    def is_opening_soon_image_visible(self):
        return self.is_element_visible(*self._opening_soon_image)

    @property
    def are_pointer_images_visible(self):
        return self.is_element_visible(*self._test_apps_image) and \
        self.is_element_visible(*self._build_fanbase_image) and \
        self.is_element_visible(*self._target_consumers_image)

    @property
    def check_submit_apps_button_url(self):
        element = self.selenium.find_element(*self._submit_apps_button)
        url = element.get_attribute('href')
        return url
