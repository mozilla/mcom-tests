#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page


class DownloadFirefox(Page):

    _osx_download_locator = (By.CSS_SELECTOR, '.os_osx > a')
    _windows_download_locator = (By.CSS_SELECTOR, '.os_windows > a')
    _linux_download_locator = (By.CSS_SELECTOR, '.os_linux > a')

    _systems_and_languages_locator = (By.CSS_SELECTOR, '.download-other.os_linux.os_osx.os_windows > a:nth-of-type(1)')
    _whats_new_locator = (By.CSS_SELECTOR, '.download-other.os_linux.os_osx.os_windows > a:nth-of-type(2)')
    _privacy_locator = (By.CSS_SELECTOR, '.download-other.os_linux.os_osx.os_windows > a:nth-of-type(3)')

    def click_download_for_mac(self):
        self.selenium.find_element(*self._osx_download_locator).click()

    def click_download_for_windows(self):
        self.selenium.find_element(*self._windows_download_locator).click()

    @property
    def is_download_link_visible(self):
        return self.is_element_visible(*self._osx_download_locator) or \
            self.is_element_visible(*self._windows_download_locator) or \
            self.is_element_visible(*self._linux_download_locator)

    @property
    def are_secondary_links_visible(self):
        return self.is_element_visible(*self._systems_and_languages_locator) and \
            self.is_element_visible(*self._whats_new_locator) and \
            self.is_element_visible(*self._privacy_locator)
