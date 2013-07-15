#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert
from pages.desktop.partnerships import Partnerships
from mocks.mock_partnership_request import MockPartnershipRequest


class TestPartnerships:

    @pytest.mark.nondestructive
    def test_section_links_are_visible(self, mozwebqa):
        partnerships_page = Partnerships(mozwebqa)
        partnerships_page.go_to_page()
        bad_links = []
        for link in partnerships_page.section_links_list:
            if not partnerships_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_section_link_destinations_are_correct(self, mozwebqa):
        partnerships_page = Partnerships(mozwebqa)
        partnerships_page.go_to_page()
        bad_links = []
        for link in partnerships_page.section_links_list:
            url = partnerships_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_section_link_urls_are_valid(self, mozwebqa):
        partnerships_page = Partnerships(mozwebqa)
        partnerships_page.go_to_page()
        bad_urls = []
        for link in partnerships_page.section_links_list:
            url = partnerships_page.link_destination(link.get('locator'))
            response_code = partnerships_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_images_are_visible(self, mozwebqa):
        partnerships_page = Partnerships(mozwebqa)
        partnerships_page.go_to_page()
        bad_images = []
        for image in partnerships_page.images_list:
            if not partnerships_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_image_srcs_are_correct(self, mozwebqa):
        partnerships_page = Partnerships(mozwebqa)
        partnerships_page.go_to_page()
        bad_images = []
        for image in partnerships_page.images_list:
            src = partnerships_page.image_source(image.get('locator'))
            if not image.get('img_name_contains') in src:
                bad_images.append('%s does not contain %s' % (src, image.get('img_name_contains')))
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_image_srcs_are_valid(self, mozwebqa):
        partnerships_page = Partnerships(mozwebqa)
        partnerships_page.go_to_page()
        bad_urls = []
        for image in partnerships_page.images_list:
            url = partnerships_page.image_source(image.get('locator'))
            response_code = partnerships_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_partner_form_is_visible(self, mozwebqa):
        partnerships_page = Partnerships(mozwebqa)
        partnerships_page.go_to_page()
        partner_form = partnerships_page.partner_form
        Assert.true(partner_form.is_form_present)
        Assert.true(partner_form.is_title_visible, 'The title is not visible on the form')
        for field in partner_form.fields_list:
            Assert.true(partner_form.is_element_visible(*field), 'The %s field is not visible on the form' % field[1:])
        Assert.true(partner_form.is_submit_button_visible, 'The submit button is not visible on the form')

    def test_partner_form_submit_is_successful(self, mozwebqa):
        partnerships_page = Partnerships(mozwebqa)
        partnerships_page.go_to_page()
        partner_form = partnerships_page.partner_form
        partnership_request = MockPartnershipRequest()
        partner_form.fill_out_form(partnership_request)
        partner_form.submit_form()
        partner_form.wait_for_form_success_visible()
        Assert.true(partner_form.is_form_success_visible, 'Form success section is not visible')
