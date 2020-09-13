from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def name_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def price_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text


    def check_name_in_basket(self):
        assert self.name_of_product() == self.browser.find_element(*ProductPageLocators.BASKET_NAME).text,\
         "Product not added to basket"


    def check_price_in_basket(self):
        assert self.price_of_product() == self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text,\
         "Product price in basket is different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is not presented, but should be"
