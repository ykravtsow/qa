from src.page_objects import BasePage


class CategoryPage(BasePage):

    CategoryPageLocators = {
        'SearchElement': '//input[@placeholder="Search"]',
        'Logo': '//body/header/div/div/div/div/h1/a[text()[contains(., "Your Store")]]',
        'Filters': '//body/main/div/div/aside/div/a[text()[contains(., "Desktops")]]',
        'RefineSearch': '//body/main/div/div/div/h3[text()[contains(., "Refine Search")]]',
        'ProductCompare': '//span[text()[contains(., "Product Compare")]]'
    }

    def __init__(self, browser, url):
        BasePage.__init__(self, browser, url, self.CategoryPageLocators)

