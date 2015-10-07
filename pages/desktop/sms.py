# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class SMS(Base):

    def go_to_page(self):
        self.open('/firefox/sms/')

    info_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.more p:nth-child(1) a'),
            'url_suffix': 'support.mozilla.org/kb/will-firefox-work-my-mobile-device',
        }, {
            'locator': (By.CSS_SELECTOR, '.more p:nth-child(2) a'),
            'url_suffix': '/firefox/android/',
        }
    ]
