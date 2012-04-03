#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By
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
