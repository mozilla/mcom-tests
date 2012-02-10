#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import MozillaBasePage


class AuroraPage(MozillaBasePage):


    _aurora_header = "css=#main-feature > h2 > img"
    _aurora_btn_locator = "css=.home-download > li > a"
    _all_systems_locator = "css=.download-other > a:nth-child(1)"
    _privacy_policy_locator = "css=.download-other > a:nth-child(2)"
    _email_locator = "css=#email"
    _aurora_checkbox_locator = "css=#check_aurora"
    _privacy_policy_checkbox_locator = "css=#inline-privacy-check"
    _sign_up_btn_locator = "css=#subscribe.button"
    _preview_features_locator = "css=#feature-list > li:nth-child(1) > h3"
    _share_feedback_locator = "css=#feature-list > li:nth-child(2) > h3"
    _shape_firefox_locator = "css=#feature-list > li:nth-child(3) > h3"
    _success_pane_locator = "css=.success-pane>h3"

    def go_to_aurora_page(self):
        self.open("/aurora/")

    @property
    def is_preview_features_header_present(self):
        return self.is_element_present(self._preview_features_locator)

    @property
    def is_share_feedback_header_present(self):
        return self.is_element_present(self._share_feedback_locator)

    @property
    def is_shape_firefox_header_present(self):
        return self.is_element_present(self._shape_firefox_locator)

    @property
    def is_aurora_header_present(self):
        return self.is_element_present(self._aurora_header)

    @property
    def is_aurora_download_button_present(self):
        return self.is_element_present(self._aurora_btn_locator)

    @property
    def is_all_systems_and_languages_link_present(self):
        return self.is_element_present(self._all_systems_locator)

    @property
    def is_privacy_policy_link_present(self):
        return self.is_element_present(self._privacy_policy_locator)

    def type_email(self, email):
        self.selenium.type(self._email_locator, email)

    def check_aurora_checkbox(self):
        return self.selenium.check(self._aurora_checkbox_locator)

    def agree_to_privacy_policy(self):
        self.selenium.check(self._privacy_policy_checkbox_locator)

    def click_sign_me_up(self):
        self.selenium.click(self._sign_up_btn_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def newsletter_submitted_sucessfully(self):
        return self.get_text(self._success_pane_locator)
