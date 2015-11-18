# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.base import Base


class HomePage(Base):

    _url = '{base_url}/{locale}'

    major_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#firefox-download-section header a'),
            'url_suffix': '/firefox/',
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

    sign_up_form_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'label.privacy-check-label > span > a'),
            'url_suffix': '/privacy/',
        },
    ]

    def __init__(self, base_url, selenium):
        super(HomePage, self).__init__(base_url, selenium)
        # issue mozilla/mcom-tests#399
        # events area of home page will come and go based on whether
        # remo is responding at the time of deployment. This is reliably
        # testable on stage and prod, but not dev.
        if 'www-dev.allizom.org' not in base_url:
            self.major_links_list.append({
                'locator': (By.CSS_SELECTOR, '#upcoming-events .more-large'),
                'url_suffix': '/contribute/events/',
            })
