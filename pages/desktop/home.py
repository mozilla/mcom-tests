#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from pages.desktop.regions.download_firefox import DownloadFirefox


class Home(Base):

    def go_to_page(self):
        self.open('/')

    @property
    def download_firefox(self):
        return DownloadFirefox(self)
