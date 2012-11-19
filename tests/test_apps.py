#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.apps import Apps
from unittestzero import Assert


class TestApps:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        apps_page = Apps(mozwebqa)
        apps_page.go_to_page()
        Assert.contains(apps_page.footer.expected_footer_logo_destination,
                        apps_page.footer.footer_logo_destination)
        Assert.contains(apps_page.footer.expected_footer_logo_img,
                        apps_page.footer.footer_logo_img)
        bad_links = []
        for link in Apps.Footer.footer_links_list:
            url = apps_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        apps_page = Apps(mozwebqa)
        apps_page.go_to_page()
        Assert.true(apps_page.header.is_tabzilla_panel_visible)
        apps_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Apps.Header.tabzilla_links_list:
            url = apps_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_page_links_are_visible(self, mozwebqa):
        apps_page = Apps(mozwebqa)
        apps_page.go_to_page()
        bad_links = []
        for link in apps_page.page_links_list:
            if not apps_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_page_link_destinations_are_correct(self, mozwebqa):
        apps_page = Apps(mozwebqa)
        apps_page.go_to_page()
        bad_links = []
        for link in apps_page.page_links_list:
            url = apps_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_page_link_urls_are_valid(self, mozwebqa):
        apps_page = Apps(mozwebqa)
        apps_page.go_to_page()
        bad_urls = []
        for link in apps_page.page_links_list:
            url = apps_page.link_destination(link.get('locator'))
            if not apps_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_showcased_apps_link_urls_are_valid(self, mozwebqa):
        apps_page = Apps(mozwebqa)
        apps_page.go_to_page()
        bad_urls = []
        for link in apps_page.showcased_apps_links:
            url = link.get_attribute('href')
            if not apps_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_sign_up_form_is_visible(self, mozwebqa):
        apps_page = Apps(mozwebqa)
        apps_page.go_to_page()
        Assert.true(apps_page.is_sign_up_form_present, 'The sign up form is not present on the page.')
        apps_page.expand_sign_up_form()
        Assert.true(apps_page.are_sign_up_form_fields_visible, 'The fields on the sign up form are not all visible.')
