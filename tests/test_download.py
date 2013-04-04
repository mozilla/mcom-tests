#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re
import time
import pytest
import requests

from BeautifulSoup import BeautifulStoneSoup
from unittestzero import Assert

from pages.desktop.home import Home


@pytest.mark.nondestructive
class TestDownload(object):

    @pytest.fixture
    def browsermob_proxy(self, request):
        bmp = request.config.pluginmanager.getplugin('browsermob_proxy')
        if not bmp:
            raise Exception('The BrowserMob proxy plugin is required. Install '
                            'using pip install pytest-browsermob-proxy.')
        if not hasattr(request.config, 'browsermob_test_proxy'):
            raise Exception('A BrowserMob test proxy is not running! Start '
                            'one by specifying --bmp-test-proxy.')
        return request.config.browsermob_test_proxy

    @pytest.mark.skipif("config.getvalue('platform') != 'MAC'")
    def test_download_firefox_for_mac_from_home_page(self, mozwebqa, browsermob_proxy):
        home_page = Home(mozwebqa)
        home_page.go_to_page()
        home_page.download_firefox.click_download_for_mac()

        download_url = self.get_request_url(browsermob_proxy, '\.dmg$', mozwebqa.timeout)
        request = requests.head(download_url)

        assert request.status_code == 200
        assert request.headers['content-type'] == 'application/x-apple-diskimage'
        assert int(request.headers['content-length']) > 34000000

    @pytest.mark.skipif("config.getvalue('platform') != 'WINDOWS'")
    def test_download_firefox_for_windows_from_home_page(self, mozwebqa, browsermob_proxy):
        home_page = Home(mozwebqa)
        home_page.go_to_page()
        home_page.download_firefox.click_download_for_windows()

        download_url = self.get_request_url(browsermob_proxy, '\.exe$', mozwebqa.timeout)
        request = requests.head(download_url)

        assert request.status_code == 200
        assert request.headers['content-type'] == 'application/octet-stream'
        assert int(request.headers['content-length']) > 17000000

    def get_request_url(self, proxy, match, timeout):
        end_time = time.time() + timeout
        while(True):
            network_traffic = proxy.har
            last_entry = network_traffic['log']['entries'][-1]
            if re.search(match, last_entry['request']['url']):
                return last_entry['request']['url']
            time.sleep(1)
            if(time.time() > end_time):
                raise Exception('Timeout waiting for download request.')

    def download_base_url(self, base_url):
        if '/b' in base_url:
            return '%s/en-US/products/download.html' % base_url.replace('/b', '')
        else:
            return '%s/en-US/products/download.html' % base_url

    @pytest.mark.skip_selenium
    def test_osx_download_button_returns_status_code_200(self, mozwebqa):
        url = self.download_base_url(mozwebqa.base_url)
        response = requests.get(url)
        html = BeautifulStoneSoup(response.content)
        link = html.find('li', 'os_osx').a['href']
        print link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    @pytest.mark.skip_selenium
    def test_linux_download_button_returns_status_code_200(self, mozwebqa):
        url = self.download_base_url(mozwebqa.base_url)
        response = requests.get(url)
        html = BeautifulStoneSoup(response.content)
        link = html.find('li', 'os_linux').a['href']
        print link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    @pytest.mark.skip_selenium
    def test_windows_download_button_returns_status_code_200(self, mozwebqa):
        url = self.download_base_url(mozwebqa.base_url)
        response = requests.get(url)
        html = BeautifulStoneSoup(response.content)
        link = html.find('li', 'os_windows').a['href']
        print link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)

    @pytest.mark.skip_selenium
    def test_download_button_returns_status_code_200_using_google_chrome(self, mozwebqa):
        '''https://bugzilla.mozilla.org/show_bug.cgi?id=672713'''
        url = self.download_base_url(mozwebqa.base_url)
        response = requests.get(url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2'})
        html = BeautifulStoneSoup(response.content)
        link = html.find('li', 'os_windows').a['href']
        print link
        response = requests.head(link, allow_redirects=True)
        print response.url
        Assert.equal(response.status_code, 200)
