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
        Assert.contains(about_page.footer.expected_footer_logo_destination,
                        about_page.footer.footer_logo_destination)
        Assert.contains(about_page.footer.expected_footer_logo_img,
                        about_page.footer.footer_logo_img)
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
        Assert.contains(about_page.footer.expected_footer_logo_destination,
                        about_page.footer.footer_logo_destination)
        Assert.contains(about_page.footer.expected_footer_logo_img,
                        about_page.footer.footer_logo_img)
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
            if not url.endswith(link.get('url_suffix')):
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
    def test_get_mozilla_updates_links_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_email_input).click()
        about_page.wait_for_element_visible(*about_page.GetMozillaUpdates._get_mozilla_updates_privacy_checkbox)
        bad_links = []
        for link in about_page.GetMozillaUpdates.get_mozilla_updates_link_list:
            if not about_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_get_mozilla_updates_link_destinations_are_correct(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_links = []
        for link in about_page.GetMozillaUpdates.get_mozilla_updates_link_list:
            url = about_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_get_mozilla_updates_link_urls_are_valid(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        bad_urls = []
        for link in about_page.GetMozillaUpdates.get_mozilla_updates_link_list:
            url = about_page.link_destination(link.get('locator'))
            response_code = about_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_get_mozilla_updates_form_elements_are_visible(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_email_input).click()
        about_page.wait_for_element_visible(*about_page.GetMozillaUpdates._get_mozilla_updates_privacy_checkbox)
        about_page.is_element_visible(*about_page.GetMozillaUpdates._get_mozilla_updates_country_select)

    def test_get_mozilla_updates_form_submit_is_successful(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        valid_email = 'noreply@mozilla.com'
        country = 'US'
        success_url = 'https://donate.mozilla.org/page/st/sign-up-for-mozilla'
        about_page.go_to_page()
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_email_input).click()
        about_page.wait_for_element_visible(*about_page.GetMozillaUpdates._get_mozilla_updates_privacy_checkbox)
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_email_input).send_keys(valid_email)
        about_page.select_option(country, about_page.GetMozillaUpdates._get_mozilla_updates_country_select)
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_privacy_checkbox).click()
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_submit_button).click()
        Assert.true(success_url == about_page.url_current_page[:len(success_url)],
            'Expected current URL to be %s, found %s instead.' % (success_url, about_page.url_current_page[:len(success_url)]))

    def test_get_mozilla_updates_form_invalid_email(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        invalid_email = 'noreplymozilla.com'
        country = 'US'
        about_page.go_to_page()
        mozillabased_url = about_page.url_current_page
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_email_input).click()
        about_page.wait_for_element_visible(*about_page.GetMozillaUpdates._get_mozilla_updates_privacy_checkbox)
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_email_input).send_keys(invalid_email)
        about_page.select_option(country, about_page.GetMozillaUpdates._get_mozilla_updates_country_select)
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_privacy_checkbox).click()
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_submit_button).click()
        Assert.true(mozillabased_url == about_page.url_current_page[:len(mozillabased_url)],
            'Expected current URL to be %s, found %s instead.' % (mozillabased_url, about_page.url_current_page[:len(mozillabased_url)]))

    def test_get_mozilla_updates_form_privacy_policy_unchecked(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        valid_email = 'noreply@mozilla.com'
        country = 'US'
        about_page.go_to_page()
        mozillabased_url = about_page.url_current_page
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_email_input).click()
        about_page.wait_for_element_visible(*about_page.GetMozillaUpdates._get_mozilla_updates_privacy_checkbox)
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_email_input).send_keys(valid_email)
        about_page.select_option(country, about_page.GetMozillaUpdates._get_mozilla_updates_country_select)
        about_page.selenium.find_element(*about_page.GetMozillaUpdates._get_mozilla_updates_submit_button).click()
        Assert.true(mozillabased_url == about_page.url_current_page[:len(mozillabased_url)],
            'Expected current URL to be %s, found %s instead.' % (mozillabased_url, about_page.url_current_page[:len(mozillabased_url)]))
