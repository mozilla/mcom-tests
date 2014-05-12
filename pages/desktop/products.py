#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class ProductsPage(Base):

    def go_to_page(self):
        self.open('/products/')

    product_nav_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#products-nav li:nth-child(1) a'),
            'url_suffix': '/products/#firefox',
        }, {
            'locator': (By.CSS_SELECTOR, '#products-nav li:nth-child(2) a'),
            'url_suffix': '/products/#mozilla',
        }, {
            'locator': (By.CSS_SELECTOR, '#products-nav li:nth-child(3) a'),
            'url_suffix': '/products/#developers',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox li:nth-child(1) a img'),
            'img_name_suffix': 'badge-firefox.jpg?2013-06',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox li:nth-child(2) a img'),
            'img_name_suffix': 'badge-android.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox li:nth-child(3) a img'),
            'img_name_suffix': 'badge-firefoxos.jpg?2013-06',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox li:nth-child(4) a img'),
            'img_name_suffix': 'badge-marketplace.jpg?2013-06',
        }, {
            'locator': (By.CSS_SELECTOR, '#mozilla li:nth-child(1) a img'),
            'img_name_suffix': 'badge-persona.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#mozilla li:nth-child(2) a img'),
            'img_name_suffix': 'badge-webmaker.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#mozilla li:nth-child(3) a img'),
            'img_name_suffix': 'badge-thunderbird.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(1) a img'),
            'img_name_suffix': 'badge-bugzilla.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(2) a img'),
            'img_name_suffix': 'badge-firebug.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(3) a img'),
            'img_name_suffix': 'badge-xulrunner.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(4) img'),
            'img_name_suffix': 'badge-gecko.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(5) img'),
            'img_name_suffix': 'badge-api.jpg',
        }
    ]

    firefox_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox li:nth-child(1) a'),
            'url_suffix': '/firefox/desktop/',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox li:nth-child(2) a'),
            'url_suffix': '/firefox/android/',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox li:nth-child(3) a'),
            'url_suffix': '/firefox/os/',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox li:nth-child(4) a'),
            'url_suffix': 'marketplace.firefox.com/',
        }
    ]

    mozilla_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#mozilla li:nth-child(1) a'),
            'url_suffix': '/persona/',
        }, {
            'locator': (By.CSS_SELECTOR, '#mozilla li:nth-child(2) a'),
            'url_suffix': 'webmaker.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#mozilla li:nth-child(3) a'),
            'url_suffix': '/thunderbird/',
        }
    ]

    developers_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(1) a'),
            'url_suffix': 'bugzilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(2) a'),
            'url_suffix': 'getfirebug.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(3) a'),
            'url_suffix': '/XULRunner',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(4) a'),
            'url_suffix': '/Gecko',
        }, {
            'locator': (By.CSS_SELECTOR, '#developers li:nth-child(5) a'),
            'url_suffix': '/Apps/Reference',
        }
    ]
