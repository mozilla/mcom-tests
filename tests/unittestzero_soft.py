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
# The Original Code is UnittestZero.
#
# The Initial Developer of the Original Code is
# Portions created by the Initial Developer are Copyright (C) 2011

# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#                 Joel Andersson <janderssn@gmail.com>
#                 Bebe<florin.strugariu@softvision.ro>
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


from unittestzero import Assert


class SoftAsserter(object):
    """
    Used to call soft asserts from within a test
    """

    def __init__(self):
        # a list which collects failure messages
        self._failure_list = []

    def __getattr__(self, name):
        """
        Passes calls to unittestzero.Assert to test the logic and generate failure messages
        """
        def get(self, *args, **kwargs):
            try:
                method = getattr(Assert(), name)
                method(*args, **kwargs)
            except Exception as e:
                # the assert failed, so add the failure message into the list
                self._failure_list.append(e.message)
        return get.__get__(self)

    def summarize(self):
        """
        Checks whether any failures occurred and if so reports them all back via a failed assertion
        """
        Assert.equal(0, len(self._failure_list), '%s problems found: ' % len(self._failure_list) + ', '.join(self._failure_list))
