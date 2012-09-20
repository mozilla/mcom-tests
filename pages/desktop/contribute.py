#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.desktop.base import Base
from pages.page import Page


class Contribute(Base):

    def go_to_page(self):
        self.open('/contribute/')

    @property
    def help_form(self):
        return self.HelpForm(self.testsetup)

    class HelpForm(Page):

        _want_to_help_title_locator = (By.CSS_SELECTOR, 'div.row > .form-column-1 > h3')
        _email_field_locator = (By.ID, 'id_email')
        _area_of_interest_locator = (By.ID, 'id_interest')
        _submit_button_locator = (By.ID, 'form-submit')

        _comments_locator = (By.ID, 'id_comments')

        _privacy_checkbox_locator = (By.ID, 'id_privacy')
        _privacy_title_locator = (By.CSS_SELECTOR, '.privacy-check-label span.title')

        _newsletter_checkbox_locator = (By.ID, 'id_newsletter')
        _newsletter_title_locator = (By.CSS_SELECTOR, '.field-newsletter > label')

        _recaptcha_table_locator = (By.ID, 'recaptcha_table')
        _recaptcha_response_field_locator = (By.ID, 'recaptcha_response_field')

        privacy_link = {
            'locator': (By.CSS_SELECTOR, '.privacy-check-label span.title > a'),
            'url_suffix': '/privacy-policy'
        }

        @property
        def elements_are_visible(self):
            return self.is_element_visible(*self._want_to_help_title_locator) and\
                self.is_element_visible(*self._comments_locator) and\
                self.is_element_visible(*self._area_of_interest_locator) and\
                self.is_element_visible(*self._privacy_checkbox_locator) and\
                self.is_element_visible(*self._privacy_title_locator) and\
                self.is_element_visible(*self._newsletter_checkbox_locator) and\
                self.is_element_visible(*self._newsletter_title_locator) and\
                self.is_element_visible(*self._recaptcha_table_locator) and\
                self.is_element_visible(*self._recaptcha_response_field_locator) and\
                self.is_element_visible(*self._submit_button_locator)

        def click_email(self):
            self.selenium.find_element(*self._email_field_locator).click()
            self.wait_for_ajax()
