import pytest
from selenium import webdriver


def test_category_page_search_element(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/category&path=20')
    assert 'Search' in browser.find_element_by_xpath('//input[@placeholder="Search"]').get_attribute("placeholder")


def test_category_page_logo(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/category&path=20')
    assert 'Your Store' in browser.find_element_by_xpath(
        '//body/header/div/div/div/div/h1/a[text()[contains(., "Your Store")]]').text


def test_category_page_filters(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/category&path=20')
    assert 'Desktops' in browser.find_element_by_xpath(
        '//body/main/div/div/aside/div/a[text()[contains(., "Desktops")]]').text


def test_category_page_refine_search(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/category&path=20')
    assert 'Refine Search' in browser.find_element_by_xpath(
        '//body/main/div/div/div/h3[text()[contains(., "Refine Search")]]').text


def test_category_page_product_compare(url, browser):
    browser.get(url=str(url)+'/index.php?route=product/category&path=20')
    assert 'Product Compare' in browser.find_element_by_xpath(
        '//span[text()[contains(., "Product Compare")]]').text

