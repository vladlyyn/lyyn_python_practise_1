import selene
from selene import browser, be, have

import pytest

@pytest.fixture(scope='session', autouse=True)
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10
    yield


def test_search(browser_setup):
    browser.open("https://duckduckgo.com/")
    browser.element('input[name="q"]').should(be.visible).set_value("shrek").press_enter()
    browser.element('html').should(have.text('shrek'))

def test_delusion(browser_setup):
    browser.open("https://duckduckgo.com/")
    browser.element('input[name="q"]').should(be.visible).set_value("шоцуа99wj323nkщшоцштiojiwj9").press_enter()
    browser.element('html').should(have.text('ничего не найдено'))
