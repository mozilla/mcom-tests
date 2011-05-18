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


class CustomizePage(Page):

    def __init__(self, selenium):
        self.selenium = selenium
        self.selenium.open("/firefox/customize/")

    _style_ico = "css=.cust-style"
    _addons_ico = "css=.cust-addons"
    _plugins_ico = "css=.cust-plugins"
    _interface_ico = "css=.cust-interface"
    _sync_ico = "css=.cust-sync"
    _style_img = "css=.persona-preview"
    _plugins_img = "css=#plugins>.features-image>img"
    _interface_img = "css=#interface>.features-image>img"
    _sync_img = "css=.mozilla-video-control-overlay"
    _addons_feature = "css=.mozilla-video-control-overlay"
    _top_feature = "css=#top-features"

    @property
    def style_icon(self):
        return self.is_element_present(self._style_ico)

    @property
    def addons_icon(self):
        return self.is_element_present(self._addons_ico)

    @property
    def plugins_icon(self):
        return self.is_element_present(self._plugins_ico)

    @property
    def interface_icon(self):
        return self.is_element_present(self._interface_ico)

    @property
    def sync_icon(self):
        return self.is_element_present(self._sync_ico)

    @property
    def style_image(self):
        return self.is_element_present(self._style_img)

    @property
    def plugins_image(self):
        return self.is_element_present(self._plugins_img)

    @property
    def interface_image(self):
        return self.is_element_present(self._interface_img)

    @property
    def sync_image(self):
        return self.is_element_present(self._sync_img)

    @property
    def addons_feature(self):
        return self.is_element_present(self._addons_feature)

    @property
    def top_feature(self):
        return self.is_element_present(self._top_feature)
