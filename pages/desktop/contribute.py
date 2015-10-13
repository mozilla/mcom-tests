# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.base import Base


class Contribute(Base):

    _url = '{base_url}/{locale}/contribute'

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#contribute-nav-menu li:nth-child(1) a'),
            'url_suffix': 'contribute/',
        }, {
            'locator': (By.CSS_SELECTOR, '#contribute-nav-menu li:nth-child(2) a'),
            'url_suffix': 'events/',
        }, {
            'locator': (By.CSS_SELECTOR, '#contribute-nav-menu li:nth-child(3) a'),
            'url_suffix': 'stories/',
        }, {
            'locator': (By.CSS_SELECTOR, '#landing-mission .mission-cta a'),
            'url_suffix': '//videos.cdn.mozilla.net/uploads/mozillaorg/Mozilla_2014_i_am.webm',
        }, {
            'locator': (By.CSS_SELECTOR, '.section.landing-howto a'),
            'url_suffix': 'signup/',
        }, {
            'locator': (By.CSS_SELECTOR, '.other-actions li:nth-child(1) a'),
            'url_suffix': 'Give-Now?source=mozillaorg&ref=volunteer_getinvolvedpage201410&utm_campaign=volunteer_getinvolvedpage201410&utm_source=mozillaorg&utm_medium=referral',
        }, {
            'locator': (By.CSS_SELECTOR, '.other-actions li:nth-child(2) a'),
            'url_suffix': 'firefox/',
        }, {
            'locator': (By.CSS_SELECTOR, '.other-actions li:nth-child(3) a'),
            'url_suffix': '//www.facebook.com/mozilla',
        }, {
            'locator': (By.CSS_SELECTOR, '.other-actions li:nth-child(4) a'),
            'url_suffix': '//twitter.com/mozilla',
        }, {
            'locator': (By.CSS_SELECTOR, '.extra-links ul:nth-of-type(1) li:nth-child(1) a'),
            'url_suffix': 'contact/communities/',
        }, {
            'locator': (By.CSS_SELECTOR, '.extra-links ul:nth-of-type(1) li:nth-child(2) a'),
            'url_suffix': 'about/forums/',
        }, {
            'locator': (By.CSS_SELECTOR, '.extra-links ul:nth-of-type(1) li:nth-child(3) a'),
            'url_suffix': '//wiki.mozilla.org/IRC',
        }
    ]
