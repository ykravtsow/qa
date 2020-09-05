import pytest
from selenium import webdriver


def test_login_page_new_customer(url, browser):
    browser.get(url=str(url)+'/index.php?route=account/login&language=en-gb')
    assert 'New Customer' in browser.find_element_by_xpath('//h2[text()[contains(., "New Customer")]]').text


def test_login_page_continue_button(url, browser):
    browser.get(url=str(url)+'/index.php?route=account/login&language=en-gb')
    assert 'Continue' in browser.find_element_by_xpath(
        '/html/body/main/div/div/div/div/div/div/div/a').text


def test_login_page_login_button(url, browser):
    browser.get(url=str(url)+'/index.php?route=account/login&language=en-gb')
    assert 'Login' in browser.find_element_by_xpath(
        '//button[@class="btn btn-primary"]').text


def test_login_page_email_address(url, browser):
    browser.get(url=str(url)+'/index.php?route=account/login&language=en-gb')
    assert 'E-Mail Address' in browser.find_element_by_xpath(
        '//input[@id="input-email"]').get_attribute("placeholder")


def test_login_page_forgotten_password(url, browser):
    browser.get(url=str(url)+'/index.php?route=account/login&language=en-gb')
    assert 'Forgotten Password' in browser.find_element_by_xpath(
        '//div[@class="form-group"]/a').text

