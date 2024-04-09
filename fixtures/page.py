import pytest
from nullsafe import _
from selenium import webdriver

from common.enums import Browser


@pytest.fixture
def page(request):
    """
    Pytest fixture to return a Selenium WebDriver instance based on command line argument.

    Parameters:
    - request: Pytest request object.

    Returns:
    - WebDriver: Selenium WebDriver instance.

    Usage:
    - Pass --chrome, --firefox, --edge or --cross-browser argument to specify browser.
      If not specified, defaults to Chrome.
    - Example: pytest --firefox
    - If --headless is passed as an argument the browser will be set to run in that mode
    """
    if _(request).param:
        browser, headless_mode = _(request).param
    else:
        browser, headless_mode = None, None
    match browser:
        case Browser.FIREFOX:
            options = webdriver.FirefoxOptions()
            if headless_mode:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options)
            driver.implicitly_wait(1)
            driver.maximize_window()
        case Browser.EDGE:
            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            if headless_mode:
                options.add_argument("--enable-chrome-browser-cloud-management")
                options.add_argument("--headless=new")
            driver = webdriver.Edge(options)
        case _:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            if headless_mode:
                options.add_argument("--headless=new")
            driver = webdriver.Chrome(options)
    yield driver
    driver.close()
