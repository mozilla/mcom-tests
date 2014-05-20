#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert
from pages.desktop.products import ProductsPage


class TestProductsPage:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in ProductsPage.Footer.footer_links_list:
            url = products_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        Assert.true(products_page.header.is_tabzilla_panel_visible)
        products_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in ProductsPage.Header.tabzilla_links_list:
            url = products_page.link_destination(link.get('locator'))
            if url.find(link.get('url_suffix')) < 1:
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_product_nav_links_are_visible(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in products_page.product_nav_links_list:
            if not products_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_product_nav_link_destinations_are_correct(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in products_page.product_nav_links_list:
            url = products_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_product_nav_link_urls_are_valid(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_urls = []
        for link in products_page.product_nav_links_list:
            url = products_page.link_destination(link.get('locator'))
            response_code = products_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_images_are_visible(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_images = []
        for image in products_page.images_list:
            if not products_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_image_srcs_are_correct(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_images = []
        for image in products_page.images_list:
            src = products_page.image_source(image.get('locator'))
            if not src.endswith(image.get('img_name_suffix')):
                bad_images.append('%s does not end with %s' % (src, image.get('img_name_suffix')))
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_firefox_links_are_visible(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in products_page.firefox_links_list:
            if not products_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_firefox_link_destinations_are_correct(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in products_page.firefox_links_list:
            url = products_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_firefox_link_urls_are_valid(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_urls = []
        for link in products_page.firefox_links_list:
            url = products_page.link_destination(link.get('locator'))
            response_code = products_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_mozilla_links_are_visible(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in products_page.mozilla_links_list:
            if not products_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_mozilla_link_destinations_are_correct(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in products_page.mozilla_links_list:
            url = products_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_mozilla_link_urls_are_valid(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_urls = []
        for link in products_page.mozilla_links_list:
            url = products_page.link_destination(link.get('locator'))
            response_code = products_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_developers_links_are_visible(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in products_page.developers_links_list:
            if not products_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_developers_link_destinations_are_correct(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_links = []
        for link in products_page.developers_links_list:
            url = products_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_developers_link_urls_are_valid(self, mozwebqa):
        products_page = ProductsPage(mozwebqa)
        products_page.go_to_page()
        bad_urls = []
        for link in products_page.developers_links_list:
            url = products_page.link_destination(link.get('locator'))
            response_code = products_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))
