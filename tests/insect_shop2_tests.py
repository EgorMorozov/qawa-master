from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.insect_shop import Insect_shop
from pages.shop_page import Shop_page
from Services.ramdomizer import Randomizer
from common import test_data

class Infinum_insect_shop2(BaseTest):

    def setUp(self):
        super().setUp()
        self.insect_shop = Insect_shop(self.driver)
        self.shop_page = Shop_page(self.driver)

    def test_log_in_with_wrong_password(self):
        log_message("Registering a new user")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.insect_shop.manipulate_user(username, password, self.insect_shop.register_button)

        self.insect_shop.manipulate_user(username, Randomizer.get_password(), self.insect_shop.login_to_store_button)
        self.assertEqual(self.insect_shop.messages_types.get('invalid_credentials'),
                         self.insect_shop.get_message_text(), "Actual message is different from expected")

        log_message("Clearing up test data")
        self.insect_shop.manipulate_user(username, password, self.insect_shop.delete_account_button)

    def test_delete_account_with_wrong_password(self):
        log_message("Registering a new user")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.insect_shop.manipulate_user(username, password, self.insect_shop.register_button)

        for i in range(5):
            self.insect_shop.manipulate_user(username, Randomizer.get_password(),
                                             self.insect_shop.delete_account_button)
            self.assertEqual(self.insect_shop.messages_types.get('invalid_credentials'),
                             self.insect_shop.get_message_text(), "Actual message is different from expected")

        log_message("Clearing up test data")
        self.insect_shop.manipulate_user(username, password, self.insect_shop.delete_account_button)

    def test_login(self):

        self.insect_shop.login(test_data.USERNAME, test_data.PASSWORD)
        self.assertTrue(self.shop_page.is_user_logged_in())







