import pytest
from selenium import webdriver


def test_goods_page_image(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/product&path=57&product_id=49')
    assert 'samsung_tab_1-500x500.jpg' in browser.find_element_by_xpath(
        '/html/body/main/div/div/div/div/div/ul/li/a').get_attribute('href')


def test_goods_page_heart(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/product&path=57&product_id=49')
    assert 'fas fa-heart' in browser.find_element_by_xpath(
        '//i[@class="fas fa-heart"]').get_attribute('class')


def test_goods_page_description(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/product&path=57&product_id=49')
    assert 'Description' in browser.find_element_by_xpath(
        '//a[@id="description-tab"]').text


def test_goods_page_add_to_cart(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/product&path=57&product_id=49')
    assert 'Add to Cart' in browser.find_element_by_xpath(
        '//button[@id="button-cart"]').text


def test_goods_page_input_quantity(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/product&path=57&product_id=49')
    assert 'quantity' in browser.find_element_by_xpath(
        '//input[@id="input-quantity"]').get_attribute("name")

