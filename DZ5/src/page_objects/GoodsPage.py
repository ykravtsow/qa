from src.page_objects import BasePage


class GoodsPage(BasePage):

    GoodsPageLocators = {
        'Image': '/html/body/main/div/div/div/div/div/ul/li/a',
        'Heart': '//i[@class="fas fa-heart"]',
        'Description': '//a[@id="description-tab"]',
        'Add to Cart': '//button[@id="button-cart"]',
        'Input Quantity': '//input[@id="input-quantity"]'
    }

    def __init__(self, browser, url):
        BasePage.__init__(self, browser,
                          url+'/index.php?route=product/product&path=57&product_id=49',
                          self.GoodsPageLocators)

