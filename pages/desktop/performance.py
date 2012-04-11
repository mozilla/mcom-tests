#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class PerformancePage(Base):

    _perf_web = (By.CSS_SELECTOR, "#perf-web")
    _perf_hardware = (By.CSS_SELECTOR, "#perf-hardware")
    _perf_hardware_img = (By.CSS_SELECTOR, "#hardware>.section-image")
    _video_overlay = (By.CSS_SELECTOR, ".mozilla-video-control-overlay")

    @property
    def perf_web_ico(self):
        return self.is_element_present(self._perf_web)

    @property
    def perf_hardware_ico(self):
        return self.is_element_present(self._perf_hardware)

    @property
    def perf_hardware_img(self):
        return self.is_element_present(self._perf_hardware_img)

    @property
    def video_overlay(self):
        return self.is_element_present(self._video_overlay)
