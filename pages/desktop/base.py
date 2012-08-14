#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.page import Page


class Base(Page):
    
    _desktop_link = (By.CSS_SELECTOR, '#nav-main-features > a')
    _mobile_link = (By.CSS_SELECTOR, '#nav-main-mobile > a')
    _releases_link = (By.CSS_SELECTOR, '#nav-main-releases > a')
    _addons_link = (By.CSS_SELECTOR, '#nav-main-addons > a')
    _support_link = (By.CSS_SELECTOR, '#nav-main-support > a')
    _about_link = (By.CSS_SELECTOR, '#nav-main-about > a')

    @property
    def header(self):
        return self.Header(self.testsetup)

    @property
    def footer(self):
        return self.Footer(self.testsetup)

    @property
    def downloadRegion(self):
        return self.DownloadRegion(self.testsetup)

    class Header(Page):

        _tabzilla = (By.ID, 'tabzilla')
        _tabzilla_panel = (By.ID, 'tabzilla-panel')
        _tabzilla_about_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(2) > a')
        _tabzilla_mission_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(1) > a')
        _tabzilla_projects_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(3) > a')
        _tabzilla_support_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(4) > a')
        _tabzilla_developer_network_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(5) > a')
        _tabzilla_firefox_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(1) > a')
        _tabzilla_thunderbird_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(2) > a')
        _tabzilla_webfwd_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(1) > a')
        _tabzilla_labs_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(2) > a')
        _tabzilla_webmaker_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(3) > a')
        _tabzilla_volunteer_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(1) > a')
        _tabzilla_work_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(2) > a')
        _tabzilla_findus_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(3) > a')
        _tabzilla_joinus_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(4) > a')
        _tabzilla_search_textbox = (By.CSS_SELECTOR, '#tabzilla-search #q')

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

        @property
        def are_tabzilla_links_visible(self):
            return self.is_element_visible(*self._tabzilla_mission_link) and \
                self.is_element_visible(*self._tabzilla_about_link) and \
                self.is_element_visible(*self._tabzilla_projects_link) and \
                self.is_element_visible(*self._tabzilla_support_link) and \
                self.is_element_visible(*self._tabzilla_developer_network_link) and \
                self.is_element_visible(*self._tabzilla_firefox_link) and \
                self.is_element_visible(*self._tabzilla_thunderbird_link) and \
                self.is_element_visible(*self._tabzilla_webfwd_link) and \
                self.is_element_visible(*self._tabzilla_labs_link) and \
                self.is_element_visible(*self._tabzilla_webmaker_link) and \
                self.is_element_visible(*self._tabzilla_volunteer_link) and \
                self.is_element_visible(*self._tabzilla_work_link) and \
                self.is_element_visible(*self._tabzilla_findus_link) and \
                self.is_element_visible(*self._tabzilla_joinus_link)

    class Footer(Page):

        _footer_locator = (By.CSS_SELECTOR, '#colophon')
        _footer_logo_link_locator = (By.CSS_SELECTOR, '.footer-logo > a')
        _footer_logo_img_locator = (By.CSS_SELECTOR, '.footer-logo img')
        expected_footer_logo_destination = '/en-US/'
        expected_footer_logo_img = '/media/img/sandstone/footer-mozilla.png'

        footer_links_list = [
            {
                'text': 'Creative Commons license',
                'href': '/foundation/licensing/website-content.html',
            },{
                'text': 'Contact Us',
                'href': '/en-US/about/contact.html#map-mountain_view',
            },{
                'text': 'Privacy Policy',
                'href': '/en-US/privacy-policy.html',
            },{
                'text': 'Legal Notices',
                'href': '/en-US/about/legal.html',
            },{
                'text': 'Report Trademark Abuse',
                'href': '/en-US/legal/fraud-report/index.html',
            },{
                'text': 'Twitter',
                'href': 'twitter.com/firefox',
            },{
                'text': 'Facebook',
                'href': 'facebook.com/Firefox',
            },{
                'text': 'Firefox Affiliates',
                'href': 'affiliates.mozilla.org',
            },
        ]

        def footer_link_destination(self, footer_link_text):
            footer_link = self.selenium.find_element(*self._footer_locator).find_element(
                By.LINK_TEXT, footer_link_text)
            return footer_link.get_attribute('href')

        def footer_link_functions(self, footer_link_href):
            return self.get_response_code(footer_link_href)

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
        def are_download_links_present(self):
            return self.is_element_visible(*self._osx_download_locator) or \
            self.is_element_visible(*self._windows_download_locator) or \
            self.is_element_visible(*self._linux_download_locator)

        @property
        def are_secondary_links_visible(self):
            return self.is_element_visible(*self._systems_and_languages_locator) and \
            self.is_element_visible(*self._whats_new_locator) and \
            self.is_element_visible(*self._privacy_locator)
