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
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
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
from selenium import selenium
from page import Page


class AboutPage(Page):

    _participate_img = "css=#get-involved>h3>a>span"
    _txt_participate = "css=#get-involved>h3>a"
    _communications_img = "css=#press>h3>a>span"
    _txt_communications = "css=#press>h3>a"
    _careers_img = "css=#careers>h3>a>span"
    _txt_careers = "css=#careers>h3>a"
    _partnerships_img = "css=#partnerships>h3>a>span"
    _txt_partnerships = "css=#partnerships>h3>a"
    _legal_img = "css=#licensing>h3>a>span"
    _txt_legal = "css=#licensing>h3>a"
    _contact_us_img = "css=#contact>h3>a>span"
    _txt_contact_us = "css=#contact>h3>a"
    _store_img = "css=#store>h3>a>span"
    _txt_store = "css=#store>h3>a"
    _blog_img = "css=#blog>h3>a>span"
    _txt_blog = "css=#blog>h3>a"

    @property
    def participate_image(self):
        return self.is_element_present(self._participate_img)

    @property
    def participate_text(self):
        return self.is_element_present(self._txt_participate)

    @property
    def communications_image(self):
        return self.is_element_present(self._communications_img)

    @property
    def communications_text(self):
        return self.is_element_present(self._txt_communications)

    @property
    def careers_image(self):
        return self.is_element_present(self._careers_img)

    @property
    def careers_text(self):
        return self.is_element_present(self._txt_careers)

    @property
    def partnerships_image(self):
        return self.is_element_present(self._partnerships_img)

    @property
    def partnerships_text(self):
        return self.is_element_present(self._txt_partnerships)

    @property
    def legal_image(self):
        return self.is_element_present(self._legal_img)

    @property
    def legal_text(self):
        return self.is_element_present(self._txt_legal)

    @property
    def contact_us_image(self):
        return self.is_element_present(self._contact_us_img)

    @property
    def contact_us_text(self):
        return self.is_element_present(self._txt_contact_us)

    @property
    def store_image(self):
        return self.is_element_present(self._store_img)

    @property
    def store_text(self):
        return self.is_element_present(self._txt_store)

    @property
    def blog_image(self):
        return self.is_element_present(self._blog_img)

    @property
    def  blog_text(self):
        return self.is_element_present(self._txt_blog)
