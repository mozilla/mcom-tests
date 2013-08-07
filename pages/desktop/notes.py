#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class Notes(Base):

    _firefox_notes_header_locator = (By.CSS_SELECTOR, '#main-feature > h2')
    _notes_page_url = '/firefox/notes/'

    def go_to_page(self):
        self.open(self._notes_page_url)

    @property
    def notes_page_url(self):
        return self._notes_page_url

    @property
    def firefox_notes_header_text(self):
        return self.selenium.find_element(*self._firefox_notes_header_locator).text
