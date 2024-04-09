import allure
from assertpy import assert_that
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from automation.fixtures.page import page
from automation.fixtures.navigation import fixture_navigate_storage as navigate_storage
from automation.fixtures.navigation import fixture_navigate_main_page as navigate_main_page
from automation.page_objects.components.navbar import Navbar
from automation.page_objects.components.nearest_storage_facility import NearestStorageFacility
from automation.page_objects.pages.storage_results import StorageResults


@allure.title("Find a storage using location")
@allure.description("Check the correct behavior when a user adds a valid location "
                    "and click on the button with the label “Find Storage")
def test_find_storage_using_location(page, navigate_main_page):
    navbar = Navbar(page)
    navbar.menu_storage.click_sub_menu_option_by_name("Self-Storage at U-Haul")
    assert_that(page.current_url).is_equal_to("https://www.uhaul.com/Storage/")
    form_storage_facility = NearestStorageFacility(page)
    form_storage_facility.input_your_location.send_keys("California City, CA")
    form_storage_facility.btn_find_storage.click()
    WebDriverWait(page, 5).until(ec.url_to_be("https://www.uhaul.com/Storage/California-City-CA/Results/"))
    storage_results_page = StorageResults(page)
    assert_that(storage_results_page.title.text).is_equal_to("Find a Storage Unit Near You in California City, CA")
    assert_that(storage_results_page.input_your_location.get_attribute("value")).is_equal_to("California City, CA")


@allure.title("Select and deselect options in the “unit size” and “types of storage” dropdown menus")
@allure.description("Check the correct behavior of the “unit size” and “types of storage” dropdown "
                    "menus when the user select and deselect options")
def test_select_deselect_options_dropdown_menus(page, navigate_main_page):
    navbar = Navbar(page)
    navbar.menu_storage.click_sub_menu_option_by_name("Move-In Online Today!")
    assert_that(page.current_url).is_equal_to("https://www.uhaul.com/Storage/Online-Move-In/")
    form_storage_facility = NearestStorageFacility(page)
    form_storage_facility.menu_unit_size.click_sub_menu_options_by_name(["Small", "Large", "Medium"])
    form_storage_facility.menu_types_storage.click_sub_menu_option_by_name("Wine Storage")
    form_storage_facility.menu_types_storage.delete_options_by_ids(["OnlineMoveIn", "Wine"])
    form_storage_facility.menu_unit_size.delete_options_by_ids(["Large", "Small", "Medium"])
    assert_that(form_storage_facility.menu_unit_size.is_empty()).is_true()
    assert_that(form_storage_facility.menu_types_storage.is_empty()).is_true()


@allure.title("Check the error when a user clicks on “Find Storage” without filling “Your Location” input")
@allure.description("Check the error and the correct behavior of the form “Find the Nearest Storage Facility” "
                    "when a user clicks on “Find Storage” without filling “Your Location” input")
def test_check_error_not_input(page, navigate_storage):
    form_storage_facility = NearestStorageFacility(page)
    form_storage_facility.btn_find_storage.click()
    assert_that(form_storage_facility.get_error().text).is_equal_to("Please enter your "
                                                                    "zip/postal code, city or address.")


@allure.title("Check the error when a user clicks on “Find Storage” when add an incorrect postal code")
@allure.description("Check the error and the correct behavior of the form “Find the Nearest Storage Facility” "
                    "when a user clicks on “Find Storage” when add an incorrect postal code")
def test_check_error_incorrect_input(page, navigate_storage):
    form_storage_facility = NearestStorageFacility(page)
    form_storage_facility.input_your_location.send_keys("abcdeg987654321")
    form_storage_facility.btn_find_storage.click()
    assert_that(form_storage_facility.get_error().text).is_equal_to("We could not find your location. "
                                                                    "Please enter your zip/postal code, "
                                                                    "city or address again.")
