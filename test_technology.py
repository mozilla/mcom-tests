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
from technology_page import TechnologyPage


class TestTechnology:

    def test_technology_icons(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        technology_pg = TechnologyPage(mozwebqa)
        technology_pg.open("/firefox/technology/")
        Assert.true(technology_pg.innovation_button)
        Assert.true(technology_pg.css_button)
        Assert.true(technology_pg.api_button)
        Assert.true(technology_pg.dev_button)
        Assert.true(technology_pg.svg_button)
        Assert.true(technology_pg.security_button)
        Assert.true(technology_pg.rollover_button)

    def test_all_sections(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        technology_pg = TechnologyPage(mozwebqa)
        technology_pg.open("/firefox/technology/")
        Assert.true(technology_pg.html5_section)
        Assert.true(technology_pg.css_section)
        Assert.true(technology_pg.api_section)
        Assert.true(technology_pg.tools_section)
        Assert.true(technology_pg.svg_section)
        Assert.true(technology_pg.security_section)

    def test_html_sections(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        technology_pg = TechnologyPage(mozwebqa)
        technology_pg.open("/firefox/technology/")
        Assert.true(technology_pg.forms)
        Assert.true(technology_pg.parser)
        Assert.true(technology_pg.webm)
