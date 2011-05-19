import pytest
import py
from selenium import selenium


def pytest_runtest_setup(item):
    item.host = item.config.option.hub
    item.browser = item.config.option.browser
    item.port = item.config.option.port
    TestSetup.base_url = item.config.option.site
    item.timeout = item.config.option.timeout
    TestSetup.timeout = item.timeout

    if not 'skip_selenium' in item.keywords:
        TestSetup.skip_selenium = False
        TestSetup.selenium = selenium(item.host, item.port,
            item.browser, TestSetup.base_url)

        TestSetup.selenium.start()
        TestSetup.selenium.set_timeout(item.timeout)
    else:
        TestSetup.skip_selenium = True


def pytest_runtest_teardown(item):
    if not TestSetup.skip_selenium:
        TestSetup.selenium.stop()


def pytest_funcarg__testsetup(request):
    return TestSetup(request)


def pytest_addoption(parser):
    parser.addoption("--hub", action="store", default="localhost",
        help="specify where to run")
    parser.addoption("--port", action="store", default="4444",
        help="specify where to run")
    parser.addoption("--browser", action="store", default="*firefox",
        help="specify the browser")
    parser.addoption("--site", action="store", default=None,
        help="specify the AUT")
    parser.addoption("--timeout", action="store", default=120000,
        help="specify the timeout")


class TestSetup:
    def __init__(self, request):
        self.request = request
