#!/usr/bin/env python

import pytest
import requests


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
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
            assert response.status_code == 200, 'got status {} from {}'.format(
                response.status_code, url)
