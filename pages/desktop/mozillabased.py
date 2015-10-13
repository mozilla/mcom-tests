# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.base import Base


class MozillaBasedPage(Base):

    _url = '{base_url}/{locale}/projects/mozilla-based'

    _productlist_locator = (By.CSS_SELECTOR, '.productlist')
    _product_locator = (By.CSS_SELECTOR, 'li > h3 > a')
    _logo_locator = (By.CSS_SELECTOR, 'img')
    _billboard_locator = (By.CSS_SELECTOR, '#featured.billboard')

    breadcrumbs_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'nav.breadcrumbs > a:nth-of-type(1)'),
            'url_suffix': '/en-US/',
        }, {
            'locator': (By.CSS_SELECTOR, 'nav.breadcrumbs > a:nth-of-type(2)'),
            'url_suffix': '/en-US/firefox/products/',
        },
    ]

    main_feature_link_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-feature > p:nth-of-type(2) > a:nth-of-type(1)'),
            'url_suffix': '/projects/technologies.html',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-feature > p:nth-of-type(2) > a:nth-of-type(2)'),
            'url_suffix': '/contact/spaces/',
        },
    ]

    find_out_more_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > p:nth-of-type(1) > a'),
            'url_suffix': 'https://developer.mozilla.org/En/List_of_Mozilla-Based_Applications',
        }, {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > ul > li:nth-of-type(1) > a'),
            'url_suffix': 'https://developer.mozilla.org/En/Using_Mozilla_code_in_other_projects',
        }, {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > ul > li:nth-of-type(2) > a'),
            'url_suffix': 'http://www.mozdev.org/community/books.html',
        }, {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > ul > li:nth-of-type(3) > a'),
            'url_suffix': 'https://wiki.mozilla.org/Consulting',
        }, {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > div > a'),
            'url_suffix': '/poweredby',
        },
    ]

    get_mozilla_updates_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'label.privacy-check-label > span > a'),
            'url_suffix': '/en-US/privacy-policy',
        },
    ]

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
