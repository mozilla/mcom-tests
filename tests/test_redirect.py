#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

nondestructive = pytest.mark.nondestructive
parametrize = pytest.mark.parametrize
redirect = pytest.mark.redirect
skip_selenium = pytest.mark.skip_selenium


@redirect
@skip_selenium
class TestRedirects(object):
    def _test_get_redirect(self, mozwebqa, origin, final,
                           allow_redirects=True,
                           status_code=requests.codes.moved_permanently):
        if origin.startswith('http'):
            url = origin
        else:
            url = mozwebqa.base_url + origin
        response = requests.get(url, allow_redirects=allow_redirects)
        if final.startswith('http'):
            result = final
        else:
            result = mozwebqa.base_url + final
        if allow_redirects:
            assert result == response.url
        else:
            assert result == response.headers['location']
            assert status_code == response.status_code

    @nondestructive
    def test_redirects_from_mozilla_dot_com(self, mozwebqa):
        url = mozwebqa.base_url
        response = requests.get(url)
        assert url in response.url

    @nondestructive
    def test_fennec_redirects_to_mobile(self, mozwebqa):
        url = mozwebqa.base_url + "/fennec/"
        response = requests.get(url)
        result = mozwebqa.base_url + "/en-US/firefox/partners/"
        assert result == response.url

    @nondestructive
    def test_firefox_mobile_redirects_to_mobile(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
                                "/firefox/mobile/",
                                "/en-US/firefox/android/")

    @nondestructive
    def test_aurora_redirects_to_firefox_aurora(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
                                '/aurora/',
                                '/firefox/channel/#developer',
                                False)

    @nondestructive
    def test_beta_redirects_to_firefox_beta(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
                                '/beta/',
                                '/firefox/channel/#beta',
                                False)

    @nondestructive
    def test_redirect_community_to_contribute(self, mozwebqa):
        url = mozwebqa.base_url + "/community/"
        response = requests.get(url)
        assert '/contribute/' in response.url

    @nondestructive
    def test_redirect_mobile_notes_to_android_notes(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
                                '/mobile/notes/',
                                '/firefox/android/notes/',
                                False)
        self._test_get_redirect(mozwebqa,
                                '/mobile/beta/notes/',
                                '/firefox/android/beta/notes/',
                                False)
        self._test_get_redirect(mozwebqa,
                                '/mobile/aurora/notes/',
                                '/firefox/android/aurora/notes/',
                                False)
        self._test_get_redirect(mozwebqa,
                                '/mobile/37.0/releasenotes/',
                                '/firefox/android/37.0/releasenotes/',
                                False)
        self._test_get_redirect(mozwebqa,
                                '/mobile/37.0beta/releasenotes/',
                                '/firefox/android/37.0beta/releasenotes/',
                                False)
        self._test_get_redirect(mozwebqa,
                                '/mobile/37.0a2/auroranotes/',
                                '/firefox/android/37.0a2/auroranotes/',
                                False)

    @nondestructive
    def test_redirect_mobile_to_firefox_mobile(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
                                "/mobile/faq/",
                                "/en-US/firefox/android/faq/")
        self._test_get_redirect(mozwebqa,
                                "/mobile/features/",
                                "/en-US/firefox/android/")
        url = mozwebqa.base_url + "/mobile/platforms/"
        response = requests.get(url)
        assert requests.codes.ok == response.status_code
        assert 'support.mozilla.org' in response.url

    @nondestructive
    def test_redirect_some_m_to_firefox_mobile(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
                                "/m/faq/",
                                "/en-US/firefox/android/faq/")
        self._test_get_redirect(mozwebqa,
                                "/m/features/",
                                "/en-US/firefox/android/")
        url = mozwebqa.base_url + "/m/platforms/"
        response = requests.get(url)
        assert requests.codes.ok == response.status_code
        assert 'support.mozilla.org' in response.url

    @nondestructive
    def test_redirect_m(self, mozwebqa):
        self._test_get_redirect(mozwebqa,
                                "/m/",
                                "/en-US/firefox/new/")

    @nondestructive
    def test_rhino_docs_redirect(self, mozwebqa):
        origin = mozwebqa.base_url + '/rhino/doc.html'
        result = 'https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino/Documentation'
        self._test_get_redirect(mozwebqa, origin, result)

    @nondestructive
    def test_rhino_download_redirect(self, mozwebqa):
        origin = mozwebqa.base_url + '/rhino/download.html'
        result = \
            'https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino/Download_Rhino'
        self._test_get_redirect(mozwebqa, origin, result)

    @nondestructive
    def test_rhino_redirect(self, mozwebqa):
        origin = mozwebqa.base_url + '/rhino/'
        result = \
            'https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino'
        self._test_get_redirect(mozwebqa, origin, result)

    @nondestructive
    def test_redirect_firefox_home_the_product(self, mozwebqa):
        result = \
            'https://blog.mozilla.org/services/2012/08/31/retiring-firefox-home/'
        self._test_get_redirect(mozwebqa, '/mobile/home/', result)
        self._test_get_redirect(mozwebqa, '/fr/mobile/home/', result)

    @nondestructive
    def test_notes_redirects_to_firefox_notes(self, mozwebqa):
        url = mozwebqa.base_url + "/firefox/notes/"
        response = requests.get(url)
        assert '/firefox/' in response.url
        assert '/releasenotes/' in response.url

    @nondestructive
    def test_all_older_redirect(self, mozwebqa):
        url = mozwebqa.base_url + "/firefox/all-older.html"
        response = requests.get(url)
        assert '/firefox/new' in response.url

    @nondestructive
    def test_old_firstrun_redirect(self, mozwebqa):
        url = mozwebqa.base_url + "/en-US/projects/firefox/3.6.13/firstrun/"
        response = requests.get(url)
        assert requests.codes.not_found != response.status_code

    @nondestructive
    def test_old_whatsnew_redirect(self, mozwebqa):
        url = mozwebqa.base_url + '/en-US/projects/firefox/3.6.13/whatsnew/'
        response = requests.get(url)
        assert requests.codes.not_found != response.status_code

    @nondestructive
    def test_partners_redirect(self, mozwebqa):
        url = mozwebqa.base_url + '/b2g/'
        response = requests.get(url)
        assert '/partners/' in response.url

    @nondestructive
    def test_firefox_metro_redirect(self, mozwebqa):
        url = mozwebqa.base_url + '/metrofirefox'
        response = requests.head(url)
        assert requests.codes.not_found != response.status_code

    @nondestructive
    def test_locale_redirect_for_newsletter(self, mozwebqa):
        url = mozwebqa.base_url + '/newsletter'
        response = requests.get(url, headers={'Accept-Language': 'pl'})
        assert mozwebqa.base_url + '/pl/newsletter/' == response.url

    @nondestructive
    def test_firefox_os_mobile_redirect(self, mozwebqa):
        url = mozwebqa.base_url + '/firefox/mobile/faq/?os=firefox-os'
        response = requests.get(url, headers={'Accept-Language': 'en-US'})
        assert '/firefox/os/faq/' in response.url

    @nondestructive
    def test_account_manager_redirect(self, mozwebqa):
        """
        Test that /firefox/account manager redirects
        to /persona
        """
        url = mozwebqa.base_url + '/firefox/accountmanager'
        response = requests.get(url, headers={'Accept-Language': 'en-US'})
        assert '/persona' in response.url

    @nondestructive
    def test_developer_redirect(self, mozwebqa):
        """
        Test aurora.mozilla.org redirects to
        http://www.mozilla.org/firefox/channel/#developer
        """
        url = 'http://aurora.mozilla.org'
        response = requests.get(url)
        history = [r.headers.get('location', '') for r in response.history]
        assert 'https://www.mozilla.org/firefox/channel/#developer' in history
        assert requests.codes.ok == response.status_code

    @nondestructive
    def test_beta_redirect(self, mozwebqa):
        """
        Test beta.mozilla.org redirects to
        http://www.mozilla.org/firefox/channel/#beta
        """
        url = 'http://beta.mozilla.org'
        response = requests.get(url)
        history = [r.headers.get('location', '') for r in response.history]
        assert 'http://www.mozilla.org/en-US/firefox/channel/#beta' in history
        assert requests.codes.ok == response.status_code

    @nondestructive
    def test_apps_redirect(self, mozwebqa):
        """
        Test mozilla.org/apps redirects to
        http[s]://marketplace.firefox.com
        """
        url = mozwebqa.base_url + '/apps'
        response = requests.get(url)
        assert 'marketplace.firefox.com' in response.url
        assert requests.codes.ok == response.status_code

    @nondestructive
    def test_technology_redirect(self, mozwebqa):
        """
        Test mozilla.org/firefox/technology redirects to
        http[s]://developer.mozilla.org/docs/Tools
        """
        url = mozwebqa.base_url + '/firefox/technology'
        response = requests.get(url, allow_redirects=False)
        assert requests.codes.moved_permanently == response.status_code

    @nondestructive
    def test_performance_redirect(self, mozwebqa):
        """
        Test mozilla.org/firefox/performance redirects to
        http[s]://www.mozilla.org/en-US/firefox/desktop/fast/
        """
        url = mozwebqa.base_url + '/firefox/performance'
        response = requests.get(url)
        assert '/firefox/desktop/fast/' in response.url
        assert requests.codes.ok == response.status_code

    @nondestructive
    def test_security_redirect(self, mozwebqa):
        """
        Test mozilla.org/firefox/security redirects to
        http[s]://www.mozilla.org/en-US/firefox/desktop/trust/
        """
        url = mozwebqa.base_url + '/firefox/security'
        response = requests.get(url)
        assert '/firefox/desktop/trust/' in response.url
        assert requests.codes.ok == response.status_code

    @nondestructive
    @parametrize("locale", ['son', 'zh-CN', 'ta'])
    def test_firefox_new_redirect(self, mozwebqa, locale):
        url = mozwebqa.base_url + '/firefox/new'
        response = requests.get(url, headers={'Accept-Language': locale})
        assert locale in response.url

    @nondestructive
    def test_policy_archive_redirect(self, mozwebqa):
        url = mozwebqa.base_url + '/privacy/archive/'
        response = requests.get(url)
        assert requests.codes.ok == response.status_code
        assert requests.codes.moved_permanently == response.history[0].status_code
        assert response.history[0].headers['location'].endswith('/en-US/privacy/archive/')

    @nondestructive
    def test_dnt_redirect(self, mozwebqa):
        url = mozwebqa.base_url + '/dnt'
        response = requests.get(url)
        assert requests.codes.ok == response.status_code
        assert requests.codes.moved_permanently == response.history[-1].status_code
        assert response.history[-1].headers['location'].endswith('/firefox/dnt/')

    @nondestructive
    def test_firefox_os_notes_redirect(self, mozwebqa):
        url = mozwebqa.base_url + '/firefox/os/notes/'
        response = requests.get(url)
        assert requests.codes.ok == response.status_code
        assert requests.codes.moved_permanently == response.history[0].status_code
        assert 'https://developer.mozilla.org/Firefox_OS/Releases' == response.history[0].headers['location']

    @nondestructive
    def test_firefox_os_notes_version_redirect(self, mozwebqa):
        url = mozwebqa.base_url + '/firefox/os/notes/2.0'
        response = requests.get(url)
        assert requests.codes.ok == response.status_code
        assert requests.codes.moved_permanently == response.history[0].status_code
        assert 'https://developer.mozilla.org/Firefox_OS/Releases/2.0' == response.history[0].headers['location']
