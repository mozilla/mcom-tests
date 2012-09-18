#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class AboutPage(Base):

    def go_to_page(self):
        self.open('/about/')

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(1) a'),
            'url_suffix': '/mission/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(2) a'),
            'url_suffix': 'careers.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(3) a'),
            'url_suffix': 'blog.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(4) a'),
            'url_suffix': '/styleguide',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(5) a'),
            'url_suffix': '/about/contact',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(1) a'),
            'url_suffix': '/products/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(2) a'),
            'url_suffix': '/contribute/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(3) a'),
            'url_suffix': 'blog.mozilla.org/press/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(4) a'),
            'url_suffix': '/privacy/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(5) a'),
            'url_suffix': '/about/partnerships',
        }
    ]
