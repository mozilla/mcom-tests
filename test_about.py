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
from about_page import AboutPage


class TestAbout:
	    
    def test_about_images(self,testsetup):
        self.selenium = testsetup.selenium
        about_pg = AboutPage(testsetup)
        about_pg.open("/about/")
        Assert.true(about_pg.participate_image)
        Assert.true(about_pg.communications_image)
        Assert.true(about_pg.careers_image)
        Assert.true(about_pg.partnerships_image)
        Assert.true(about_pg.legal_image)
        Assert.true(about_pg.contact_us_image)
        Assert.true(about_pg.store_image)
        Assert.true(about_pg.blog_image)
        
    def test_about_text(self,testsetup):
        self.selenium = testsetup.selenium
        about_pg = AboutPage(testsetup)
        about_pg.open("/about/")
        Assert.true(about_pg.participate_text)
        Assert.true(about_pg.communications_text)
        Assert.true(about_pg.careers_text)
        Assert.true(about_pg.partnerships_text)
        Assert.true(about_pg.legal_text)
        Assert.true(about_pg.contact_us_text)
        Assert.true(about_pg.store_text)
        Assert.true(about_pg.blog_text)
