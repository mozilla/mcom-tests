# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait

from pages.page import Page


class Base(Page):

    def wait_for_page_to_load(self):
        el = self.selenium.find_element(By.TAG_NAME, 'html')
        Wait(self.selenium, self.timeout).until(
            lambda s: 'loaded' in el.get_attribute('class'))
        return self
