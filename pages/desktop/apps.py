#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pages.desktop.base import Base


class Apps(Base):

    def go_to_page(self):
        self.open('/apps/')

    page_links_list = [
        {
            'locator': (By.ID, 'marketplace-button'),
            'url_suffix': 'marketplace.firefox.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#showcased-nonfx a'),
            'url_suffix': '/mobile/aurora/',
        }, {
            'locator': (By.CSS_SELECTOR, '#apps-preview ul li:nth-of-type(1) > a'),
            'url_suffix': '#games',
        }, {
            'locator': (By.CSS_SELECTOR, '#apps-preview ul li:nth-of-type(2) > a'),
            'url_suffix': '#news',
        }, {
            'locator': (By.CSS_SELECTOR, '#apps-preview ul li:nth-of-type(3) > a'),
            'url_suffix': '#productivity',
        }, {
            'locator': (By.CSS_SELECTOR, '#build ul li:nth-of-type(1) > a'),
            'url_suffix': 'marketplace.firefox.com/developers/',
        }, {
            'locator': (By.CSS_SELECTOR, '#build ul li:nth-of-type(2) > a'),
            'url_suffix': 'marketplace.firefox.com/developers/partners',
        }
    ]

    _showcased_apps_links_locator = (By.CSS_SELECTOR, 'div.billboard a')
    _sign_up_form_locator = (By.ID, 'footer-email-form')
    _sign_up_form_email_input_locator = (By.ID, 'id_email')
    _sign_up_form_html_radio_locator = (By.ID, 'id_fmt_0')
    _sign_up_form_text_radio_locator = (By.ID, 'id_fmt_1')
    _sign_up_form_privacy_checkbox_locator = (By.ID, 'id_privacy')
    _sign_up_form_submit_button_locator = (By.ID, 'footer_email_submit')

    @property
    def showcased_apps_links(self):
        return self.selenium.find_elements(*self._showcased_apps_links_locator)

    @property
    def is_sign_up_form_present(self):
        return self.is_element_present(*self._sign_up_form_locator)

    @property
    def are_sign_up_form_fields_visible(self):
        return self.is_element_visible(*self._sign_up_form_email_input_locator) \
            and self.is_element_visible(*self._sign_up_form_html_radio_locator) \
            and self.is_element_visible(*self._sign_up_form_text_radio_locator) \
            and self.is_element_visible(*self._sign_up_form_privacy_checkbox_locator) \
            and self.is_element_visible(*self._sign_up_form_submit_button_locator)

    def expand_sign_up_form(self):
        self.selenium.find_element(*self._sign_up_form_email_input_locator).click()
