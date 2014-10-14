#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Contribute(Base):

    def go_to_page(self):
        self.open('/contribute/')

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#contribute-nav-menu li:nth-child(1) a'),
            'url_suffix': 'contribute/',
        }, {
            'locator': (By.CSS_SELECTOR, '#contribute-nav-menu li:nth-child(2) a'),
            'url_suffix': 'events/',
        }, {
            'locator': (By.CSS_SELECTOR, '#contribute-nav-menu li:nth-child(3) a'),
            'url_suffix': 'stories/',
        }, {
            'locator': (By.CSS_SELECTOR, '.section.landing-mission .cta a'),
            'url_suffix': '//videos.cdn.mozilla.net/uploads/mozillaorg/Mozilla_2014_i_am.webm',
        }, {
            'locator': (By.CSS_SELECTOR, '.section.landing-howto a'),
            'url_suffix': 'signup/',
        }, {
            'locator': (By.CSS_SELECTOR, '.other-actions li:nth-child(1) a'),
            'url_suffix': 'Give-Now?source=mozillaorg_default_footer&ref=volunteer_getinvolvedpage201410&utm_campaign=volunteer_getinvolvedpage201410&utm_source=newsletter-mofo&utm_medium=referral',
        }, {
            'locator': (By.CSS_SELECTOR, '.other-actions li:nth-child(2) a'),
            'url_suffix': 'firefox/',
        }, {
            'locator': (By.CSS_SELECTOR, '.other-actions li:nth-child(3) a'),
            'url_suffix': '//www.facebook.com/mozilla',
        }, {
            'locator': (By.CSS_SELECTOR, '.other-actions li:nth-child(4) a'),
            'url_suffix': '//twitter.com/mozilla',
        }, {
            'locator': (By.CSS_SELECTOR, '.extra-links ul:nth-of-type(1) li:nth-child(1) a'),
            'url_suffix': 'contact/communities/',
        }, {
            'locator': (By.CSS_SELECTOR, '.extra-links ul:nth-of-type(1) li:nth-child(2) a'),
            'url_suffix': 'about/forums/',
        }, {
            'locator': (By.CSS_SELECTOR, '.extra-links ul:nth-of-type(1) li:nth-child(3) a'),
            'url_suffix': '//wiki.mozilla.org/IRC',
        }
    ]

    _signup_link_locator = (By.CSS_SELECTOR, '.section.landing-howto a')

    def click_signup(self):
        signup_link = self.selenium.find_element(*self._signup_link_locator)
        signup_link.click()
        return Signup(self.testsetup)


class Signup(Contribute):

    def go_to_page(self):
        self.open('/contribute/signup')

    _testing_area_locator = (By.CSS_SELECTOR, '.categories .option #category-testing')
    _sign_up_form_select_testing_area_locator = (By.ID, 'id_area_testing')
    _sign_up_form_locator = (By.CSS_SELECTOR, '.personal')
    _sign_up_form_name_input_locator = (By.ID, 'id_name')
    _sign_up_form_email_input_locator = (By.ID, 'id_email')
    _sign_up_form_country_select_locator = (By.ID, 'id_country')
    _sign_up_form_privacy_checkbox_locator = (By.ID, 'id_privacy')
    _sign_up_form_html_format_radio_button_locator = (By.CSS_SELECTOR, '.form-format input[type=radio][value=H]')
    _sign_up_form_submit_button_locator = (By.CSS_SELECTOR, 'button')

    def click_testing_area(self):
        self.selenium.find_element(*self._testing_area_locator).click()

    sign_up_form_fields = [
        {
            'locator': (By.ID, 'id_name'),
        },
        {
            'locator': (By.ID, 'id_email'),
        }, {
            'locator': (By.ID, 'id_country'),
        }, {
            'locator': (By.ID, 'id_privacy'),
        }, {
            'locator': (By.CSS_SELECTOR, 'button'),
        },
    ]

    def input_name(self, name):
        self.selenium.find_element(*self._sign_up_form_name_input_locator).send_keys(name)

    def input_email(self, email):
        self.selenium.find_element(*self._sign_up_form_email_input_locator).send_keys(email)

    def check_privacy_checkbox(self):
        self.selenium.find_element(*self._sign_up_form_privacy_checkbox_locator).click()

    def select_html_format(self):
        self.selenium.find_element(*self._sign_up_form_html_format_radio_button_locator).click()

    def submit_form(self):
        self.selenium.find_element(*self._sign_up_form_submit_button_locator).click()

    @property
    def is_sign_up_form_present(self):
        return self.is_element_present(*self._sign_up_form_locator)
