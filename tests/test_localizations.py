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
        languages = localizations_page.released_languages + localizations_page.beta_languages
        #languages = [localizations_page.language_by_id('ar')] # short list for debugging
        bad_statuses = []
        for language in languages:
            for (url, os_name) in ((language.windows_url, "Windows"),
                                   (language.osx_url, "OSX"),
                                   (language.linux_url, "Linux")):
                response = requests.head(url, allow_redirects=False)
                status = response.status_code
                if status != 302:
                    bad_statuses.append("Lang '%s' %s link: status %s"
                                            % (language.id, os_name, status))
        Assert.equal(0, len(bad_statuses),
                        'Expected status code 302.  ' + ",  ".join(bad_statuses))
