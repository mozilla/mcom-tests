#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from pages.desktop.contribute import Contribute
from unittestzero import Assert


class TestContribute:

    @pytest.mark.nondestructive
    def test_images_are_visible(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_images = []
        for image in contribute_page.images_list:
            if not contribute_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_image_srcs_are_correct(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_images = []
        for image in contribute_page.images_list:
            src = contribute_page.image_source(image.get('locator'))
            if not src.endswith(image.get('img_name_suffix')):
                bad_images.append('%s does not end with %s' % (src, image.get('img_name_suffix')))
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_images_srcs_are_valid(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_urls = []
        for image in contribute_page.images_list:
            url = contribute_page.image_source(image.get('locator'))
            response_code = contribute_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_tools_links_are_visible(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_links = []
        for link in contribute_page.details_links:
            if not contribute_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tools_link_destinations_are_correct(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_links = []
        for link in contribute_page.details_links:
            url = contribute_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    @pytest.xfail(reason='863449 link to developer.mozilla.org is broken')
    def test_tools_link_urls_are_valid(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_urls = []
        for link in contribute_page.details_links:
            url = contribute_page.link_destination(link.get('locator'))
            response_code = contribute_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        Assert.contains(contribute_page.footer.expected_footer_logo_destination,
                        contribute_page.footer.footer_logo_destination)
        Assert.contains(contribute_page.footer.expected_footer_logo_img,
                        contribute_page.footer.footer_logo_img)
        bad_links = []
        for link in Contribute.Footer.footer_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_tabzilla_links_are_correct(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        Assert.true(contribute_page.header.is_tabzilla_panel_visible)
        contribute_page.header.toggle_tabzilla_dropdown()
        bad_links = []
        for link in Contribute.Header.tabzilla_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_want_to_help_form_is_correct(self, mozwebqa):
        if mozwebqa.base_url == 'https://www.allizom.org':
            pytest.xfail(reason='Bug 793002 - reCaptcha key for staging is bad')
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        help_form = contribute_page.help_form
        # Expand the help form
        help_form.click_email()
        Assert.true(contribute_page.help_form.elements_are_visible)
        privacy_link = help_form.privacy_link
        url = contribute_page.link_destination(privacy_link.get('locator'))
        Assert.true(url.endswith(privacy_link.get('url_suffix')), '%s does not end with %s' % (url, privacy_link.get('url_suffix')))
        response_code = contribute_page.get_response_code(url)
        Assert.equal(response_code, requests.codes.ok, '%s is not a valid url - status code: %s.' % (url, response_code))
