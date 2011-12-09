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


class ChannelPage(MozillaBasePage):


    _aurora_btn_locator = "css=#download_aurora_button"
    _aurora_mobile_btn_locator = "css=#download_aurora_mobile_button"
    _beta_mobile_btn_locator = "css=#download_beta_mobile_button"
    _beta_btn_locator = "css=#download_beta > .beta-download"
    _aurora_systems_and_languages_locator = \
    "css=#download_aurora_button > .download-other > a:nth-child(1)"
    _aurora_privacy_policy_locator = \
    "css=#download_aurora_button > .download-other > a:nth-child(2)"
    _aurora_mobile_supported_device_locator = \
    "css=#download_aurora_mobile_button > .home-download > .download-other > a:nth-child(1)"
    _aurora_mobile_privacy_policy_locator = \
    "css=#download_aurora_mobile_button >.home-download >.download-other > a:nth-child(2)"
    _beta_systems_and_languages_locator = \
    "css=#download_beta > #download-button > .download-other > span > a:nth-child(1)"
    _beta_privacy_policy_locator = \
    "css=#download_beta > #download-button > .download-other > span > a:nth-child(2)"
    _beta_mobile_supported_devices_locator = \
    "css=#download_beta_mobile_button > .home-download > .download-other > a:nth-child(1)"
    _beta_mobile_privacy_policy_locator = \
    "css=#download_beta_mobile_button >.home-download > .download-other > a:nth-child(2)"
    _aurora_header_locator = "css=#download_aurora > h3"
    _beta_header_locator = "css=#download_beta > h3"


    @property
    def aurora_download_button(self):
        return self.is_element_present(self._aurora_btn_locator)

    @property
    def aurora_mobile_download_button(self):
        return self.is_element_present(self._aurora_mobile_btn_locator)

    @property
    def beta_download_button(self):
        return self.is_element_present(self._beta_btn_locator)

    @property
    def beta_mobile_download_button(self):
        return self.is_element_present(self._beta_mobile_btn_locator)

    @property
    def aurora_systems_and_languages_link(self):
        return self.is_element_present(self._aurora_systems_and_languges_locator)

    @property
    def aurora_privacy_link(self):
        return self.is_element_present(self._aurora_privacy_policy_locator)

    @property
    def aurora_mobile_supported_devices_link(self):
        return self.is_element_present(self._aurora_mobile_supported_devices_locator)

    @property
    def aurora_mobile_privacy_link(self):
        return self.is_element_present(self.aurora_mobile_privacy_locator)

    @property
    def beta_privacy_link(self):
        return self.is_element_present(self._beta_privacy_policy_locator)

    @property
    def beta_systems_and_languages_link(self):
        return self.is_element_present(self._beta_systems_and_languages_locator)

    @property
    def beta_mobile_supported_devices_link(self):
        return self.is_element_present(self.beta_mobile_supported_devices_locator)

    @property
    def beta_mobile_privacy_link(self):
        return self.is_element_present(self._beta_mobile_privacy_policy_locator)

    @property
    def aurora_header(self):
        return self.is_element_present(self._aurora_header_locator)

    @property
    def beta_header(self):
        return self.is_element_present(self._beta_header_locator)
