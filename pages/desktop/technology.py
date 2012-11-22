#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Technology(Base):

    def go_to_page(self):
        self.open('/firefox/technology/')

    billboard_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(1) > a'),
            'url_suffix': '#tools',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(2) > a'),
            'url_suffix': '#html5',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(3) > a'),
            'url_suffix': '#css',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(4) > a'),
            'url_suffix': '#apis',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(5) > a'),
            'url_suffix': '#svg',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(6) > a'),
            'url_suffix': '#security',
        }
    ]

    more_info_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(1) > a'),
            'url_suffix': 'developer.mozilla.org/demos',
        }, {
            'locator': (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(2) > a'),
            'url_suffix': '/firefox/performance/',
        }, {
            'locator': (By.CSS_SELECTOR, '#more-info ul > li:nth-of-type(3) > a'),
            'url_suffix': 'developer.mozilla.org/',
        }
    ]
