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
import unittest
from mozilla_base_page  import  MozillaBasePage
from mobile_page import MobilePage



class TestMobile(unittest.TestCase):
	
	def setUp(self):
		self.selenium = selenium( ConnectionParameters.server, ConnectionParameters.port,
													ConnectionParameters.browser, ConnectionParameters.baseurl)
		self.selenium.start()
		self.selenium.set_timeout(ConnectionParameters.page_load_timeout)
		
	def tearDown(self):
		self.selenium.stop()
		
		
	def test_header_and_footer_links_are_present(self):
		homepageBase = MozillaBasePage(self.selenium)
		homepageBase.selenium.open('/mobile/')
		
		for x in homepageBase.headers_list:
			homepageBase.selenium.get_text(x)
			self.assertTrue(homepageBase.is_element_present(x))
			
		for x in homepageBase.footer_features_list:
			homepageBase.selenium.get_text(x)
			self.assertTrue(homepageBase.is_element_present(x))
			
		for x in homepageBase.footer_social_media_list:
			homepageBase.selenium.get_text(x)
			self.assertTrue(homepageBase.is_element_present(x))
			
		for x in homepageBase.footer_mobile_list:
			homepageBase.selenium.get_text(x)
			self.assertTrue(homepageBase.is_element_present(x))
			
		for x in homepageBase.footer_support_list:
			homepageBase.selenium.get_text(x)
			self.assertTrue(homepageBase.is_element_present(x))
			
		for x in homepageBase.footer_addons_list:
			homepageBase.selenium.get_text(x)
			self.assertTrue(homepageBase.is_element_present(x))
			
		for x in homepageBase.footer_about_list:
			homepageBase.selenium.get_text(x)
			self.assertTrue(homepageBase.is_element_present(x))
			


	


	def test_sub_sections_are_present(self):
		mobile_pg = MobilePage(self.selenium)
		mobile_pg.selenium.open('/mobile/')
		mobile_pg.get_tour_text
		self.assertTrue(mobile_pg.is_element_present(mobile_pg.tour_locator))
		mobile_pg.get_sync_text
		self.assertTrue(mobile_pg.is_element_present(mobile_pg.sync_locator))
		mobile_pg.get_addons_text
		self.assertTrue(mobile_pg.is_element_present(mobile_pg.addons_locator))
		mobile_pg.get_download_text
		self.assertTrue(mobile_pg.is_element_present(mobile_pg.download_locator ))
		
		
			
			
		
		
		
if __name__ =="__main__":
	unittest.main()
		

		
	
	
