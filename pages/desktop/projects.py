#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Projects(Base):

    def go_to_page(self):
        self.open('/research/projects/')

    billboard_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(1) > a'),
            'url_suffix': '#rust',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(2) > a'),
            'url_suffix': '#servo',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(3) > a'),
            'url_suffix': '#shumway',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(4) > a'),
            'url_suffix': '#emscripten',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(5) > a'),
            'url_suffix': '#daala',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(6) > a'),
            'url_suffix': '#sweetjs',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(7) > a'),
            'url_suffix': '#lljs',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(8) > a'),
            'url_suffix': '#broadwayjs',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(9) > a'),
            'url_suffix': '#parallel',
        }, {
            'locator': (By.CSS_SELECTOR, '#project-list > ul > li:nth-of-type(10) > a'),
            'url_suffix': '#asmjs',
        }
    ]

    projects_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#rust > div.intro > ul > li:nth-of-type(1) > a'),
            'url_suffix': 'www.rust-lang.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#rust > div.intro > ul > li:nth-of-type(2) > a'),
            'url_suffix': 'github.com/mozilla/rust',
        }, {
            'locator': (By.CSS_SELECTOR, '#servo > div.intro > ul > li > a'),
            'url_suffix': 'github.com/mozilla/servo',
        }, {
            'locator': (By.CSS_SELECTOR, '#shumway > div.intro > ul > li > a'),
            'url_suffix': 'github.com/mozilla/shumway',
        }, {
            'locator': (By.CSS_SELECTOR, '#emscripten > div.intro > ul > li > a'),
            'url_suffix': 'github.com/kripken/emscripten',
        }, {
            'locator': (By.CSS_SELECTOR, '#sweetjs > div.intro > ul > li:nth-of-type(1) > a'),
            'url_suffix': 'sweetjs.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#sweetjs > div.intro > ul > li:nth-of-type(2) > a'),
            'url_suffix': 'github.com/mozilla/sweet.js',
        }, {
            'locator': (By.CSS_SELECTOR, '#lljs > div.intro > ul > li:nth-of-type(1) > a'),
            'url_suffix': 'lljs.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#lljs > div.intro > ul > li:nth-of-type(2) > a'),
            'url_suffix': 'github.com/mbebenita/LLJS',
        }, {
            'locator': (By.CSS_SELECTOR, '#broadwayjs > div.intro > ul > li > a'),
            'url_suffix': 'github.com/mbebenita/broadway',
        }, {
            'locator': (By.CSS_SELECTOR, '#parallel > div.intro > ul > li:nth-of-type(1) > a'),
            'url_suffix': 'wiki.ecmascript.org/doku.php?id=strawman:data_parallelism',
        }, {
            'locator': (By.CSS_SELECTOR, '#parallel > div.intro > ul > li:nth-of-type(2) > a'),
            'url_suffix': 'github.com/syg/iontrail/',
        }, {
            'locator': (By.CSS_SELECTOR, '#asmjs > div.intro > ul > li > a'),
            'url_suffix': 'github.com/dherman/asm.js',
        }
    ]
