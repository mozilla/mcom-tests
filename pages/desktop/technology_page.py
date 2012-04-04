#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


class TechnologyPage(Base):

    def go_to_page(self):
        self.open('/en-US/firefox/technology/')

    _developer_tools_link = (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(1) > a')
    _html5_link = (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(1) > a')
    _css_link = (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(1) > a')
    _apis_link = (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(1) > a')
    _svg_link = (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(1) > a')
    _security_link = (By.CSS_SELECTOR, '.menu-bar > ul > li:nth-of-type(1) > a')

    _demo_studio_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(1) > a')
    _easy_customization_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(2) > a')
    _mdn_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(1) > a')

    _web_console_section = (By.CSS_SELECTOR, '#tools > article:nth-of-type(1) > h1')
    _page_inspector_section = (By.CSS_SELECTOR, '#tools > article:nth-of-type(2) > h1')
    _scratch_pad_section = (By.CSS_SELECTOR, '#tools > article:nth-of-type(3) > h1')
    _firebug_section = (By.CSS_SELECTOR, '#tools > article:nth-of-type(4) > h1')
    _more_development_resources = (By.CSS_SELECTOR, '#tools > article:nth-of-type(5) > h1')

    _forms_section = (By.CSS_SELECTOR, '#html5 > article:nth-of-type(1) > h1')
    _parser_section = (By.CSS_SELECTOR, '#html5 > article:nth-of-type(2) > h1')
    _webm_section = (By.CSS_SELECTOR, '#html5 > article:nth-of-type(3) > h1')
    _video_buffer_section = (By.CSS_SELECTOR, '#html5 > article:nth-of-type(4) > h1')
    _video_preload_section = (By.CSS_SELECTOR, '#html5 > article:nth-of-type(5) > h1')
    _history_state_section = (By.CSS_SELECTOR, '#html5 > article:nth-of-type(6) > h1')

    _bulb_aricle_locator = (By.CSS_SELECTOR, '#wall article > article')

    @property
    def is_developer_tools_link_visible(self):
        return self.is_element_visible(*self._developer_tools_link)

    @property
    def is_html5_link_visible(self):
        return self.is_element_visible(*self._html5_link)

    @property
    def is_css_link_visible(self):
        return self.is_element_visible(*self._css_link)

    @property
    def is_apis_link_visible(self):
        return self.is_element_visible(*self._apis_link)

    @property
    def is_svg_link_visible(self):
        return self.is_element_visible(*self._svg_link)

    @property
    def is_security_link_visible(self):
        return self.is_element_visible(*self._security_link)

    @property
    def bulbs(self):
        return [self.Bulb(self.testsetup, bulb) for bulb in self.selenium.find_elements(*self._bulb_aricle_locator)]

    class Bulb(Page):

        _learn_more_locator = (By.CSS_SELECTOR, 'a.learn')

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root = element

        def hover(self):
            ActionChains(self._root).mouse_over(self._root).perform()

        @property
        def is_learn_more_present(self):
            try:
                self._root.find_element(*self._learn_more_locator)
                return True
            except NoSuchElementException:
                return False

        @property
        def is_learn_more_displayed(self):
            return self._root.find_element(*self._learn_more_locator).is_displayed()
