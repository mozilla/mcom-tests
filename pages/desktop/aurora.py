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
# Portions created by the Initial Developer are Copyright (C) 2011
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

    @property
    def go_to_aurora_page(self):
        self.open("/aurora/")

    @property
    def preview_features_header(self):
        return self.is_element_present(self._preview_features_locator)

    @property
    def share_feedback_header(self):
        return self.is_element_present(self._share_feedback_locator)

    @property
    def shape_firefox_header(self):
        return self.is_element_present(self._shape_firefox_locator)

    @property
    def aurora_header(self):
        return self.is_element_present(self._aurora_header)

    @property
    def aurora_download_button(self):
        return self.is_element_present(self._aurora_btn_locator)

    @property
    def all_systems_and_languages_link(self):
        return self.is_element_present(self._all_systems_locator)

    @property
    def privacy_policy_link(self):
        return self.is_element_present(self._privacy_policy_locator)

    def type_email(self, email):
        self.selenium.type(self._email_locator, email)

    @property
    def check_aurora_checkbox(self):
        return self.selenium.check(self._aurora_checkbox_locator)

    @property
    def agree_to_privacy_policy(self):
        self.selenium.check(self._privacy_policy_checkbox_locator)

    @property
    def click_sign_me_up(self):
        self.selenium.click(self._sign_up_btn_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def newsletter_submitted_sucessfully(self):
        return self.get_text(self._success_pane_locator)
