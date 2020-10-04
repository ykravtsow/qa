from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser, url, locators={}):
        self.browser = browser
        self.url = url
        self.locators = locators
        self.open()

    def find_element_by_xpath(self, selector):
        return self.browser.find_element_by_xpath(self.locators[selector])

    def find_element(self, selector):
        return self.find_element_by_xpath(selector).text

    def find_element_attribute(self, selector, attribute):
        return self.find_element_by_xpath(selector).get_attribute(attribute)

    def open(self):
        self.browser.get(url=self.url)

    def perform(self, selector, keys_send=None):
        elem = self.find_element_by_xpath(selector)
        elem.click()
        if keys_send is not None:
            elem.send_keys(keys_send)
        return elem

    def wait_for(self, seconds, selector):
        wait = WebDriverWait(self.browser, seconds)
        wait.until(EC.presence_of_element_located((By.XPATH, self.locators[selector])))
