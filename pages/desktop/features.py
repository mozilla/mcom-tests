#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import MozillaBasePage


class FeaturesPage(MozillaBasePage):

    _made_easy_locator = \
    "css=#main-feature>.feature-links>#made-easy>a"
    _high_performance_locator =  \
    "css=#main-feature>.feature-links>#high-performance>a"
    _advanced_security_locator = \
    "css=#main-feature>.feature-links>#advanced-security>a"
    _powerful_personalization_locator = \
    "css=#main-feature>.feature-links>#powerful-personalization>a"
    _universal_access_locator = \
    "css=#main-feature>.feature-links>#cutting-edge>a"
    _cutting_edge_locator = \
    "css=#main-feature>.feature-links>#universal-access>a"

    _made_easy_image = \
    "css=#madeeasy>.features-container>.feature>.right"
    _app_tabs_image = \
    "css=#madeeasy>.features-container>.feature>.column1>.sub-feature>.right"
    _switch_tab_image = \
    "css=#madeeasy>.features-container>.feature>.column2>.sub-feature>.right"
    _panorama_image = \
    "css=#madeeasy>.features-container>.feature>.column3>.sub-feature>.right"
    _sync_image = \
    "css=#madeeasy>.features-container>.column-span>.right"
    _easy_search_image = \
    "//*[@id='madeeasy']/div/div[8]/div[4]/img"
    _one_bookmark_image = \
    "css=#madeeasy>.features-container>.feature>.oneclickbookmarking>.right"
    _speed_image = \
    "css=.mozilla-video-control-overlay"
    _security_image = \
    "css=#advancedsecurity>.features-container>.column1>.feature>.right"
    _private_browsing_image = \
    "css=#advancedsecurity>.features-container>.column2>.feature>.right"
    _auto_update_image = \
    "css=#advancedsecurity>.features-container>.column3>.feature>.right"
    _addons_manager_image = \
    "css=#powerfulpersonalization>.features-container>.addons-manager>.right"
    personas_image = \
    "css=#powerfulpersonalization>.features-container>.column1>.feature>.right"

    @property
    def made_easy(self):
        return self.is_element_present(self._made_easy_locator)

    @property
    def high_performance(self):
        return self.is_element_present(self._high_performance_locator)

    @property
    def advanced_security(self):
        return self.is_element_present(self._advanced_security_locator)

    @property
    def powerful_personalization(self):
        return self.is_element_present(self._powerful_personalization_locator)

    @property
    def universal_access(self):
        return self.is_element_present(self._universal_access_locator)

    @property
    def cutting_edge(self):
        return self.is_element_present(self._cutting_edge_locator)

    @property
    def made_easy_img(self):
        return self.is_element_present(self._made_easy_image)

    @property
    def app_tabs_img(self):
        return self.is_element_present(self._app_tabs_image)

    @property
    def switch_tab_img(self):
        return self.is_element_present(self._switch_tab_image)

    @property
    def panorama_img(self):
        return self.is_element_present(self._panorama_image)

    @property
    def sync_img(self):
        return self.is_element_present(self._sync_image)

    @property
    def easy_search_img(self):
        return self.is_element_present(self._easy_search_image)

    @property
    def one_bookmark_img(self):
        return self.is_element_present(self._one_bookmark_image)

    @property
    def speed_img(self):
        return self.is_element_present(self._speed_image)

    @property
    def security_img(self):
        return self.is_element_present(self._security_image)

    @property
    def private_browsing_img(self):
        return self.is_element_present(self._private_browsing_image)

    @property
    def auto_update_img(self):
        return self.is_element_present(self._auto_update_image)
