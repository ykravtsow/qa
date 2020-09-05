import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


def admin_prepare(url, browser):
    browser.get(url=str(url) + '/admin')
    # print(browser.page_source)
    uname = browser.find_element_by_xpath('//input[@id="input-username"]')
    uname.click()
    uname.send_keys('admin')

    passwd = browser.find_element_by_xpath('//input[@id="input-password"]')
    passwd.click()
    passwd.send_keys('password')

    log_btn = browser.find_element_by_xpath('//button[@class="btn btn-primary"]')
    log_btn.click()

    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, '//li[@id="menu-extension"]')))


def test_admin_interface_login(url, browser):
    admin_prepare(url, browser)
    assert 'Extensions' in browser.find_element_by_xpath('//li[@id="menu-extension"]/a').text


def test_admin_interface_logout(url, browser):
    admin_prepare(url, browser)

    logout = browser.find_element_by_xpath('/html/body/div[1]/header/div/ul/li[2]/a')
    logout.click()

    wait = WebDriverWait(browser, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="input-username"]')))
    assert 'Username' in browser.find_element_by_xpath('//input[@id="input-username"]').get_attribute('placeholder')


def test_admin_interface_get_products(url, browser):
    admin_prepare(url, browser)

    catalog = browser.find_element_by_xpath('/html/body/div[1]/nav/ul/li[2]/a')
    catalog.click()
    wait = WebDriverWait(browser, 5)

    products = browser.find_element_by_xpath('/html/body/div[1]/nav/ul/li[2]/ul/li[2]/a')
    products.click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//form[@id="form-product"]')))
    assert len(browser.find_element_by_xpath(
        '/html/body/div/div/div[2]/div/div[2]/div/div[2]/form/div/table/tbody/tr[1]/td[2]/img')
               .get_attribute('src')) > 0


