#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
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
