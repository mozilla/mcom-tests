#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.products import ProductsPage


class TestProductsPage:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        for link in ProductsPage.Footer.footer_links_list:
            url = products_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        Assert.true(products_page.header.is_tabzilla_panel_visible)
        products_page.header.toggle_tabzilla_dropdown()
        for link in ProductsPage.Header.tabzilla_links_list:
            url = products_page.link_destination(link.get('locator'))
            Assert.true(url.endswith(link.get('url_suffix')), '%s does not end with %s' % (url, link.get('url_suffix')))

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
