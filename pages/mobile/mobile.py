#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import MozillaBasePage


class MobilePage(MozillaBasePage):

    _text_download_android = "css=#android > h3"
    _text_download_iphone = "css=#iphone > h3"
    _btn_download_android = "css=#android > p.dl > a"
    _btn_download_iphone = "css=#iphone >p.dl > a"
    _btn_download_android_beta = "css=#beta_android > a"
    _btn_download_desktop = "css=#desktop_download>li > a"
    _newsletter_link = "css=.mail > a"
    _twitter_link = "css=li.twitter > a"
    _facebook_link = "css=.facebook > a"
    _get_firefox_for_android_btn = "css=#download > .download"

    @property
    def get_firefox_for_android_button(self):
        return self.is_element_present(self._get_firefox_for_android_btn)

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
