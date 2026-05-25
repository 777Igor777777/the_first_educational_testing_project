# from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
