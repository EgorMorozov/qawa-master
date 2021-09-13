from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.insect_shop import Insect_shop
from Services.ramdomizer import Randomizer
import time


class Infinum_inspect_shop(BaseTest):

    def setUp(self):
        super().setUp()
        self.insect_shop = Insect_shop(self.driver)

    def test_register_user(self):
        log_message("Registering a new user")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.insect_shop.manipulate_user(username, password, self.insect_shop.register_button)

        log_message("Expected message is: " + self.insect_shop.messages_types.get('registration_success'))
        log_message("Actual message is: " + self.insect_shop.get_message_text())

        self.assertEqual(self.insect_shop.messages_types.get('registration_success'),
                         self.insect_shop.get_message_text(), "Actual message is different from expected")

        log_message("Clearing up test data")
        self.insect_shop.manipulate_user(username, password, self.insect_shop.delete_accout_button)

    def test_register_without_store_name(self):
        log_message("Create test credentials")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()

        log_message("Username is: " + username + ", and password is: " + password)

        self.insect_shop.press_button(self.insect_shop.register_button)
        self.assertEqual(self.insect_shop.messages_types.get('empty_state'), self.insect_shop.get_message_text(),
                         "Actual message is different from expected")

        self.insect_shop.enter_password(password)
        self.insect_shop.press_button(self.insect_shop.register_button)
        self.assertEqual(self.insect_shop.messages_types.get('empty_state'), self.insect_shop.get_message_text(),
                         "Actual message is different from expected")

        self.insect_shop.clear_up_input(self.insect_shop.enter_password_field)

        self.insect_shop.enter_store_name(username)
        self.insect_shop.press_button(self.insect_shop.register_button)
        self.assertEqual(self.insect_shop.messages_types.get('empty_state'), self.insect_shop.get_message_text(),
                         "Actual message is different from expected")

        self.insect_shop.clear_up_all_inputs()

    def test_double_registration(self):
        log_message("Create test credentials")
        username = Randomizer.get_random_username()
        password = Randomizer.get_password()
        log_message("Username is: " + username + ", and password is: " + password)

        self.insect_shop.manipulate_user(username, password, self.insect_shop.register_button)
        self.assertEqual(self.insect_shop.messages_types.get('registration_success'),
                         self.insect_shop.get_message_text(), "Actual message is different from expected")

        self.insect_shop.manipulate_user(username, password, self.insect_shop.register_button)
        # need to use sleep because selenium works faster than text on the page changes
        # TODO - find the solution how to avoid "sleep" call
        time.sleep(1)
        self.assertEqual(self.insect_shop.messages_types.get('user_exist'), self.insect_shop.get_message_text(),
                         "Actual message is different from expected")

        log_message("Clearing up test data")
        self.insect_shop.manipulate_user(username, password, self.insect_shop.delete_accout_button)
