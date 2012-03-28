from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Base(Page):

    _tabzilla = (By.CSS_SELECTOR, '#tabzilla')
    _tabzilla_mission_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(1) > a')
    _tabzilla_about_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(2) > a')
    _tabzilla_projects_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(3) > a')
    _tabzilla_support_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(4) > a')
    _tabzilla_developer_network_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(1) > ul > li:nth-of-type(5) > a')
    _tabzilla_firefox_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(1) > a')
    _tabzilla_thunderbird_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(2) > ul > li:nth-of-type(2) > a')
    _tabzilla_webfwd_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(1) > a')
    _tabzilla_labs_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(3) > ul > li:nth-of-type(2) > a')
    _tabzilla_volunteer_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(1) > a')
    _tabzilla_work_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(2) > a')
    _tabzilla_findus_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(3) > a')
    _tabzilla_joinus_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(4) > a')
    _tabzilla_learnmore_link = (By.CSS_SELECTOR, '#tabzilla-nav > ul > li:nth-child(4) > ul > li:nth-of-type(5) > a')
    _tabzilla_search_textbox = (By.CSS_SELECTOR, '#q')
    _desktop_link = (By.CSS_SELECTOR, '#nav-main-features > a')
    _mobile_link = (By.CSS_SELECTOR, '#nav-main-mobile > a')
    _releases_link = (By.CSS_SELECTOR, '#nav-main-releases > a')
    _addons_link = (By.CSS_SELECTOR, '#nav-main-addons > a')
    _support_link = (By.CSS_SELECTOR, '#nav-main-support > a')
    _about_link = (By.CSS_SELECTOR, '#nav-main-about > a')

    _footer_mozilla_link = (By.CSS_SELECTOR, '.footer-logo > img')
    _contact_us_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(1) > a')
    _privacy_policy_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(2) > a')
    _legal_notices_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(3) > a')
    _report_trademark_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(4) > a')
    _abuse_link = (By.CSS_SELECTOR, '.span2:nth-of-type(1) > ul > li:nth-of-type(5) > a')
    _twitter_link = (By.CSS_SELECTOR, '.span2:nth-of-type(2) > ul > li:nth-of-type(1) > a')
    _facebook_link = (By.CSS_SELECTOR, '.span2:nth-of-type(2) > ul > li:nth-of-type(2) > a')
    _firefox_affiliates_link = (By.CSS_SELECTOR, '.span2:nth-of-type(2) > ul > li:nth-of-type(3) > a')
    _creative_commons_license = (By.CSS_SELECTOR, '.span3 > p > a')

    @property
    def are_tabzilla_links_present(self):
        try:
            self.is_element_present(*self._tabzilla)
            self.is_element_present(*self._tabzilla_mission_link)
            self.is_element_present(*self._tabzilla_about_link)
            self.is_element_present(*self._tabzilla_projects_link)
            self.is_element_present(*self._tabzilla_support_link)
            self.is_element_present(*self._tabzilla_developer_network_link)
            self.is_element_present(*self._tabzilla_firefox_link)
            self.is_element_present(*self._tabzilla_thunderbird_link)
            self.is_element_present(*self._tabzilla_webfwd_link)
            self.is_element_present(*self._tabzilla_labs_link)
            self.is_element_present(*self._tabzilla_volunteer_link)
            self.is_element_present(*self._tabzilla_work_link)
            self.is_element_present(*self._tabzilla_findus_link)
            self.is_element_present(*self._tabzilla_learnmore_link)
            self.is_element_present(*self._tabzilla_search_textbox)
            return True
        except NoSuchElementException:
            return False

    def toggle_tabzilla_dropdown(self):
        self.selenium.find_element(*self._tabzilla).click()

    @property
    def are_footer_links_present(self):
        try:
            self.is_element_present(*self._footer_mozilla_link)
            self.is_element_present(*self._contact_us_link)
            self.is_element_present(*self._privacy_policy_link)
            self.is_element_present(*self._legal_notices_link)
            self.is_element_present(*self._report_trademark_link)
            self.is_element_present(*self._abuse_link)
            self.is_element_present(*self._twitter_link)
            self.is_element_present(*self._facebook_link)
            self.is_element_present(*self._firefox_affiliates_link)
            self.is_element_present(*self._creative_commons_license)
            return True
        except NoSuchElementException:
            return False
