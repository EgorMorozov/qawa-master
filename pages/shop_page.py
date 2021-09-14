from selenium.webdriver.common.by import By
from utilities.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common import test_data
from utilities import config


class Shop_page(BasePage):
    slug = "store/" + test_data.USERNAME
    load_sample_bugs_button = (By.XPATH, "//button[@data-testid='load-sample-bugs-button']")
    clear_inventory_button = (By.XPATH, "//button[@data-testid='clear-inventory-button']")
    universal_inventory_bug_locator = (By.XPATH, "//div[@class='fish-edit']")
    universal_bug_shop_locator = (By.XPATH, "//li[@data-testid='bug-shop-item']")
    universal_remove_inventory_bug_button = (By.XPATH, "//button[@data-testid='bug-remove-button']")
    # This is sample for creating specific locator in the remove_bug_by_name method for example
    specific_inventory_bug_locator = "//input[@data-testid='bug-name-input' and @value='{}']"

    def is_user_logged_in(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(self.slug))
        if self.driver.current_url == config.BASE_URL + self.slug:
            return True
        else:
            return False

    def load_sample_bugs(self):
        self.get_present_element(self.load_sample_bugs_button).click()

    def clear_inventory(self):
        self.get_present_element(self.clear_inventory_button).click()

    def get_records_number_from_table(self, locator):
        return len(self.get_present_elements(locator))

    def remove_bug_by_position(self, position):
        elements = self.get_present_elements(self.universal_remove_inventory_bug_button)
        elements[position].click()

    def remove_bug_by_name(self, name):
        remove_button = (By.XPATH, self.specific_inventory_bug_locator.format(name) + "/following-sibling::button")
        self.get_present_element(remove_button).click()

    def is_inventory_record_exits(self, name):
        item_locator = (By.XPATH, self.specific_inventory_bug_locator.format(name))
        try:
            self.get_present_element(item_locator)
        except Exception:
            return False
