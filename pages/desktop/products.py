#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class ProductsPage(Base):

    def go_to_page(self):
        self.open('/products/')

    products_nav_link = (By.CSS_SELECTOR, '#products-nav li:nth-child(1) a')
    innovations_nav_link = (By.CSS_SELECTOR, '#products-nav li:nth-child(2) a')
    tools_nav_link = (By.CSS_SELECTOR, '#products-nav li:nth-child(3) a')
    platforms_nav_link = (By.CSS_SELECTOR, '#products-nav li:nth-child(4) a')
    main_nav_link = [
        products_nav_link,
        innovations_nav_link,
        tools_nav_link,
        platforms_nav_link
    ]

    _firefox_image = (By.CSS_SELECTOR, '#products li:nth-child(1) a img')
    _boot_to_gecko_image = (By.CSS_SELECTOR, '#products li:nth-child(2) a img')
    _marketplace_image = (By.CSS_SELECTOR, '#products li:nth-child(3) a img')
    _persona_iamge = (By.CSS_SELECTOR, '#products li:nth-child(4) a img')
    _thunderbird_image = (By.CSS_SELECTOR, '#products li:nth-child(5) a img')
    _webmaker_image = (By.CSS_SELECTOR, '#products li:nth-child(6) a img')
    _webfwd_image = (By.CSS_SELECTOR, '#innovations li:nth-child(1) a img')
    _labs_image = (By.CSS_SELECTOR, '#innovations li:nth-child(2) a img')
    _pancake_image = (By.CSS_SELECTOR, '#innovations li:nth-child(3) a img')
    _dev_tools_image = (By.CSS_SELECTOR, '#tools li:nth-child(1) a img')
    _bugzilla_image = (By.CSS_SELECTOR, '#tools li:nth-child(2) a img')
    _firebug_image = (By.CSS_SELECTOR, '#tools li:nth-child(3) a img')
    _gecko_image = (By.CSS_SELECTOR, '#platforms li:nth-child(1) a img')
    _xul_runner_image = (By.CSS_SELECTOR, '#platforms li:nth-child(2) a img')
    _future_products_image = (By.CSS_SELECTOR, '#platforms li:nth-child(3)')
    images_list = [
        _firefox_image,
        _boot_to_gecko_image,
        _marketplace_image,
        _persona_iamge,
        _thunderbird_image,
        _webfwd_image,
        _webmaker_image,
        _labs_image,
        _pancake_image,
        _dev_tools_image,
        _bugzilla_image,
        _firefox_image,
        _gecko_image,
        _xul_runner_image,
        _future_products_image
    ]

    _firefox_product_link = (By.CSS_SELECTOR, '#products li:nth-child(1) a')
    _boot_to_gecko_product_link = (By.CSS_SELECTOR, '#products li:nth-child(2) a')
    _marketplace_product_link = (By.CSS_SELECTOR, '#products li:nth-child(3) a')
    _persona_product_link = (By.CSS_SELECTOR, '#products li:nth-child(4) a')
    _thuderbird_product_link = (By.CSS_SELECTOR, '#products li:nth-child(5) a')
    _webmaker_product_link = (By.CSS_SELECTOR, '#products li:nth-child(6) a')
    products_link_list = [
        _firefox_product_link,
        _boot_to_gecko_product_link,
        _marketplace_product_link,
        _persona_product_link,
        _thuderbird_product_link,
        _webmaker_product_link
    ]

    _webfwd_innovation_link = (By.CSS_SELECTOR, '#innovations li:nth-child(1) a')
    _labs_innovation_link = (By.CSS_SELECTOR, '#innovations li:nth-child(2) a')
    _pancake_innovation_link = (By.CSS_SELECTOR, '#innovations li:nth-child(3) a')
    innovation_links_list = [
        _webfwd_innovation_link,
        _labs_innovation_link,
        _pancake_innovation_link
    ]

    _firefox_developer_tools_link = (By.CSS_SELECTOR, '#tools li:nth-child(1) a')
    _bugzilla_tools_link = (By.CSS_SELECTOR, '#tools li:nth-child(2) a')
    _firebug_tools_link = (By.CSS_SELECTOR, '#tools li:nth-child(3) a')
    tools_links_list = [
        _firefox_developer_tools_link,
        _bugzilla_tools_link,
        _firebug_tools_link
    ]

    _gecko_platform_link = (By.CSS_SELECTOR, '#platforms li:nth-child(1) a')
    _xulrunner_platform_link = (By.CSS_SELECTOR, '#platforms li:nth-child(2) a')
    platform_links = [
        _gecko_platform_link,
        _xulrunner_platform_link
    ]
