#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


class MockPartnershipRequest(dict):

    def __init__(self, **kwargs):
        # set your default values
        import time

        current_time = str(time.time()).split('.')[0]
        self['first_name'] = 'John%s' % current_time
        self['last_name'] = 'Smith%s' % current_time
        self['title'] = 'Mr'
        self['company'] = 'Test Company Name %s' % current_time
        self['URL'] = 'http://test%s.com/' % current_time
        self['email'] = 'test%s@testemail.com' % current_time
        self['phone'] = '4086780945'
        self['mobile'] = '4095780732'
        self['street'] = '25 Park Street'
        self['city'] = 'Boston'
        self['state'] = 'MA'
        self['country'] = 'US'
        self['zip'] = '02129'
        self['interest'] = 'Firefox for Android'
        self['description'] = 'Description of the partnership request %s' % current_time

        # update with any keyword arguments passed
        self.update(**kwargs)

    # allow getting items as if they were attributes
    def __getattr__(self, attr):
        return self[attr]
