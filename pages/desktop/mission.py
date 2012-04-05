#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class MissionPage(Base):

    _mission_sidebar_link = (By.CSS_SELECTOR, '.sidebar > nav > ul > li:nth-of-type(1) > a')
    _forums_sidebar_link = (By.CSS_SELECTOR, '.sidebar > nav > ul > li:nth-of-type(2) > a')
    _governance_sidebar_link = (By.CSS_SELECTOR, '.sidebar > nav > ul > li:nth-of-type(3) > a')
    _history_sidebar_link = (By.CSS_SELECTOR, '.sidebar > nav > ul > li:nth-of-type(4) > a')
    _home_breadcrumb_link = (By.CSS_SELECTOR, '.breadcrumbs > a')
    _mission_breadcrumb_link = (By.CSS_SELECTOR, '.breadcrumbs > span')
    _video_section = (By.CSS_SELECTOR, '.mozilla-video-control-overlay')
    _our_projects_learn_more_link = (By.CSS_SELECTOR, '.reference:nth-of-type(1)  > .more')
    _get_involved_learn_more_link = (By.CSS_SELECTOR, '.reference:nth-of-type(2) > .more')

    def go_to_page(self):
        self.open('/en-US/mission')

    @property
    def are_sidebar_links_visible(self):
        self.is_element_visible(*self._mission_sidebar_link)
        self.is_element_visible(*self._forums_sidebar_link)
        self.is_element_visible(*self._governance_sidebar_link)
        self.is_element_visible(*self._history_sidebar_link)
        return True

    @property
    def are_breadcrumb_links_visible(self):
        self.is_element_visible(*self._home_breadcrumb_link)
        self.is_element_visible(*self._mission_breadcrumb_link)
        return True

    @property
    def are_learn_more_links_visible(self):
        self.is_element_visible(*self._our_projects_learn_more_link)
        self.is_element_visible(*self._get_involved_learn_more_link)
        return True
