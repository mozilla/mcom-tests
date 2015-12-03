# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.base import Base


class Spaces(Base):

    _url = '{base_url}/{locale}/contact/spaces'

    spaces_nav_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=mountain-view] > a'),
            'url_suffix': '/contact/spaces/mountain-view/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=auckland] > a'),
            'url_suffix': '/contact/spaces/auckland/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=beijing] > a'),
            'url_suffix': '/contact/spaces/beijing/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=berlin] > a'),
            'url_suffix': '/contact/spaces/berlin/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=london] > a'),
            'url_suffix': '/contact/spaces/london/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=paris] > a'),
            'url_suffix': '/contact/spaces/paris/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=portland] > a'),
            'url_suffix': '/contact/spaces/portland/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=san-francisco] > a'),
            'url_suffix': '/contact/spaces/san-francisco/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=taipei] > a'),
            'url_suffix': '/contact/spaces/taipei/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=tokyo] > a'),
            'url_suffix': '/contact/spaces/tokyo/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=toronto] > a'),
            'url_suffix': '/contact/spaces/toronto/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-spaces > ul > li[data-id=vancouver] > a'),
            'url_suffix': '/contact/spaces/vancouver/'
        }
    ]


class Communities(Base):

    _url = '{base_url}/{locale}/contact/communities'

    region_nav_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=north-america] > a'),
            'url_suffix': '/contact/communities/north-america/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=latin-america] > a'),
            'url_suffix': '/contact/communities/latin-america/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=europe] > a'),
            'url_suffix': '/contact/communities/europe/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=asia] > a'),
            'url_suffix': '/contact/communities/asia-south-pacific/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=antarctica] > a'),
            'url_suffix': '/contact/communities/antarctica/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=africa] > a'),
            'url_suffix': '/contact/communities/africa-middle-east/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=arabic] > a'),
            'url_suffix': '/contact/communities/arabic/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=francophone] > a'),
            'url_suffix': '/contact/communities/francophone/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=hispano] > a'),
            'url_suffix': '/contact/communities/hispano/'
        }, {
            'locator': (By.CSS_SELECTOR, '#nav-communities > ul > li[data-id=balkans] > a'),
            'url_suffix': '/contact/communities/balkans/'
        }
    ]

    region_legend_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=north-america] > a'),
            'url_suffix': '/contact/communities/north-america/'
        }, {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=latin-america] > a'),
            'url_suffix': '/contact/communities/latin-america/'
        }, {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=europe] > a'),
            'url_suffix': '/contact/communities/europe/'
        }, {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=asia] > a'),
            'url_suffix': '/contact/communities/asia-south-pacific/'
        }, {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=antarctica] > a'),
            'url_suffix': '/contact/communities/antarctica/'
        }, {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=africa] > a'),
            'url_suffix': '/contact/communities/africa-middle-east/'
        }, {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=arabic] > a'),
            'url_suffix': '/contact/communities/arabic/'
        }, {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=francophone] > a'),
            'url_suffix': '/contact/communities/francophone/'
        }, {
            'locator': (By.CSS_SELECTOR, '#map > ul > li[data-id=hispano] > a'),
            'url_suffix': '/contact/communities/hispano/'
        },
    ]
