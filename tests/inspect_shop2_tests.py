from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.inspect_shop import Inspect_shop
from pages.shop_page import Shop_page
from Services.ramdomizer import Randomizer
from common import test_data
from utilities import config


class Infinum_inspect_shop2(BaseTest):

    def setUp(self):
        super().setUp()
        self.inspect_shop = Inspect_shop(self.driver)
        self.shop_page = Shop_page(self.driver)

    def test_log_in_with_wrong_password(self):
        log_message("Registering a new user")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.register_button)

        self.inspect_shop.manipulate_user(username, Randomizer.get_password(), self.inspect_shop.login_to_store_button)
        self.assertEqual(self.inspect_shop.messages_types.get('invalid_credentials'),
                         self.inspect_shop.get_message_text(), "Actual message is different from expected")

        log_message("Clearing up test data")
        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.delete_accout_button)

    def test_delete_account_with_wrong_password(self):
        log_message("Registering a new user")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.register_button)

        for i in range(5):
            self.inspect_shop.manipulate_user(username, Randomizer.get_password(),
                                              self.inspect_shop.delete_accout_button)
            self.assertEqual(self.inspect_shop.messages_types.get('invalid_credentials'),
                             self.inspect_shop.get_message_text(), "Actual message is different from expected")

        log_message("Clearing up test data")
        self.inspect_shop.manipulate_user(username, password, self.inspect_shop.delete_accout_button)

    def test_login(self):

        self.inspect_shop.login(test_data.USERNAME, test_data.PASSWORD)
        self.assertTrue(self.shop_page.is_user_logged_in())







