#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Contribute(Base):

    details_links = [
        {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(1) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '//support.mozilla.org/get-involved',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(1) >.content > p > a:nth-of-type(2)'),
            'url_suffix': '//support.mozilla.org/get-involved',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(2) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '//quality.mozilla.org/teams/desktop-firefox/',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(2) >.content > p > a:nth-of-type(2)'),
            'url_suffix': '//quality.mozilla.org/teams/web-qa/',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(2) >.content > p > a:nth-of-type(3)'),
            'url_suffix': '//quality.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(3) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '//developer.mozilla.org/docs/Introduction',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(3) >.content > p > a:nth-of-type(2)'),
            'url_suffix': '//www.whatcanidoformozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(4) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '//affiliates.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(4) >.content > p > a:nth-of-type(2)'),
            'url_suffix': '//wiki.mozilla.org/MarketingGuide',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(5) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '//wiki.mozilla.org/L10n',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(5) >.content > p > a:nth-of-type(2)'),
            'url_suffix': '//wiki.mozilla.org/L10n:Web_parts',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(6) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '//wiki.mozilla.org/Webdev/GetInvolved',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(6) >.content > p > a:nth-of-type(2)'),
            'url_suffix': '//developer.mozilla.org/docs/Mozilla/Firefox_OS/Platform/Gaia/Hacking',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(7) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '//addons.mozilla.org/developers/docs/getting-started',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(7) >.content > p > a:nth-of-type(2)'),
            'url_suffix': '//wiki.mozilla.org/AMO:Editors/Applying',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(8) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '/blog.mozilla.org/creative/',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(9) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '//developer.mozilla.org/docs/Project:How_to_Help',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(10) >.content > p > a:nth-of-type(1)'),
            'url_suffix': '/webmaker.org/',
        }, {
            'locator': (By.CSS_SELECTOR, 'li:nth-of-type(10) >.content > p > a:nth-of-type(2)'),
            'url_suffix': '/webmaker.org/events/',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(1) > img'),
            'img_name_suffix': 'sumo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(2) > img'),
            'img_name_suffix': 'qmo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(3) > img'),
            'img_name_suffix': 'dinohead.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(4) > img'),
            'img_name_suffix': 'firefox.png?2013-06',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(5) > img'),
            'img_name_suffix': 'localization.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(6) > img'),
            'img_name_suffix': 'web.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(7) > img'),
            'img_name_suffix': 'marketplace.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(8) > img'),
            'img_name_suffix': 'addons.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(9) > img'),
            'img_name_suffix': 'creativecollective.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(10) > img'),
            'img_name_suffix': 'mdn.png?03-2014',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-options > li:nth-child(11) > img'),
            'img_name_suffix': 'webmaker.png',
        }
    ]

    locations_list = [
        {
            'locator': (By.CSS_SELECTOR, '.locations > li:nth-child(1) > a > img'),
            'img_name_suffix': 'map-th-northamerica.png?03-2014'
        }, {
            'locator': (By.CSS_SELECTOR, '.locations > li:nth-child(2) > a > img'),
            'img_name_suffix': 'map-th-europe.png?03-2014'
        }, {
            'locator': (By.CSS_SELECTOR, '.locations > li:nth-child(3) > a > img'),
            'img_name_suffix': 'map-th-latinamerica.png?03-2014'
        }, {
            'locator': (By.CSS_SELECTOR, '.locations > li:nth-child(4) > a > img'),
            'img_name_suffix': 'map-th-africamideast.png?03-2014'
        }, {
            'locator': (By.CSS_SELECTOR, '.locations > li:nth-child(5) > a > img'),
            'img_name_suffix': 'map-th-asia.png?03-2014'
        }, {
            'locator': (By.CSS_SELECTOR, '.locations > li:nth-child(6) > a > img'),
            'img_name_suffix': 'map-th-southpole.png?03-2014'
        }
    ]

    def go_to_page(self):
        self.open('/contribute/')
