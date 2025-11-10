"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have

SCREEN_SIZES = {
    "desktop_hd": (1280, 720),
    "desktop_full_hd": (1920, 1080),
    "mobile_pixel_7": (412, 915),
    "mobile_iphone_se": (375, 667),
}


@pytest.fixture(params=[
    "desktop_hd",
    "desktop_full_hd",
    "mobile_pixel_7",
    "mobile_iphone_se"
], scope="session")
def setup_browser(request):
    browser.config.window_width, browser.config.window_height = SCREEN_SIZES[request.param]
    browser.config.base_url = "https://github.com"

    yield browser.config.window_width
    browser.quit()


@pytest.fixture()
def is_mobile(setup_browser):
    width = setup_browser
    return width < 1011


def test_github_desktop(setup_browser, is_mobile):
    if is_mobile:
        pytest.skip('Пропуск мобильных экранов в десктоп-тестах')
    else:
        browser.open("/")
        browser.element(".HeaderMenu-link--sign-up").click()
        browser.element("html").should(have.text("Sign up for GitHub"))


def test_github_mobile(setup_browser, is_mobile):
    if is_mobile:
        browser.open("/")
        browser.element(".js-header-menu-toggle").click()
        browser.element(".HeaderMenu-link--sign-up").click()
        browser.element("html").should(have.text("Sign up for GitHub"))
    else:
        pytest.skip('Пропуск десктопных экранов в мобильных тестах')
