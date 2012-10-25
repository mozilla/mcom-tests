#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class MozillaBasedPage(Base):
    _productlist_locator = (By.CSS_SELECTOR, '.productlist')
    _product_locator = (By.CSS_SELECTOR, 'li > h3 > a')
    _logo_locator = (By.CSS_SELECTOR, 'img')
    _billboard_locator = (By.CSS_SELECTOR, '#featured.billboard')

    def go_to_page(self):
        self.open('/projects/mozilla-based/')

    def get_product_properties(self, unorderedlist_locator):
        products = []
        unorderedlist = self.selenium.find_element(*unorderedlist_locator)
        for product in unorderedlist.find_elements(*self._product_locator):
            product_properties = {}
            product_properties['text'] = product.get_attribute('text')
            product_properties['url'] = product.get_attribute('href')
            product_properties['logo'] = \
                product.find_element(*self._logo_locator).get_attribute('src')
            products.append(product_properties)
        return products

    @property
    def get_product_list(self):
        return self.get_product_properties(self._productlist_locator)

    @property
    def get_billboard_product_list(self):
        return self.get_product_properties(self._billboard_locator)
