#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from pages.desktop.contribute import Contribute, Signup
from unittestzero import Assert


class TestContribute:

    @pytest.mark.nondestructive
    @pytest.mark.xfail(reason='Contribute page redesign')
    def test_images_are_visible(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_images = []
        for image in contribute_page.images_list:
            if not contribute_page.is_element_visible(*image.get('locator')):
                bad_images.append('The image at %s is not visible' % image.get('locator')[1:])
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    @pytest.mark.xfail(reason='Contribute page redesign')
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
    @pytest.mark.xfail(reason='Contribute page redesign')
    def test_location_image_srcs_are_correct(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_images = []
        for image in contribute_page.locations_list:
            src = contribute_page.image_source(image.get('locator'))
            if not src.endswith(image.get('img_name_suffix')):
                bad_images.append('%s does not end with %s' % (src, image.get('img_name_suffix')))
        Assert.equal(0, len(bad_images), '%s bad images found: ' % len(bad_images) + ', '.join(bad_images))

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
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
            if url.find(link.get('url_suffix')) < 1:
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_major_links_are_visible(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_links = []
        for link in contribute_page.major_links_list:
            if not contribute_page.is_element_visible(*link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_major_link_destinations_are_correct(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_links = []
        for link in contribute_page.major_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_major_link_urls_are_valid(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        bad_urls = []
        for link in contribute_page.major_links_list:
            url = contribute_page.link_destination(link.get('locator'))
            response_code = contribute_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_sign_up_form_fields_are_visible(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        signup_page = contribute_page.click_signup()
        bad_fields = []
        for field in signup_page.sign_up_form_fields:
            if not signup_page.is_element_visible(*field.get('locator')):
                bad_fields.append('The field at %s is not visible' % field.get('locator')[1:])
        Assert.equal(0, len(bad_fields), '%s bad fields found: ' % len(bad_fields) + ', '.join(bad_fields))

    @pytest.mark.nondestructive
    def test_sign_up_form_is_visible(self, mozwebqa):
        signup_page = Signup(mozwebqa)
        signup_page.go_to_page()
        Assert.true(signup_page.is_sign_up_form_present, 'The sign up form is not present on the page.')

    def test_sign_up_with_valid_email(self, mozwebqa):
        valid_email = 'noreply@mozilla.com'
        country = 'us'
        name = 'mozilla'
        success_url_slug = 'thankyou'
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        signup_page = contribute_page.click_signup()
        signup_page.click_testing_area()
        signup_page.select_option('testing-firefox', signup_page._sign_up_form_select_testing_area_locator)
        signup_page.input_name(name)
        signup_page.input_email(valid_email)
        signup_page.select_option(country, signup_page._sign_up_form_country_select_locator)
        signup_page.select_html_format()
        signup_page.check_privacy_checkbox()
        signup_page.submit_form()
        Assert.true(success_url_slug in signup_page.url_current_page,
                    'Expected current URL slug to be %s, but was not found in %s.' %
                    (success_url_slug, signup_page.url_current_page))
