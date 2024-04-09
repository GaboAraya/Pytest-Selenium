from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_objects.generic.submenu import SubMenu


class DropdownMenu(WebElement):

    def __init__(self, page, by_option, selector):
        self.page = page
        element = page.find_element(by_option, selector)
        super().__init__(element.parent, element.id)
        self.sub_menu = SubMenu(self,
                                By.CLASS_NAME,
                                "selectbox-options",
                                By.TAG_NAME, "li")

    def click_sub_menu_option_by_name(self, name_option):
        self.click()
        self.sub_menu.click_sub_menu_option_by_name(name_option)
        self.click()

    def click_sub_menu_options_by_name(self, name_options):
        self.click()
        for option in name_options:
            self.sub_menu.click_sub_menu_option_by_name(option)
        self.click()

    def delete_option_by_id(self, id_option):
        option = super().find_element(By.CSS_SELECTOR, f"a[data-control-id='{id_option}']")
        option.click()

    def delete_options_by_ids(self, ids_options):
        for option in ids_options:
            self.delete_option_by_id(option)

    def is_empty(self):
        container = super().find_element(By.CLASS_NAME, "selection-container")
        container_elements = container.find_elements(By.CLASS_NAME, "selectbox-selection")
        return False if container_elements else True
