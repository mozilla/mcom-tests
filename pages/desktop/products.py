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
            'url_suffix': '/products/#products',
        }, {
            'locator': (By.CSS_SELECTOR, '#products-nav li:nth-child(2) a'),
            'url_suffix': '/products/#innovations',
        }, {
            'locator': (By.CSS_SELECTOR, '#products-nav li:nth-child(3) a'),
            'url_suffix': '/products/#tools',
        }, {
            'locator': (By.CSS_SELECTOR, '#products-nav li:nth-child(4) a'),
            'url_suffix': '/products/#platforms',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(1) a img'),
            'img_name_suffix': 'badge-firefox.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(2) a img'),
            'img_name_suffix': 'badge-firefoxos.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(3) a img'),
            'img_name_suffix': 'badge-marketplace.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(4) a img'),
            'img_name_suffix': 'badge-persona.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(5) a img'),
            'img_name_suffix': 'badge-thunderbird.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(6) a img'),
            'img_name_suffix': 'badge-webmaker.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#innovations li:nth-child(1) a img'),
            'img_name_suffix': 'badge-webfwd.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#innovations li:nth-child(2) a img'),
            'img_name_suffix': 'badge-labs.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#innovations li:nth-child(3) a img'),
            'img_name_suffix': 'badge-pancake.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#tools li:nth-child(1) a img'),
            'img_name_suffix': 'badge-tools.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#tools li:nth-child(2) a img'),
            'img_name_suffix': 'badge-bugzilla.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#tools li:nth-child(3) a img'),
            'img_name_suffix': 'badge-firebug.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#platforms li:nth-child(1) a img'),
            'img_name_suffix': 'badge-gecko.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#platforms li:nth-child(2) a img'),
            'img_name_suffix': 'badge-xulrunner.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#platforms li:nth-child(3) img'),
            'img_name_suffix': 'badge-reserved.jpg',
        }
    ]

    products_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(1) a'),
            'url_suffix': '/firefox/',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(2) a'),
            'url_suffix': '/firefoxos/',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(3) a'),
            'url_suffix': '/apps/',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(4) a'),
            'url_suffix': '/persona/',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(5) a'),
            'url_suffix': '/thunderbird/',
        }, {
            'locator': (By.CSS_SELECTOR, '#products li:nth-child(6) a'),
            'url_suffix': 'webmaker.org/',
        }
    ]

    innovations_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#innovations li:nth-child(1) a'),
            'url_suffix': 'webfwd.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#innovations li:nth-child(2) a'),
            'url_suffix': 'mozillalabs.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#innovations li:nth-child(3) a'),
            'url_suffix': 'wiki.mozilla.org/Pancake',
        }
    ]

    tools_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#tools li:nth-child(1) a'),
            'url_suffix': '/Tools/',
        }, {
            'locator': (By.CSS_SELECTOR, '#tools li:nth-child(2) a'),
            'url_suffix': 'www.bugzilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#tools li:nth-child(3) a'),
            'url_suffix': 'getfirebug.com/',
        }
    ]

    platforms_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#platforms li:nth-child(1) a'),
            'url_suffix': '/Gecko',
        }, {
            'locator': (By.CSS_SELECTOR, '#platforms li:nth-child(2) a'),
            'url_suffix': '/XULRunner',
        }
    ]
