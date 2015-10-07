# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from pages.desktop.about import AboutPage

link_check = pytest.mark.link_check
nondestructive = pytest.mark.nondestructive


class TestAboutPage:

    @nondestructive
    def test_footer_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in AboutPage.Footer.footer_links_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_footer_links_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in AboutPage.Footer.footer_links_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @nondestructive
    def test_navbar_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.Header.nav_links_list:
            if not about_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        assert [] == bad_links

    @nondestructive
    def test_navbar_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.Header.nav_links_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_navbar_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in about_page.Header.nav_links_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @nondestructive
    def test_major_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.major_links_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_major_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in about_page.major_links_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @nondestructive
    def test_sign_up_form_is_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        assert about_page.is_sign_up_form_present, 'The sign up form is not present on the page.'

    @nondestructive
    def test_sign_up_form_fields_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.expand_sign_up_form()
        bad_fields = []
        for field in about_page.sign_up_form_fields:
            if not about_page.is_element_visible(*field.get('locator')):
                bad_fields.append('The field at %s is not visible' % field.get('locator')[1:])
        assert [] == bad_fields

    @nondestructive
    def test_sign_up_form_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.expand_sign_up_form()
        about_page.wait_for_element_visible(*about_page._sign_up_form_privacy_checkbox_locator)
        bad_links = []
        for link in about_page.sign_up_form_link_list:
            if not about_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        assert [] == bad_links

    @nondestructive
    def test_sign_up_form_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.sign_up_form_link_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_sign_up_form_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in about_page.sign_up_form_link_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @nondestructive
    def test_sign_up_form_elements_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.expand_sign_up_form()
        about_page.wait_for_element_visible(*about_page._sign_up_form_privacy_checkbox_locator)
        assert about_page.is_element_visible(*about_page._sign_up_form_country_select_locator)

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
        assert expected_url == about_page.url_current_page[:len(expected_url)]

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
        assert expected_url == about_page.url_current_page[:len(expected_url)]
