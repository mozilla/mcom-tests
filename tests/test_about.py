# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from pages.desktop.about import AboutPage


class TestAboutPage:

    @pytest.mark.nondestructive
    def test_footer_link_destinations_are_correct(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_links = []
        for link in AboutPage.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.link_check
    @pytest.mark.nondestructive
    def test_footer_links_are_valid(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_urls = []
        for link in AboutPage.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            response_code = page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @pytest.mark.nondestructive
    def test_navbar_links_are_visible(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_links = []
        for link in page.Header.nav_links_list:
            if not page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        assert [] == bad_links

    @pytest.mark.nondestructive
    def test_navbar_link_destinations_are_correct(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_links = []
        for link in page.Header.nav_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.link_check
    @pytest.mark.nondestructive
    def test_navbar_link_urls_are_valid(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_urls = []
        for link in page.Header.nav_links_list:
            url = page.link_destination(link.get('locator'))
            response_code = page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @pytest.mark.nondestructive
    def test_major_link_destinations_are_correct(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_links = []
        for link in page.major_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.link_check
    @pytest.mark.nondestructive
    def test_major_link_urls_are_valid(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_urls = []
        for link in page.major_links_list:
            url = page.link_destination(link.get('locator'))
            response_code = page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @pytest.mark.nondestructive
    def test_sign_up_form_is_visible(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        assert page.is_sign_up_form_present, 'The sign up form is not present on the page.'

    @pytest.mark.nondestructive
    def test_sign_up_form_fields_are_visible(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        page.expand_sign_up_form()
        bad_fields = []
        for field in page.sign_up_form_fields:
            if not page.is_element_visible(*field.get('locator')):
                bad_fields.append('The field at %s is not visible' % field.get('locator')[1:])
        assert [] == bad_fields

    @pytest.mark.nondestructive
    def test_sign_up_form_links_are_visible(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        page.expand_sign_up_form()
        page.wait_for_element_visible(*page._sign_up_form_privacy_checkbox_locator)
        bad_links = []
        for link in page.sign_up_form_link_list:
            if not page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        assert [] == bad_links

    @pytest.mark.nondestructive
    def test_sign_up_form_link_destinations_are_correct(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_links = []
        for link in page.sign_up_form_link_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.link_check
    @pytest.mark.nondestructive
    def test_sign_up_form_link_urls_are_valid(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        bad_urls = []
        for link in page.sign_up_form_link_list:
            url = page.link_destination(link.get('locator'))
            response_code = page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @pytest.mark.nondestructive
    def test_sign_up_form_elements_are_visible(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        page.expand_sign_up_form()
        page.wait_for_element_visible(*page._sign_up_form_privacy_checkbox_locator)
        assert page.is_element_visible(*page._sign_up_form_country_select_locator)

    @pytest.mark.nondestructive
    def test_sign_up_form_invalid_email(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        invalid_email = 'noreplymozilla.com'
        country = 'US'
        expected_url = page.url_current_page
        page.expand_sign_up_form()
        page.wait_for_element_visible(*page._sign_up_form_privacy_checkbox_locator)
        page.input_email(invalid_email)
        page.select_option(country, page._sign_up_form_country_select_locator)
        page.check_privacy_checkbox()
        page.submit_form()
        assert expected_url == page.url_current_page[:len(expected_url)]

    @pytest.mark.nondestructive
    def test_sign_up_form_privacy_policy_unchecked(self, base_url, selenium):
        page = AboutPage(base_url, selenium).open()
        valid_email = 'noreply@mozilla.com'
        country = 'US'
        expected_url = page.url_current_page
        page.expand_sign_up_form()
        page.wait_for_element_visible(*page._sign_up_form_privacy_checkbox_locator)
        page.input_email(valid_email)
        page.select_option(country, page._sign_up_form_country_select_locator)
        page.submit_form()
        assert expected_url == page.url_current_page[:len(expected_url)]
