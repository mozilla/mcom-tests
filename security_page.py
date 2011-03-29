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
from vars import ConnectionParameters
from page import Page


class SecurityPage(Page):
	
	_privacy_icon_locator = "li#security-privacy > a"
	_security_icon_locator = "li#security-secure > a"
	_control_icon_locator = "li#security-control > a"
	_mission_icon_locator = "li#security-mission > a"
	_privacy_screenshot_locator = "div#privacy.section > div.section-image >img"
	_security_screenshot_locator = "div#secure.section > .section-image >img"
	_control_screenshot_locator = "div#control.section > .section-image >img"
	_mission_screenshot_locator = "div#mission.section > div.section-image >img"
	
	def __init__(self,selenium):
		self.selenium = selenium
		self.selenium.open('/firefox/security/')
		self.selenium.window_maximize()
	
	
	@property
	def privacy_icon(self):
		return self._privacy_icon_locator
		
	@property
	def security_icon(self):
		return self._security_icon_locator
		
	@property
	def control_icon(self):
		return self._control_icon_locator
		
	@property
	def misson_icon(self):
		return self._mission_icon_locator
		
	@property
	def privacy_screenshot(self):
		return self._privacy_screenshot_locator
		
	@property
	def security_screenshot(self):
		return self._security_screenshot_locator
		
	@property
	def control_screenshot(self):
		return self._control_screenshot_locator
		
	@property
	def mission_screenshot(self):
		return self._mission_screenshot_locator
		