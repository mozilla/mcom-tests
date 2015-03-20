#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
import requests

from bs4 import BeautifulSoup
from unittestzero import Assert


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class TestDownload(object):

    def test_osx_download_button_returns_status_code_200(self, mozwebqa):
        response = requests.get(mozwebqa.base_url)
        html = BeautifulSoup(response.content)
        link = html.find('li', 'os_osx').a['href']
        link = mozwebqa.base_url + link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    def test_linux_download_button_returns_status_code_200(self, mozwebqa):
        response = requests.get(mozwebqa.base_url)
        html = BeautifulSoup(response.content)
        link = html.find('li', 'os_linux').a['href']
        link = mozwebqa.base_url + link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    def test_windows_download_button_returns_status_code_200(self, mozwebqa):
        response = requests.get(mozwebqa.base_url)
        html = BeautifulSoup(response.content)
        link = html.find('li', 'os_win').a['href']
        link = mozwebqa.base_url + link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    def test_download_button_returns_status_code_200_using_google_chrome(self, mozwebqa):
        '''https://bugzilla.mozilla.org/show_bug.cgi?id=672713'''
        response = requests.get(mozwebqa.base_url,
                                headers={'User-Agent': 'AppleWebKit/537.36 \
                                          (KHTML, like Gecko) Chrome/35.0.1916.153 \
                                          Safari/537.36'})
        html = BeautifulSoup(response.content)
        link = html.find('li', 'os_win').a['href']
        link = mozwebqa.base_url + link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)
