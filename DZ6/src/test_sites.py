import pytest
import allure
import logging


def get_logger(name='logger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logger.level)
    formatter = logging.Formatter('%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


@allure.feature('Яндекс')
@allure.title('Тест главной страницы Яндекс')
def test_yandex_main(browser):
    print()
    logger = get_logger('yandex')
    browser.get('http://yandex.ru')
    #browser.execute_script("console.warn('Here is the WARNING message!')")
    #l = browser.get_log('browser')
    #logger.debug(l)
    with allure.step('Открытие главной страницы Яндекс'):
        allure.attach(
            body=browser.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
    logger.debug('page title: ' + browser.title)
    assert "Яндекс" == browser.title


@allure.feature('Яндекс')
@allure.title('Тест Яндекс.Музыка')
def test_yandex_music(browser):
    print()
    logger = get_logger('yandex')
    browser.get('http://music.yandex.ru')
    with allure.step('Открытие страницы Яндекс.Музыка'):
        allure.attach(
            body=browser.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
    logger.debug('page title: ' + browser.title)
    assert "Яндекс.Музыка — собираем музыку и подкасты для вас" == browser.title


@allure.feature('Facebook')
@allure.title('Тест главной страницы Facebook')
def test_facebook_main(browser):
    print()
    logger = get_logger('facebook')
    browser.get('http://facebook.com')
    with allure.step('Открытие главной страницы Facebook'):
        allure.attach(
            body=browser.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
    logger.debug('page title: ' + browser.title)
    assert "Facebook – log in or sign up" == browser.title
