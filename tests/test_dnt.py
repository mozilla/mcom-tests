# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from fnmatch import fnmatchcase

import pytest

from pages.desktop.dnt import DoNotTrack

nondestructive = pytest.mark.nondestructive


class TestDoNotTrack:

    @nondestructive
    def test_footer_section(self, mozwebqa):
        dnt_page = DoNotTrack(mozwebqa)
        dnt_page.go_to_page()
        bad_links = []
        for link in DoNotTrack.Footer.footer_links_list:
            url = dnt_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @nondestructive
    def test_status_section(self, mozwebqa):
        dnt_page = DoNotTrack(mozwebqa)
        dnt_page.go_to_page()
        assert dnt_page.is_status_wrapper_visible
        assert dnt_page.is_status_text_visible
        assert dnt_page.is_enable_dnt_image_visible
        assert dnt_page.is_enable_dnt_text_visible
        bad_links = []
        for link in dnt_page.tracking_protection_links_list:
            url = dnt_page.link_destination(link.get('locator'))
            if not fnmatchcase(url, '*/' + link.get('url_suffix')):
                bad_links.append('%s does not match %s' % (url, link.get('url_suffix')))
        assert [] == bad_links
