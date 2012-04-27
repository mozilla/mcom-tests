#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Security(Base):

    _menu_protect_your_privacy = (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(1) > a')
    _menu_browse_with_security = (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(2) > a')
    _menu_stay_in_control = (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(3) > a')
    _menu_part_of_our_mission = (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(4) > a')

    _privacy_screeenshot = (By.CSS_SELECTOR, '#privacy > .row > .section-image > .platform-img.js')
    _security_screenshot = (By.CSS_SELECTOR, '#secure > .row > .section-image > .platform-img.js')
    _control_image = (By.CSS_SELECTOR, '#control > .row > .section-image > .platform-img.js')
    _mission_image = (By.CSS_SELECTOR, '#mission > .row > .section-image.span4 > img')

    _section_do_not_track_ = (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(1 ) > h4')
    _section_private_browsing = (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(2) > h4')
    _section_clear_recent_history = (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(3) > h4')
    _section_forget_this_site = (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(4) > h4')
    _section_content_security_policy = (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(5) > h4')

    _section_instant_web_id = (By.CSS_SELECTOR, '#secure > .row > .section-list.span3 > li:nth-of-type(1) > h4')
    _section_anti_phishing_malware = (By.CSS_SELECTOR, '#secure > .row > .section-list.span3 > li:nth-of-type(2) > h4')
    _section_secure_installation = (By.CSS_SELECTOR, '#secure > .row > .section-list.span3 > li:nth-of-type(3) > h4')
    _section_av_integration = (By.CSS_SELECTOR, '#secure > .row > .section-list.span3 > li:nth-of-type(4) > h4')

    _section_plugin_check = (By.CSS_SELECTOR, '#control > .row > .section-list.span3 > li:nth-of-type(1) > h4')
    _section_parental_controls = (By.CSS_SELECTOR, '#control > .row > .section-list.span3 > li:nth-of-type(2) > h4')
    _section_customized_settings = (By.CSS_SELECTOR, '#control > .row > .section-list.span3 > li:nth-of-type(3) > h4')

    _section_privacy_commitment = (By.CSS_SELECTOR, '#mission > .row > .section-list.span3 > li:nth-of-type(1) > h4')
    _section_mission_matters = (By.CSS_SELECTOR, '#mission > .row > .section-list.span3 > li:nth-of-type(2) > h4')

    _return_to_top_link = (By.CSS_SELECTOR, '.top-link > a')

    def go_to_page(self):
        self.open('/firefox/security/')

    @property
    def are_menus_visible(self):
        return self.is_element_visible(*self._menu_protect_your_privacy)  and \
        self.is_element_visible(*self._menu_browse_with_security)  and \
        self.is_element_visible(*self._menu_stay_in_control)  and \
        self.is_element_visible(*self._menu_part_of_our_mission)

    @property
    def are_screenshots_visible(self):
        return self.is_element_visible(*self._privacy_screenshot)  and \
        self.is_element_visible(*self._security_screenshot)  and \
        self.is_element_visible(*self._control_image)  and \
        self.is_element_visible(*self._mission_image)

    @property
    def are_privacy_titles_visible(self):
        return self.is_element_visible(*self._section_do_not_track)  and \
        self.is_element_visible(*self._section_private_browsing)  and \
        self.is_element_visible(*self._section_clear_recent_history)  and \
        self.is_element_visible(*self._section_forget_this_site)  and \
        self.is_element_visible(*self._section_content_security_policy)

    @property
    def click_return_to_top(self):
        self.click(self._return_to_top_link)
