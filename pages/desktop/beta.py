#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2012
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

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
