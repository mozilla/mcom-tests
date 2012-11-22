#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.page import Page


class Base(Page):

    @property
    def header(self):
        return self.Header(self.testsetup)

    @property
    def footer(self):
        return self.Footer(self.testsetup)

    @property
    def downloadRegion(self):
        return self.DownloadRegion(self.testsetup)

    def link_destination(self, locator):
        link = self.selenium.find_element(*locator)
        return link.get_attribute('href')

    def image_source(self, locator):
        link = self.selenium.find_element(*locator)
        return link.get_attribute('src')

    class Header(Page):

        _tabzilla = (By.ID, 'tabzilla')
        _tabzilla_panel = (By.ID, 'tabzilla-panel')
        _tabzilla_search_textbox = (By.CSS_SELECTOR, '#tabzilla-search #q')

        tabzilla_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(1) > a'),
                'url_suffix': '/mission/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(2) > a'),
                'url_suffix': '/about/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(3) > a'),
                'url_suffix': '/projects/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(4) > a'),
                'url_suffix': 'support.mozilla.org/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(5) > a'),
                'url_suffix': 'developer.mozilla.org/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(1) > a'),
                'url_suffix': 'www.mozilla.org/firefox',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(2) > a'),
                'url_suffix': 'www.mozilla.org/thunderbird',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(3) > a'),
                'url_suffix': 'www.mozilla.org/firefoxos',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(1) > a'),
                'url_suffix': 'webfwd.org/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(2) > a'),
                'url_suffix': 'mozillalabs.com/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(3) > a'),
                'url_suffix': 'webmaker.org/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(1) > a'),
                'url_suffix': 'www.mozilla.org/contribute/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(2) > a'),
                'url_suffix': '/about/careers.html',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(3) > a'),
                'url_suffix': '/about/mozilla-spaces/',
            }, {
                'locator': (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(4) > a'),
                'url_suffix': 'donate.mozilla.org/',
            },
        ]

        nav_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-child(1) > a'),
                'url_suffix': '/mission/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-child(2) > a'),
                'url_suffix': '/about/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-child(3) > a'),
                'url_suffix': '/products/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-child(4) > a'),
                'url_suffix': '/contribute/',
            }
        ]

        def toggle_tabzilla_dropdown(self):
            toggle_state = self.selenium.execute_script('return Tabzilla.opened')
            self.selenium.find_element(*self._tabzilla).click()
            WebDriverWait(self.selenium, 5).until(lambda state: toggle_state != state.execute_script('return Tabzilla.opened'))

        @property
        def is_tabzilla_panel_visible(self):
            return self.is_element_visible(*self._tabzilla)

        @property
        def is_tabzilla_search_box_visible(self):
            return self.is_element_visible(*self._tabzilla_search_textbox)

    class Footer(Page):

        _footer_locator = (By.CSS_SELECTOR, '#colophon')
        _footer_logo_link_locator = (By.CSS_SELECTOR, '.footer-logo > a')
        _footer_logo_img_locator = (By.CSS_SELECTOR, '.footer-logo img')
        expected_footer_logo_destination = '/en-US/'
        expected_footer_logo_img = '/media/img/sandstone/footer-mozilla.png'

        footer_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#colophon div.footer-license p:nth-child(1) a'),
                'url_suffix': '/foundation/licensing/website-content.html',
            }, {
                'locator': (By.CSS_SELECTOR, '#colophon ul.footer-nav:nth-of-type(1) li:nth-child(1) a'),
                'url_suffix': '/about/contact.html#map-mountain_view',
            }, {
                'locator': (By.CSS_SELECTOR, '#colophon ul.footer-nav:nth-of-type(1) li:nth-child(2) a'),
                'url_suffix': '/privacy/',
            }, {
                'locator': (By.CSS_SELECTOR, '#colophon ul.footer-nav:nth-of-type(1) li:nth-child(3) a'),
                'url_suffix': '/about/legal.html',
            }, {
                'locator': (By.CSS_SELECTOR, '#colophon ul.footer-nav:nth-of-type(1) li:nth-child(4) a'),
                'url_suffix': '/legal/fraud-report/index.html',
            }, {
                'locator': (By.CSS_SELECTOR, '#colophon ul.footer-nav:nth-of-type(2) li:nth-child(1) a'),
                'url_suffix': 'twitter.com/firefox',
            }, {
                'locator': (By.CSS_SELECTOR, '#colophon ul.footer-nav:nth-of-type(2) li:nth-child(2) a'),
                'url_suffix': 'facebook.com/Firefox',
            }, {
                'locator': (By.CSS_SELECTOR, '#colophon ul.footer-nav:nth-of-type(2) li:nth-child(3) a'),
                'url_suffix': 'affiliates.mozilla.org/',
            },
        ]

        @property
        def footer_logo_destination(self):
            footer_logo_link = self.selenium.find_element(*self._footer_logo_link_locator)
            return footer_logo_link.get_attribute('href')

        @property
        def footer_logo_img(self):
            footer_logo_img = self.selenium.find_element(*self._footer_logo_img_locator)
            return footer_logo_img.get_attribute('src')

    class DownloadRegion(Page):

        _osx_download_locator = (By.CSS_SELECTOR, '.os_osx > a')
        _windows_download_locator = (By.CSS_SELECTOR, '.os_windows > a')
        _linux_download_locator = (By.CSS_SELECTOR, '.os_linux > a')

        _systems_and_languages_locator = (By.CSS_SELECTOR, '.download-other > a:nth-of-type(1)')
        _whats_new_locator = (By.CSS_SELECTOR, '.download-other > a:nth-of-type(2)')
        _privacy_locator = (By.CSS_SELECTOR, '.download-other > a:nth-of-type(3)')

        @property
        def is_download_link_visible(self):
            return self.is_element_visible(*self._osx_download_locator) or \
                self.is_element_visible(*self._windows_download_locator) or \
                self.is_element_visible(*self._linux_download_locator)

        @property
        def are_secondary_links_visible(self):
            return self.is_element_visible(*self._systems_and_languages_locator) and \
                self.is_element_visible(*self._whats_new_locator) and \
                self.is_element_visible(*self._privacy_locator)
