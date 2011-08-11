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
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#                 Dave Hunt <dhunt@mozilla.com>
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
from selenium import selenium

from page import Page


class NewsletterPage(Page):

    _email_locator = "css=.email"
    _agree_to_privacy_policy_checkbox_locator = "css=.privacy-check"
    _submit_button_locator = "css=.subscribe"
    _privacy_policy_error_locator = "css=.privacy-error"
    _success_pane_locator = "css=.success-pane"

    def go_to_newsletter_page(self):
        self.selenium.open("/en-US/newsletter/")

    def type_email(self, email):
        self.selenium.type(self._email_locator, email)

    def agree_to_privacy_policy(self):
        self.selenium.check(self._agree_to_privacy_policy_checkbox_locator)

    def click_sign_me_up(self):
        self.selenium.click(self._submit_button_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def is_privacy_policy_error_visible(self):
        return self.is_element_visible(self._privacy_policy_error_locator)

    @property
    def is_thanks_for_subscribing_visible(self):
        return self.is_element_visible(self._success_pane_locator)
