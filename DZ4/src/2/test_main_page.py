import pytest
from selenium import webdriver


def test_main_page_search_element(url, browser):
    browser.get(url=str(url))
    assert 'Search' in browser.find_element_by_xpath('//input[@placeholder="Search"]').get_attribute("placeholder")


def test_main_page_bin_element(url, browser):
    browser.get(url=str(url))
    assert 'cart-total' in browser.find_element_by_xpath('//button/span[@id="cart-total"]').get_attribute("id")


def test_main_page_top_element(url, browser):
    browser.get(url=str(url))
    assert 'Currency' in browser.find_element_by_xpath(
        '//nav[@id="top"]/div/div/ul/li/form/div/div/span[text()[contains(., "Currency")]]').text


def test_main_page_menu_element(url, browser):
    browser.get(url=str(url))
    assert 'Desktops' in browser.find_element_by_xpath(
        '//nav[@id="menu"]/div/ul/li/a[text()[contains(., "Desktops")]]').text


def test_main_page_slideshow_element(url, browser):
    browser.get(url=str(url))
    assert 'swiper-wrapper' in browser.find_element_by_xpath(
        '//main/div/div/div/div/div/div[@class="swiper-wrapper"]').get_attribute("class")
