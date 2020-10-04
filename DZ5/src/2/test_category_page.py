import pytest
from selenium import webdriver
from src.page_objects import *


def test_category_page_search_element(url, browser):
    c = CategoryPage(browser, url+'/index.php?route=product/category&path=20')
    assert 'Search' in c.find_element_attribute('SearchElement', 'placeholder')


def test_category_page_logo(url, browser):
    c = CategoryPage(browser, url+'/index.php?route=product/category&path=20')
    assert 'Your Store' in c.find_element('Logo')


def test_category_page_filters(url, browser):
    c = CategoryPage(browser, url+'/index.php?route=product/category&path=20')
    assert 'Desktops' in c.find_element('Filters')


def test_category_page_refine_search(url, browser):
    c = CategoryPage(browser, url+'/index.php?route=product/category&path=20')
    assert 'Refine Search' in c.find_element('RefineSearch')


def test_category_page_product_compare(url, browser):
    c = CategoryPage(browser, url+'/index.php?route=product/category&path=20')
    assert 'Product Compare' in c.find_element('ProductCompare')

