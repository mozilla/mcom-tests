# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from bs4 import BeautifulSoup
import pytest
import requests


class TestDownload(object):

    @pytest.mark.nondestructive
    def test_osx_download_button_returns_status_code_200(self, base_url):
        html = BeautifulSoup(requests.get(base_url).content, 'html.parser')
        link = html.find('li', 'os_osx').a['href']
        link = base_url + link
        r = requests.head(link, allow_redirects=True)
        assert requests.codes.ok == r.status_code, r.url

    @pytest.mark.nondestructive
    def test_linux_download_button_returns_status_code_200(self, base_url):
        html = BeautifulSoup(requests.get(base_url).content, 'html.parser')
        link = html.find('li', 'os_linux').a['href']
        link = base_url + link
        r = requests.head(link, allow_redirects=True)
        assert requests.codes.ok == r.status_code, r.url

    @pytest.mark.nondestructive
    def test_windows_download_button_returns_status_code_200(self, base_url):
        html = BeautifulSoup(requests.get(base_url).content, 'html.parser')
        link = html.find('li', 'os_win').a['href']
        link = base_url + link
        r = requests.head(link, allow_redirects=True)
        assert requests.codes.ok == r.status_code, r.url

    @pytest.mark.nondestructive
    def test_download_button_returns_status_code_200_using_google_chrome(self, base_url):
        '''https://bugzilla.mozilla.org/show_bug.cgi?id=672713'''
        r = requests.get(base_url, headers={
            'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/35.0.1916.153 Safari/537.36'})
        html = BeautifulSoup(r.content, 'html.parser')
        link = html.find('li', 'os_win').a['href']
        link = base_url + link
        r = requests.head(link, allow_redirects=True)
        assert requests.codes.ok == r.status_code, r.url
