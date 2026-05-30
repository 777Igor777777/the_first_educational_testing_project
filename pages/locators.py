from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_links")


class MainPageLocators:
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_REPEAT_PASSWORD = (By.ID, "id_registration-password2")


class ProductPageLocators:
    PRODUCT_BASKET = (
        By.CSS_SELECTOR,
        "button.btn.btn-lg.btn-primary.btn-add-to-basket",
    )
    PRODUCT_ADDED_IN_THE_BASKET_TEXT = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page div div p.price_color")
    PRODUCT_BASKET_COST = (By.CSS_SELECTOR, ".alertinner p strong")
