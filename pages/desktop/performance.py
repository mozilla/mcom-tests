#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class Performance(Base):

    _perf_hardware_img_locator = (By.CSS_SELECTOR, "#hardware > .row > .span7 > img")
    _video_overlay_locator = (By.CSS_SELECTOR, ".mozilla-video-control-overlay")
    _video_sources_locator = (By.CSS_SELECTOR, 'video source')

    def go_to_page(self):
        self.open("/firefox/performance/")

    billboard_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(1) > a'),
            'url_suffix': '#web',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(2) > a'),
            'url_suffix': '#hardware',
        }
    ]

    @property
    def perf_hardware_img_src(self):
        return self.selenium.find_element(*self._perf_hardware_img_locator).get_attribute('src')

    @property
    def is_video_overlay_visible(self):
        return self.is_element_present(*self._video_overlay_locator)

    @property
    def video_sources_list(self):
        srcs = []
        for source in self.selenium.find_elements(*self._video_sources_locator):
            srcs.append(source.get_attribute('src'))
        return srcs
