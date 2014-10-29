#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert
from pages.desktop.projects import Projects


class TestProjects:

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        projects_page = Projects(mozwebqa)
        projects_page.go_to_page()
        Assert.true(projects_page.header.is_tabzilla_panel_visible)
        projects_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Projects.Header.tabzilla_links_list:
            url = projects_page.link_destination(link.get('locator'))
            if url.find(link.get('url_suffix')) < 1:
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_destinations_are_correct(self, mozwebqa):
        projects_page = Projects(mozwebqa)
        projects_page.go_to_page()
        bad_links = []
        for link in projects_page.billboard_links_list:
            url = projects_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_billboard_link_urls_are_valid(self, mozwebqa):
        projects_page = Projects(mozwebqa)
        projects_page.go_to_page()
        bad_urls = []
        for link in projects_page.billboard_links_list:
            url = projects_page.link_destination(link.get('locator'))
            response_code = projects_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_projects_link_destinations_are_correct(self, mozwebqa):
        projects_page = Projects(mozwebqa)
        projects_page.go_to_page()
        bad_links = []
        for link in projects_page.projects_links_list:
            url = projects_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_projects_link_urls_are_valid(self, mozwebqa):
        projects_page = Projects(mozwebqa)
        projects_page.go_to_page()
        bad_urls = []
        for link in projects_page.projects_links_list:
            url = projects_page.link_destination(link.get('locator'))
            response_code = projects_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))
