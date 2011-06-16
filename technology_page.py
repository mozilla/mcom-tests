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
from page import Page


class TechnologyPage(Page):
    
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
                  