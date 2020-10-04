from src.page_objects import *


class AdminPage(BasePage):

    AdminPageLocators = {
        'Logo': '//img[@title="OpenCart"]',
        'LoginButton': '//button[@class="btn btn-primary"]',
        'UsernameInput': '//input[@id="input-username"]',
        'footer': '//footer[@id="footer"]/a',
        'PasswordInput': '//input[@id="input-password"]',
        'Menu': '//li[@id="menu-extension"]',
        'Logout': '/html/body/div[1]/header/div/ul/li[2]/a',
        'Catalog': '/html/body/div[1]/nav/ul/li[2]/a',
        'Navigation': '/html/body/div[1]/nav/ul/li[2]/ul/li[2]/a',
        'FormProduct': '//form[@id="form-product"]',
        'Image': '/html/body/div/div/div[2]/div/div[2]/div/div[2]/form/div/table/tbody/tr[1]/td[2]/img'
    }

    def __init__(self, browser, url):
        BasePage.__init__(self, browser, url + '/admin', self.AdminPageLocators)

