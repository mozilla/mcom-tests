#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class Mission(Base):

    _midpage_link_locator_expression = 'a[href$="%s"]'
    _video_locator = (By.TAG_NAME, 'video')
    _video_overlay_locator = (By.CSS_SELECTOR, '.mozilla-video-control-overlay')
    _video_srcs_locator = (By.CSS_SELECTOR, 'video source')

    midpage_links_list = [
        '/about/manifesto.html',
        '/contribute/',
        '/about/history.html',
        '/about/forums/',
        '/about/governance.html'
    ]

    def midpage_link_href(self, url_suffix):
        return self.selenium.find_element(
            By.CSS_SELECTOR, self._midpage_link_locator_expression % url_suffix
        ).get_attribute('href')

    def go_to_page(self):
        self.open('/mission/')

    @property
    def is_video_visible(self):
        return self.is_element_visible(*self._video_locator) and \
            self.is_element_visible(*self._video_overlay_locator)

    @property
    def video_srcs(self):
        srcs = []
        sources = self.selenium.find_elements(*self._video_srcs_locator)
        for source in sources:
            srcs.append(source.get_attribute('src'))
        return srcs
