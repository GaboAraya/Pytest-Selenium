from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.generic.dropdown_menu import DropdownMenu


class NearestStorageFacility:

    def __init__(self, page):
        self.page = page
        self.input_your_location = page.find_element(By.CSS_SELECTOR, "#useDeviceLocation + input")
        self.menu_unit_size = DropdownMenu(page, By.ID, "storageUnitSizeSelectbox")
        self.menu_types_storage = DropdownMenu(page, By.ID, "storageSelectbox")
        self.btn_find_storage = page.find_element(By.CSS_SELECTOR, ".form-content button")

    def get_error(self):
        try:
            callback = ec.presence_of_element_located((By.CSS_SELECTOR, ".validation-summary-errors li"))
            error_message = (WebDriverWait(self.page, 3).until(callback))
            return error_message
        except Exception as error:
            raise Exception(f"No error message in the form.\n Selenium error: {error}")
