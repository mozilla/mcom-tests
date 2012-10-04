#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


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
