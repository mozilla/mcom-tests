#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.privacy import Privacy


class TestPrivacy:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        bad_links = []
        for link in Privacy.Footer.footer_links_list:
            url = privacy_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        Assert.true(privacy_page.header.is_tabzilla_panel_visible)
        privacy_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Privacy.Header.tabzilla_links_list:
            url = privacy_page.link_destination(link.get('locator'))
            if url.find(link.get('url_suffix')) < 1:
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_page_sections(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        bad_links = []
        for link in privacy_page.section_links_list:
            url = privacy_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
