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

    billboard_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.billboard.menu-bar > ul > li:nth-of-type(1) > a'),
            'url_suffix': '#platform',
        }, {
            'locator': (By.CSS_SELECTOR, '.billboard.menu-bar > ul > li:nth-of-type(2) > a'),
            'url_suffix': '#marketplace',
        }, {
            'locator': (By.CSS_SELECTOR, '.billboard.menu-bar > ul > li:nth-of-type(3) > a'),
            'url_suffix': 'marketplace.mozilla.org/developers/',
        }
    ]

    _mdn_apps_link_locator = (By.CSS_SELECTOR, '#mdn-link > a')
    _opening_soon_image_locator = (By.ID, 'sign')
    _test_apps_image_locator = (By.ID, 'test')
    _build_fanbase_image_locator = (By.ID, 'build')
    _target_consumers_image_locator = (By.ID, 'target')

    @property
    def is_opening_soon_image_visible(self):
        return self.is_element_visible(*self._opening_soon_image_locator)

    @property
    def are_pointer_images_visible(self):
        return self.is_element_visible(*self._test_apps_image_locator) and \
            self.is_element_visible(*self._build_fanbase_image_locator) and \
            self.is_element_visible(*self._target_consumers_image_locator)

    @property
    def mdn_apps_link_destination(self):
        return self.selenium.find_element(*self._mdn_apps_link_locator).get_attribute('href')
