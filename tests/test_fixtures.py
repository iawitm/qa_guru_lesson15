"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.fixture
def desktop_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://github.com"
    yield
    browser.quit()


@pytest.fixture
def mobile_browser():
    browser.config.window_width = 412
    browser.config.window_height = 915
    browser.config.base_url = "https://github.com"
    yield
    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open("/")
    browser.element(".HeaderMenu-link--sign-up").click()
    browser.element("html").should(have.text("Sign up for GitHub"))


def test_github_mobile(mobile_browser):
    browser.open("/")
    browser.element(".js-header-menu-toggle").click()
    browser.element(".HeaderMenu-link--sign-up").click()
    browser.element("html").should(have.text("Sign up for GitHub"))
    pass
