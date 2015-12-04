# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.base import Base


class Mission(Base):

    _url = '{base_url}/{locale}/mission'

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-content div.main a'),
            'url_suffix': '/about/manifesto/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links li:nth-child(1) a'),
            'url_suffix': '/contribute/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links li:nth-child(2) a'),
            'url_suffix': '/about/history/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links li:nth-child(3) a'),
            'url_suffix': '/about/forums/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content ul.links li:nth-child(4) a'),
            'url_suffix': '/about/governance/',
        }
    ]

    _video_sources_locator = (By.CSS_SELECTOR, 'video source')

    @property
    def video_sources_list(self):
        srcs = []
        for source in self.selenium.find_elements(*self._video_sources_locator):
            srcs.append(source.get_attribute('src'))
        return srcs
