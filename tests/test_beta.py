#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert
from pages.desktop.beta import BetaPage


class TestBeta:

    @pytest.mark.nondestructive
    def test_that_headers_are_present(self, mozwebqa):
        beta_pg = BetaPage(mozwebqa)
        beta_pg.go_to_mobile_beta_page()
        Assert.true(beta_pg.is_test_features_header_present)
        Assert.true(beta_pg.is_do_part_header_present)
        Assert.true(beta_pg.is_polish_header_present)
        Assert.true(beta_pg.is_beta_header_present)

    @pytest.mark.nondestructive
    def test_download_button_section(self, mozwebqa):
        beta_pg = BetaPage(mozwebqa)
        beta_pg.go_to_mobile_beta_page()
        Assert.true(beta_pg.is_beta_download_button_present)
        Assert.true(beta_pg.is_supported_devices_link_present)
        Assert.true(beta_pg.is_privacy_policy_link_present)

    @pytest.mark.nondestructive
    def test_beta_newsletter_submission(self, mozwebqa):
        beta_pg = BetaPage(mozwebqa)
        beta_pg.go_to_mobile_beta_page()
        beta_pg.type_email("test@test.com")
        beta_pg.check_beta_checkbox()
        beta_pg.agree_to_privacy_policy()
        beta_pg.click_sign_me_up()
        Assert.equal(beta_pg.newsletter_submitted_sucessfully, "Thanks for subscribing!")
