#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.contribute import Contribute
from unittestzero import Assert


class TestContribute:

    @pytest.mark.nondestructive
    def test_footer_section(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        Assert.contains(contribute_page.footer.expected_footer_logo_destination,
                        contribute_page.footer.footer_logo_destination)
        Assert.contains(contribute_page.footer.expected_footer_logo_img,
                        contribute_page.footer.footer_logo_img)
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
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.xfail(reason="XXXFIXME - xfailing until we can take a closer look")
    @pytest.mark.nondestructive
    def test_want_to_help_form_is_correct(self, mozwebqa):
        contribute_page = Contribute(mozwebqa)
        contribute_page.go_to_page()
        help_form = contribute_page.help_form
        # Expand the help form
        help_form.click_email()
        Assert.true(contribute_page.help_form.elements_are_visible)
        privacy_link = help_form.privacy_link
        url = contribute_page.link_destination(privacy_link.get('locator'))
        Assert.true(url.endswith(privacy_link.get('url_suffix')), '%s does not end with %s' % (url, privacy_link.get('url_suffix')))
        Assert.true(contribute_page.is_valid_link(url), '%s is not a valid url.' % url)
