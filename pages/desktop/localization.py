from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class Localization(Base):
    _released_languages_locator = (By.CSS_SELECTOR, '#languages table.downloads')
    _beta_languages_locator = (By.CSS_SELECTOR, '#beta_versions table.downloads')
    _language_locator = (By.CSS_SELECTOR, 'tbody tr')
    _windows_download_link = (By.CSS_SELECTOR, 'td a.download-windows')
    _osx_download_link = (By.CSS_SELECTOR, 'td a.download-osx')
    _linux_download_link = (By.CSS_SELECTOR, 'td a.download-linux')
    
    def go_to_page(self):
        self.open('/firefox/all.html')
    
    def get_language_properties(self, table_locator):
        languages = []
        table = self.selenium.find_element(*table_locator)
        for language in table.find_elements(*self._language_locator):
            language_properties = {}  #dictionary to hold language properties
            language_properties['id'] = language.get_attribute('id')
            language_properties['windows_url'] = language.find_element(*self._windows_download_link).get_attribute('href')
            language_properties['osx_url'] = language.find_element(*self._osx_download_link).get_attribute('href')
            language_properties['linux_url'] = language.find_element(*self._linux_download_link).get_attribute('href')
            languages.append(language_properties)
        return languages
    
    @property
    def get_released_languages(self):
        return self.get_language_properties(self._released_languages_locator)
    
    @property
    def get_beta_languages(self):
        return self.get_language_properties(self._beta_languages_locator)
    
