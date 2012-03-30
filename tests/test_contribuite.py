#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.contribute import Contribuite

class TestContribute:

    areas_of_interest=[u'Area of interest?', u'Helping Users', u'Localization',
                       u'Testing and QA', u'Coding', u'Add-ons', u'Marketing',
                       u'Student Reps', u'Web Development', u'Developer Documentation',
                       u'Systems Administration', u'User Research', u'Thunderbird',
                       u'Accessibility', u'Firefox Suggestions', u'Other']

    @pytest.mark.nondestructive
    def test_want_to_help_area(self, mozwebqa):
        contribuite=Contribuite(mozwebqa)
        contribuite.got_to_page()

        help_form=contribuite.help_form

        Assert.equal('Want to help?', help_form.title)
        Assert.equal('YOUR EMAIL HERE', help_form.email_placeholder)

        for idx, area in enumerate(help_form.areas_of_interest_text):
            Assert.equal(self.areas_of_interest[idx], area)

        Assert.equal('Area of interest?', help_form.area_of_interest_selected_option)
        Assert.equal(u'Submit\xa0\xbb', help_form.submit_button_text)

        Assert.false(help_form.is_additional_info_visible)

        help_form.click_email()

        Assert.true(help_form.is_additional_info_visible)

        Assert.equal('Send us a note and we can get you started right away.', help_form.note_message)
        Assert.equal(u'Hi, I\u2019m interested in\u2026', help_form.comments_placeholder)
        Assert.equal('I agree to the Privacy Policy', help_form.privacy_text)
        Assert.equal('http://www-dev.allizom.org/en-US/privacy-policy', help_form.privacy_link)
        Assert.equal('I’d like to receive regular contribution news by email', help_form.newsletter_text)

    @pytest.mark.nondestructive
    def test_that_clicking_on_areas_of_interest_opens_the_help_form(self, mozwebqa):
        contribuite=Contribuite(mozwebqa)
        contribuite.got_to_page()

        help_form=contribuite.help_form

        Assert.false(help_form.is_additional_info_visible)
        help_form.click_email()
        Assert.true(help_form.is_additional_info_visible)
