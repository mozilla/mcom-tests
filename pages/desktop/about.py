#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class AboutPage(Base):

    def go_to_page(self):
        self.open('/about/')

    _mission_header_link = (By.CSS_SELECTOR, '#nav-main li:nth-child(1) > a')
    _about_header_link = (By.CSS_SELECTOR, '#nav-main li:nth-child(2) > a')
    _projects_header_link = (By.CSS_SELECTOR, '#nav-main li:nth-child(3) > a')
    _get_involved_header_link = (By.CSS_SELECTOR, '#nav-main li:nth-child(4) > a')
    _get_to_know_mozilla_header = (By.CSS_SELECTOR, '.large.center')
    _career_center_link = (By.CSS_SELECTOR, '.links:nth-of-type(1) > li:nth-of-type(1) > h4 > a')
    _press_center_link = (By.CSS_SELECTOR, '.links:nth-of-type(1) > li:nth-of-type(2) > h4 > a')
    _mozilla_blog_link = (By.CSS_SELECTOR, '.links:nth-of-type(1) > li:nth-of-type(3) > h4 > a')
    _privacy_center_link = (By.CSS_SELECTOR, '.links:nth-of-type(1) > li:nth-of-type(4) > h4 > a')
    _forums_link = (By.CSS_SELECTOR, '.links:nth-of-type(1) > li:nth-of-type(5) > h4 > a')
    _governance_link = (By.CSS_SELECTOR, '.links:nth-of-type(2) > li:nth-of-type(5) > h4 > a')
    _get_involved_link = (By.CSS_SELECTOR, '.links:nth-of-type(2) > li:nth-of-type(4) > h4 > a')
    _locations_link = (By.CSS_SELECTOR, '.links:nth-of-type(2) > li:nth-of-type(3) > h4 > a')
    _partnerships_link = (By.CSS_SELECTOR, '.links:nth-of-type(2) > li:nth-of-type(2) > h4 > a')
    _brand_toolkit_link = (By.CSS_SELECTOR, '.links:nth-of-type(2) > li:nth-of-type(1) > h4 > a')

    major_links_list = [
            _career_center_link,
            _press_center_link,
            _mozilla_blog_link,
            _privacy_center_link,
            _forums_link,
            _governance_link,
            _get_involved_header_link,
            _locations_link,
            _partnerships_link,
            _brand_toolkit_link,
        ]

    nav_links_list = [
            _mission_header_link,
            _about_header_link,
            _projects_header_link,
            _get_involved_link,
        ]

    @property
    def is_know_mozilla_header_present(self):
        return self.is_element_present(*self._get_to_know_mozilla_header)
