from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)

    def check_absence_of_items_in_empty_basket_page(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
