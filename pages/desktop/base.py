# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait

from pages.page import Page


class Base(Page):

    def wait_for_page_to_load(self):
        el = self.selenium.find_element(By.TAG_NAME, 'html')
        Wait(self.selenium, self.timeout).until(
            lambda s: 'loaded' in el.get_attribute('class'))
        return self

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

        nav_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-child(1) > a'),
                'url_suffix': '/about/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-child(2) > a'),
                'url_suffix': '/contribute/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-child(3) > a'),
                'url_suffix': '/firefox/products/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-child(4) > a'),
                'url_suffix': ('//donate.mozilla.org/?presets=100,50,25,15'
                               '&amount=50&ref=EOYFR2015&utm_campaign=EOYFR2015'
                               '&utm_source=mozilla.org&utm_medium=referral&utm_content=header'),
            }
        ]

    class Footer(Page):

        _footer_locator = (By.CSS_SELECTOR, '#colophon')
        _footer_logo_link_locator = (By.CSS_SELECTOR, 'h1.logo> a')
        footer_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#colophon p.license a'),
                'url_suffix': '/foundation/licensing/website-content/',

            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-join > li:nth-of-type(1) >a'),
                'url_suffix': '/contact/',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-join > li:nth-of-type(2) >a'),
                'url_suffix': '/about/partnerships/',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-join > li:nth-of-type(3) >a'),
                'url_suffix': ('//donate.mozilla.org/'),
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-join > li:nth-of-type(4) >a'),
                'url_suffix': '/contribute/friends/',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-join > li:nth-of-type(5) >a'),
                'url_suffix': '//wiki.mozilla.org/Webdev/GetInvolved/mozilla.org',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-legal>li:nth-of-type(1) >a'),
                'url_suffix': '/privacy/',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-legal>li:nth-of-type(2) >a'),
                'url_suffix': '/privacy/websites/#cookies',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-legal>li:nth-of-type(3) >a'),
                'url_suffix': '/about/legal/',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-legal>li:nth-of-type(4) >a'),
                'url_suffix': '/legal/fraud-report/',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-social>li:nth-child(1) > ul > li:nth-child(1) > a'),
                'url_suffix': 'twitter.com/mozilla',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-social>li:nth-child(1) > ul > li:nth-child(2) > a'),
                'url_suffix': 'facebook.com/mozilla',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-social>li:nth-child(2) > ul > li:nth-child(1) > a'),
                'url_suffix': 'twitter.com/firefox',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-social>li:nth-child(2) > ul > li:nth-child(2) > a'),
                'url_suffix': 'facebook.com/Firefox',
            }, {
                'locator': (By.CSS_SELECTOR, 'ul.links-social>li:nth-child(2) > ul > li:nth-child(3) > a'),
                'url_suffix': 'www.youtube.com/firefoxchannel',
            },
        ]

        @property
        def footer_logo_destination(self):
            footer_logo_link = self.selenium.find_element(*self._footer_logo_link_locator)
            return footer_logo_link.get_attribute('href')

    class DownloadRegion(Page):
        _osx_download_locator = (By.CSS_SELECTOR, '.os_osx > a')
        _windows_download_locator = (By.CSS_SELECTOR, '.os_win > a')
        _linux_download_locator = (By.CSS_SELECTOR, '.os_linux > a')

        _systems_and_languages_locator = (By.CSS_SELECTOR, '.download-other.os_linux.os_osx.os_win > a:nth-of-type(1)')
        _whats_new_locator = (By.CSS_SELECTOR, '.download-other.os_linux.os_osx.os_win > a:nth-of-type(2)')
        _privacy_locator = (By.CSS_SELECTOR, '.download-other.os_linux.os_osx.os_win > a:nth-of-type(3)')

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
