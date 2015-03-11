#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.desktop.base import Base


class Contribute(Base):

    def go_to_page(self):
        self.open('/contribute/')

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

    _signup_link_locator = (By.CSS_SELECTOR, '.section.landing-howto a')

    def click_signup(self):
        signup_link = self.selenium.find_element(*self._signup_link_locator)
        signup_link.click()
        return Signup(self.testsetup)


class Signup(Contribute):

    def go_to_page(self):
        self.open('/contribute/signup')

    _testing_area_locator = (By.CSS_SELECTOR, '.categories .option #category-testing')
    _sign_up_form_locator = (By.CSS_SELECTOR, '.personal')
    _coding_topic_locator = (By.CSS_SELECTOR, 'label.category-coding')
    _testing_topic_locator = (By.CSS_SELECTOR, 'label.category-testing')
    _coding_subtopic_locator = (By.ID, 'id_area_coding')
    _testing_subtopic_locator = (By.ID, 'id_area_testing')
    _submit_button_locator = (By.CSS_SELECTOR, '.submit button')

    def click_testing_area(self):
        self.selenium.find_element(*self._testing_area_locator).click()

    def click_coding_topic(self):
        self.selenium.find_element(*self._coding_topic_locator).click()

    def click_testing_topic(self):
        self.selenium.find_element(*self._testing_topic_locator).click()

    def select_random_coding_subtopic(self):
        coding_subtopics = ['coding-firefox', 'coding-firefoxos',
                            'coding-websites', 'coding-addons',
                            'coding-marketplace', 'coding-webcompat',
                            'coding-cloud']

        element = self.selenium.find_element(*self._coding_subtopic_locator)
        select = Select(element)
        select.select_by_value(coding_subtopics[randint(0, 6)])

    def select_random_testing_subtopic(self):
        subtopics = ['testing-firefox', 'testing-addons', 'testing-marketplace',
                     'testing-websites', 'testing-webcompat']

        element = self.selenium.find_element(*self._testing_subtopic_locator)
        select = Select(element)
        select.select_by_value(subtopics[randint(0, 4)])

    sign_up_form_fields = [
        {
            'locator': (By.ID, 'id_name'),
        },
        {
            'locator': (By.ID, 'id_email'),
        }, {
            'locator': (By.ID, 'id_country'),
        }, {
            'locator': (By.CSS_SELECTOR, 'input[type="radio"][value="T"]'),
        }, {
            'locator': (By.ID, 'id_privacy'),
        },
    ]

    @property
    def is_sign_up_form_present(self):
        return self.is_element_present(*self._sign_up_form_locator)

    def complete_sign_up_form(self):
        # Name
        element = self.selenium.find_element(*self.sign_up_form_fields[0]['locator'])
        element.send_keys('QA Test User')
        # Email
        element = self.selenium.find_element(*self.sign_up_form_fields[1]['locator'])
        element.send_keys('f1258291@trbvm.com')
        # Country
        element = self.selenium.find_element(*self.sign_up_form_fields[2]['locator'])
        select = Select(element)
        select.select_by_value('us')
        # Format
        element = self.selenium.find_element(*self.sign_up_form_fields[3]['locator'])
        element.click()
        # Privacy
        element = self.selenium.find_element(*self.sign_up_form_fields[4]['locator'])
        element.click()

    def click_submit_button(self):
        self.selenium.find_element(*self._submit_button_locator).click()
        return ConfirmationPage(self.testsetup)


class ConfirmationPage(Contribute):

    _confirmation_text_locator = (By.CSS_SELECTOR, '#thankyou .section-tagline')

    def confirmation_text(self):
        return (self.selenium.find_element(*self._confirmation_text_locator)).text
