#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.notes import Notes
import pytest


class TestNotes:

    @pytest.mark.nondestructive
    def test_all_links(self, mozwebqa):
        notes_page = Notes(mozwebqa)
        notes_page.go_to_page()
        Assert.contains("Notes", notes_page.firefox_notes_header_text)
        bad_urls = []
        for url in notes_page.all_links:
            if not notes_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))
