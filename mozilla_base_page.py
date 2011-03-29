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


class MozillaBasePage(Page):
	
	def __init__(self,selenium):
		self.selenium = selenium
		self.selenium.open('/')
		self.selenium.window_maximize()
	
	_features_header_locator ="css=#nav-main-features > a"
	_mobile_header_locator = "css=#nav-main-mobile > a"
	_addons_header_locator ="css=#nav-main-addons > a"
	_support_header_locator ="css=#nav-main-support > a"
	_about_header_locator = "css=#nav-main-about > a"
	_mozilla_header_locator ="css=#header > div a.mozilla"
	_header_list = [_features_header_locator,
					 _mobile_header_locator,
					 _addons_header_locator,
					 _support_header_locator,
					 _about_header_locator,
					 _mozilla_header_locator]
					
	_footer_features_locator = "css=#footer-menu > ul >li:nth-child(1) > ul > li:nth-child(1) > a"
	_footer_security_locator = "css=#footer-menu > ul >li:nth-child(1) > ul > li:nth-child(2) > a"
	_footer_performance_locator = "css=#footer-menu > ul >li:nth-child(1) > ul > li:nth-child(3) > a"
	_footer_custom_locator = "css=#footer-menu > ul >li:nth-child(1) > ul > li:nth-child(4) > a"
	_footer_tech_locator = "css=#footer-menu > ul >li:nth-child(1) > ul > li:nth-child(5) > a"
	_footer_videos_locator = "css=#footer-menu > ul >li:nth-child(1) > ul > li:nth-child(6) > a"
	_footer_tour_locator = "css=#footer-menu > ul >li:nth-child(1) > ul > li:nth-child(7) > a"
	_footer_features_list = [_footer_features_locator,
							  _footer_security_locator,
							  _footer_performance_locator,
							  _footer_custom_locator,
							  _footer_tech_locator,
							  _footer_videos_locator,
							  _footer_tour_locator]
	
	_footer_twitter_locator = "css=#footer-twitter a"
	_footer_facebook_locator = "css=#sub-footer-newsletter a"
	_footer_moreways_locator = "css=#footer-connect a"
	_footer_montlynews_locator = "css=#sub-footer-newsletter a"
	_footer_social_media_list = [_footer_twitter_locator,
	                              _footer_facebook_locator,
	                              _footer_moreways_locator]
	
	_footer_mobile_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(1) > a"
	_footer_mobile_download_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(2) > a"
	_footer_mfeatures_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(3) > a"
	_footer_mcustom_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(4) > a"
	_footer_msync_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(5) > a"
	_footer_mdevelop_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(6) > a"
	_footer_minvolved_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(7) > a"
	_footer_mfaq_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(8) > a"
	_footer_mblog_locator = "css=#footer-menu > ul > li:nth-child(2) > ul > li:nth-child(9) > a"
	_footer_mobile_list = [_footer_mobile_locator,
	                        _footer_mobile_download_locator,
	                        _footer_mfeatures_locator,
	                        _footer_mcustom_locator,
	                        _footer_msync_locator, 
	                        _footer_mdevelop_locator,
	                        _footer_minvolved_locator,
	                        _footer_mfaq_locator,
	                        _footer_mblog_locator]
	
	_footer_addons_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(1) > a"
	_footer_feat_addons_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(2) > a"
	_footer_extensions_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(3) > a"
	_footer_themes_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(4) > a"
	_footer_personas_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(5) > a"
	_footer_searchtools_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(6) > a"
	_footer_lang_support_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(7) > a"
	_footer_collections_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(8) > a"
	_footer_mobile_addons_locator = "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(9) > a"
	_footer_dev_hub_locator =  "css=#footer-menu > ul > li:nth-child(3) > ul > li:nth-child(10) > a"
	_footer_addons_list = [_footer_addons_locator,
	                        _footer_feat_addons_locator,
							_footer_extensions_locator,
							_footer_themes_locator,
							_footer_personas_locator,
							_footer_searchtools_locator,
							_footer_lang_support_locator,
							_footer_collections_locator,
							_footer_mobile_addons_locator,
							_footer_dev_hub_locator]
							
	_footer_support_locator = "css=#footer-menu > ul > li:nth-child(4) > ul > li:nth-child(1) > a"
	_footer_msupport_locator = "css=#footer-menu > ul > li:nth-child(4) > ul > li:nth-child(2) > a"
	_footer_thunderbird_locator = "css=#footer-menu > ul > li:nth-child(4) > ul > li:nth-child(3) > a"
	_footer_support_list = [_footer_support_locator,
							 _footer_msupport_locator,
							 _footer_thunderbird_locator]
							
	_footer_about_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(1) > a"
	_footer_join_mozilla_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(2) > a"
	_footer_participate_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(3) > a"
	_footer_press_center_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(4) > a"
	_footer_careers_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(5) > a"
	_footer_partnerships_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(6) > a"
 	_footer_legal_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(7) > a"
	_footer_contact_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(8) > a"
	_footer_blog_locator = "css=#footer-menu > ul > li:nth-child(5) > ul > li:nth-child(9) > a"
	_footer_about_list = [ _footer_about_locator ,
						   _footer_join_mozilla_locator,
						   _footer_participate_locator,
						   _footer_press_center_locator,
						   _footer_careers_locator,
						   _footer_partnerships_locator,
						   _footer_legal_locator,
						   _footer_contact_locator,
						   _footer_blog_locator]
							
	
	@property
	def footer_about_list(self):
		return self._footer_about_list

	@property
	def footer_support_list(self):
		return self._footer_support_list
		
							
	@property
	def headers_list(self):
		return self._header_list
		
	@property
	def footer_features_list(self):
		return self._footer_features_list
		
	@property
	def footer_social_media_list(self):
		return self._footer_social_media_list
	
	@property
	def footer_mobile_list(self):
		return self._footer_mobile_list
		
	@property
	def footer_addons_list(self):
		return self._footer_addons_list