# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.base import Base


class DoNotTrack(Base):

    _url = '{base_url}/{locale}/firefox/dnt'

    tracking_protection_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.sidebar-box > p > a:nth-of-type(1)'),
            'url_suffix': 'ie.microsoft.com/testdrive/Browser/TrackingProtectionLists/faq.html'
        },
        {
            'locator': (By.CSS_SELECTOR, '.sidebar-box > p > a:nth-of-type(2)'),
            'url_suffix': 'dnt-enabler.*.tpl'
        }
    ]
