"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(params=['Desktop', 'Mobile'])
def setup_browser(request):
    if request.param == 'Desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'Mobile':
        browser.config.window_width = 412
        browser.config.window_height = 915
    browser.config.base_url = "https://github.com"
    yield
    browser.quit()


@pytest.mark.parametrize('setup_browser', ['Desktop'], indirect=True)
def test_github_desktop(setup_browser):
    browser.open("/")
    browser.element(".HeaderMenu-link--sign-up").click()
    browser.element("html").should(have.text("Sign up for GitHub"))


@pytest.mark.parametrize('setup_browser', ['Mobile'], indirect=True)
def test_github_mobile(setup_browser):
    browser.open("/")
    browser.element(".js-header-menu-toggle").click()
    browser.element(".HeaderMenu-link--sign-up").click()
    browser.element("html").should(have.text("Sign up for GitHub"))
    pass
