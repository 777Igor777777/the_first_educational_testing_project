from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_basket_on_the_product_page()
        self.should_be_add_product_in_the_basket()
        self.solve_quiz_and_get_code()
        self.should_be_right_text_product_in_the_basket()
        self.should_be_right_cost_product_in_the_basket()

    def should_be_product_url(self):
        assert "/?promo=newYear" in self.browser.current_url, (
            "Product URL is not correct"
        )

    def should_be_basket_on_the_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BASKET), (
            "Basket is not present"
        )

    def should_be_add_product_in_the_basket(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET).click()

    def should_be_right_text_product_in_the_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert (
            f"{product_name} был добавлен в вашу корзину."
            in self.browser.find_element(
                *ProductPageLocators.PRODUCT_ADDED_IN_THE_BASKET_TEXT
            ).text
        ), "Incorrect message"

    def should_be_right_cost_product_in_the_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert (
            price
            == self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_COST).text
        ), "Incorrect cost"
