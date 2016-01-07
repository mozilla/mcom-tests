# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.desktop.partnerships import Partnerships


class TestPartnerships:

    @pytest.mark.nondestructive
    def test_section_link_destinations_are_correct(self, base_url, selenium):
        page = Partnerships(base_url, selenium).open()
        bad_links = []
        for link in page.section_links_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @pytest.mark.nondestructive
    def test_image_srcs_are_correct(self, base_url, selenium):
        page = Partnerships(base_url, selenium).open()
        bad_images = []
        for image in page.images_list:
            src = page.image_source(image.get('locator'))
            if not image.get('img_name_contains') in src:
                bad_images.append('%s does not contain %s' % (src, image.get('img_name_contains')))
        assert [] == bad_images

    @pytest.mark.nondestructive
    def test_partner_form_is_visible(self, base_url, selenium):
        page = Partnerships(base_url, selenium).open()
        partner_form = page.partner_form
        assert partner_form.is_form_present
        assert partner_form.is_title_visible, 'The title is not visible on the form'
        for field in partner_form.fields_list:
            assert partner_form.is_element_visible(*field), 'The %s field is not visible on the form' % field[1:]
        assert partner_form.is_submit_button_visible, 'The submit button is not visible on the form'
