#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Privacy(Base):

    def go_to_page(self):
        self.open('/privacy/')

    privacy_policy_list = [
        {
            'locator': (By.CSS_SELECTOR, '.policy-moz-websites'),
            'url_suffix': '/privacy-policy.html',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-firefox'),
            'url_suffix': '/legal/privacy/firefox.html',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-thunderbird'),
            'url_suffix': '/en-US/thunderbird/legal/privacy/',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-marketplace'),
            'url_suffix': 'https://marketplace.firefox.com/privacy-policy',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-sync'),
            'url_suffix': 'https://services.mozilla.com/privacy-policy/',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-test-pilot'),
            'url_suffix': 'https://testpilot.mozillalabs.com/privacy.php',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-persona'),
            'url_suffix': '/persona/privacy-policy/',
        }
    ]

    _principles_section_link = (By.CSS_SELECTOR, '#top > ul > li:nth-of-type(1) > a')
    _information_section_link = (By.CSS_SELECTOR, '#top > ul > li:nth-of-type(2) > a')
    _choices_section_link = (By.CSS_SELECTOR, '#top > ul > li:nth-of-type(3) > a')
    _share_section_link = (By.CSS_SELECTOR, '#top > ul > li:nth-of-type(4) > a')
    _contact_us_section_link = (By.CSS_SELECTOR, '#top > ul > li:nth-of-type(5) > a')
    _back_to_top_link = (By.CSS_SELECTOR, 'p:nth-of-type(2)> .top')

    def click_back_to_top(self):
        self.selenium.find_element(*self._back_to_top_link).click()

    def click_principles_section(self):
        self.selenium.find_element(*self._principles_section_link).click()

    def click_information_section(self):
        self.selenium.find_element(*self._information_section_link).click()

    def click_choices_section(self):
        self.selenium.find_element(*self._choices_section_link).click()

    def click_share_section(self):
        self.selenium.find_element(*self._share_section_link).click()

    def click_contact_us_section(self):
        self.selenium.find_element(*self._contact_us_section_link).click()
