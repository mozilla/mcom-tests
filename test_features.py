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
from unittestzero import Assert
from features_page import FeaturesPage
import pytest
xfail = pytest.mark.xfail


class TestFeatures:
    
    @xfail(reason="Bug 661285 - [Fx5LaunchDay] Remove Perf graphs from moz.com and add new content to take its place on the Performance page")      
    def test_page(self,testsetup):
        self.selenium = testsetup.selenium
        features_pg = FeaturesPage(testsetup)
        features_pg.open("/firefox/features/")
        Assert.true(features_pg.made_easy)
        Assert.true(features_pg.high_performance)
        Assert.true(features_pg.advanced_security)
        Assert.true(features_pg.powerful_personalization)
        Assert.true(features_pg.universal_access)
        Assert.true(features_pg.cutting_edge)
        Assert.true(features_pg.made_easy_img)
        Assert.true(features_pg.app_tabs_img)
        Assert.true(features_pg.switch_tab_img)
        Assert.true(features_pg.panorama_img)
        Assert.true(features_pg.sync_img)
        Assert.true(features_pg.easy_search_img)
        Assert.true(features_pg.one_bookmark_img)
        Assert.true(features_pg.speed_img)
        Assert.true(features_pg.security_img)
        Assert.true(features_pg.private_browsing_img)
        Assert.true(features_pg.auto_update_img)
