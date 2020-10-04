import pytest
from selenium import webdriver
from src.page_objects import GoodsPage


def test_goods_page_image(url, browser):
    g = GoodsPage(browser, url)
    assert 'samsung_tab_1-500x500.jpg' in g.find_element_attribute('Image', 'href')


def test_goods_page_heart(url, browser):
    g = GoodsPage(browser, url)
    assert 'fas fa-heart' in g.find_element_attribute('Heart', 'class')


def test_goods_page_description(url, browser):
    g = GoodsPage(browser, url)
    assert 'Description' in g.find_element('Description')


def test_goods_page_add_to_cart(url, browser):
    g = GoodsPage(browser, url)
    assert 'Add to Cart' in g.find_element('Add to Cart')


def test_goods_page_input_quantity(url, browser):
    g = GoodsPage(browser, url)
    assert 'quantity' in g.find_element_attribute('Input Quantity', 'name')

