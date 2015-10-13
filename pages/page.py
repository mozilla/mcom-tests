# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait as Wait


class Page(object):

    _url = None

    def __init__(self, base_url, selenium, locale='en-US'):
        self.base_url = base_url
        self.selenium = selenium
        self.locale = locale
        self.timeout = 10

    def open(self):
        self.selenium.get(self.url)
        self.wait_for_page_to_load()
        return self

    @property
    def url(self):
        if self._url is not None:
            return self._url.format(base_url=self.base_url, locale=self.locale)
        return self.base_url

    def wait_for_page_to_load(self):
        return self

    @property
    def is_the_current_page(self):
        assert self._page_title == self.page_title
        return True

    @property
    def url_current_page(self):
        return(self.selenium.current_url)

    @property
    def page_title(self):
        return Wait(self.selenium, self.timeout).until(lambda s: s.title)

    def refresh(self):
        self.selenium.refresh()

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
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_element_present(self, *locator):
        Wait(self.selenium, self.timeout).until(
            expected.presence_of_element_located(locator))

    def wait_for_element_visible(self, *args):
        if len(args) == 1 and isinstance(args[0], WebElement):
            Wait(self.selenium, self.timeout).until(
                expected.visibility_of(args[0]))
        else:
            Wait(self.selenium, self.timeout).until(
                expected.visibility_of_element_located(args))

    def get_response_code(self, url):
        # return the response status
        # this sets max_retries to 10
        requests.adapters.DEFAULT_RETRIES = 10
        try:
            r = requests.get(url, verify=False, allow_redirects=True, timeout=self.timeout)
            return r.status_code
        except requests.exceptions.Timeout:
            return 408
