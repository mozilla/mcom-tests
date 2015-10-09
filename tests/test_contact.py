# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.desktop.contact import Contact, Spaces, Communities

nondestructive = pytest.mark.nondestructive


class TestContact:

    def check_bad_links(self, page, link_list):
        bad_links = []
        for link in link_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @nondestructive
    def test_spaces_links_are_correct(self, mozwebqa):
        spaces_page = Spaces(mozwebqa)
        spaces_page.go_to_page()
        self.check_bad_links(spaces_page, spaces_page.spaces_nav_links_list)

    @nondestructive
    def test_start_on_contact(self, mozwebqa):
        contact_page = Contact(mozwebqa)
        contact_page.go_to_page()
        assert 'current' == contact_page.contact_tab.get_attribute('class'), 'Page does not start on contact us tab.'

    @nondestructive
    def test_switching_tabs_list_display(self, mozwebqa):
        spaces_page = Spaces(mozwebqa)
        spaces_page.go_to_page()
        communities_page = spaces_page.click_communities_tab()
        spaces_page.wait_until_element_visible(communities_page.region_list)
        assert communities_page.region_list.is_displayed(), 'List of regions not displayed on communities tab.'
        spaces_page = communities_page.click_spaces_tab()
        spaces_page.wait_until_element_visible(spaces_page.spaces_list)
        assert spaces_page.spaces_list.is_displayed(), 'List of spaces not displayed on spaces tab.'

    @nondestructive
    def test_spaces_map_marker_visibility(self, mozwebqa):
        spaces_page = Spaces(mozwebqa)
        spaces_page.go_to_page()
        print len(spaces_page.spaces_markers)
        bad_markers = []
        for index, space in enumerate(spaces_page.spaces_links):
            space.click()
            spaces_page.wait_until_element_visible(spaces_page.spaces_markers[index])
            if not spaces_page.spaces_markers[index].is_displayed():
                bad_markers.append('%s marker is not visible.' % space.text)
        assert [] == bad_markers

    @nondestructive
    def test_region_links_are_correct(self, mozwebqa):
        communities_page = Communities(mozwebqa)
        communities_page.go_to_page()
        self.check_bad_links(communities_page, communities_page.region_nav_links_list)

    @nondestructive
    def test_region_legend_links_are_correct(self, mozwebqa):
        communities_page = Communities(mozwebqa)
        communities_page.go_to_page()
        assert communities_page.region_legend.is_displayed(), 'Legend not displayed'
        self.check_bad_links(communities_page, communities_page.region_legend_links_list)

    @nondestructive
    def test_region_dropdown_link(self, mozwebqa):
        communities_page = Communities(mozwebqa)
        communities_page.go_to_page()
        click_regions = [
            communities_page.click_north_america,
            communities_page.click_latin_america,
            communities_page.click_europe,
            communities_page.click_asia_south_pacific,
            communities_page.click_africa_middle_east
        ]
        region_communities = [
            communities_page.north_america_communities,
            communities_page.latin_america_communities,
            communities_page.europe_communities,
            communities_page.asia_south_pacific_communities,
            communities_page.africa_middle_east_communities,
            communities_page.balkans_communities
        ]
        bad_communities = []
        for index, action in enumerate(click_regions):
            action()
            for community in region_communities[index]:
                communities_page.wait_until_element_visible(community)
                if not community.is_displayed():
                    bad_communities.append('%s is not displayed.' % community.text)
        assert [] == bad_communities
