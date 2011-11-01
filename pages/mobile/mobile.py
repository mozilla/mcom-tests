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


class MobilePage(MozillaBasePage):

    _text_download_android = "css=#android>h3"
    _text_download_iphone = "css=#iphone>h3"
    _btn_download_android = "css=#android>p.dl>a"
    _btn_download_iphone = "css=#iphone>p.dl>a"
    _btn_download_android_beta = "css=#beta_android>a"
    _btn_download_desktop = "css=#desktop_download>li>a"
    _newsletter_link = "css=.mail>a"
    _twitter_link = "css=li.twitter>a"
    _facebook_link = "css=.facebook>a"

    @property
    def android_header_text(self):
        return self.is_element_present(self._text_download_android)

    @property
    def iphone_header_text(self):
        return self.is_element_present(self._text_download_iphone)

    @property
    def android_button(self):
        return self.is_element_present(self._btn_download_android)

    @property
    def iphone_button(self):
        return self.is_element_present(self._btn_download_iphone)

    @property
    def android_beta_button(self):
        return self.is_element_present(self._btn_download_android_beta)

    @property
    def mobile_desktop_button(self):
        return self.is_element_present(self._btn_download_desktop)

    @property
    def newsletter_link(self):
        return self.is_element_present(self._newsletter_link)

    @property
    def twitter_link(self):
        return self.is_element_present(self._twitter_link)

    @property
    def facebook_link(self):
        return self.is_element_present(self._facebook_link)

    @property
    def click_newsletter_link(self):
        self.click(self._newsletter_link, True)
        return self.get_url_current_page()

    @property
    def click_facebook_link(self):
        self.click(self._facebook_link, True)
        return self.get_url_current_page()
