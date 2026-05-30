from math import log, sin

from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how: str, what: str, timeout: int = 4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how: str, what: str, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, (TimeoutException,)).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), (
            "Login link is not presented"
        )

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()

    # def is_not_product_in_the_basket_text(self):
    #     assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_TEXT), (
    #         "The product added in the basket, but should no"
    #     )

    # def is_the_basket_empty(self):
    #     assert self.is_not_element_present(*BasePageLocators.NOT_EMPTY_BASKET_TEXT), (
    #         "Basket should be empty"
    #     )
