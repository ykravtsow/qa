from . import BasePage


class MainPage(BasePage):

    MainPageLocators = {
        'Title String': 'Your Store',
        'Title Selector': '//a[text()[contains(., "OpenCart")]]',
        'Search Element': '//input[@placeholder="Search"]',
        'Bin Element': '//button/span[@id="cart-total"]',
        'Top Element': '//nav[@id="top"]/div/div/ul/li/form/div/div/span[text()[contains(., "Currency")]]',
        'Menu Element': '//nav[@id="menu"]/div/ul/li/a[text()[contains(., "Desktops")]]',
        'Slideshow Element': '//main/div/div/div/div/div/div[@class="swiper-wrapper"]'
    }

    def __init__(self, browser, url):
        BasePage.__init__(self, browser, url, self.MainPageLocators)
