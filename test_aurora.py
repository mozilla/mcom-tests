#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.aurora import AuroraPage
import pytest
xfail = pytest.mark.xfail


class TestAurora:

    def test_that_headers_are_present(self, mozwebqa):
        aurora_pg = AuroraPage(mozwebqa)
        aurora_pg.go_to_aurora_page()
        Assert.true(aurora_pg.is_preview_features_header_present)
        Assert.true(aurora_pg.is_share_feedback_header_present)
        Assert.true(aurora_pg.is_shape_firefox_header_present)
        Assert.true(aurora_pg.is_aurora_header_present)

    def test_download_button_section(self, mozwebqa):
        aurora_pg = AuroraPage(mozwebqa)
        aurora_pg.go_to_aurora_page()
        Assert.true(aurora_pg.is_aurora_download_button_present)
        Assert.true(aurora_pg.is_all_systems_and_languages_link_present)
        Assert.true(aurora_pg.is_privacy_policy_link_present)

    def test_aurora_newsletter_submission(self, mozwebqa):
        aurora_pg = AuroraPage(mozwebqa)
        aurora_pg.go_to_aurora_page()
        aurora_pg.type_email("me@example.com")
        aurora_pg.check_aurora_checkbox()
        aurora_pg.agree_to_privacy_policy()
        aurora_pg.click_sign_me_up()
        Assert.equal(aurora_pg.newsletter_submitted_sucessfully, "Thanks for subscribing!")
