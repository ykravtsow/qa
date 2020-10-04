import pytest
from selenium import webdriver
from src.page_objects import LoginPage


def test_login_page_new_customer(url, browser):
    l = LoginPage(browser, url)
    assert 'New Customer' in l.find_element('New Customer')


def test_login_page_continue_button(url, browser):
    l = LoginPage(browser, url)
    assert 'Continue' in l.find_element('Continue Button')


def test_login_page_login_button(url, browser):
    l = LoginPage(browser, url)
    assert 'Login' in l.find_element('Login Button')


def test_login_page_email_address(url, browser):
    l = LoginPage(browser, url)
    assert 'E-Mail Address' in l.find_element_attribute('Email Address', 'placeholder')


def test_login_page_forgotten_password(url, browser):
    l = LoginPage(browser, url)
    assert 'Forgotten Password' in l.find_element('Forgotten Password')

