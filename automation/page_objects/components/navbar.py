from selenium.webdriver.common.by import By

from automation.page_objects.generic.navbar_menu import NavbarMenu


class Navbar:

    def __init__(self, page):
        self.page = page
        self.menu_trucks = page.find_element(By.LINK_TEXT, "Trucks")
        self.menu_trailers_towing = NavbarMenu(page, By.LINK_TEXT, "Trailers & Towing")
        self.menu_containers = NavbarMenu(page, By.CSS_SELECTOR, "a[href='https://www.uhaul.com/UBox/']")
        self.menu_storage = NavbarMenu(page, By.LINK_TEXT, "Storage")
        self.menu_boxes_packing = NavbarMenu(page, By.LINK_TEXT, "Boxes & Packing Supplies")
        self.menu_moving_labor = page.find_element(By.LINK_TEXT, "Moving Labor")
        self.menu_hitches_accessories = NavbarMenu(page, By.LINK_TEXT, "Hitches & Accessories")

