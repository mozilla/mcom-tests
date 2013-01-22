#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base


class MozillaBasedPage(Base):

    def go_to_page(self):
        self.open('/projects/mozilla-based/')

    breadcrumbs_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'nav.breadcrumbs > a:nth-of-type(1)'),
            'url_suffix': '/en-US/',
        }, {
            'locator': (By.CSS_SELECTOR, 'nav.breadcrumbs > a:nth-of-type(2)'),
            'url_suffix': '/en-US/products/',
        },
    ]

    main_feature_link_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-feature > p:nth-of-type(2) > a:nth-of-type(1)'),
            'url_suffix': '/projects/technologies.html',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-feature > p:nth-of-type(2) > a:nth-of-type(2)'),
            'url_suffix': '/contact/',
        },
    ]

    billboard_link_list = [
        {
            'locator': (By.CSS_SELECTOR, '#featured > li:nth-of-type(1) > h3 > a'),
            'url_suffix': 'http://www.seamonkey-project.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#featured > li:nth-of-type(2) > h3 > a'),
            'url_suffix': '/projects/calendar/',
        }, {
            'locator': (By.CSS_SELECTOR, '#featured > li:nth-of-type(3) > h3 > a'),
            'url_suffix': 'http://caminobrowser.org/',
        },
    ]

    product_link_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(1) > h3 > a'),
            'url_suffix': 'http://www.adobe.com/products/acrobat/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(2) > h3 > a'),
            'url_suffix': 'http://www.amplesdk.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(3) > h3 > a'),
            'url_suffix': 'http://apicasystem.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(4) > h3 > a'),
            'url_suffix': 'http://www.aptana.com/jaxer',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(5) > h3 > a'),
            'url_suffix': 'http://www.atmail.com/webmail-client/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(6) > h3 > a'),
            'url_suffix': 'http://www.bluegriffon.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(7) > h3 > a'),
            'url_suffix': 'http://getbuzzbird.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(8) > h3 > a'),
            'url_suffix': 'http://celtx.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(9) > h3 > a'),
            'url_suffix': 'http://www.cenzic.com/products/software/overview/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(10) > h3 > a'),
            'url_suffix': 'http://www.floodgap.com/software/classilla/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(11) > h3 > a'),
            'url_suffix': 'http://www.alwaysontechnologies.com/cloudbrowse/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(12) > h3 > a'),
            'url_suffix': 'http://www.convertigo.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(13) > h3 > a'),
            'url_suffix': 'http://couchdb.apache.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(14) > h3 > a'),
            'url_suffix': 'http://www.cyclone3.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(15) > h3 > a'),
            'url_suffix': 'http://www.webdevelopers.eu/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(16) > h3 > a'),
            'url_suffix': 'http://developer.emusic.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(17) > h3 > a'),
            'url_suffix': 'http://www.enlis.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(18) > h3 > a'),
            'url_suffix': 'http://www.epicbrowser.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(19) > h3 > a'),
            'url_suffix': 'http://www.eudora.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(20) > h3 > a'),
            'url_suffix': 'http://www.open-ils.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(21) > h3 > a'),
            'url_suffix': 'http://exelearning.org/wiki',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(22) > h3 > a'),
            'url_suffix': 'http://developers.facebook.com/fbopen/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(23) > h3 > a'),
            'url_suffix': 'http://www.wirespring.com/Solutions/digital_signage.html',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(24) > h3 > a'),
            'url_suffix': 'http://flickr.com/tools/uploadr/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(25) > h3 > a'),
            'url_suffix': 'http://www.globalmojo.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(26) > h3 > a'),
            'url_suffix': 'http://www.google.com/intl/en/adwordseditor/index.html',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(27) > h3 > a'),
            'url_suffix': 'http://code.google.com/p/google-gadgets-for-linux/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(28) > h3 > a'),
            'url_suffix': 'http://www.imvu.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(29) > h3 > a'),
            'url_suffix': 'http://instantbird.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(30) > h3 > a'),
            'url_suffix': 'http://www.kirix.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(31) > h3 > a'),
            'url_suffix': 'http://www.kiwix.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(32) > h3 > a'),
            'url_suffix': 'http://www.kompozer.net/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(33) > h3 > a'),
            'url_suffix': 'http://www.kylo.tv/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(34) > h3 > a'),
            'url_suffix': 'http://www.litl.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(35) > h3 > a'),
            'url_suffix': 'http://www.logitech.com/en-us/71/6345?moduleaction=LearnMoreAboutLogitechHarmony&wt.ac=HarmonyCat&modulename=HarmonyCat',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(36) > h3 > a'),
            'url_suffix': 'http://www.lunascape.tv/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(37) > h3 > a'),
            'url_suffix': 'http://maemo.nokia.com/features/maemo-browser/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(38) > h3 > a'),
            'url_suffix': 'http://getmockery.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(39) > h3 > a'),
            'url_suffix': 'http://www.mongodb.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(40) > h3 > a'),
            'url_suffix': 'http://wiki.laptop.org/go/Web_Browser',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(41) > h3 > a'),
            'url_suffix': 'http://oneteam.im/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(42) > h3 > a'),
            'url_suffix': 'http://www.openkomodo.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(43) > h3 > a'),
            'url_suffix': 'http://www.jedox.com/en/home/overview.html',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(44) > h3 > a'),
            'url_suffix': 'http://pencil.evolus.vn/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(45) > h3 > a'),
            'url_suffix': 'http://www.pentaho.com/products/discover_bi_suite.php',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(46) > h3 > a'),
            'url_suffix': 'http://www.postbox-inc.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(47) > h3 > a'),
            'url_suffix': 'http://www.qsos.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(48) > h3 > a'),
            'url_suffix': 'http://www.redhat.com/rhel/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(49) > h3 > a'),
            'url_suffix': 'http://scenari-platform.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(50) > h3 > a'),
            'url_suffix': 'http://www.skyfire.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(51) > h3 > a'),
            'url_suffix': 'http://www.smartreport.eu/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(52) > h3 > a'),
            'url_suffix': 'http://www.snapstick.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(53) > h3 > a'),
            'url_suffix': 'http://www.sogo.nu/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(54) > h3 > a'),
            'url_suffix': 'http://www.getsongbird.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(55) > h3 > a'),
            'url_suffix': 'http://www.spicebird.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(56) > h3 > a'),
            'url_suffix': 'http://www.splashtop.com/index.php',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(57) > h3 > a'),
            'url_suffix': 'http://www.skybound.ca/stylizer/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(58) > h3 > a'),
            'url_suffix': 'http://www.tomtom.com/services/service.php?id=16',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(59) > h3 > a'),
            'url_suffix': 'http://www.trustedbird.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(60) > h3 > a'),
            'url_suffix': 'http://www.tuneupmedia.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(61) > h3 > a'),
            'url_suffix': 'http://www.twitfactory.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(62) > h3 > a'),
            'url_suffix': 'http://www.virtualbox.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(63) > h3 > a'),
            'url_suffix': 'http://www-01.ibm.com/software/integration/lombardi-edition/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(64) > h3 > a'),
            'url_suffix': 'http://www.wesabe.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(65) > h3 > a'),
            'url_suffix': 'http://www.winehq.org/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(66) > h3 > a'),
            'url_suffix': 'http://www.worksmart.net/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(67) > h3 > a'),
            'url_suffix': 'http://www.wyzo.com/',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(68) > h3 > a'),
            'url_suffix': 'http://www.yoono.com/desktop_features.html',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(69) > h3 > a'),
            'url_suffix': 'http://www.zimbra.com/products/desktop.html',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(70) > h3 > a'),
            'url_suffix': 'http://www.zkoss.org/',
        },
    ]

    find_out_more_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > p:nth-of-type(1) > a'),
            'url_suffix': 'https://developer.mozilla.org/En/List_of_Mozilla-Based_Applications',
        }, {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > ul > li:nth-of-type(1) > a'),
            'url_suffix': 'https://developer.mozilla.org/En/Using_Mozilla_code_in_other_projects',
        }, {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > ul > li:nth-of-type(2) > a'),
            'url_suffix': 'http://www.mozdev.org/community/books.html',
        }, {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > ul > li:nth-of-type(3) > a'),
            'url_suffix': 'https://wiki.mozilla.org/Consulting',
        }, {
            'locator': (By.CSS_SELECTOR, 'aside.sidebar > div > a'),
            'url_suffix': '/poweredby',
        },
    ]

    get_mozilla_updates_link_list = [
        {
            'locator': (By.CSS_SELECTOR, 'label.privacy-check-label > span > a'),
            'url_suffix': '/en-US/privacy-policy',
        },
    ]

    product_image_list = [
        {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(1) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/acrobat.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(2) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/ample.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(3) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/apica.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(4) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/jaxer.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(5) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/atmail.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(6) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/bluegriffon.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(7) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/buzzbird.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(8) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/celtx.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(9) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/cenzic.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(10) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/classilla.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(11) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/cloudbrowse.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(12) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/convertigo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(13) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/couchdb.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(14) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/cyclone3.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(15) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/elixon.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(16) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/emusic_remote.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(17) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/enlis.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(18) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/epic.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(19) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/eudora.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(20) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/evergreen.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(21) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/exe.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(22) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/facebook.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(23) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/firecast.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(24) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/flickr_uploadr.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(25) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/globalmojo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(26) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/adwords.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(27) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/gadgets.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(28) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/imvu.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(29) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/instantbird.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(30) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/strata.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(31) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/kiwix.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(32) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/kompozer.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(33) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/kylo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(34) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/litl.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(35) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/logitech.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(36) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/lunascape.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(37) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/maemo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(38) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/mockery.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(39) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/mongodb.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(40) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/xo_logo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(41) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/oneteam.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(42) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/komodo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(43) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/palo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(44) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/pencil.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(45) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/pentaho.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(46) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/postbox.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(47) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/qsos.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(48) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/redhat.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(49) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/scenari.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(50) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/skyfire.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(51) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/smartreport.jpg',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(52) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/snapstick.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(53) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/sogo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(54) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/songbird.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(55) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/spicebird.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(56) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/splashtop.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(57) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/stylizer.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(58) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/tomtomhome.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(59) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/trustedbird.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(60) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/tuneup.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(61) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/twitfactory.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(62) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/virtualbox.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(63) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/websphere.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(64) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/wesabe.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(65) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/wine.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(66) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/worksmart.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(67) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/wyzo.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(68) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/yoono.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(69) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/zimbra.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#main-content > ul > li:nth-of-type(70) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/zk.png',
        },
    ]

    billboard_image_list = [
        {
            'locator': (By.CSS_SELECTOR, '#featured > li:nth-of-type(1) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/seamonkey.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#featured > li:nth-of-type(2) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/sunbird.png',
        }, {
            'locator': (By.CSS_SELECTOR, '#featured > li:nth-of-type(3) > h3 > a > img'),
            'url_suffix': '//mozorg.cdn.mozilla.net/media/img/projects/mozilla-based/camino.png',
        },
    ]
