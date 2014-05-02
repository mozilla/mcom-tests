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

    def download_base_url(self, base_url):
        if '/b' in base_url:
            return '%s/en-US/products/download.html' % base_url.replace('/b', '')
        else:
            return '%s/en-US/products/download.html' % base_url

    def test_osx_download_button_returns_status_code_200(self, mozwebqa):
        url = self.download_base_url(mozwebqa.base_url)
        response = requests.get(url)
        html = BeautifulSoup(response.content)
        link = html.find('li', 'os_osx').a['href']
        print link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    def test_linux_download_button_returns_status_code_200(self, mozwebqa):
        url = self.download_base_url(mozwebqa.base_url)
        response = requests.get(url)
        html = BeautifulSoup(response.content)
        link = html.find('li', 'os_linux').a['href']
        print link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    def test_windows_download_button_returns_status_code_200(self, mozwebqa):

        url = self.download_base_url(mozwebqa.base_url)
        response = requests.get(url)
        html = BeautifulSoup(response.content)
        link = html.find('li', 'os_windows').a['href']
        print link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    def test_download_button_returns_status_code_200_using_google_chrome(self, mozwebqa):
        '''https://bugzilla.mozilla.org/show_bug.cgi?id=672713'''
        url = self.download_base_url(mozwebqa.base_url)
        response = requests.get(url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2'})
        html = BeautifulSoup(response.content)
        link = html.find('li', 'os_windows').a['href']
        print link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)
