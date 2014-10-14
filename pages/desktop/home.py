#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.desktop.base import Base


class HomePage(Base):

    def go_to_page(self):
        self.open('')

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#promo-1 a'),
            'url_suffix': '//openstandard.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#promo-2 a'),
            'url_suffix': '/privacy/you/',
        }, {
            'locator': (By.CSS_SELECTOR, '#promo-5 .fxos-link'),
            'url_suffix': '/firefox/desktop/',
        }, {
            'locator': (By.CSS_SELECTOR, '#promo-6 a'),
            'url_suffix': '//webmaker.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#promo-8 a'),
            'url_suffix': '//webmaker.org/appmaker',
        }, {
            'locator': (By.CSS_SELECTOR, '#promo-10 a'),
            'url_suffix': '/firefox/desktop/trust/',
        }, {
            'locator': (By.CSS_SELECTOR, '#promo-11 a'),
            'url_suffix': '//support.mozilla.org/get-involved',
        }, {
            'locator': (By.CSS_SELECTOR, '#promo-16 .twt-actions a:nth-child(1)'),
            'url_suffix': '//twitter.com/firefox',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox-download-section header a'),
            'url_suffix': '/firefox/',
        }, {
            'locator': (By.CSS_SELECTOR, '#open-standard .more-large'),
            'url_suffix': '//openstandard.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#upcoming-events .more-large'),
            'url_suffix': '//reps.mozilla.org/events/',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-btn'),
            'url_suffix': '/contribute/',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary-links li:nth-child(1) a'),
            'url_suffix': '//addons.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary-links li:nth-child(2) a'),
            'url_suffix': '//careers.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary-links li:nth-child(3) a'),
            'url_suffix': '//support.mozilla.org/',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '.container h1 img'),
            'img_name_suffix': 'mozilla-wordmark-white-high-res.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.primary img'),
            'img_name_suffix': 'firefox-logo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox-promo-link img'),
            'img_name_suffix': 'firefox-logo-wordmark-white.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.os-header img'),
            'img_name_suffix': 'tos-wordmark-high-res.png',
        }
    ]

    _sign_up_form_locator = (By.ID, 'mozorg-newsletter-form')
    _sign_up_form_email_input_locator = (By.ID, 'id_email')
    _sign_up_form_country_select_locator = (By.ID, 'country')
    _sign_up_form_privacy_checkbox_locator = (By.ID, 'id_privacy')
    _sign_up_form_submit_button_locator = (By.ID, 'footer_email_submit')

    sign_up_form_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'label.privacy-check-label > span > a'),
            'url_suffix': '/privacy/',
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
        WebDriverWait(self.selenium, 10).until(EC.visibility_of_element_located(self._sign_up_form_privacy_checkbox_locator))

    @property
    def is_sign_up_form_present(self):
        return self.is_element_present(*self._sign_up_form_locator)
