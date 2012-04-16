#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class AboutPage(Base):

    _participate_img = (By.CSS_SELECTOR, '#get-involved > h3 > a > span');
    _txt_participate = (By.CSS_SELECTOR, '#get-involved > h3 > a');
    _communications_img = (By.CSS_SELECTOR, '#press > h3 > a > span');
    _txt_communications = (By.CSS_SELECTOR, '#press > h3 > a');
    _careers_img = (By.CSS_SELECTOR, '#careers > h3 > a > span');
    _txt_careers = (By.CSS_SELECTOR, '#careers > h3 > a');
    _partnerships_img = (By.CSS_SELECTOR, '#partnerships > h3 > a > span');
    _txt_partnerships = (By.CSS_SELECTOR, '#partnerships > h3 > a');
    _legal_img = (By.CSS_SELECTOR, '#licensing > h3 > a > span');
    _txt_legal = (By.CSS_SELECTOR, '#licensing > h3 > a');
    _contact_us_img = (By.CSS_SELECTOR, '#contact > h3 > a > span');
    _txt_contact_us = (By.CSS_SELECTOR, '#contact > h3 > a');
    _store_img = (By.CSS_SELECTOR, '#store > h3 > a > span');
    _txt_store = (By.CSS_SELECTOR, '#store > h3 > a');
    _blog_img = (By.CSS_SELECTOR, '#blog > h3 > a > span');
    _txt_blog = (By.CSS_SELECTOR, '#blog > h3 > a');

    @property
    def participate_image(self):
        return self.is_element_present(self._participate_img)

    @property
    def participate_text(self):
        return self.is_element_present(self._txt_participate)

    @property
    def communications_image(self):
        return self.is_element_present(self._communications_img)

    @property
    def communications_text(self):
        return self.is_element_present(self._txt_communications)

    @property
    def careers_image(self):
        return self.is_element_present(self._careers_img)

    @property
    def careers_text(self):
        return self.is_element_present(self._txt_careers)

    @property
    def partnerships_image(self):
        return self.is_element_present(self._partnerships_img)

    @property
    def partnerships_text(self):
        return self.is_element_present(self._txt_partnerships)

    @property
    def legal_image(self):
        return self.is_element_present(self._legal_img)

    @property
    def legal_text(self):
        return self.is_element_present(self._txt_legal)

    @property
    def contact_us_image(self):
        return self.is_element_present(self._contact_us_img)

    @property
    def contact_us_text(self):
        return self.is_element_present(self._txt_contact_us)

    @property
    def store_image(self):
        return self.is_element_present(self._store_img)

    @property
    def store_text(self):
        return self.is_element_present(self._txt_store)

    @property
    def blog_image(self):
        return self.is_element_present(self._blog_img)

    @property
    def  blog_text(self):
        return self.is_element_present(self._txt_blog)
