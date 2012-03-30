#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.home import Home


class TestTechnologyPage:

    @pytest.mark.nondestructive
    def test_blog_links(self, mozwebqa):
        home=Home(mozwebqa)
        home.got_to_page()

        Assert.equal('In the news', home.home_news_title)

        for link in home.home_news_links:
            Assert.contains('blog.mozilla', link)

    @pytest.mark.nondestructive
    def test_get_updates_area(self, mozwebqa):
        home=Home(mozwebqa)
        home.got_to_page()

        email_form=home.email_form

        Assert.equal('Get Mozilla updates:', email_form.title)
        Assert.equal('YOUR EMAIL HERE', email_form.email_placeholder)
        Assert.equal(u'Sign me up\xa0\xbb', email_form.submit_button_text)

        Assert.false(email_form.is_additional_info_visible)

        email_form.click_email()

        Assert.true(email_form.is_additional_info_visible)

        Assert.equal('I agree to the Privacy Policy', email_form.privacy_text)
        Assert.equal('http://www-dev.allizom.org/en-US/privacy-policy', email_form.privacy_link)
        Assert.equal('We will only send you Mozilla-related information.', email_form.form_details_text)

        Assert.equal(232, email_form.country_count)
