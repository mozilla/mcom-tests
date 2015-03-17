#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import pytest
import requests
from unittestzero import Assert
from pages.desktop.home import HomePage


class TestHomePage:

    @pytest.mark.nondestructive
    @pytest.mark.xfail("'-dev' in config.getvalue('base_url')",
                       reason='Bug 1143814 - Missing "Upcoming Events" section and Mozilla Reps Tweets on dev')
    def test_promo_links_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_urls = []
        for link in home_page.promo_links_list:
            url = home_page.link_destination(link.get('locator'))
            response_code = home_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.xfail("'-dev' in config.getvalue('base_url')",
                       reason='Bug 1143814 - Missing "Upcoming Events" section and Mozilla Reps Tweets on dev')
    @pytest.mark.nondestructive
    def test_major_link_urls_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_urls = []
        for link in home_page.major_links_list:
            url = home_page.link_destination(link.get('locator'))
            response_code = home_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.xfail("'-dev' in config.getvalue('base_url')",
                       reason='Bug 1143814 - Missing "Upcoming Events" section and Mozilla Reps Tweets on dev')
    @pytest.mark.nondestructive
    def test_major_link_destinations_are_correct(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.major_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_footer_link_destinations_are_correct(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in HomePage.Footer.footer_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_footer_links_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_urls = []
        for link in HomePage.Footer.footer_links_list:
            url = home_page.link_destination(link.get('locator'))
            response_code = home_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad links found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_sign_up_form_is_visible(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.true(home_page.is_sign_up_form_present, 'The sign up form is not present on the page.')

    @pytest.mark.nondestructive
    def test_sign_up_form_link_destinations_are_correct(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.sign_up_form_link_list:
            url = home_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_sign_up_form_link_urls_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_urls = []
        for link in home_page.sign_up_form_link_list:
            url = home_page.link_destination(link.get('locator'))
            response_code = home_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))
