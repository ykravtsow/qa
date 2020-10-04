import sys
import pytest
from selenium import webdriver
from src.page_objects import *


def test_main_page_object_title(url, browser):
    m = MainPage(browser, url)
    assert browser.title == m.locators['Title String']
    assert 'OpenCart' in m.find_element_attribute('Title Selector', 'text')

