#!/usr/bin/env python

import pytest
import requests


nondestructive = pytest.mark.nondestructive
skip_selenium = pytest.mark.skip_selenium


@nondestructive
@skip_selenium
class TestThunderbirdURLs(object):

    paths = [
        '/thunderbird/all/',
        '/thunderbird/releases/',
    ]

    def test_urls_ok(self, mozwebqa):
        for path in self.paths:
            url = mozwebqa.base_url + '/en-US' + path
            response = requests.get(url, timeout=3)
            assert len(response.history) <= 2
            assert requests.codes.ok == response.status_code, url
