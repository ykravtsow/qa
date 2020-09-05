import pytest
from selenium import webdriver


def test_opencart_title(url, browser):
    browser.get(url=url)
    assert browser.title == "Your Store"
    assert 'OpenCart' in browser.find_element_by_xpath('//a[text()[contains(., "OpenCart")]]').get_attribute('text')



