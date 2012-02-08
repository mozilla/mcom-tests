#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium import selenium
from unittestzero import Assert
from pages.base import MozillaBasePage
import pytest
xfail = pytest.mark.xfail


class TestCommon:

    def test_header_and_footer_links(self, mozwebqa, url="/firefox/fx/"):
        home_pg = MozillaBasePage(mozwebqa)
        home_pg.open(url)
        home_pg.click_tabzilla()

        for x in home_pg.get_tabzilla_header_links:
            print home_pg.is_element_present(x)

        for x in home_pg.header_links:
            print home_pg.is_element_present(x)

        for x in home_pg.footer_support_links:
            print home_pg.is_element_present(x)

        for x in home_pg.footer_desktop_links:
            print home_pg.is_element_present(x)

        for x in home_pg.footer_social_links:
            print home_pg.is_element_present(x)

        for x in home_pg.footer_mobile_links:
            print home_pg.is_element_present(x)

        for x in home_pg.footer_release_download_links:
            print home_pg.is_element_present(x)

        for x in home_pg.footer_about_links:
            print home_pg.is_element_present(x)

        for x in home_pg.footer_addons_links:
            print home_pg.is_element_present(x)

        for x in home_pg.footer_legal_links:
            print home_pg.is_element_present(x)


    def test_all_page_header_and_footer_links(self, mozwebqa):
        urls = [
            "/firefox/channel/",
            "/firefox/security/",
            "/firefox/performance/",
            "/en-US/firefox/customize/",
            "/firefox/technology/",
            "/firefox/video/",
            "/firefox/central/",
            "/mobile/",
            "/mobile/features/",
            "/mobile/customize/",
            "/mobile/sync/",
            "/mobile/getinvolved/",
            "/mobile/faq/",
            "/firefox/video/",
            "/en-US/about/",
            "/about/participate/",
            "/press/",
            "/about/partnerships.html",
            "/about/legal.html",
            "/about/contact.html",
            "/firefox/all.html"]

        for x in urls:
            print x
            self.test_header_and_footer_links(mozwebqa, url=x)

    def test_download_buttons(self, mozwebqa, url="/firefox/features/"):
        self.selenium = mozwebqa.selenium
        home_pg = MozillaBasePage(mozwebqa)
        home_pg.open(url)
        for x in home_pg.get_upper_download_links:
            print home_pg.get_text(x)
            print home_pg.is_element_present(x)
            print home_pg.is_element_visible(x)

    def test_footer_newsletter_submission(self, mozwebqa, url="/firefox/features"):
        self.selenium = mozwebqa.selenium
        home_pg = MozillaBasePage(mozwebqa)
        home_pg.open(url)
        home_pg.type(home_pg.monthly_news_locator, home_pg.test_email_address)
        home_pg.click(home_pg.monthly_news_locator_button)
        home_pg.click(home_pg.inline_privacy_checkbox)
        home_pg.click(home_pg.sign_me_up_button, True)
        home_pg.is_element_present(home_pg.success_pane_locator)
        

    def test_all_download_buttons(self,mozwebqa):
        urls = [
            "/firefox/security/",
            "/firefox/performance/",
            "/en-US/firefox/customize/",
            "/firefox/technology/",
            "/firefox/video/",
            "/firefox/central/",
            "/firefox/video/"]

        for x in urls:
            print x
            self.test_download_buttons(mozwebqa, url=x)
        
