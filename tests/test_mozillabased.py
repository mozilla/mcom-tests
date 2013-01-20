#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
import pytest
from pages.desktop.mozillabased import MozillaBasedPage
from unittestzero import Assert


class TestMozillaBasedPagePage:

    @pytest.mark.nondestructive
    def test_breadcrumbs_links_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.breadcrumbs_link_list:
            if not mozillabased_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_breadcrumbs_link_destinations_are_correct(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.breadcrumbs_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_breadcrumbs_link_urls_are_valid(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_urls = []
        for link in mozillabased_page.breadcrumbs_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            response_code = mozillabased_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_main_feature_links_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.main_feature_link_list:
            if not mozillabased_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_main_feature_link_destinations_are_correct(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.main_feature_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_main_feature_link_urls_are_valid(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_urls = []
        for link in mozillabased_page.main_feature_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            response_code = mozillabased_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_billboard_links_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.billboard_link_list:
            if not mozillabased_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_destinations_are_correct(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.billboard_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_urls_are_valid(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_urls = []
        for link in mozillabased_page.billboard_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            response_code = mozillabased_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_product_links_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.product_link_list:
            if not mozillabased_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_product_link_destinations_are_correct(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.product_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_product_link_urls_are_valid(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_urls = []
        for link in mozillabased_page.product_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            response_code = mozillabased_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_find_out_more_links_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.find_out_more_link_list:
            if not mozillabased_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_find_out_more_link_destinations_are_correct(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.find_out_more_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_find_out_more_link_urls_are_valid(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_urls = []
        for link in mozillabased_page.find_out_more_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            response_code = mozillabased_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_get_mozilla_updates_links_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_email_input).click()
        mozillabased_page.wait_for_element_visible(*mozillabased_page._get_mozilla_updates_privacy_checkbox)
        bad_links = []
        for link in mozillabased_page.get_mozilla_updates_link_list:
            if not mozillabased_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_get_mozilla_updates_link_destinations_are_correct(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_links = []
        for link in mozillabased_page.get_mozilla_updates_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_get_mozilla_updates_link_urls_are_valid(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_urls = []
        for link in mozillabased_page.get_mozilla_updates_link_list:
            url = mozillabased_page.link_destination(link.get('locator'))
            response_code = mozillabased_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_get_mozilla_updates_form_elements_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_email_input).click()
        mozillabased_page.wait_for_element_visible(*mozillabased_page._get_mozilla_updates_privacy_checkbox)
        mozillabased_page.is_element_visible(*mozillabased_page._get_mozilla_updates_country_select)

    def test_get_mozilla_updates_form_submit_is_successful(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_email_input).click()
        mozillabased_page.wait_for_element_visible(*mozillabased_page._get_mozilla_updates_privacy_checkbox)
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_email_input).send_keys(mozillabased_page._valid_email)
        mozillabased_page.select_option(mozillabased_page._country, mozillabased_page._get_mozilla_updates_country_select)
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_privacy_checkbox).click()
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_submit_button).click()
        Assert.true(mozillabased_page._get_mozilla_updates_success_url == mozillabased_page.url_current_page[:len(mozillabased_page._get_mozilla_updates_success_url)], 'Expected current URL to be %s, found %s instead.' % (mozillabased_page._get_mozilla_updates_success_url, mozillabased_page.url_current_page[:len(mozillabased_page._get_mozilla_updates_success_url)]))

    def test_get_mozilla_updates_form_invalid_email(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        mozillabased_url = mozillabased_page.url_current_page
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_email_input).click()
        mozillabased_page.wait_for_element_visible(*mozillabased_page._get_mozilla_updates_privacy_checkbox)
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_email_input).send_keys(mozillabased_page._invalid_email)
        mozillabased_page.select_option(mozillabased_page._country, mozillabased_page._get_mozilla_updates_country_select)
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_privacy_checkbox).click()
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_submit_button).click()
        Assert.true(mozillabased_url == mozillabased_page.url_current_page[:len(mozillabased_url)], 'Expected current URL to be %s, found %s instead.' % (mozillabased_url, mozillabased_page.url_current_page[:len(mozillabased_url)]))

    def test_get_mozilla_updates_form_privacy_policy_unchecked(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        mozillabased_url = mozillabased_page.url_current_page
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_email_input).click()
        mozillabased_page.wait_for_element_visible(*mozillabased_page._get_mozilla_updates_privacy_checkbox)
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_email_input).send_keys(mozillabased_page._valid_email)
        mozillabased_page.select_option(mozillabased_page._country, mozillabased_page._get_mozilla_updates_country_select)
        mozillabased_page.selenium.find_element(*mozillabased_page._get_mozilla_updates_submit_button).click()
        Assert.true(mozillabased_url == mozillabased_page.url_current_page[:len(mozillabased_url)], 'Expected current URL to be %s, found %s instead.' % (mozillabased_url, mozillabased_page.url_current_page[:len(mozillabased_url)]))

    @pytest.mark.nondestructive
    def test_product_images_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_images = []
        for link in mozillabased_page.product_image_list:
            if not mozillabased_page.is_element_visible(*link.get('locator')):
                bad_images.append('The image at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_billboard_images_are_visible(self, mozwebqa):
        mozillabased_page = MozillaBasedPage(mozwebqa)
        mozillabased_page.go_to_page()
        bad_images = []
        for link in mozillabased_page.billboard_image_list:
            if not mozillabased_page.is_element_visible(*link.get('locator')):
                bad_images.append('The image at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_footer_section_links(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        Assert.contains(page.footer.expected_footer_logo_destination,
                        page.footer.footer_logo_destination)
        Assert.contains(page.footer.expected_footer_logo_img,
                        page.footer.footer_logo_img)
        bad_links = []
        for link in MozillaBasedPage.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        Assert.true(page.header.is_tabzilla_panel_visible)
        page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in MozillaBasedPage.Header.tabzilla_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_visible(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        Assert.true(page.header.is_tabzilla_panel_visible)
        page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in page.header.tabzilla_links_list:
            if not page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_navbar_links_are_visible(self, mozwebqa):
        page = MozillaBasedPage(mozwebqa)
        page.go_to_page()
        bad_links = []
        for link in page.Header.nav_links_list:
            if not page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
