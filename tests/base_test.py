#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert


class BaseTest:
    """A base test class that can be extended by other tests to include utility methods."""

    def verify_footer_section(self, page_object):
        """Do the verification tasks that are common to all pages."""
        Assert.contains(page_object.footer.expected_footer_logo_destination,
            page_object.footer.footer_logo_destination)
        Assert.contains(page_object.footer.expected_footer_logo_img,
            page_object.footer.footer_logo_img)
        for link in page_object.Footer.footer_links_list:
            url = page_object.footer.footer_link_href(link)
            Assert.true(page_object.is_valid_link(url))

    def verify_header_section(self, page_object):
        """Do the verification tasks that are common to all pages."""
        Assert.true(page_object.header.is_tabzilla_panel_visible)
        page_object.header.toggle_tabzilla_dropdown()
        Assert.true(page_object.header.are_tabzilla_links_visible)

