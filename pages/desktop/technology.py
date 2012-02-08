#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import MozillaBasePage


class TechnologyPage(MozillaBasePage):

    _innovation_btn = "css=#tech-html5"
    _css_btn = "css=#tech-css"
    _api_btn = "css=#tech-apis"
    _dev_btn = "css=#tech-tools"
    _svg_btn = "css=#tech-svg"
    _security_btn = "css=#tech-security"
    _rollover_btn = "css=#click-star>span"

    _section_html5 = "css=#html5"
    _section_css = "css=#css"
    _section_api = "css=#apis"
    _section_tools = "css=#tools"
    _section_svg = "css=#svg"
    _section_security = "css=#security"

    _html5_forms = "css=#html5>article:nth-of-type(1)>h1"
    _html5_parser = "css=#html5>article:nth-of-type(3)>h1"
    _html5_webm = "css=#html5>article:nth-of-type(4)>h1"
    _html5_video = "css=#html5>article:nth-of-type(5)>h1"
    _html5_videop = "css=#html5>article:nth-of-type(6)>h1"
    _html5_history = "css=#html5>article:nth-of-type(7)>h1"

    _css_transitions = "css=#css>article:nth-of-type(1)>h1"
    _css_calc = "css=#css>article:nth-of-type(2)>h1"
    _css_any = "css=#css>article:nth-of-type(3)>h1"
    _css_element = "css=#css>article:nth-of-type(4)>h1"
    _css_placeholder = "css=#css>article:nth-of-type(5)>h1"
    _css_border = "css=#css>article:nth-of-type(6)>h1"
    _css_boxshadow = "css=#css>article:nth-of-type(7)>h1"
    _css_font = "css=#css>article:nth-of-type(8)>h1"
    _css_units = "css=#css>article:nth-of-type(9)>h1"
    _css_unit = "css=#css>article:nth-of-type(10)>h1"
    _css_device = "css=#css>article:nth-of-type(11)>h1"
    _css_tabsize = "css=#css>article:nth-of-type(12)>h1"
    _css_focusring = "css=#css>article:nth-of-type(13)>h1"
    _css_image_rect = "css=#css>article:nth-of-type(14)>h1"
    _css_resizeable = "css=#css>article:nth-of-type(15)>h1"

    _api_ecmascript = "css=#apis>article:nth-of-type(1)>h1"
    _api_webgl = "css=#apis>article:nth-of-type(2)>h1"
    _api_csupport = "css=#apis>article:nth-of-type(3)>h1"
    _api_slice = "css=#apis>article:nth-of-type(4)>h1"
    _api_fileapi = "css=#apis>article:nth-of-type(5)>h1"
    _api_touchevents = "css=#apis>article:nth-of-type(6)>h1"
    _api_click = "css=#apis>article:nth-of-type(7)>h1"
    _api_indexeddb = "css=#apis>article:nth-of-type(8)>h1"
    _api_formdata = "css=#apis>article:nth-of-type(9)>h1"
    _api_canvas = "css=#apis>article:nth-of-type(10)>h1"
    _api_audio = "css=#apis>article:nth-of-type(11)>h1"

    _dev_webconsole = "css=#tools>article:nth-of-type(1)>h1"
    _dev_firebug = "css=#tools>article:nth-of-type(2)>h1"

    _svg_animation = "css=#svg>article:nth-of-type(1)>h1"
    _svg_backgrounds = "css=#svg>article:nth-of-type(2)>h1"

    _security_csp = "css=#security>article:nth-of-type(1)>h1"
    _security_xframe = "css=#security>article:nth-of-type(2)>h1"
    _security_hsts = "css=#security>article:nth-of-type(3)>h1"
    _security_cors = "css=#security>article:nth-of-type(4)>h1"
    _security_visited = "css=#security>article:nth-of-type(5)>h1"

    @property
    def innovation_button(self):
        return self.is_element_present(self._innovation_btn)

    @property
    def css_button(self):
        return self.is_element_present(self._css_btn)

    @property
    def api_button(self):
        return self.is_element_present(self._api_btn)

    @property
    def dev_button(self):
        return self.is_element_present(self._dev_btn)

    @property
    def svg_button(self):
        return self.is_element_present(self._svg_btn)

    @property
    def security_button(self):
        return self.is_element_present(self._security_btn)

    @property
    def rollover_button(self):
        return self.is_element_present(self._rollover_btn)

    @property
    def html5_section(self):
        return self.is_element_present(self._section_html5)

    @property
    def css_section(self):
        return self.is_element_present(self._section_css)

    @property
    def api_section(self):
        return self.is_element_present(self._section_api)

    @property
    def tools_section(self):
        return self.is_element_present(self._section_tools)

    @property
    def svg_section(self):
        return self.is_element_present(self._section_svg)

    @property
    def security_section(self):
        return self.is_element_present(self._section_security)

    @property
    def forms(self):
        return self.is_element_present(self._html5_forms)

    @property
    def parser(self):
        return self.is_element_present(self._html5_parser)

    @property
    def webm(self):
        return self.is_element_present(self._html5_webm)

    @property
    def video(self):
        return self.is_element_present(self._html5_video)

    @property
    def videop(self):
        return self.is_element_present(self._html5_videop)

    @property
    def history(self):
        return self.is_element_present(self._html5_history)
