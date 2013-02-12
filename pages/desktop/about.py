#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class AboutPage(Base):

    def go_to_page(self):
        self.open('/about/')

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(1) a'),
            'url_suffix': '/mission/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(2) a'),
            'url_suffix': 'careers.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(3) a'),
            'url_suffix': 'blog.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(4) a'),
            'url_suffix': '/styleguide',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(5) a'),
            'url_suffix': '/about/contact',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(1) a'),
            'url_suffix': '/products/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(2) a'),
            'url_suffix': '/contribute/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(3) a'),
            'url_suffix': 'blog.mozilla.org/press/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(4) a'),
            'url_suffix': '/privacy/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(5) a'),
            'url_suffix': '/about/partnerships',
        }
    ]

    _sign_up_form_locator = (By.ID, 'footer-email-form')
    _sign_up_form_email_input_locator = (By.ID, 'id_email')
    _sign_up_form_country_select_locator = (By.ID, 'country')
    _sign_up_form_privacy_checkbox_locator = (By.ID, 'id_privacy')
    _sign_up_form_submit_button_locator = (By.ID, 'footer_email_submit')

    sign_up_form_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'label.privacy-check-label > span > a'),
            'url_suffix': '/en-US/privacy-policy',
        },
    ]

    sign_up_form_fields = [
        {
            'locator': (By.ID, 'id_email'),
        }, {
            'locator': (By.ID, 'country'),
        }, {
            'locator': (By.ID, 'id_privacy'),
        }, {
            'locator': (By.ID, 'footer_email_submit'),
        },
    ]

    def input_email(self, email):
        self.selenium.find_element(*self._sign_up_form_email_input_locator).send_keys(email)

    def check_privacy_checkbox(self):
        self.selenium.find_element(*self._sign_up_form_privacy_checkbox_locator).click()

    def submit_form(self):
        self.selenium.find_element(*self._sign_up_form_submit_button_locator).click()

    def expand_sign_up_form(self):
        self.selenium.find_element(*self._sign_up_form_email_input_locator).click()

    @property
    def is_sign_up_form_present(self):
        return self.is_element_present(*self._sign_up_form_locator)
