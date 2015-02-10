#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class DoNotTrack(Base):

    def go_to_page(self):
        self.open('/firefox/dnt')

    _dnt_status_wrapper_locator = (By.ID, 'dnt-status-wrapper')
    _dnt_status_text_locator = (By.CSS_SELECTOR, '#dnt-status > h4')
    _enable_dnt_text_locator = (By.CSS_SELECTOR, '.sidebar-inset > h4')
    _enable_dnt_image_locator = (By.CSS_SELECTOR, '.sidebar-inset > p > a > img')
    _enable_dnt_link_locator = (By.CSS_SELECTOR, '.sidebar-inset > p > a')
    tracking_protection_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.sidebar-box > p > a:nth-of-type(1)'),
            'url_suffix': 'ie.microsoft.com/testdrive/Browser/TrackingProtectionLists/faq.html'
        },
        {
            'locator': (By.CSS_SELECTOR, '.sidebar-box > p > a:nth-of-type(2)'),
            'url_suffix': 'dnt-enabler.*.tpl'
        }
    ]

    @property
    def is_status_wrapper_visible(self):
        return self.is_element_visible(*self._dnt_status_wrapper_locator)

    @property
    def is_status_text_visible(self):
        return self.is_element_visible(*self._dnt_status_text_locator)

    @property
    def is_enable_dnt_text_visible(self):
        return self.is_element_visible(*self._enable_dnt_text_locator)

    @property
    def is_enable_dnt_image_visible(self):
        return self.is_element_visible(*self._enable_dnt_image_locator)

    def are_tracking_protection_links_visible(self, locator):
        return self.is_element_visible(*locator)
