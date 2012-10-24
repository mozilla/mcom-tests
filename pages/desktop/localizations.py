#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Localizations(Base):
    # element containing languages
    _released_languages_locator = (By.CSS_SELECTOR, '#languages table.downloads')
    _beta_languages_locator = (By.CSS_SELECTOR, '#beta_versions table.downloads')
    # element containing a language
    _language_locator = (By.CSS_SELECTOR, 'tbody tr')
    # element for a specific language based on id attribute
    def _language_by_id_locator(self, language_id):
        return (By.CSS_SELECTOR, 'tbody tr#%s' % language_id)

    # elements in a language
    _windows_link_locator = (By.CSS_SELECTOR, 'td a.download-windows')
    _osx_link_locator = (By.CSS_SELECTOR, 'td a.download-osx')
    _linux_link_locator = (By.CSS_SELECTOR, 'td a.download-linux')

    def go_to_page(self):
        self.open('/firefox/all.html')

    class Language():
        ''' data values for a language '''
        def __init__(self, language_element):
            self.id = language_element.get_attribute('id')
            self.windows_url = language_element.find_element(
                *Localizations._windows_link_locator).get_attribute('href')
            self.osx_url = language_element.find_element(
                *Localizations._osx_link_locator).get_attribute('href')
            self.linux_url = language_element.find_element(
                *Localizations._linux_link_locator).get_attribute('href')

    def _get_language_table(self, table_locator):
        ''' get languages from 'table_locator' table '''
        languages = []
        table = self.selenium.find_element(*table_locator)
        for language in table.find_elements(*self._language_locator):
            languages.append(self.Language(language))
        return languages

    @property
    def released_languages(self):
        return self._get_language_table(self._released_languages_locator)

    @property
    def beta_languages(self):
        return self._get_language_table(self._beta_languages_locator)

    def language_by_id(self, language_id):
        return self.Language(self.selenium.find_element(
                                               *self._language_by_id_locator(language_id)))
