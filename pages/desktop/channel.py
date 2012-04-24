#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class ChannelPage(Base):

    _mozilla_firefox_logo = (By.CSS_SELECTOR, "#header > div > h1 > a")
    _beta_logo = (By.CSS_SELECTOR, "#toggler-logo-beta")
    _firefox_logo = (By.CSS_SELECTOR, "#toggler-logo-firefox")
    _aurora_logo = (By.CSS_SELECTOR, "#toggler-logo-aurora")
    _firefox_desktop_button = (By.CSS_SELECTOR, "#firefox-desktop-link > a")
    _firefox_mobile_button = (By.CSS_SELECTOR, "#firefox-mobile-link > a")
    _aurora_desktop_button = (By.CSS_SELECTOR, "#aurora-desktop-link > a")
    _aurora_mobile_button = (By.CSS_SELECTOR, "#aurora-mobile-link > a")
    _beta_desktop_button = (By.CSS_SELECTOR, "#beta-desktop-link > a")
    _beta_mobile_button = (By.CSS_SELECTOR, "#beta-mobile-link > a")
    _learn_more_button = (By.CSS_SELECTOR, ".more > a")
    _left_carousel = (By.CSS_SELECTOR, "#carousel-left")
    _right_carousel = (By.CSS_SELECTOR, "#carousel-right")
    _main_feature_header = (By.CSS_SELECTOR, "#main-feature > h2")

    def go_to_channel_page(self):
        self.open("/firefox/channel")

    def click_aurora_logo(self):
        self.selenium.find_element(*self._aurora_logo).click()

    def click_beta_logo(self):
        self.selenium.find_element(*self._beta_logo).click()

    def click_firefox_logo(self):
        self.selenium.find_element(*self._firefox_logo).click()

    @property
    def is_main_feature_heading_present(self):
        return self.is_element_present(*self._main_feature_header)

    @property
    def is_mozilla_firefox_logo_present(self):
        return self.is_element_present(*self._mozilla_firefox_logo)

    @property
    def is_beta_logo_present(self):
        return self.is_element_present(*self._beta_logo)

    @property
    def is_firefox_logo_present(self):
        return self.is_element_present(*self._firefox_logo)

    @property
    def is_aurora_logo_present(self):
        return self.is_element_present(*self._aurora_logo)

    @property
    def is_left_carousel_present(self):
        return self.is_element_present(*self._left_carousel)

    @property
    def is_right_carousel_present(self):
        return self.is_element_present(*self._right_carousel)

    def click_right_carousel(self):
        self.selenium.find_element(*self._right_carousel).click()

    def click_left_carousel(self):
        self.selenium.find_element(*self._left_carousel).click()
