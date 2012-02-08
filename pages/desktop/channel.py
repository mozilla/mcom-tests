#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import MozillaBasePage


class ChannelPage(MozillaBasePage):


    _mozilla_firefox_logo = "css=#header > div > h1 > a"
    _beta_logo = "css=#toggler-logo-beta"
    _firefox_logo = "css=#toggler-logo-firefox"
    _aurora_logo = "css=#toggler-logo-aurora"
    _firefox_desktop_button = "css=#firefox-desktop-link > a"
    _firefox_mobile_button = "css=#firefox-mobile-link > a"
    _aurora_desktop_button = "css=#aurora-desktop-link > a"
    _aurora_mobile_button = "css=#aurora-mobile-link > a"
    _beta_desktop_button = "css=#beta-desktop-link > a"
    _beta_mobile_button = "css=#beta-mobile-link > a"
    _learn_more_button = "css=.more>a"
    _left_carousel = "css=#carousel-left"
    _right_carousel = "css=#carousel-right"
    _main_feature_header = "css=#main-feature > h2"


    def go_to_channel_page(self):
        self.open("/firefox/channel")


    def click_aurora_logo(self):
        self.click(self._aurora_logo)


    def click_beta_logo(self):
        self.click(self._beta_logo)


    def click_firefox_logo(self):
        self.click(self._firefox_logo)

    @property
    def is_main_feature_heading_present(self):
        return self.is_element_present(self._main_feature_header)

    @property
    def is_mozilla_firefox_logo_present(self):
        return self.is_element_present(self._mozilla_firefox_logo)

    @property
    def is_beta_logo_present(self):
        return self.is_element_present(self._beta_logo)

    @property
    def is_firefox_logo_present(self):
        return self.is_element_present(self._firefox_logo)

    @property
    def is_aurora_logo_present(self):
        return self.is_element_present(self._aurora_logo)

    @property
    def is_left_carousel_present(self):
        return self.is_element_present(self._left_carousel)

    @property
    def is_right_carousel_present(self):
        return self.is_element_present(self._right_carousel)

    def click_right_carousel(self):
        self.click(self._right_carousel)

    def click_left_carousel(self):
        self.click(self._left_carousel)
