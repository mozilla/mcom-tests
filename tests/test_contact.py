# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.desktop.contact import Contact, Spaces, Communities


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
    def test_start_on_contact(self, base_url, selenium):
        page = Contact(base_url, selenium).open()
        assert 'current' == page.contact_tab.get_attribute('class'), 'Page does not start on spaces tab.'

    @pytest.mark.nondestructive
    def test_switching_tabs_list_display(self, base_url, selenium):
        spaces_page = Spaces(base_url, selenium).open()
        communities_page = spaces_page.click_communities_tab()
        communities_page.wait_for_element_visible(communities_page.region_list)
        assert communities_page.region_list.is_displayed(), 'List of regions not displayed on communities tab.'
        spaces_page = communities_page.click_spaces_tab()
        spaces_page.wait_for_element_visible(spaces_page.spaces_list)
        assert spaces_page.spaces_list.is_displayed(), 'List of spaces not displayed on spaces tab.'

    @pytest.mark.nondestructive
    def test_spaces_map_marker_visibility(self, base_url, selenium):
        page = Spaces(base_url, selenium).open()
        print len(page.spaces_markers)
        bad_markers = []
        for index, space in enumerate(page.spaces_links):
            space.click()
            page.wait_for_element_visible(page.spaces_markers[index])
            if not page.spaces_markers[index].is_displayed():
                bad_markers.append('%s marker is not visible.' % space.text)
        assert [] == bad_markers

    @pytest.mark.nondestructive
    def test_region_links_are_correct(self, base_url, selenium):
        page = Communities(base_url, selenium).open()
        self.check_bad_links(page, page.region_nav_links_list)

    @pytest.mark.nondestructive
    def test_region_legend_links_are_correct(self, base_url, selenium):
        page = Communities(base_url, selenium).open()
        assert page.region_legend.is_displayed(), 'Legend not displayed'
        self.check_bad_links(page, page.region_legend_links_list)

    @pytest.mark.nondestructive
    def test_region_dropdown_link(self, base_url, selenium):
        page = Communities(base_url, selenium).open()
        click_regions = [
            page.click_north_america,
            page.click_latin_america,
            page.click_europe,
            page.click_asia_south_pacific,
            page.click_africa_middle_east]
        region_communities = [
            page.north_america_communities,
            page.latin_america_communities,
            page.europe_communities,
            page.asia_south_pacific_communities,
            page.africa_middle_east_communities,
            page.balkans_communities]
        bad_communities = []
        for index, action in enumerate(click_regions):
            action()
            for community in region_communities[index]:
                page.wait_for_element_visible(community)
                if not community.is_displayed():
                    bad_communities.append('%s is not displayed.' % community.text)
        assert [] == bad_communities
