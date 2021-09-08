from utilities.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common import test_data
from utilities import config


class Shop_page(BasePage):

    slug = "store/" + test_data.USERNAME

    def is_user_logged_in(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(self.slug))
        if self.driver.current_url == config.BASE_URL + self.slug:
            return True
        else:
            return False
