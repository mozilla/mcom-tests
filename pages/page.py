#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''
Created on Jun 21, 2010

'''
import re
import time

import requests
from unittestzero import Assert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from requests.exceptions import Timeout

http_regex = re.compile('https?://((\w+\.)+\w+\.\w+)')


class Page(object):
    """
    Base class for all Pages
    """

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    @property
    def is_the_current_page(self):
        if self._page_title:
            page_title = self.page_title
            Assert.equal(page_title, self._page_title,
                         "Expected page title: %s. Actual page title: %s" %
                         (self._page_title, page_title))

    @property
    def url_current_page(self):
        return(self.selenium.current_url)

    @property
    def page_title(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)
        return self.selenium.title

    def refresh(self):
        self.selenium.refresh()

    def open(self, url_fragment):
        self.selenium.get(self.base_url + url_fragment)
        self.selenium.maximize_window()

    def select_option(self, value, locator):
        dropdown = self.selenium.find_element(*locator)
        option_found = False
        all_options = dropdown.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") == value:
                option_found = True
                option.click()
                break
        if option_found is False:
            raise Exception("Option '" + value + "' was not found, thus not selectable.")

    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            # this will return a snapshot, which takes time.
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (ElementNotVisibleException, NoSuchElementException):
            # this will return a snapshot, which takes time.
            return False

    def wait_for_element_present(self, *locator):
        count = 0
        while not self.is_element_present(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout:
                raise Exception(':'.join(locator) + ' has not loaded')

    def wait_for_element_visible(self, *locator):
        count = 0
        while not self.is_element_visible(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout:
                raise Exception(':'.join(locator) + " is not visible")

    def wait_for_ajax(self):
        count = 0
        while count < self.timeout:
            time.sleep(1)
            count += 1
            if self.selenium.execute_script("return jQuery.active == 0"):
                return
        raise Exception("Wait for AJAX timed out after %s seconds" % count)

    def get_response_code(self, url):
        # return the response status
        # this sets max_retries to 5
        requests.adapters.DEFAULT_RETRIES = 10
        try:
            r = requests.get(url, verify=False, allow_redirects=True, timeout=self.timeout)
            return r.status_code
        except Timeout:
            return 408
