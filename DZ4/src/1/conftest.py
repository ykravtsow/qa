import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver import IeOptions



def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="http://localhost"
    )

    parser.addoption(
        "--browser",
        default="firefox"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    r = request.config.getoption("--browser")
    browsers = {
        "firefox": webdriver.Firefox,
        "chrome": webdriver.Chrome,
        "ie": webdriver.Ie
    }
    options = {
        "firefox": FirefoxOptions(),
        "chrome": ChromeOptions(),
        "ie": IeOptions()
    }
    if r in options:
        option = options[r]
    option.headless = True
    if r in browsers:
        br = browsers[r](options=option)
    else:
        raise Exception("Unknown browser requested")
    yield br
    br.quit()



