#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.desktop.products import ProductsPage
from tests.base_test import BaseTest


class TestProductsPage(BaseTest):

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        self.verify_footer_section(products_page)

    @pytest.mark.nondestructive
    def test_header_section(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        self.verify_header_section(products_page)

    @pytest.mark.nondestructive
    def test_main_nav_section(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        for link in products_page.main_nav_links_list:
            Assert.true(products_page.is_element_present(*link), link[1])

    @pytest.mark.nondestructive
    def test_image_section(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        for link in products_page.images_list:
            Assert.true(products_page.is_element_present(*link), link[1])

    @pytest.mark.nondestructive
    def test_links_are_valid(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        for link in products_page.products_link_list:
            Assert.true(products_page.is_element_visible(*link), link[1])

