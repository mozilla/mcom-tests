#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.desktop.base import Base
from pages.page import Page


class Home(Base):
    _home_news_title_locator=(By.CSS_SELECTOR, '#home-news > h3')
    _home_news_links_locator=(By.CSS_SELECTOR, '#home-news > h4 > a')

    def got_to_page(self):
        self.selenium.get(self.base_url)

    @property
    def home_news_title(self):
        return self.selenium.find_element(*self._home_news_title_locator).text

    @property
    def home_news_links(self):
        return [news.get_attribute('href') for news in self.selenium.find_elements(*self._home_news_links_locator)]

    @property
    def email_form(self):
        return self.EmailForm(self.testsetup)

    class EmailForm(Page):

        _title_locator=(By.TAG_NAME, 'h3')

        _email_field_locator=(By.ID, 'id_email')
        _country_selector_locator=(By.ID, 'country')
        _privacy_checkbox_locator=(By.ID, 'id_privacy')
        _privacy_title_locator=(By.CSS_SELECTOR, '.field-privacy  span.title')
        _privacy_title_link_locator=(By.CSS_SELECTOR, 'div.field.field-privacy  span.title > a')

        _submit_button_locator=(By.ID, 'footer_email_submit')
        _form_details_locator=(By.CSS_SELECTOR, '.form-submit > p > small')

        _root_locator=(By.ID, 'footer-email-form')

        def __init__(self, testsetup):
            Page.__init__(self, testsetup)
            self._root=self.selenium.find_element(*self._root_locator)

        @property
        def title(self):
            return self._root.find_element(*self._title_locator).text

        @property
        def email_placeholder(self):
            return self._root.find_element(*self._email_field_locator).get_attribute('placeholder')

        @property
        def submit_button_text(self):
            return self._root.find_element(*self._submit_button_locator).get_attribute('value')

        @property
        def privacy_text(self):
            return self._root.find_element(*self._privacy_title_locator).text

        @property
        def privacy_link(self):
            return self._root.find_element(*self._privacy_title_link_locator).get_attribute('href')

        @property
        def form_details_text(self):
            return self._root.find_element(*self._form_details_locator).text

        @property
        def is_additional_info_visible(self):
            return self.is_element_visible(*self._privacy_title_locator) and \
                    self.is_element_visible(*self._privacy_checkbox_locator) and\
                    self.is_element_visible(*self._form_details_locator) and \
                    self.is_element_visible(*self._country_selector_locator)

        @property
        def country_count(self):
            return len(Select(self._root.find_element(*self._country_selector_locator)).options)

        def click_email(self):
            self._root.find_element(*self._email_field_locator).click()
            self.wait_for_ajax()
