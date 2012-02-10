#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import MozillaBasePage


class CustomizePage(MozillaBasePage):

    _style_ico = "css=#cust-style"
    _addons_ico = "css=#cust-addons"
    _plugins_ico = "css=#cust-plugins"
    _interface_ico = "css=#cust-interface"
    _sync_ico = "css=#cust-sync"
    _style_img = "css=.persona-preview"
    _plugins_img = "css=#plugins>.features-image>img"
    _interface_img = "css=#interface>.features-image>img"
    _sync_img = "css=.mozilla-video-control-overlay"
    _addons_feature = "css=.mozilla-video-control-overlay"
    _top_feature = "css=#top-features"

    @property
    def style_icon(self):
        return self.is_element_present(self._style_ico)

    @property
    def addons_icon(self):
        return self.is_element_present(self._addons_ico)

    @property
    def plugins_icon(self):
        return self.is_element_present(self._plugins_ico)

    @property
    def interface_icon(self):
        return self.is_element_present(self._interface_ico)

    @property
    def sync_icon(self):
        return self.is_element_present(self._sync_ico)

    @property
    def style_image(self):
        return self.is_element_present(self._style_img)

    @property
    def plugins_image(self):
        return self.is_element_present(self._plugins_img)

    @property
    def interface_image(self):
        return self.is_element_present(self._interface_img)

    @property
    def sync_image(self):
        return self.is_element_present(self._sync_img)

    @property
    def addons_feature(self):
        return self.is_element_present(self._addons_feature)

    @property
    def top_feature(self):
        return self.is_element_present(self._top_feature)
