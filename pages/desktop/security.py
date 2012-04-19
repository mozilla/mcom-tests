#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class SecurityPage(Base):

    _protecting_privacy_ico = (By.CSS_SELECTOR, "#security-privacy")
    _browser_security_ico = (By.CSS_SELECTOR, "#security-secure")
    _in_control_ico = (By.CSS_SELECTOR, "#security-control")
    _mission_ico = (By.CSS_SELECTOR, "#security-mission")
    _privacy_img = (By.CSS_SELECTOR, "#privacy>.section-image>img")
    _browser_security_img = (By.CSS_SELECTOR, "#secure>.section-image>img")
    _control_img = (By.CSS_SELECTOR, "#control>.section-image>img")
    _mission_img = (By.CSS_SELECTOR, "#mission>.section-image>img")

    @property
    def protecting_privacy_ico(self):
        return self.is_element_present(self._protecting_privacy_ico)

    @property
    def browser_security_ico(self):
        return self.is_element_present(self._browser_security_ico)

    @property
    def in_control_ico(self):
        return self.is_element_present(self._in_control_ico)

    @property
    def mission_ico(self):
        return self.is_element_present(self._mission_ico)

    @property
    def privacy_img(self):
        return self.is_element_present(self._privacy_img)

    @property
    def browser_security_img(self):
        return self.is_element_present(self._browser_security_img)

    @property
    def control_img(self):
        return self.is_element_present(self._control_img)

    @property
    def mission_img(self):
        return self.is_element_present(self._mission_img)
