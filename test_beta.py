#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2012
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#                 
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from unittestzero import Assert
from pages.desktop.beta import BetaPage
import pytest
xfail = pytest.mark.xfail


class TestBeta:

    def test_headers(self, mozwebqa):
        beta_pg = BetaPage(mozwebqa)
        beta_pg.go_to_mobile_beta_page
        Assert.true(beta_pg.test_features_header)
        Assert.true(beta_pg.do_part_header)
        Assert.true(beta_pg.polish_header)
        Assert.true(beta_pg.beta_header)

    def test_download_button(self, mozwebqa):
        beta_pg = BetaPage(mozwebqa)
        beta_pg.go_to_mobile_beta_page
        Assert.true(beta_pg.beta_download_button)
        Assert.true(beta_pg.supported_devices_link)
        Assert.true(beta_pg.privacy_policy_link)

    def test_beta_newsletter(self, mozwebqa):
        beta_pg = BetaPage(mozwebqa)
        beta_pg.go_to_mobile_beta_page
        beta_pg.type_email("me@example.com")
        beta_pg.check_beta_checkbox
        beta_pg.agree_to_privacy_policy
        beta_pg.click_sign_me_up
        Assert.equal(beta_pg.newsletter_submitted_sucessfully, "Thanks for subscribing!")
