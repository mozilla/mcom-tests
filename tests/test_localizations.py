#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.localizations import Localizations
import requests
import pytest


class TestLocalizations:

    @pytest.mark.nondestructive
    def test_that_download_links_return_302(self, mozwebqa):
        '''
            Check that download links return a status 302.
        '''
        localizations_page = Localizations(mozwebqa)
        localizations_page.go_to_page()

        # get all languages from both tables
        languages = localizations_page.released_languages + localizations_page.beta_languages
        #languages = [localizations_page.language_by_id('ar')] # short list for debugging
        failure_buffer = ''

        for language in languages:
            for (url, os) in ((language.windows_url, "Windows"),
                              (language.osx_url, "OSX"),
                              (language.linux_url, "Linux")):
                response = requests.head(url, allow_redirects=False)
                status = response.status_code
                if status != 302:
                    failure_buffer = failure_buffer + \
                                  "Lang '%s' %s link: status %s.  " % (language.id, os, status)

        # generate a collective failure for failed link checks
        if len(failure_buffer) > 0:
            Assert.fail('Expected status code 302.  ' + failure_buffer)
