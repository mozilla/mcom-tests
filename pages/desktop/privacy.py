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
            'locator': (By.CSS_SELECTOR, '.policy-websites'),
            'url_suffix': '/privacy/websites/',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-firefox'),
            'url_suffix': '/privacy/firefox/',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-firefox-os'),
            'url_suffix': '/privacy/firefox-os/',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-firefox-cloud'),
            'url_suffix': '/privacy/firefox-cloud/',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-marketplace'),
            'url_suffix': 'https://marketplace.firefox.com/privacy-policy',
        }, {
            'locator': (By.CSS_SELECTOR, '.policy-persona'),
            'url_suffix': '/persona/privacy-policy/',
        }
    ]

    section_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#side-principles > p > a'),
            'url_suffix': 'privacy/principles/'

        }, {
            'locator': (By.CSS_SELECTOR, '#side-involved > p:nth-of-type(1) > a'),
            'url_suffix': '/mozilla.governance'

        }, {
            'locator': (By.CSS_SELECTOR, '#side-involved > p:nth-of-type(2) > a:nth-of-type(1)'),
            'url_suffix': '/privacy/'

        }, {
            'locator': (By.CSS_SELECTOR, '#side-involved > p:nth-of-type(2) > a:nth-of-type(2)'),
            'url_suffix': '/Privacy'

        }, {
            'locator': (By.CSS_SELECTOR, '#side-archives > h2 > a'),
            'url_suffix': '/privacy/archive/'

        }
    ]
