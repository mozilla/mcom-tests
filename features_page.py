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


class FeaturesPage(Page):
    
    _made_easy_locator = \
    "css=#main-feature>.feature-links>#made-easy>a"
    _high_performance_locator =  \
    "css=#main-feature>.feature-links>#high-performance>a"
    _advanced_security_locator = \
    "css=#main-feature>.feature-links>#advanced-security>a"
    _powerful_personalization_locator = \
    "css=#main-feature>.feature-links>#powerful-personalization>a"
    _universal_access_locator = \
    "css=#main-feature>.feature-links>#cutting-edge>a"
    _cutting_edge_locator = \
    "css=#main-feature>.feature-links>#universal-access>a"
    
    _made_easy_image = \
    "css=#madeeasy>.features-container>.feature>.right"
    _app_tabs_image = \
    "css=#madeeasy>.features-container>.feature>.column1>.sub-feature>.right"
    _switch_tab_image = \
    "css=#madeeasy>.features-container>.feature>.column2>.sub-feature>.right"
    _panorama_image = \
    "css=#madeeasy>.features-container>.feature>.column3>.sub-feature>.right"
    _sync_image = \
    "css=#madeeasy>.features-container>.column-span>.right"
    _easy_search_image = \
    "//*[@id='madeeasy']/div/div[8]/div[4]/img"
    _one_bookmark_image = \
    "css=#madeeasy>.features-container>.feature>.oneclickbookmarking>.right"
    _speed_image = \
    "css=#highperformance>.features-container>.column1>.feature>#performance-chart"
    _security_image = \
    "css=#advancedsecurity>.features-container>.column1>.feature>.right"
    _private_browsing_image = \
    "css=#advancedsecurity>.features-container>.column2>.feature>.right"
    _auto_update_image = \
    "css=#advancedsecurity>.features-container>.column3>.feature>.right"
    _addons_manager_image = \
    "css=#powerfulpersonalization>.features-container>.addons-manager>.right"
    personas_image = \
    "css=#powerfulpersonalization>.features-container>.column1>.feature>.right"
    
    
    
    @property
    def made_easy(self):
        return self.is_element_present(self._made_easy_locator)
        
    @property
    def high_performance(self):
        return self.is_element_present(self._high_performance_locator)
        
    @property
    def advanced_security(self):
        return self.is_element_present(self._advanced_security_locator)
        
    @property
    def powerful_personalization(self):
        return self.is_element_present(self._powerful_personalization_locator)
    
    @property
    def universal_access(self):
        return self.is_element_present(self._universal_access_locator)
        
    @property
    def cutting_edge(self):
        return self.is_element_present(self._cutting_edge_locator)
        
    @property
    def made_easy_img(self):
        return self.is_element_present(self._made_easy_image)
        
    @property
    def app_tabs_img(self):
        return self.is_element_present(self._app_tabs_image)
        
    @property
    def switch_tab_img(self):
        return self.is_element_present(self._switch_tab_image)
        
    @property
    def panorama_img(self):
        return self.is_element_present(self._panorama_image)
        
    @property
    def sync_img(self):
        return self.is_element_present(self._sync_image)
        
    @property
    def easy_search_img(self):
        return self.is_element_present(self._easy_search_image)
        
    @property
    def one_bookmark_img(self):
        return self.is_element_present(self._one_bookmark_image)
        
    @property
    def speed_img(self):
        return self.is_element_present(self._speed_image)
        
    @property
    def security_img(self):
        return self.is_element_present(self._security_image)
        
    @property
    def private_browsing_img(self):
        return self.is_element_present(self._private_browsing_image)
    
    @property
    def auto_update_img(self):
        return self.is_element_present(self._auto_update_image)
