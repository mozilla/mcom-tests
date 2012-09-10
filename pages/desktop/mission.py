#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class Mission(Base):

    _contribute_midpage_link = (By.CSS_SELECTOR, 'ul.links > li:nth-of-type(1) > h4 > a')
    _history_midpage_link = (By.CSS_SELECTOR, 'ul.links > li:nth-of-type(2) > h4 > a')
    _forums_midpage_link = (By.CSS_SELECTOR, 'ul.links > li:nth-of-type(3) > h4 > a')
    _governance_midpage_link = (By.CSS_SELECTOR, 'ul.links > li:nth-of-type(4) > h4 > a')
    _manifesto_midpage_link = (By.CSS_SELECTOR, '#main-content > div > p:nth-of-type(3) > a')
    _video = (By.TAG_NAME, 'video')
    _video_overlay = (By.CSS_SELECTOR, '.mozilla-video-control-overlay')

    def go_to_page(self):
        self.open('/mission/')

    @property
    def are_midpage_links_visible(self):
        return self.is_element_visible(*self._contribute_midpage_link) and \
        self.is_element_visible(*self._forums_midpage_link) and \
        self.is_element_visible(*self._governance_midpage_link) and \
        self.is_element_visible(*self._history_midpage_link) and\
        self.is_element_visible(*self._manifesto_midpage_link)

    @property
    def is_video_visible(self):
        return self.is_element_visible(*self._video) and\
               self.is_element_visible(*self._video_overlay)
