import pytest
from selenium import webdriver
from src.page_objects import MainPage


def test_main_page_search_element(url, browser):
    m = MainPage(browser, url)
    assert 'Search' in m.find_element_attribute('Search Element', 'placeholder')


def test_main_page_bin_element(url, browser):
    m = MainPage(browser, url)
    assert 'cart-total' in m.find_element_attribute('Bin Element', 'id')


def test_main_page_top_element(url, browser):
    m = MainPage(browser, url)
    assert 'Currency' in m.find_element('Top Element')


def test_main_page_menu_element(url, browser):
    m = MainPage(browser, url)
    assert 'Desktops' in m.find_element('Menu Element')


def test_main_page_slideshow_element(url, browser):
    m = MainPage(browser, url)
    assert 'swiper-wrapper' in m.find_element_attribute('Slideshow Element', 'class')
