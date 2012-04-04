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

        _title_locator = (By.CSS_SELECTOR, 'div.row > .form-column-1 > h3')
        _email_field_locator = (By.ID, 'id_email')
        _area_of_interest_locator = (By.ID, 'id_interest')
        _submit_button_locator = (By.ID, 'form-submit')

        _note_message_locator = (By.CSS_SELECTOR, '#form-details > .form-column-1 > p')
        _comments_locator = (By.ID, 'id_comments')

        _privacy_checkbox_locator = (By.ID, 'id_privacy')
        _privacy_title_locator = (By.CSS_SELECTOR, '.privacy-check-label  span.title')
        _privacy_title_link_locator = (By.CSS_SELECTOR, '.privacy-check-label  span.title > a')

        _newsletter_checkbox_locator = (By.ID, 'id_newsletter')
        _newsletter_title_locator = (By.CSS_SELECTOR, '.field-newsletter > label')

        _root_locator = (By.ID, 'help-form')

        def __init__(self, testsetup):
            Page.__init__(self, testsetup)
            self._root = self.selenium.find_element(*self._root_locator)

        @property
        def title(self):
            return self._root.find_element(*self._title_locator).text

        @property
        def email_placeholder(self):
            return self._root.find_element(*self._email_field_locator).get_attribute('placeholder')

        @property
        def areas_of_interest_text(self):
            return [area.text for area in Select(self._root.find_element(*self._area_of_interest_locator)).options]

        @property
        def area_of_interest_selected_option(self):
            return Select(self._root.find_element(*self._area_of_interest_locator)).first_selected_option.text

        @property
        def submit_button_text(self):
            return self._root.find_element(*self._submit_button_locator).get_attribute('value')

        @property
        def note_message(self):
            return self._root.find_element(*self._note_message_locator).text

        @property
        def comments_placeholder(self):
            return self._root.find_element(*self._comments_locator).get_attribute('placeholder')

        @property
        def privacy_text(self):
            return self._root.find_element(*self._privacy_title_locator).text

        @property
        def privacy_link(self):
            return self._root.find_element(*self._privacy_title_link_locator).get_attribute('href')

        @property
        def newsletter_text(self):
            return self._root.find_element(*self._newsletter_title_locator).text

        @property
        def is_additional_info_visible(self):
            return self.is_element_visible(*self._privacy_title_locator) and \
                    self.is_element_visible(*self._privacy_checkbox_locator) and\
                    self.is_element_visible(*self._note_message_locator) and\
                    self.is_element_visible(*self._comments_locator) and\
                    self.is_element_visible(*self._newsletter_checkbox_locator) and\
                    self.is_element_visible(*self._newsletter_title_locator)

        def click_email(self):
            self._root.find_element(*self._email_field_locator).click()
            self.wait_for_ajax()

        def click_area_of_interest(self):
            self._root.find_element(*self._area_of_interest_locator).click()
            self.wait_for_ajax()
