import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from src.page_objects import AdminPage


def admin_prepare(url, browser):
    a = AdminPage(browser, url)
    a.perform('UsernameInput', 'admin')
    a.perform('PasswordInput', 'password')
    a.perform('LoginButton')
    a.wait_for(5, 'Menu')
    return a


def test_admin_interface_login(url, browser):
    a = admin_prepare(url, browser)
    assert 'Extensions' in a.find_element('Menu')


def test_admin_interface_logout(url, browser):
    a = admin_prepare(url, browser)
    a.perform('Logout')
    a.wait_for(5, 'UsernameInput')
    assert 'Username' in a.find_element_attribute('UsernameInput', 'placeholder')


def test_admin_interface_get_products(url, browser):
    a = admin_prepare(url, browser)
    a.perform('Catalog')
    a.perform('Navigation')
    a.wait_for(5, 'FormProduct')
    assert len(a.find_element_attribute('Image', 'src')) > 0


