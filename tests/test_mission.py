# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from pages.desktop.mission import Mission


class TestMission:

    @pytest.mark.nondestructive
    def test_major_link_destinations_are_correct(self, base_url, selenium):
        page = Mission(base_url, selenium).open()
        bad_links = []
        for link in page.major_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.link_check
    @pytest.mark.nondestructive
    def test_major_link_urls_are_valid(self, base_url, selenium):
        page = Mission(base_url, selenium).open()
        bad_urls = []
        for link in page.major_links_list:
            url = page.link_destination(link.get('locator'))
            response_code = page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @pytest.mark.link_check
    @pytest.mark.nondestructive
    def test_video_srcs_are_valid(self, base_url, selenium):
        page = Mission(base_url, selenium).open()
        bad_srcs = []
        for src in page.video_sources_list:
            response_code = page.get_response_code(src)
            if response_code != requests.codes.ok:
                bad_srcs.append('%s is not a valid url - status code: %s.' % (src, response_code))
        assert [] == bad_srcs

    @pytest.mark.nondestructive
    def test_footer_section(self, base_url, selenium):
        page = Mission(base_url, selenium).open()
        bad_links = []
        for link in Mission.Footer.footer_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links
