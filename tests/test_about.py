#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert
from pages.desktop.about import AboutPage


class TestAboutPage:

    @pytest.mark.nondestructive
    def test_footer_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in AboutPage.Footer.footer_links_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_footer_links_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in AboutPage.Footer.footer_links_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad links found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_tabzilla_link_destinations_are_corrects(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in AboutPage.Header.tabzilla_links_list:
            url = about_page.link_destination(link.get('locator'))
            if url.find(link.get('url_suffix')) < 1:
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        bad_urls = []
        for link in AboutPage.Header.tabzilla_links_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad links found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.header.is_tabzilla_panel_visible)
        about_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in about_page.header.tabzilla_links_list:
            if not about_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_navbar_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.Header.nav_links_list:
            if not about_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_navbar_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.Header.nav_links_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_navbar_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in about_page.Header.nav_links_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_major_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.major_links_list:
            if not about_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_major_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.major_links_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_major_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in about_page.major_links_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_sign_up_form_is_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.true(about_page.is_sign_up_form_present, 'The sign up form is not present on the page.')

    @pytest.mark.nondestructive
    def test_sign_up_form_fields_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.expand_sign_up_form()
        bad_fields = []
        for field in about_page.sign_up_form_fields:
            if not about_page.is_element_visible(*field.get('locator')):
                bad_fields.append('The field at %s is not visible' % field.get('locator')[1:])
        Assert.equal(0, len(bad_fields), '%s bad fields found: ' % len(bad_fields) + ', '.join(bad_fields))

    @pytest.mark.nondestructive
    def test_sign_up_form_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.expand_sign_up_form()
        about_page.wait_for_element_visible(*about_page._sign_up_form_privacy_checkbox_locator)
        bad_links = []
        for link in about_page.sign_up_form_link_list:
            if not about_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_sign_up_form_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.sign_up_form_link_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_sign_up_form_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in about_page.sign_up_form_link_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_sign_up_form_elements_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.expand_sign_up_form()
        about_page.wait_for_element_visible(*about_page._sign_up_form_privacy_checkbox_locator)
        about_page.is_element_visible(*about_page._sign_up_form_country_select_locator)

    def test_sign_up_form_submit_is_successful(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        valid_email = 'noreply@mozilla.com'
        country = 'US'
        success_url_slug = 'sign-up-for-mozilla'
        about_page.go_to_page()
        about_page.expand_sign_up_form()
        about_page.wait_for_element_visible(*about_page._sign_up_form_privacy_checkbox_locator)
        about_page.input_email(valid_email)
        about_page.select_option(country, about_page._sign_up_form_country_select_locator)
        about_page.check_privacy_checkbox()
        about_page.submit_form()
        Assert.true(success_url_slug in about_page.url_current_page,
                    'Expected current URL slug to be %s, but was not found in %s.' %
                    (success_url_slug, about_page.url_current_page))

    def test_sign_up_form_invalid_email(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        invalid_email = 'noreplymozilla.com'
        country = 'US'
        about_page.go_to_page()
        expected_url = about_page.url_current_page
        about_page.expand_sign_up_form()
        about_page.wait_for_element_visible(*about_page._sign_up_form_privacy_checkbox_locator)
        about_page.input_email(invalid_email)
        about_page.select_option(country, about_page._sign_up_form_country_select_locator)
        about_page.check_privacy_checkbox()
        about_page.submit_form()
        Assert.true(expected_url == about_page.url_current_page[:len(expected_url)],
                    'Expected current URL to be %s, found %s instead.' %
                    (expected_url, about_page.url_current_page[:len(expected_url)]))

    def test_sign_up_form_privacy_policy_unchecked(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        valid_email = 'noreply@mozilla.com'
        country = 'US'
        about_page.go_to_page()
        expected_url = about_page.url_current_page
        about_page.expand_sign_up_form()
        about_page.wait_for_element_visible(*about_page._sign_up_form_privacy_checkbox_locator)
        about_page.input_email(valid_email)
        about_page.select_option(country, about_page._sign_up_form_country_select_locator)
        about_page.submit_form()
        Assert.true(expected_url == about_page.url_current_page[:len(expected_url)],
                    'Expected current URL to be %s, found %s instead.' %
                    (expected_url, about_page.url_current_page[:len(expected_url)]))
