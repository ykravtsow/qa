from src.page_objects import BasePage


class LoginPage(BasePage):

    LoginPageSelectors = {
        'New Customer': '//h2[text()[contains(., "New Customer")]]',
        'Continue Button': '/html/body/main/div/div/div/div/div/div/div/a',
        'Login Button': '//button[@class="btn btn-primary"]',
        'Email Address': '//input[@id="input-email"]',
        'Forgotten Password': '//div[@class="form-group"]/a'
    }

    def __init__(self, browser, url):
        BasePage.__init__(self, browser, url+'/index.php?route=account/login&language=en-gb', self.LoginPageSelectors)

