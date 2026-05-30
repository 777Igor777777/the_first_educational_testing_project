from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_not_product_in_the_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), (
            "The product added in the basket, but should no"
        )

    def is_the_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET_TEXT), (
            "Basket should be empty"
        )
