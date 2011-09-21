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


class SecurityPage(Page):

    _protecting_privacy_ico = "css=#security-privacy"
    _browser_security_ico = "css=#security-secure"
    _in_control_ico = "css=#security-control"
    _mission_ico = "css=#security-mission"
    _privacy_img = "css=#privacy>.section-image>img"
    _browser_security_img = "css=#secure>.section-image>img"
    _control_img = "css=#control>.section-image>img"
    _mission_img = "css=#mission>.section-image>img"

    @property
    def protecting_privacy_ico(self):
        return self.is_element_present(self._protecting_privacy_ico)

    @property
    def browser_security_ico(self):
        return self.is_element_present(self._browser_security_ico)

    @property
    def in_control_ico(self):
        return self.is_element_present(self._in_control_ico)

    @property
    def mission_ico(self):
        return self.is_element_present(self._mission_ico)

    @property
    def privacy_img(self):
        return self.is_element_present(self._privacy_img)

    @property
    def browser_security_img(self):
        return self.is_element_present(self._browser_security_img)

    @property
    def control_img(self):
        return self.is_element_present(self._control_img)

    @property
    def mission_img(self):
        return self.is_element_present(self._mission_img)
