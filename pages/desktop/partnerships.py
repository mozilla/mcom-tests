#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Partnerships(Base):

    def go_to_page(self):
        self.open('/about/partnerships/')

    section_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox > p > a'),
            'url_suffix': '/en-US/about/partnerships/distribution/',
        }, {
            'locator': (By.CSS_SELECTOR, '#marketplace > p > a'),
            'url_suffix': '/en-US/apps/',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox > img:nth-of-type(1)'),
            'img_name_contains': 'banner-firefox',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox > img:nth-of-type(2)'),
            'img_name_contains': 'icon-firefox',
        }, {
            'locator': (By.CSS_SELECTOR, '#android > img:nth-of-type(1)'),
            'img_name_contains': 'banner-android',
        }, {
            'locator': (By.CSS_SELECTOR, '#android > img:nth-of-type(2)'),
            'img_name_contains': 'icon-android',
        }, {
            'locator': (By.CSS_SELECTOR, '#marketplace > img:nth-of-type(1)'),
            'img_name_contains': 'banner-marketplace',
        }, {
            'locator': (By.CSS_SELECTOR, '#marketplace > img:nth-of-type(2)'),
            'img_name_contains': 'icon-marketplace',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefoxos > img:nth-of-type(1)'),
            'img_name_contains': 'banner-firefoxos',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefoxos > img:nth-of-type(2)'),
            'img_name_contains': 'icon-firefox',
        }, {
            'locator': (By.CSS_SELECTOR, '#cobrand > img:nth-of-type(1)'),
            'img_name_contains': 'banner-cobrand',
        }, {
            'locator': (By.CSS_SELECTOR, '#cobrand > img:nth-of-type(2)'),
            'img_name_contains': 'icon-cobrand',
        }
    ]
