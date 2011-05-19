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
import unittest
from selenium import selenium
from vars import ConnectionParameters
from features_page import FeaturesPage


class TestFeatures(unittest.TestCase):
    
    def setUp(self):
        self.selenium = selenium(ConnectionParameters.server,
        ConnectionParameters.port,
        ConnectionParameters.browser, ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(ConnectionParameters.page_load_timeout)
        
    def tearDown(self):
        self.selenium.stop()
        
        
    def test_page(self):
        features_pg = FeaturesPage(self.selenium)
        features_pg.open("/firefox/features/")
        self.assertTrue(features_pg.made_easy)
        self.assertTrue(features_pg.high_performance)
        self.assertTrue(features_pg.advanced_security)
        self.assertTrue(features_pg.powerful_personalization)
        self.assertTrue(features_pg.universal_access)
        self.assertTrue(features_pg.cutting_edge)
        self.assertTrue(features_pg.made_easy_img)
        self.assertTrue(features_pg.app_tabs_img)
        self.assertTrue(features_pg.switch_tab_img)
        self.assertTrue(features_pg.panorama_img)
        self.assertTrue(features_pg.sync_img)
        self.assertTrue(features_pg.easy_search_img)
        self.assertTrue(features_pg.one_bookmark_img)
        self.assertTrue(features_pg.speed_img)
        self.assertTrue(features_pg.security_img)
        self.assertTrue(features_pg.private_browsing_img)
        self.assertTrue(features_pg.auto_update_img)
        
        
if __name__ == "__main__":
    unittest.main()
