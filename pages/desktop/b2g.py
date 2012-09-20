#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.desktop.base import Base
from pages.page import Page


class BootToGecko(Base):

    def go_to_page(self):
        self.open('/b2g/')

    b2g_nav_links_list = [
        {
            'name': 'Home',
            'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-of-type(1) > a'),
            'url_suffix': '/b2g/',
        }, {
            'name': 'About',
            'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-of-type(2) > a'),
            'url_suffix': '/b2g/about/',
        }, {
            'name': 'FAQ',
            'locator': (By.CSS_SELECTOR, '#nav-main > ul > li:nth-of-type(3) > a'),
            'url_suffix': '/b2g/faq/',
        }
    ]

    breadcrumb_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '.breadcrumbs > a:nth-of-type(1)'),
            'url_suffix': '/',
        }, {
            'locator': (By.CSS_SELECTOR, '.breadcrumbs > a:nth-of-type(2)'),
            'url_suffix': '/b2g/',
        }
    ]

    more_information_links_list = [
        {
            'locator': (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(1) > a'),
            'url_suffix': 'blog.mozilla.org/blog/2012/07/02/firefox-mobile-os/',
        }, {
            'locator': (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(2) > a'),
            'url_suffix': '/b2g/about/',
        }, {
            'locator': (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(3) > a'),
            'url_suffix': '/b2g/faq/',
        }, {
            'locator': (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(4) > a'),
            'url_suffix': 'brendaneich.com/2012/02/mobile-web-api-evolution/',
        }, {
            'locator': (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(5) > a'),
            'url_suffix': 'blog.mozilla.com/blog/2012/02/27/mozilla-in-mobile-the-web-is-the-platform/',
        }, {
            'locator': (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(6) > a'),
            'url_suffix': 'pressoffice.telefonica.com/jsp/base.jsp?contenido=/jsp/notasdeprensa/notadetalle.jsp&selectNumReg=5&pagina=1&id=66&origen=notapres&idm=eng&pais=1&elem=17874',
        }
    ]

    images_list = [
        {
            'locator': (By.CSS_SELECTOR, '#primary > img'),
            'img_name_suffix': 'hero.png',
        }, {
            'locator': (By.CSS_SELECTOR, '.span5:nth-of-type(1) figure img:nth-child(1)'),
            'img_name_suffix': 'example-messages.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '.span5:nth-of-type(1) figure img:nth-child(2)'),
            'img_name_suffix': 'example-contacts.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '.span5:nth-of-type(2) figure img:nth-child(1)'),
            'img_name_suffix': 'example-incoming.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '.span5:nth-of-type(2) figure img:nth-child(2)'),
            'img_name_suffix': 'example-camera.jpg',
        }
    ]

    _mobile_devices_header_locator = (By.CSS_SELECTOR, '#main-feature > .large')
    _welcome_section_locator = (By.CSS_SELECTOR, '#primary')
    _developer_opportunities_header_locator = (By.CSS_SELECTOR, '.span5:nth-of-type(1) > h3:nth-of-type(1)')
    _customizations_for_oems_header_locator = (By.CSS_SELECTOR, '.span5:nth-of-type(1)> h3:nth-of-type(2)')
    _consumer_freedom_header_locator = (By.CSS_SELECTOR, '.span5:nth-of-type(1)> h3:nth-of-type(3)')
    _new_web_standards_header_locator = (By.CSS_SELECTOR, '.span5:nth-of-type(2) > h3:nth-of-type(1)')
    _freedom_platforms_header_locator = (By.CSS_SELECTOR, '.span5:nth-of-type(2) > h3:nth-of-type(2)')

    @property
    def is_mobile_devices_header_visible(self):
        return self.is_element_visible(*self._mobile_devices_header_locator)

    @property
    def is_welcome_section_visible(self):
        return self.is_element_visible(*self._welcome_section_locator)

    @property
    def is_developer_opportunities_header_visible(self):
        return self.is_element_visible(*self._developer_opportunities_header_locator)

    @property
    def is_customizations_for_oems_header_visible(self):
        return self.is_element_visible(*self._customizations_for_oems_header_locator)

    @property
    def is_consumer_freedom_header_visible(self):
        return self.is_element_visible(*self._consumer_freedom_header_locator)

    @property
    def is_new_web_standards_header_visible(self):
        return self.is_element_visible(*self._new_web_standards_header_locator)

    @property
    def is_freedom_platforms_header_visible(self):
        return self.is_element_visible(*self._freedom_platforms_header_locator)

    @property
    def about_page(self):
        return self.AboutPage(self.testsetup)

    @property
    def faq_page(self):
        return self.FaqPage(self.testsetup)

    class AboutPage(Page):

        def go_to_page(self):
            self.open('/b2g/about/')

        _about_the_project_header_locator = (By.CSS_SELECTOR, '.span6 > h1')
        _technology_header_locator = (By.CSS_SELECTOR, '.span6 > h2:nth-of-type(1)')
        _open_standards_header_locator = (By.CSS_SELECTOR, '.span6 > h2:nth-of-type(2)')

        @property
        def is_about_the_project_header_visible(self):
            return self.is_element_visible(*self._about_the_project_header)

        @property
        def is_technology_header_visible(self):
            return self.is_element_visible(*self._technology_header)

        @property
        def is_open_standards_header_visible(self):
            return self.is_element_visible(*self._open_standards_header)

    class FaqPage(Page):

        def go_to_page(self):
            self.open('/b2g/faq/')

        _faq_header_locator = (By.CSS_SELECTOR, '.span6 > h1')
        _what_is_boot_to_gecko_header_locator = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(1)')
        _aim_of_project_header_locator = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(2)')
        _team_size_header_locator = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(3)')
        _relationships_header_locator = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(4)')
        _webapi_replacement_header_locator = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(5)')

        @property
        def is_faq_header_visible(self):
            return self.is_element_visible(*self._faq_header)

        @property
        def is_what_is_boot_to_gecko_header_visible(self):
            return self.is_element_visible(*self._what_is_boot_to_gecko_header)

        @property
        def is_aim_of_project_header_visible(self):
            return self.is_element_visible(*self._aim_of_project_header)

        @property
        def is_team_size_header_visible(self):
            return self.is_element_visible(*self._team_size_header)

        @property
        def is_relationships_header_visible(self):
            return self.is_element_visible(*self._relationships_header)

        @property
        def is_webapi_replacement_header_visible(self):
            return self.is_element_visible(*self._webapi_replacement_header)
