# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.desktop.contact import Spaces, Communities


class TestContact:

    def check_bad_links(self, page, link_list):
        bad_links = []
        for link in link_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.nondestructive
    def test_spaces_links_are_correct(self, base_url, selenium):
        page = Spaces(base_url, selenium).open()
        self.check_bad_links(page, page.spaces_nav_links_list)

    @pytest.mark.nondestructive
    def test_region_links_are_correct(self, base_url, selenium):
        page = Communities(base_url, selenium).open()
        self.check_bad_links(page, page.region_nav_links_list)

    @pytest.mark.nondestructive
    def test_region_legend_links_are_correct(self, base_url, selenium):
        page = Communities(base_url, selenium).open()
        self.check_bad_links(page, page.region_legend_links_list)
