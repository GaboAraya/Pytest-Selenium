from common.enums import Browser


def pytest_addoption(parser):
    parser.addoption("--chrome",
                     action="store_true",
                     help="Run the test cases using Chrome browser")
    parser.addoption("--edge",
                     action="store_true",
                     help="Run the test cases using Edge browser")
    parser.addoption("--firefox",
                     action="store_true",
                     help="Run the test cases using Firefox browser")
    parser.addoption("--cross-browser",
                     action="store_true",
                     help="Run the test cases using Chrome, Edge and Firefox browsers")
    parser.addoption("--headless",
                     action="store_true",
                     help="Run the test cases in headless mode")


def pytest_generate_tests(metafunc):
    if "page" in metafunc.fixturenames:
        headless_mode = metafunc.config.getoption("--headless", default=None)
        if metafunc.config.getoption("--cross-browser", default=None):
            params = [(browser, headless_mode) for browser in Browser]
        else:
            params = []
            if metafunc.config.getoption("--firefox", default=None):
                params.append((Browser.FIREFOX, headless_mode))
            if metafunc.config.getoption("--edge", default=None):
                params.append((Browser.EDGE, headless_mode))
            if metafunc.config.getoption("--chrome", default=None):
                params.append((Browser.CHROME, headless_mode))
            params = params if params else [(Browser.CHROME, headless_mode)]
        metafunc.parametrize("page", params, indirect=True)
