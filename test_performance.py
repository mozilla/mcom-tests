#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium import selenium
from unittestzero import Assert
from pages.desktop.performance import PerformancePage
import pytest
xfail = pytest.mark.xfail


class TestPerformance:

    def test_performance_icons(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        performance_pg = PerformancePage(mozwebqa)
        performance_pg.open("/firefox/performance/")
        Assert.true(performance_pg.video_overlay)
        Assert.true(performance_pg.perf_web_ico)
        Assert.true(performance_pg.perf_hardware_ico)

    def test_performance_images(self, mozwebqa):
        self.selenium = mozwebqa.selenium
        performance_pg = PerformancePage(mozwebqa)
        performance_pg.open("/firefox/performance/")
        Assert.true(performance_pg.perf_hardware_img)
