import pytest
from selenium import webdriver
from src.page_objects import *


def test_admin_page_logo(url, browser):
    a = AdminPage(browser, url)
    assert 'view/image/logo.png' in a.find_element_attribute('Logo', 'src')


def test_admin_page_login_button(url, browser):
    a = AdminPage(browser, url)
    assert 'Login' in a.find_element('LoginButton')


def test_admin_page_username(url, browser):
    a = AdminPage(browser, url)
    assert 'Username' in a.find_element_attribute('UsernameInput', 'placeholder')


def test_admin_page_footer(url, browser):
    a = AdminPage(browser, url)
    assert 'OpenCart' in a.find_element('footer')

