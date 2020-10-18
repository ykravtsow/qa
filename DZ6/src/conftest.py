import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver import IeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
import logging


# class MyListener(AbstractEventListener):
#     def before_navigate_to(self, url, driver):
#         print("Before navigate to %s" % url)
#
#     def after_navigate_to(self, url, driver):
#         print("After navigate to %s" % url)


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--browser_version", default="")
    parser.addoption("--selenoid", default="localhost")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    selenoid = request.config.getoption("--selenoid")
    fixture_logger = logging.getLogger("browser_fixture")

    executor_url = f"http://{selenoid}:4444/wd/hub"
    caps = {
        "browserName": browser,
        "browserVersion": browser_version,
        "name": request.node.name,
        "headless": True
    }

    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    driver.implicitly_wait(2)
    #driver = EventFiringWebDriver(driver, MyListener())
    fixture_logger.info(f"Start session {driver.session_id}")
    request.addfinalizer(driver.quit)
    return driver

