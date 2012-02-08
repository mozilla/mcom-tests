#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium import selenium
from page import Page


class MozillaBasePage(Page):

    _header_tab_mozilla = "css=#tabzilla-nav>ul>li:nth-child(1)>h2"
    _header_tab_products = "css=#tabzilla-nav>ul>li:nth-child(2)>h2"
    _header_tab_innovation = "css=#tabzilla-nav>ul>li:nth-child(3)>h2"
    _header_tab_get_involved = "css=#tabzilla-nav>ul>li:nth-child(4)>h2"
    _header_tab_list = [
    _header_tab_mozilla,
    _header_tab_products,
    _header_tab_innovation,
    _header_tab_get_involved
    ]

    _header_logo_locator = "css=#header > div > h1 > a"
    #_desktop_header_locator = "css=#nav-main-desktop>a"
    _mobile_header_locator = "css=#nav-main-mobile > a"
    _addons_header_locator = "css=#nav-main-addons > a"
    _support_header_locator = "css=#nav-main-support > a"
    _about_header_locator = "css=#nav-main-about > a"
    _mozilla_header_locator = "css=#tabzilla"
    _header_list = [
    _header_logo_locator,
    _mobile_header_locator,
    _addons_header_locator,
    _support_header_locator,
    _about_header_locator,
    _mozilla_header_locator]

    _footer_features_locator = \
    "css=#footer-menu > ul > li:nth-child(1) > ul > li:nth-child(1) > a"
    _footer_customize_locator = \
    "css=#footer-menu > ul > li:nth-child(1) > ul > li:nth-child(2) > a"
    _footer_performance_locator = \
    "css=#footer-menu > ul > li:nth-child(1) > ul > li:nth-child(3) > a"
    _footer_technology_locator = \
    "css=#footer-menu > ul > li:nth-child(1) > ul > li:nth-child(4) > a"
    _footer_privacy_locator = \
    "css=#footer-menu > ul > li:nth-child(1) > ul > li:nth-child(5) > a"
    _footer_desktop_list = [
    _footer_features_locator,
    _footer_customize_locator,
    _footer_performance_locator,
    _footer_technology_locator,
    _footer_privacy_locator]

    _footer_twitter_locator = "css=#footer-twitter a"
    _footer_facebbook_locator = "css=#sub-footer-newsletter a"
    #_footer_moreways_locator = "css=#footer-connect a"
    _footer_affiliates_locator = "css=#footer-affiliates a"
    _footer_monthly_newsletter_locator = "css=#sub-footer-newsletter a"
    _footer_social_media_list = [
    _footer_twitter_locator,
    _footer_facebbook_locator,
    #_footer_moreways_locator,
    _footer_affiliates_locator,
    _footer_monthly_newsletter_locator]

    _footer_mobile_download_locator = \
    "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(1) > a"
    _footer_mfeatures_locator = \
    "css=#footer-menu >ul > li:nth-child(2) > ul > li:nth-child(2) > a"
    _footer_mcustom_locator = \
    "css=#footer-menu > ul >li:nth-child(2) > ul > li:nth-child(3) > a"
    _footer_mfaq_locator = \
    "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(4) > a"
    _footer_mobile_list = [
    _footer_mobile_download_locator,
    _footer_mfeatures_locator,
    _footer_mcustom_locator,
    _footer_mfaq_locator]

    _footer_release_download_locator = \
    "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(1) > a"
    _footer_aurora_locator = \
    "css=#footer-menu > ul>li:nth-child(3) > ul > li:nth-child(2) > a"
    _footer_beta_locator = \
    "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(3) > a"
    _footer_firefox_locator = \
    "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(4) > a"
    _footer_releases_list = [
    _footer_release_download_locator,
    _footer_aurora_locator,
    _footer_beta_locator,
    _footer_firefox_locator]

    _footer_desktop_addons_locator = \
    "css=#footer-menu > ul > li:nth-child(4) > ul > li:nth-child(1) > a"
    _footer_mobile_addons_locator = \
    "css=#footer-menu > ul > li:nth-child(4) > ul > li:nth-child(2) > a"
    _footer_personas_locator = \
    "css=#footer-menu > ul > li:nth-child(4) > ul > li:nth-child(3) > a"
    _footer_addons_list = [
    _footer_desktop_addons_locator,
    _footer_mobile_addons_locator,
    _footer_personas_locator]

    _footer_support_locator = \
    "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(1) > a"
    _footer_msupport_locator = \
    "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(2) > a"
    _footer_support_list = [
    _footer_support_locator,
    _footer_msupport_locator]

    _footer_blog_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(1) > a"
    _footer_about_firefox_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(2) > a"
    _footer_join_mozilla_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(3) > a"
    _footer_participate_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(4) > a"
    _footer_press_center_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(5) > a"
    _footer_brand_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(6) > a"
    _footer_careers_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(7) > a"
    _footer_partnerships_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(8) > a"
    _footer_contact_locator = \
    "css=#footer-menu > ul > li:nth-child(6) > ul > li:nth-child(9) > a"
    _footer_about_list = [
    _footer_blog_locator,
    _footer_about_firefox_locator,
    _footer_join_mozilla_locator,
    _footer_participate_locator,
    _footer_press_center_locator,
    _footer_brand_locator,
    _footer_careers_locator,
    _footer_partnerships_locator,
    _footer_contact_locator]

    _footer_privacy_policy_locator = "css=#footer-links > a:nth-child(1)"
    _footer_legal_notices_locator = "css=#footer-links > a:nth-child(2)"
    _footer_trademark_abuse_locator = "css=#footer-links > a:nth-child(3)"
    _footer_legal_list = [
    _footer_privacy_policy_locator,
    _footer_legal_notices_locator,
    _footer_trademark_abuse_locator]

    _right_download_button_locator = "css=span.download-title"
    _right_privacy_policy_locator = "link=Privacy Policy"
    _other_systems_locator = "link=Systems & Languages"
    _release_notes_locator = "link=Release Notes"
    _download_links_list = [
    _right_download_button_locator,
    _right_privacy_policy_locator,
    _other_systems_locator,
    _release_notes_locator]

    _monthly_news_locator = "css=.email.placeholder"
    _monthly_news_locator_button = "css=.email-open"
    _test_email_address = "me@example.com"
    _inline_privacy_checkbox = "css=#inline-privacy-check"
    _sign_me_up_button = "css=.subscribe"
    _success_pane_locator = "css=.successpane > h3"


    def click_tabzilla(self):
        self.click(self._mozilla_header_locator)


    @property
    def get_tabzilla_header_links(self):
        return self._header_tab_list
    @property
    def success_pane_locator(self):
        return self._success_pane_locator

    @property
    def sign_me_up_button(self):
        return self._sign_me_up_button

    @property
    def inline_privacy_checkbox(self):
        return self._inline_privacy_checkbox

    @property
    def test_email_address(self):
        return self._test_email_address

    @property
    def monthly_news_locator(self):
        return self._monthly_news_locator

    @property
    def monthly_news_locator_button(self):
        return self._monthly_news_locator_button

    @property
    def get_upper_download_links(self):
        return self._download_links_list

    @property
    def footer_about_links(self):
        return self._footer_about_list

    @property
    def footer_support_links(self):
        return self._footer_support_list

    @property
    def header_links(self):
        return self._header_list

    @property
    def footer_desktop_links(self):
        return self._footer_desktop_list

    @property
    def footer_social_links(self):
        return self._footer_social_media_list

    @property
    def footer_mobile_links(self):
        return self._footer_mobile_list

    @property
    def footer_release_download_links(self):
        return self._footer_releases_list

    @property
    def footer_addons_links(self):
        return self._footer_addons_list

    @property
    def footer_legal_links(self):
        return self._footer_legal_list
