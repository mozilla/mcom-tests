#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class BetaPage(Base):

    _beta_header = (By.CSS_SELECTOR, '#main-feature > h2 > img')
    _beta_btn_locator = (By.CSS_SELECTOR, '.home-download > a')
    _supported_devices_locator = (By.CSS_SELECTOR, '.download-other > a:nth-child(1)')
    _privacy_policy_locator = (By.CSS_SELECTOR, '.download-other > a:nth-child(2)')
    _email_locator = (By.CSS_SELECTOR, '#email')
    _beta_checkbox_locator = (By.CSS_SELECTOR, '#check_beta')
    _privacy_policy_checkbox_locator = (By.CSS_SELECTOR, '#inline-privacy-check')
    _sign_up_btn_locator = (By.CSS_SELECTOR, '#subscribe.button')
    _test_features_locator = (By.CSS_SELECTOR, '#feature-list > li:nth-child(1) > h3')
    _polish_locator = (By.CSS_SELECTOR, '#feature-list > li:nth-child(2) > h3')
    _do_part_locator = (By.CSS_SELECTOR, '#feature-list > li:nth-child(3) > h3')
    _success_pane_locator = (By.CSS_SELECTOR, '.success-pane > h3')

    def go_to_mobile_beta_page(self):
        self.open("/mobile/beta/")

    @property
    def is_test_features_header_present(self):
        return self.is_element_present(self._test_features_locator)

    @property
    def is_do_part_header_present(self):
        return self.is_element_present(self._do_part_locator)

    @property
    def is_polish_header_present(self):
        return self.is_element_present(self._polish_locator)

    @property
    def is_beta_header_present(self):
        return self.is_element_present(self._beta_header)

    @property
    def is_beta_download_button_present(self):
        return self.is_element_present(self._beta_btn_locator)

    @property
    def is_supported_devices_link_present(self):
        return self.is_element_present(self._supported_devices_locator)

    @property
    def is_privacy_policy_link_present(self):
        return self.is_element_present(self._privacy_policy_locator)

    def type_email(self, email):
        self.selenium.find_element(*self._email_locator).send_keys(email)

    def check_beta_checkbox(self):
        self.selenium.find_element(*self._beta_checkbox_locator).click()

    def agree_to_privacy_policy(self):
        self.selenium.find_element(*self._privacy_policy_checkbox_locator).click()

    def click_sign_me_up(self):
        self.selenium.find_element(*self._sign_up_btn_locator).click()

    @property
    def newsletter_submitted_sucessfully(self):
        return self.selenium.find_element(*self._success_pane_locator).text
