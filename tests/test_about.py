#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.about import AboutPage


class TestAboutPage:

    @pytest.mark.nondestructive
    def test_footer_section_links(self, mozwebqa):
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
    def test_footer_section_urls(self, mozwebqa):
        about_page = AboutPage(mozwebqa)
        about_page.go_to_page()
        Assert.contains(about_page.footer.expected_footer_logo_destination,
                        about_page.footer.footer_logo_destination)
        Assert.contains(about_page.footer.expected_footer_logo_img,
                        about_page.footer.footer_logo_img)
        bad_links = []
        for link in AboutPage.Footer.footer_links_list:
            url = about_page.link_destination(link.get('locator'))
            if not about_page.is_valid_link(url):
                bad_links.append('%s is not a valid url.' % url)
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
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
        bad_links = []
        for link in AboutPage.Header.tabzilla_links_list:
            url = about_page.link_destination(link.get('locator'))
            if not about_page.is_valid_link(url):
                bad_links.append('%s is not a valid url.' % url)
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

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
            if not about_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
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
            if not about_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))
