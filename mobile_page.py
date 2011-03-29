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


class MobilePage(Page):
	_take_tour_locator = "css=#sub-video.sub-feature a"
	_sync_locator = "css=#sub-sync.sub-feature a"
	_addons_locator = "css=#sub-addons.sub-feature a"
	_type_less_locator = "#sub-speed.sub-feature a"
	_download_locator ="css=a.download-link"
	
	@property
	def tour_locator(self):
		return self._take_tour_locator
		
	@property
	def sync_locator(self):
		return self._sync_locator
		
	@property
	def addons_locator(self):
		return self._addons_locator
		
	@property
	def type_less_locator(self):
		return self._type_less_locator
		
	@property
	def download_locator(self):
		return self._download_locator
		
	@property
	def get_tour_text(self):
		return self.selenium.get_text(self.tour_locator)
		
	@property
	def get_sync_text(self):
		return self.selenium.get_text(self.tour_locator)
		
		
	@property
	def get_addons_text(self):
		return self.selenium.get_text(self.addons_locator)
		
	@property
	def get_type_less_text(self):
		return self.selenium.get_text(self.type_less_locator)
		
	@property
	def get_download_text(self):
		return self.selenium.get_text(self.download_locator)
			
	def __init__(self, selenium):
		self.selenium = selenium