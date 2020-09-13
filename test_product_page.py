import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time


link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

@pytest.mark.skip
@pytest.mark.parametrize('offer', ["?promo=offer0", "?promo=offer1", "?promo=offer2","?promo=offer3","?promo=offer4",
                                  "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail),                                                                                                                                                                                                                                                                                                                                                                             "?promo=offer8", "?promo=offer9"])
def test_guest_check_product_after_adding_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    print(f"The name of product is {page.name_of_product()}, and his price is {page.price_of_product()} Lets check theirs with product in basket")
    page.check_name_in_basket()
    page.check_price_in_basket()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_dissapeared(*ProductPageLocators.SUCCESS_MESSAGE)
