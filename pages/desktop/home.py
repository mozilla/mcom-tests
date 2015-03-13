#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class HomePage(Base):

    def go_to_page(self):
        self.open('')

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox-download-section header a'),
            'url_suffix': '/firefox/',
        }, {
            'locator': (By.CSS_SELECTOR, '#upcoming-events .more-large'),
            'url_suffix': '/contribute/events/',
        }, {
            'locator': (By.CSS_SELECTOR, '.contribute-btn'),
            'url_suffix': '/contribute/',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary-links li:nth-child(1) a'),
            'url_suffix': '//addons.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary-links li:nth-child(2) a'),
            'url_suffix': '//careers.mozilla.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#secondary-links li:nth-child(3) a'),
            'url_suffix': '//support.mozilla.org/',
        }
    ]

    promo_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#promo-1 .panel-link')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-2 .panel-link')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-3 > a')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-4 > a')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-5 .fxos-link')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-6 .panel-link')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-7 > a')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-8 .panel-link')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-9 .panel-link')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-10 .panel-link')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-11 .panel-link')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-12 > a')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-13 > a')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-14 > a')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-15 > a')
        },
        {
            'locator': (By.CSS_SELECTOR, '#promo-16 .twt-actions a:nth-child(1)')
        },
    ]

    _sign_up_form_locator = (By.ID, 'mozorg-newsletter-form')

    sign_up_form_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'label.privacy-check-label > span > a'),
            'url_suffix': '/privacy/',
        },
    ]

    @property
    def is_sign_up_form_present(self):
        return self.is_element_present(*self._sign_up_form_locator)
