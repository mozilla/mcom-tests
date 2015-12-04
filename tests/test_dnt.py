# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from fnmatch import fnmatchcase

import pytest

from pages.desktop.dnt import DoNotTrack


class TestDoNotTrack:

    @pytest.mark.nondestructive
    def test_footer_section(self, base_url, selenium):
        page = DoNotTrack(base_url, selenium).open()
        bad_links = []
        for link in DoNotTrack.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.nondestructive
    def test_status_section(self, base_url, selenium):
        page = DoNotTrack(base_url, selenium).open()
        bad_links = []
        for link in page.tracking_protection_links_list:
            url = page.link_destination(link.get('locator'))
            if not fnmatchcase(url, '*/' + link.get('url_suffix')):
                bad_links.append('%s does not match %s' % (url, link.get('url_suffix')))
        assert [] == bad_links
