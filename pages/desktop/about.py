# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait as Wait
from pages.desktop.base import Base


class AboutPage(Base):

    _url = '{base_url}/{locale}/about'

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(1) a'),
            'url_suffix': '/mission/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(2) a'),
            'url_suffix': 'careers.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(4) a'),
            'url_suffix': '/styleguide',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(5) a'),
            'url_suffix': '/contact/spaces/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(1) li:nth-child(6) a'),
            'url_suffix': '/foundation/moco/'

        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(1) a'),
            'url_suffix': '/about/leadership/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(2) a'),
            'url_suffix': '/firefox/products/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(3) a'),
            'url_suffix': '/contribute/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(5) a'),
            'url_suffix': '/privacy/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links:nth-of-type(2) li:nth-child(6) a'),
            'url_suffix': '/foundation/'
        }
    ]

    _sign_up_form_privacy_checkbox_locator = (By.ID, 'id_privacy')
    _sign_up_form_submit_button_locator = (By.ID, 'footer_email_submit')

    sign_up_form_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'label.privacy-check-label > span > a'),
            'url_suffix': '/privacy/',
        },
    ]

    def expand_sign_up_form(self):
        self.selenium.find_element(*self._sign_up_form_submit_button_locator).click()
        Wait(self.selenium, self.timeout).until(
            expected.visibility_of_element_located(
                self._sign_up_form_privacy_checkbox_locator))
