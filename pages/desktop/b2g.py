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

    _home_breadcrumb = (By.CSS_SELECTOR, '.breadcrumbs > a:nth-of-type(1)')
    _boot_to_gecko_breadcrumb = (By.CSS_SELECTOR, '.breadcrumbs > a:nth-of-type(2)')
    _home_navbar_link = (By.CSS_SELECTOR, '#nav-main > ul > li:nth-of-type(1) > a')
    _about_navbar_link = (By.CSS_SELECTOR, '#nav-main > ul > li:nth-of-type(2) > a')
    _faq_navbar_link = (By.CSS_SELECTOR, '#nav-main > ul > li:nth-of-type(3) > a')
    _mobile_devices_header = (By.CSS_SELECTOR, '#main-feature > .large')
    _welcome_section = (By.CSS_SELECTOR, '#primary')
    _welcome_section_image = (By.CSS_SELECTOR, '#primary > img')
    _new_web_standards_header = (By.CSS_SELECTOR, '.span5:nth-of-type(2) > h3:nth-of-type(1)')
    _freedom_platforms_header = (By.CSS_SELECTOR, '.span5:nth-of-type(2) > h3:nth-of-type(2)')
    _developer_opportunities_header = (By.CSS_SELECTOR, '.span5:nth-of-type(1) > h3:nth-of-type(1)')
    _customizations_for_oems_header = (By.CSS_SELECTOR, '.span5:nth-of-type(1)> h3:nth-of-type(2)')
    _consumer_freedom_header = (By.CSS_SELECTOR, '.span5:nth-of-type(1)> h3:nth-of-type(3)')
    _more_information_section = (By.CSS_SELECTOR, '#more-info > h3')
    _about_the_project_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(1) > a')
    _faq_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(2) > a')
    _mobile_web_api_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(3) > a')
    _web_platform_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(4) > a')
    _telefonica_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(5) > a')
    _gaia_link = (By.CSS_SELECTOR, '#more-info > ul > li:nth-of-type(6) > a')
    _recommended_reading_header = (By.CSS_SELECTOR, '#references > h4')
    _boot_to_gecko_team_wiki_link = (By.CSS_SELECTOR, '#references > ul > li > a')

    @property
    def is_home_breadcrumb_visible(self):
        return self.is_element_visible(*self._homebreadcrumb)

    @property
    def is_boot_to_gecko_breadcrum_visible(self):
        return self.is_element_visible(*self._)

    @property
    def is_home_navbar_visible(self):
        return self.is_element_visible(*self._home_navbar_link)

    @property
    def is_about_navbar_visible(self):
        return self.is_element_visible(*self._about_navbar_link)

    @property
    def is_faq_navbar_visible(self):
        return self.is_element_visible(*self._faq_navbar_link)

    @property
    def is_mobile_devices_header_visible(self):
        return self.is_element_visible(*self._mobile_devices_header)

    @property
    def is_welcome_section_visible(self):
        return self.is_element_visible(*self._welcome_section)

    @property
    def is_welcome_section_image_visible(self):
        return self.is_element_visible(*self._welcome_section_image)

    @property
    def is_new_web_standards_header_visible(self):
        return self.is_element_visible(*self._new_web_standards_header)

    @property
    def is_freedom_platforms_visible(self):
        return self.is_element_visible(*self._freedom_platforms_header)

    @property
    def is_developer_opportunities_visible(self):
        return self.is_element_visible(*self._developer_opportunities_header)

    @property
    def is_customizations_for_oems_header_visible(self):
        return self.is_element_visible(*self._customizations_for_oems_header)

    @property
    def is_more_information_section_visible(self):
        return self.is_element_visible(*self._more_information_section)

    @property
    def is_about_the_project_link_visible(self):
        return self.is_element_visible(*self._about_the_project_link)

    @property
    def is_faq_link_visible(self):
        return self.is_element_visible(*self._faq_link)

    @property
    def is_mobile_web_api_link_visible(self):
        return self.is_element_visible(*self._mobile_web_api_link)

    @property
    def is_web_platform_link_visible(self):
        return self.is_element_visible(*self._web_platform_link)

    @property
    def is_telefonica_link_visible(self):
        return self.is_element_visible(*self._telefonica_link)

    @property
    def is_gaia_link_visible(self):
        return self.is_element_visible(*self._gaia_link)

    @property
    def is_recommended_reading_header_visible(self):
        return self.is_element_visible(*self._recommended_reading_header)

    @property
    def is_boot_to_gecko_team_wiki_link_visible(self):
        return self.is_element_visible(*self._boot_to_gecko_team_wiki_link)

    @property
    def about_page(self):
        return self.AboutPage(self.testsetup)

    @property
    def faq_page(self):
        return self.FaqPage(self.testsetup)

    class AboutPage(Page):

        def go_to_page(self):
            self.open('/b2g/about/')

        _about_the_project_header = (By.CSS_SELECTOR, '.span6 > h1')
        _technology_header = (By.CSS_SELECTOR, '.span6 > h2:nth-of-type(1)')
        _open_standards_header = (By.CSS_SELECTOR, '.span6 > h2:nth-of-type(2)')

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

        _faq_header = (By.CSS_SELECTOR, '.span6 > h1')
        _what_is_boot_to_gecko_header = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(1)')
        _aim_of_project_header = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(2)')
        _team_size_header = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(3)')
        _relationships_header = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(4)')
        _webapi_replacement_header = (By.CSS_SELECTOR, '.span6 > dl > dt:nth-of-type(5)')

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
