from selenium.webdriver.common.by import By


class StorageResults:

    def __init__(self, page):
        self.page = page
        self.title = page.find_element(By.CSS_SELECTOR, "#mainRow h1")
        self.input_your_location = page.find_element(By.CSS_SELECTOR, "#useDeviceLocation + input")
