#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class Notes(Base):

    _firefox_notes_header_locator = (By.CSS_SELECTOR, '#main-feature > h2')

    def go_to_page(self):
        self.open('/firefox/notes/')

    @property
    def firefox_notes_header_text(self):
        return self.selenium.find_element(*self._firefox_notes_header_locator).text

    @property
    def all_links(self):
        current_url = self.selenium.current_url
        urls = []
        links = self.selenium.find_elements(By.TAG_NAME, 'a')
        for link in links:
            href = link.get_attribute('href')
            if len(href) > 0 and href not in urls and current_url not in href:
                urls.append(href)
        return urls
