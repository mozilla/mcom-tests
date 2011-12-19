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
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#                 Dave Hunt <dhunt@mozilla.com>
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
from pages.desktop.newsletter import (NewsletterPage, MainNewsletterPage,
                                      OtherNewsletterPage, FooterNewsletterPage)
import pytest
xfail = pytest.mark.xfail


class TestNewsletter:

    def signup_workflow(self, pg):
        """Submits the form with errors, and then with values that
        should be a success"""

        pg.click_sign_me_up()

        Assert.true(pg.is_privacy_policy_error_visible)
        Assert.false(pg.is_success_visible)        

        pg.type_email('me@example.com')
        pg.agree_to_privacy_policy()
        pg.click_sign_me_up()
        
        Assert.true(pg.is_success_visible)

@xfail(reason='Bug 705916 - push updated basket-dev')
def test_newsletter(self, mozwebqa):
    pg = MainNewsletterPage(mozwebqa)
    pg.go_to_newsletter_page()
    self.signup_workflow(pg)

@xfail(reason='Bug 705916 - push updated basket-dev')
def test_other_newsletters(self, mozwebqa):
    pg = OtherNewsletterPage(mozwebqa)
    pg.goto_page('me@example.com', 'us', 'en', 'text')

    # Make sure it pre-filled the format correctly
    Assert.equal(pg.get_email(), 'me@example.com')
    Assert.equal(pg.get_country(), 'us')
    Assert.equal(pg.get_lang(), 'en')
    Assert.equal(pg.get_format(), 'text')
    Assert.true(pg.is_mozilla_and_you_selected)

    pg.click_submit()

    Assert.false(pg.is_form_visible)
    Assert.true(pg.is_success_visible)

@xfail(reason='Bug 705916 - push updated basket-dev')
def test_newsletter_fr(self, mozwebqa):
    pg = NewsletterPage(mozwebqa)
    pg.go_to_newsletter_page('/fr/newsletter/')
    self.signup_workflow(pg)

@xfail(reason='Bug 705916 - push updated basket-dev')
def test_newsletter_de(self, mozwebqa):
    pg = NewsletterPage(mozwebqa)
    pg.go_to_newsletter_page('/de/newsletter/')
    self.signup_workflow(pg)

@xfail(reason='Bug 705916 - push updated basket-dev')
def test_newsletter_pt(self, mozwebqa):
    pg = NewsletterPage(mozwebqa);
    pg.go_to_newsletter_page('/pt-BR/newsletter/')
    self.signup_workflow(pg)

@xfail(reason='Bug 705916 - push updated basket-dev')
def test_newsletter_footer(self, mozwebqa):
    pg = FooterNewsletterPage(mozwebqa)
    pg.go_to_newsletter_page()

    Assert.false(pg.is_form_pane_visible)
    pg.click_open_button()
    Assert.true(pg.is_form_pane_visible)

    self.signup_workflow(pg)
