from selenium.webdriver.remote.webelement import WebElement


class SubMenu(WebElement):

    def __init__(self, page, by_option, selector, elements_by_option, elements_selector):
        self.page = page
        element = page.find_element(by_option, selector)
        super().__init__(element.parent, element.id)
        self.elements = self.find_elements(elements_by_option, elements_selector)

    def click_sub_menu_option_by_name(self, name_option):
        option = [element for element in self.elements if name_option in element.text]
        if option:
            option[0].click()
        else:
            raise Exception(f"Option name not valid.")