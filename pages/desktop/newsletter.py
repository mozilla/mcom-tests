#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import MozillaBasePage


class NewsletterPage(MozillaBasePage):

    _email_sel = "css=.email"
    _agree_to_privacy_policy_checkbox_sel = "css=.privacy-check"
    _submit_button_sel = "css=#content input[name=submit]"
    _privacy_policy_error_sel = "css=.privacy-field.field-error"
    _success_pane_sel = "css=.success-pane"

    def go_to_newsletter_page(self, url='/en-US/newsletter/'):
        self.selenium.open(url)

    def type_email(self, email):
        self.selenium.type(self._email_sel, email)

    def agree_to_privacy_policy(self):
        self.selenium.check(self._agree_to_privacy_policy_checkbox_sel)

    def click_sign_me_up(self):
        self.selenium.click(self._submit_button_sel)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def is_privacy_policy_error_visible(self):
        return self.is_element_visible(self._privacy_policy_error_sel)

    @property
    def is_success_visible(self):
        return self.is_element_visible(self._success_pane_sel)


class MainNewsletterPage(NewsletterPage):

    _other_newsletters_sel = "css=#other-newsletters"

    @property
    def is_success_visible(self):
        return self.is_element_visible(self._other_newsletters_sel)

    
class OtherNewsletterPage(MozillaBasePage):

    _email_sel = "css=input[name=email]"
    _country_sel = "css=select[name=country]"
    _lang_sel = "css=select[name=lang]"
    _mozilla_and_you_sel = "css=input[name=mozilla-and-you]"
    _submit_sel = "css=input[name=submit]"
    _form_sel = "css=#content form"

    def goto_page(self, email, country, lang, format):
        self._format_sel = 'css=input[name=format][value=%s]' % format
        self.selenium.open('/en-US/newsletter/new/?email=%s&country=%s&lang=%s&format=%s' 
                           % (email, country, lang, format))

    def get_email(self):
        return self.selenium.get_value(self._email_sel)

    def get_country(self):
        return self.selenium.get_value(self._country_sel)

    def get_lang(self):
        return self.selenium.get_value(self._lang_sel)

    def get_format(self):
        return (self.selenium.get_value(self._format_sel) == 'on' and
                self.selenium.get_attribute(self._format_sel + '@value'))

    def click_submit(self):
        self.selenium.click(self._submit_sel)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def is_mozilla_and_you_selected(self):
        return self.selenium.get_value(self._mozilla_and_you_sel) == 'on'

    @property
    def is_form_visible(self):
        return self.selenium.is_element_present(self._form_sel)

    @property
    def is_success_visible(self):
        return (self.selenium.is_text_present('thank') or
                self.selenium.is_text_present('Thank'))


class FooterNewsletterPage(NewsletterPage):
    
    _form_pane_sel = 'css=#sub-footer .form-pane'
    _open_button_sel = 'css=#sub-footer a.email-open'
    _email_sel = "css=#sub-footer .email"
    _agree_to_privacy_policy_checkbox_sel = "css=#sub-footer .privacy-check"
    _submit_button_sel = "css=#sub-footer input[name=submit]"
    _privacy_policy_error_sel = "css=#sub-footer .privacy-field .field-error"
    _success_pane_sel = "css=#sub-footer .success-pane"

    def go_to_newsletter_page(self):
        self.selenium.open('/en-US/firefox/features/')
    
    def click_open_button(self):
        self.selenium.click(self._open_button_sel)

    @property
    def is_form_pane_visible(self):
        return self.selenium.is_visible(self._form_pane_sel)
