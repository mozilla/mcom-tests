#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Security(Base):

    billboard_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(1) > a'),
            'url_suffix': '#privacy',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(2) > a'),
            'url_suffix': '#secure',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(3) > a'),
            'url_suffix': '#control',
        }, {
            'locator': (By.CSS_SELECTOR, '.menu-bar.billboard > ul > li:nth-of-type(4) > a'),
            'url_suffix': '#mission',
        }
    ]

    section_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(1) > p > a'),
            'url_suffix': 'support.mozilla.org/kb/how-do-i-stop-websites-tracking-me',
        }, {
            'locator': (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(2) > p > a'),
            'url_suffix': 'support.mozilla.org/kb/Private%20Browsing',
        }, {
            'locator': (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(3) > p > a'),
            'url_suffix': 'support.mozilla.org/kb/Clear%20Recent%20History',
        }, {
            'locator': (By.CSS_SELECTOR, '#privacy > .row > .section-list.span3 > li:nth-of-type(4) > p > a'),
            'url_suffix': 'support.mozilla.org/kb/Clear%20Recent%20History#w_how-do-i-remove-a-single-website-from-my-history',
        }, {
            'locator': (By.CSS_SELECTOR, '#secure > .row > .section-list.span3 > li:nth-of-type(1) > p > a'),
            'url_suffix': 'support.mozilla.org/kb/Site%20Identity%20Button',
        }, {
            'locator': (By.CSS_SELECTOR, '#control > .row > .section-list.span3 > li:nth-of-type(1) > p > a'),
            'url_suffix': '/plugincheck/',
        }, {
            'locator': (By.CSS_SELECTOR, '#control > .row > .section-list.span3 > li:nth-of-type(3) > p > a'),
            'url_suffix': 'support.mozilla.org/kb/Options%20window%20-%20Security%20panel'
        }, {
            'locator': (By.CSS_SELECTOR, '#mission > .row > .section-list.span3 > li:nth-of-type(1) > p > a'),
            'url_suffix': '/legal/privacy/firefox.html',
        }, {
            'locator': (By.CSS_SELECTOR, '#mission > .row > .section-list.span3 > li:nth-of-type(2) > p > a'),
            'url_suffix': '/about/mission.html',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '#privacy > .row > .section-image > .platform-img.js'),
            'img_name_contains': 'screenshot-privacy',
        }, {
            'locator': (By.CSS_SELECTOR, '#secure > .row > .section-image > .platform-img.js'),
            'img_name_contains': 'screenshot-anti-malware',
        }, {
            'locator': (By.CSS_SELECTOR, '#control > .row > .section-image > .platform-img.js'),
            'img_name_contains': 'screenshot-plugins',
        }, {
            'locator': (By.CSS_SELECTOR, '#mission > .row > .section-image.span4 > img'),
            'img_name_contains': 'community',
        }
    ]

    def go_to_page(self):
        self.open('/firefox/security/')
