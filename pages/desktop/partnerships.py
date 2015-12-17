# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.base import Base
from pages.page import Page


class Partnerships(Base):

    _url = '{base_url}/{locale}/about/partnerships'

    section_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox > ul > li:nth-of-type(2) > a'),
            'url_suffix': '/en-US/about/partnerships/distribution/',
        }, {
            'locator': (By.CSS_SELECTOR, '#marketplace > p > a'),
            'url_suffix': 'marketplace.firefox.com/developers/',
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
        return self.PartnerForm(self.base_url, self.selenium)

    class PartnerForm(Page):

        _form_locator = (By.ID, 'partner-form')
        _get_started_title_locator = (By.CSS_SELECTOR, '#partner-form > h3')
        _first_name_textbox_locator = (By.ID, 'first_name')
        _last_name_textbox_locator = (By.ID, 'last_name')
        _title_textbox_locator = (By.ID, 'title')
        _company_textbox_locator = (By.ID, 'company')
        _website_textbox_locator = (By.ID, 'URL')
        _email_textbox_locator = (By.ID, 'email')
        _phone_textbox_locator = (By.ID, 'phone')
        _mobile_textbox_locator = (By.ID, 'mobile')
        _address_textbox_locator = (By.ID, 'street')
        _city_textbox_locator = (By.ID, 'city')
        _country_textbox_locator = (By.ID, 'country')
        _zip_textbox_locator = (By.ID, 'zip')
        _interest_field_locator = (By.ID, 'interest')
        _description_textbox_locator = (By.ID, 'description')
        _submit_button_locator = (By.ID, 'sf-form-submit')

        @property
        def fields_list(self):
            return [
                self._first_name_textbox_locator, self._last_name_textbox_locator,
                self._title_textbox_locator, self._company_textbox_locator,
                self._website_textbox_locator, self._email_textbox_locator,
                self._phone_textbox_locator, self._mobile_textbox_locator,
                self._address_textbox_locator, self._city_textbox_locator,
                self._country_textbox_locator, self._zip_textbox_locator,
                self._interest_field_locator, self._description_textbox_locator
            ]

        @property
        def is_title_visible(self):
            return self.is_element_visible(*self._get_started_title_locator)

        @property
        def is_submit_button_visible(self):
            return self.is_element_visible(*self._submit_button_locator)

        @property
        def is_form_present(self):
            return self.is_element_present(*self._form_locator)
