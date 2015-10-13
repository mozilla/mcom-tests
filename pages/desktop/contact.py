# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.desktop.base import Base


class Contact(Base):

    _url = '{base_url}/{locale}/contact'

    _spaces_tab_locator = (By.CSS_SELECTOR, '.category-tabs > li[data-id=spaces]')
    _contact_tab_locator = (By.CSS_SELECTOR, '.category-tabs > li[data-id=contact]')
    _communities_tab_locator = (By.CSS_SELECTOR, '.category-tabs > li[data-id=communities]')
    _spaces_tab_link_locator = (By.CSS_SELECTOR,
                                '#page-content > .category-tabs > li[data-id=spaces] > a')
    _communities_tab_link_locator = (By.CSS_SELECTOR,
                                     '#page-content > .category-tabs > li[data-id=communities] > a')

    @property
    def contact_tab(self):
        return self.selenium.find_element(*self._contact_tab_locator)

    @property
    def spaces_tab(self):
        return self.selenium.find_element(*self._spaces_tab_locator)

    @property
    def communities_tab(self):
        return self.selenium.find_element(*self._communities_tab_locator)

    def click_spaces_tab(self):
        spaces_tab_link = self.selenium.find_element(*self._spaces_tab_link_locator)
        spaces_tab_link.click()
        return Spaces(self.base_url, self.selenium).wait_for_page_to_load()

    def click_communities_tab(self):
        communities_tab_link = self.selenium.find_element(*self._communities_tab_link_locator)
        communities_tab_link.click()
        return Communities(self.base_url, self.selenium).wait_for_page_to_load()


class Spaces(Contact):

    _url = '{base_url}/{locale}/contact/spaces'

    _spaces_list_locator = (By.ID, 'nav-spaces')
    _spaces_marker_locator = (By.CSS_SELECTOR, '#map .leaflet-marker-pane > .leaflet-marker-icon')

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

    @property
    def spaces_markers(self):
        return self.selenium.find_elements(*self._spaces_marker_locator)

    @property
    def spaces_links(self):
        return [self.selenium.find_element(*link.get('locator'))
                for link in self.spaces_nav_links_list]

    @property
    def spaces_list(self):
        return self.selenium.find_element(*self._spaces_list_locator)


class Communities(Contact):

    _url = '{base_url}/{locale}/contact/communities'

    _region_list_locator = (By.ID, 'nav-communities')
    _region_legend_locator = (By.CSS_SELECTOR, '#map > ul')
    _communities_link_locator = (By.CSS_SELECTOR,
                                 '#nav-communities > ul > .hasmenu > .submenu > li > a')

    def click_north_america(self):
        self.selenium.find_element(By.CSS_SELECTOR,
                                   '#nav-communities > ul > li[data-id=north-america] > a').click()

    def click_latin_america(self):
        self.selenium.find_element(By.CSS_SELECTOR,
                                   '#nav-communities > ul > li[data-id=latin-america] > a').click()

    def click_europe(self):
        self.selenium.find_element(By.CSS_SELECTOR,
                                   '#nav-communities > ul > li[data-id=europe] > a').click()

    def click_asia_south_pacific(self):
        self.selenium.find_element(By.CSS_SELECTOR,
                                   '#nav-communities > ul > li[data-id=asia] > a').click()

    def click_africa_middle_east(self):
        self.selenium.find_element(By.CSS_SELECTOR,
                                   '#nav-communities > ul > li[data-id=africa] > a').click()

    def click_balkans(self):
        self.selenium.find_element(By.CSS_SELECTOR,
                                   '#nav-communities > ul > li[data-id=balkans] > a').click()

    @property
    def north_america_communities(self):
        return self.selenium.find_elements(By.CSS_SELECTOR,
                                           '#nav-communities > ul > li[data-id=north-america] > .submenu > li')

    @property
    def latin_america_communities(self):
        return self.selenium.find_elements(By.CSS_SELECTOR,
                                           '#nav-communities > ul > li[data-id=latin-america] > .submenu > li')

    @property
    def europe_communities(self):
        return self.selenium.find_elements(By.CSS_SELECTOR,
                                           '#nav-communities > ul > li[data-id=europe] > .submenu > li')

    @property
    def asia_south_pacific_communities(self):
        return self.selenium.find_elements(By.CSS_SELECTOR,
                                           '#nav-communities > ul > li[data-id=asia] > .submenu > li')

    @property
    def africa_middle_east_communities(self):
        return self.selenium.find_elements(By.CSS_SELECTOR,
                                           '#nav-communities > ul > li[data-id=africa] > .submenu > li')

    @property
    def balkans_communities(self):
        return self.selenium.find_elements(By.CSS_SELECTOR,
                                           '#nav-communities > ul > li[data-id=balkans] > .submenu > li')

    @property
    def region_list(self):
        return self.selenium.find_element(*self._region_list_locator)

    @property
    def region_legend(self):
        return self.selenium.find_element(*self._region_legend_locator)

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
