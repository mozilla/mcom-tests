#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.localization import Localization
from unittestzero import Assert
import requests
import pytest


class TestLocalizations:

    @pytest.mark.nondestructive
    def test_that_download_links_return_302(self, mozwebqa):
        '''
            Check that download links return a status 302.
        '''
        localizations_page = Localization(mozwebqa)
        localizations_page.go_to_page()
        languages = localizations_page.get_released_languages + localizations_page.get_beta_languages
        bad_links = []
        for language in languages:
            for (url, os_name) in ((language['windows_url'], "Windows"),
                                   (language['osx_url'], "OSX"),
                                   (language['linux_url'], "Linux")):
                response = requests.head(url, allow_redirects=False)
                status = response.status_code
                if status != 302:
                    bad_links.append("Lang '%s' %s link: status %s"
                                            % (language['id'], os_name, status))
        Assert.equal(0, len(bad_links),
                        'Expected status code 302.  ' + ",  ".join(bad_links))
