import pytest

from fixtures.page import page


@pytest.fixture(name="navigate_main_page")
def fixture_navigate_main_page(page):
    page.get("https://www.uhaul.com/")


@pytest.fixture(name="navigate_storage")
def fixture_navigate_storage(page):
    page.get("https://www.uhaul.com/Storage/")
