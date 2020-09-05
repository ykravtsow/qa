import pytest
from selenium import webdriver


def test_admin_page_logo(url, browser):
    browser.get(url=str(url)+'/admin')
    assert 'view/image/logo.png' in browser.find_element_by_xpath('//img[@title="OpenCart"]').get_attribute("src")


def test_admin_page_login_button(url, browser):
    browser.get(url=str(url)+'/admin')
    assert 'Login' in browser.find_element_by_xpath('//button[@class="btn btn-primary"]').text


def test_admin_page_username(url, browser):
    browser.get(url=str(url)+'/admin')
    assert 'Username' in browser.find_element_by_xpath(
        '//input[@id="input-username"]').get_attribute("placeholder")


def test_admin_page_footer(url, browser):
    browser.get(url=str(url)+'/admin')
    assert 'OpenCart' in browser.find_element_by_xpath(
        '//footer[@id="footer"]/a').text


