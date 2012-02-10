#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import MozillaBasePage


class BetaPage(MozillaBasePage):


    _beta_header = "css=#main-feature > h2 > img"
    _beta_btn_locator = "css=.home-download > a"
    _supported_devices_locator = "css=.download-other > a:nth-child(1)"
    _privacy_policy_locator = "css=.download-other > a:nth-child(2)"
    _email_locator = "css=#email"
    _beta_checkbox_locator = "css=#check_beta"
    _privacy_policy_checkbox_locator = "css=#inline-privacy-check"
    _sign_up_btn_locator = "css=#subscribe.button"
    _test_features_locator = "css=#feature-list > li:nth-child(1) > h3"
    _polish_locator = "css=#feature-list > li:nth-child(2) > h3"
    _do_part_locator = "css=#feature-list > li:nth-child(3) > h3"
    _success_pane_locator = "css=.success-pane>h3"

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
        self.selenium.type(self._email_locator, email)

    def check_beta_checkbox(self):
        self.selenium.check(self._beta_checkbox_locator)

    def agree_to_privacy_policy(self):
        self.selenium.check(self._privacy_policy_checkbox_locator)

    def click_sign_me_up(self):
        self.selenium.click(self._sign_up_btn_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def newsletter_submitted_sucessfully(self):
        return self.get_text(self._success_pane_locator)
