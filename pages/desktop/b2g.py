#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class BootToGecko(Base):

    def go_to_page(self):
        self.open('/b2g/')

    _firefox_os_header_locator = (By.CSS_SELECTOR, '#main-feature > h2')
    _welcome_section_locator = (By.CSS_SELECTOR, '#primary')
    _new_web_standards_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(1) > h3:nth-of-type(1)')
    _freedom_platforms_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(1) > h3:nth-of-type(2)')
    _customizations_for_oems_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(2) > h3')
    _developer_opportunities_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(3) > h3')
    _consumer_freedom_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(4) > h3')

    b2g_nav_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-of-type(1) > a'),
            'url_suffix': '/apps/',
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-of-type(2) > a'),
            'url_suffix': 'developer.mozilla.org/apps',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-feature > h1 > img'),
            'img_name_suffix': 'wordmark-firefoxos.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#primary > img'),
            'img_name_suffix': 'firefox-phone.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(1) img'),
            'img_name_suffix': 'example-apps.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(2) img:nth-of-type(1)'),
            'img_name_suffix': 'example-radio.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(2) img:nth-of-type(2)'),
            'img_name_suffix': 'example-music.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(3) img'),
            'img_name_suffix': 'example-browser.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(4) img:nth-of-type(1)'),
            'img_name_suffix': 'example-videos.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(4) img:nth-of-type(2)'),
            'img_name_suffix': 'example-gallery.jpg',
        }
    ]

    @property
    def is_firefox_os_header_visible(self):
        return self.is_element_visible(*self._firefox_os_header_locator)

    @property
    def is_welcome_section_visible(self):
        return self.is_element_visible(*self._welcome_section_locator)

    @property
    def is_new_web_standards_header_visible(self):
        return self.is_element_visible(*self._new_web_standards_header_locator)

    @property
    def is_freedom_platforms_header_visible(self):
        return self.is_element_visible(*self._freedom_platforms_header_locator)

    @property
    def is_customizations_for_oems_header_visible(self):
        return self.is_element_visible(*self._customizations_for_oems_header_locator)

    @property
    def is_developer_opportunities_header_visible(self):
        return self.is_element_visible(*self._developer_opportunities_header_locator)

    @property
    def is_consumer_freedom_header_visible(self):
        return self.is_element_visible(*self._consumer_freedom_header_locator)
