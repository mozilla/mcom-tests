#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.desktop.base import Base


class SMS(Base):

    def go_to_page(self):
        self.open('/firefox/sms/')

    _send_link_button = (By.CSS_SELECTOR, '.button.arrow')
    _google_play_link = (By.CSS_SELECTOR, '.also a')
    _sms_confirmation = (By.CSS_SELECTOR, '.large')
    _phone_textbox = (By.CSS_SELECTOR, '#number')

    info_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.more p:nth-child(1) a'),
            'url_suffix': 'support.mozilla.org/kb/will-firefox-work-my-mobile-device',
        }, {
            'locator': (By.CSS_SELECTOR, '.more p:nth-child(2) a'),
            'url_suffix': '/firefox/android/',
        }
    ]

    @property
    def is_textbox_visible(self):
        return self.is_element_visible(*self._phone_textbox)

    @property
    def is_google_play_link_visible(self):
        return self.is_element_visible(*self._google_play_link)

    def submit_sms_form(self, user='default'):
        credentials = self.testsetup.credentials[user]
        phonetextbox = self.selenium.find_element(*self._phone_textbox)
        phonetextbox.send_keys(credentials['phone'])
        self.selenium.find_element(*self._send_link_button).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: s.find_element(*self._sms_confirmation))
        return self.is_element_visible(*self._sms_confirmation)
