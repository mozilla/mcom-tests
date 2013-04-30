#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base
from pages.page import Page


class Partnerships(Base):

    def go_to_page(self):
        self.open('/about/partnerships/')

    section_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox > p > a'),
            'url_suffix': '/en-US/about/partnerships/distribution/',
        }, {
            'locator': (By.CSS_SELECTOR, '#marketplace > p > a'),
            'url_suffix': '/en-US/apps/',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox > img:nth-of-type(1)'),
            'img_name_contains': 'banner-firefox',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefox > img:nth-of-type(2)'),
            'img_name_contains': 'icon-firefox',
        }, {
            'locator': (By.CSS_SELECTOR, '#android > img:nth-of-type(1)'),
            'img_name_contains': 'banner-android',
        }, {
            'locator': (By.CSS_SELECTOR, '#android > img:nth-of-type(2)'),
            'img_name_contains': 'icon-android',
        }, {
            'locator': (By.CSS_SELECTOR, '#marketplace > img:nth-of-type(1)'),
            'img_name_contains': 'banner-marketplace',
        }, {
            'locator': (By.CSS_SELECTOR, '#marketplace > img:nth-of-type(2)'),
            'img_name_contains': 'icon-marketplace',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefoxos > img:nth-of-type(1)'),
            'img_name_contains': 'banner-firefoxos',
        }, {
            'locator': (By.CSS_SELECTOR, '#firefoxos > img:nth-of-type(2)'),
            'img_name_contains': 'icon-firefox',
        }, {
            'locator': (By.CSS_SELECTOR, '#cobrand > img:nth-of-type(1)'),
            'img_name_contains': 'banner-cobrand',
        }, {
            'locator': (By.CSS_SELECTOR, '#cobrand > img:nth-of-type(2)'),
            'img_name_contains': 'icon-cobrand',
        }
    ]

    @property
    def partner_form(self):
        return self.PartnerForm(self.testsetup)

    class PartnerForm(Page):

        _form_locator = (By.ID, 'partner-form')
        _get_started_title = (By.CSS_SELECTOR, '#partner-form > h3')
        _first_name_textbox = (By.ID, 'first_name')
        _last_name_textbox = (By.ID, 'last_name')
        _title_textbox = (By.ID, 'title')
        _company_textbox = (By.ID, 'company')
        _website_textbox = (By.ID, 'URL')
        _email_textbox = (By.ID, 'email')
        _phone_textbox = (By.ID, 'phone')
        _mobile_textbox = (By.ID, 'mobile')
        _address_textbox = (By.ID, 'street')
        _city_textbox = (By.ID, 'city')
        _country_textbox = (By.ID, 'country')
        _zip_textbox = (By.ID, 'zip')
        _interest_field = (By.ID, 'interest')
        _description_textbox = (By.ID, 'description')
        _submit_button = (By.ID, 'sf-form-submit')

        @property
        def fields_list(self):
            return [
            self._first_name_textbox, self._last_name_textbox,
            self._title_textbox, self._company_textbox,
            self._website_textbox, self._email_textbox,
            self._phone_textbox, self._mobile_textbox,
            self._address_textbox, self._city_textbox,
            self._country_textbox, self._zip_textbox,
            self._interest_field, self._description_textbox
        ]

        @property
        def is_title_visible(self):
            return self.is_element_visible(*self._get_started_title)

        @property
        def is_submit_button_visible(self):
            return self.is_element_visible(*self._submit_button)

        @property
        def is_present(self):
            return self.is_element_present(*self._form_locator)
