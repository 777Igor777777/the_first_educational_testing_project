import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )

    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language",
    )


@pytest.fixture(scope="function")
def browser(request: FixtureRequest):
    browser_name: str = request.config.getoption("browser_name") or "chrome"
    user_language: str = request.config.getoption("language") or "en"
    print(f"\nstart {browser_name} browser test..")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", "user_language")
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()
