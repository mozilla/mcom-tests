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


    _mozilla_firefox_logo = "css=#header > div > h1 > a"
    _beta_logo = "css=#toggler-logo-beta"
    _firefox_logo = "css=#toggler-logo-firefox"
    _aurora_logo = "css=#toggler-logo-aurora"
    _firefox_desktop_button = "css=#firefox-desktop-link > a"
    _firefox_mobile_button = "css=#firefox-mobile-link > a"
    _aurora_desktop_button = "css=#aurora-desktop-link > a"
    _aurora_mobile_button = "css=#aurora-mobile-link > a"
    _beta_desktop_button = "css=#beta-desktop-link > a"
    _beta_mobile_button = "css=#beta-mobile-link > a"
    _learn_more_button = "css=.more>a"
    _left_carousel = "css=#carousel-left"
    _right_carousel = "css=#carousel-right"
    _main_feature_header = "css=#main-feature>h2"


    def go_to_channel_page(self):
        self.open("/firefox/channel")


    def click_aurora_logo(self):
        self.click(self._aurora_logo)


    def click_beta_logo(self):
        self.click(self._beta_logo)


    def click_firefox_logo(self):
        self.click(self._firefox_logo)

    @property
    def is_main_feature_heading_present(self):
        return self.is_element_present(self._main_feature_header)

    @property
    def is_mozilla_firefox_logo_present(self):
        return self.is_element_present(self._mozilla_firefox_logo)

    @property
    def is_beta_logo_present(self):
        return self.is_element_present(self._beta_logo)

    @property
    def is_firefox_logo_present(self):
        return self.is_element_present(self._firefox_logo)

    @property
    def is_aurora_logo_present(self):
        return self.is_element_present(self._aurora_logo)

    @property
    def is_left_carousel_present(self):
        return self.is_element_present(self._left_carousel)

    @property
    def is_right_carousel_present(self):
        return self.is_element_present(self._right_carousel)

    def click_right_carousel(self):
        self.click(self._right_carousel)

    def click_left_carousel(self):
        self.click(self._left_carousel)
