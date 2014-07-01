#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.desktop.base import Base


class Partners(Base):

    _firefox_os_header_locator = (By.CSS_SELECTOR, '#main-feature > h2')
    _welcome_section_locator = (By.CSS_SELECTOR, '#primary')
    _new_web_standards_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(1) > h3:nth-of-type(1)')
    _freedom_platforms_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(1) > h3:nth-of-type(2)')
    _customizations_for_oems_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(2) > h3')
    _developer_opportunities_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(3) > h3')
    _consumer_freedom_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(4) > h3')
    _overview_menu_icon_locator = (By.CSS_SELECTOR, '#menu-overview > a')
    _os_menu_icon_locator = (By.CSS_SELECTOR, '#menu-os > a')
    _marketplace_menu_icon_locator = (By.CSS_SELECTOR, '#menu-marketplace > a')
    _android_menu_icon_locator = (By.CSS_SELECTOR, '#menu-android > a')
    _form_icon_locator = (By.CSS_SELECTOR, 'menu-form > a')
    _partner_pager_button_locator = (By.CSS_SELECTOR, '#mozilla-pager-page-2-tab')
    _partner_page_one_button_locator = (By.CSS_SELECTOR, '#mozilla-pager-page-1-tab')
    _partner_with_us_button_locator = (By.CSS_SELECTOR, '.partner-button > a')
    _phone_foxtail_image_locator = (By.CSS_SELECTOR, '.phone > #screen-overview > #foxtail')
    _phone_os_image_locator = (By.ID, 'screen-os')
    _os_overview_button_locator = (By.CSS_SELECTOR, '#os > .article-header > .tween > a.view-section:nth-of-type(1)')
    _operators_button_locator = (By.CSS_SELECTOR, '#os > .article-header > nav.tween > a.view-section[data-section=os-operators]:nth-of-type(2)')
    _phone_marketplace_image_locator = (By.ID, 'screen-marketplace')
    _phone_image_locator = (By.CSS_SELECTOR, '.phone-overlay')

    partner_images_pager_list_one = [
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(1) > img'),
            'img_name_suffix': 'telefonica.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(2) > img'),
            'img_name_suffix': 'dt.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(3) > img'),
            'img_name_suffix': 'lg.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(4) > img'),
            'img_name_suffix': 'qualcomm.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(5) > img'),
            'img_name_suffix': 'zte.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(6) > img'),
            'img_name_suffix': 'telenor.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(7) > img'),
            'img_name_suffix': 'americamovil.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(8) > img'),
            'img_name_suffix': 'tcl.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(9) > img'),
            'img_name_suffix': 'telecomitalia.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(10) > img'),
            'img_name_suffix': 'chinaunicom.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(11) > img'),
            'img_name_suffix': 'kddi.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(12) > img'),
            'img_name_suffix': 'sprint.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(13) > img'),
            'img_name_suffix': 'singtel.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(14) > img'),
            'img_name_suffix': 'etisalat.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(15) > img'),
            'img_name_suffix': 'koreatelecom.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-1 > .logos > li:nth-of-type(16) > img'),
            'img_name_suffix': 'vimpelcom.png'
        }
    ]

    partner_images_pager_list_two = [
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(2) > img'),
            'img_name_suffix': 'portugaltelecom.png'
        }, {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(2) > img'),
            'img_name_suffix': 'portugaltelecom.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(3) > img'),
            'img_name_suffix': 'megafon.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(4) > img'),
            'img_name_suffix': 'facebook.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(5) > img'),
            'img_name_suffix': 'twitter.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(6) > img'),
            'img_name_suffix': 'soundcloud.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(7) > img'),
            'img_name_suffix': 'here-com.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(8) > img'),
            'img_name_suffix': 'box.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(9) > img'),
            'img_name_suffix': 'ea.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(10) > img'),
            'img_name_suffix': 'ebay.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(11) > img'),
            'img_name_suffix': 'cuttherope.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#page-mozilla-pager-page-2 > .logos > li:nth-of-type(12) > img'),
            'img_name_suffix': 'wikipedia.png'
        }
    ]

    _operators_image_list = [
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(1) > img'),
            'url_suffix': 'telefonica.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(2) > img'),
            'url_suffix': 'dt.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(3) > img'),
            'url_suffix': 'lg.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(4) > img'),
            'url_suffix': 'qualcomm.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(5) > img'),
            'url_suffix': 'zte.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(6) > img'),
            'url_suffix': 'telenor.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(7) > img'),
            'url_suffix': 'kddi.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(8) > img'),
            'url_suffix': 'tcl.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(9) > img'),
            'url_suffix': 'telecomitalia.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(10) > img'),
            'url_suffix': 'chinaunicom.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(11) > img'),
            'url_suffix': 'sprint.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(12) > img'),
            'url_suffix': 'vimpelcom.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(13) > img'),
            'url_suffix': 'singtel.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(14) > img'),
            'url_suffix': 'etisalat.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(15) > img'),
            'url_suffix': 'koreatelecom.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(16) > img'),
            'url_suffix': 'smartcom.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(17) > img'),
            'url_suffix': 'megafon.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(18) > img'),
            'url_suffix': 'portugaltelecom.png'
        },
        {
            'locator': (By.CSS_SELECTOR, '#os-operators-logos1 > li:nth-of-type(19) > img'),
            'url_suffix': 'americamovil.png'
        }
    ]

    def go_to_page(self):
        self.open('/firefox/partners/')
        self.wait_for_element_visible(*self._partner_with_us_button_locator)

    def click_partner_pager_button(self):
        return self.selenium.find_element(*self._partner_pager_button_locator).click()

    def click_overview_menu(self):
        return self.selenium.find_element(*self._overview_menu_icon_locator).click()

    def click_marketplace_menu(self):
        return self.selenium.find_element(*self._marketplace_menu_icon_locator).click()

    def click_os_menu(self):
        self.selenium.find_element(*self._os_menu_icon_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(EC.visibility_of_element_located(self._os_overview_button_locator))

    def click_operators_button(self):
        WebDriverWait(self.selenium, self.timeout).until(EC.element_to_be_clickable(self._operators_button_locator))
        self.selenium.find_element(*self._operators_button_locator).click()
        element = WebDriverWait(self.selenium, self.timeout).until(EC.visibility_of_element_located(self._operators_image_list[-1]['locator']))
        return element

    @property
    def is_marketplace_image_visible(self):
        return self.is_element_visible(*self._phone_marketplace_image_locator)

    @property
    def is_partner_with_us_button_visible(self):
        return self.is_element_visible(*self._partner_with_us_button_locator)

    @property
    def is_foxtail_image_visible(self):
        return self.is_element_visible(*self._phone_foxtail_image_locator)

    @property
    def is_phone_overlay_visible(self):
        return self.is_element_visible(*self._phone_image_locator)

    def click_partner_page_one_button(self):
        self.selenium.find_element(*self._partner_page_one_button_locator).click()
