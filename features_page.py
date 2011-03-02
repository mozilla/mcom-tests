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


class FeaturesPage(Page):
	_made_easy_locator ="css=li#made-easy > a"
	_high_performance_locator ="css=li#high-performace > a"
	_advanced_security_locator ="css=li#advanced-security > a"
	_powerful_personalization_locator ="css=li#powerful-personalization > a"
	_universal_access_locator = "css=li#universal-access > a"
	_cutting_edge_locator = "css=li#cutting-edge > a"
	_download_link ="css=a.download-link"
	_download_link_content ="css=a.download-link > .download-content"
	
	
	@property
	def get_made_easy(self):
		return self._made_easy_locator
		
	@property
	def high_performance(self):
		return self.selenium.is_element_prese(self._high_performance_locator)
	
		
	@property
	def advanced_security(self):
		return self._advanced_security_locator
		
	@property
	def powerful_personalization(self):
		return self._powerfu_personalization_locator
		
	@property
	def universal_access(self):
		return self._universal_access_locator
		
	@property
	def cutting_edge(self):
		return self._cutting_edge_locator
		
	@property 
	def download_link(self):
		return self._download_link_locator
	
	@property
	def item_on_page(self):
		return self._some_locator
	
	def __init__(self,selenium):
		self.selenium = selenium
		self.selenium.open('/')
		self.selenium.window_maximize()