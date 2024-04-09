from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from automation.page_objects.generic.submenu import SubMenu


class NavbarMenu(WebElement):

    def __init__(self, page, by_option, selector):
        self.page = page
        element = page.find_element(by_option, selector)
        super().__init__(element.parent, element.id)
        self.sub_menu = SubMenu(self,
                                By.XPATH,
                                "following-sibling::ul",
                                By.TAG_NAME, "li")

    def click_sub_menu_option_by_name(self, name_option):
        ActionChains(self.page).move_to_element(self).perform()
        self.sub_menu.click_sub_menu_option_by_name(name_option)
