# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.desktop.privacy import Privacy

nondestructive = pytest.mark.nondestructive


class TestPrivacy:

    @nondestructive
    def test_footer_section(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        bad_links = []
        for link in Privacy.Footer.footer_links_list:
            url = privacy_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @nondestructive
    def test_page_sections(self, mozwebqa):
        privacy_page = Privacy(mozwebqa)
        privacy_page.go_to_page()
        bad_links = []
        for link in privacy_page.section_links_list:
            url = privacy_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links
