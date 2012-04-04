#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Base(Page):

    _desktop_link = (By.CSS_SELECTOR, '#nav-main-features > a')
    _mobile_link = (By.CSS_SELECTOR, '#nav-main-mobile > a')
    _releases_link = (By.CSS_SELECTOR, '#nav-main-releases > a')
    _addons_link = (By.CSS_SELECTOR, '#nav-main-addons > a')
    _support_link = (By.CSS_SELECTOR, '#nav-main-support > a')
    _about_link = (By.CSS_SELECTOR, '#nav-main-about > a')

    @property
    def header(self):
        return self.Header(self.testsetup)

    @property
    def footer(self):
        return self.Footer(self.testsetup)

    class Header(Page):

        _tabzilla = (By.ID, 'tabzilla')
        _tabzilla_panel = (By.ID, 'tabzilla-panel')

        _tabzilla_mission_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(1) > a')
        _tabzilla_about_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(2) > a')
        _tabzilla_projects_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(3) > a')
        _tabzilla_support_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(4) > a')
        _tabzilla_developer_network_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(5) > a')
        _tabzilla_firefox_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(1) > a')
        _tabzilla_thunderbird_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(2) > a')
        _tabzilla_webfwd_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(1) > a')
        _tabzilla_labs_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(2) > a')
        _tabzilla_volunteer_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(1) > a')
        _tabzilla_work_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(2) > a')
        _tabzilla_findus_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(3) > a')
        _tabzilla_joinus_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(4) > a')
        _tabzilla_learnmore_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(5) > a')
        _tabzilla_search_textbox = (By.CSS_SELECTOR, '#tabzilla-search #q')

        def toggle_tabzilla_dropdown(self):
            state = self.selenium.execute_script("return Tabzilla.opened")
            self.selenium.find_element(*self._tabzilla).click()
            WebDriverWait(self.selenium, 5).until(lambda s: state != s.execute_script("return Tabzilla.opened"))

        @property
        def is_tabzilla_panel_visible(self):
            return self.is_element_visible(*self._tabzilla)
    
        @property
        def is_tabzilla_searchbox_visible(self):
            return self.is_element_visible(*self._tabzilla_search_textbox)

    class Footer(Page):
        
        _footer = (By.TAG_NAME, 'footer')
        _footer_mozilla_link = (By.CSS_SELECTOR, '.footer-logo > img')
        _contact_us_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(1) > a')
        _privacy_policy_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(2) > a')
        _legal_notices_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(3) > a')
        _report_trademark_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(4) > a')
        _abuse_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(5) > a')
        _twitter_link = (By.CSS_SELECTOR, '.span2:nth-of-type(2) > ul > li:nth-of-type(1) > a')
        _facebook_link = (By.CSS_SELECTOR, '.span2:nth-of-type(2) > ul > li:nth-of-type(2) > a')
        _firefox_affiliates_link = (By.CSS_SELECTOR, '.span2:nth-of-type(2) > ul > li:nth-of-type(3) > a')
        _creative_commons_license = (By.CSS_SELECTOR, '.span3 > p > a')

        @property
        def is_visible(self):
            return self.is_element_visible(*self._footer)
